// CONFIGURAÇÃO DO MAPA SALVADOR
const map = L.map('map', { zoomControl: false }).setView([-13.0003, -38.5192], 15);

L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
    attribution: '© OpenStreetMap contributors © CARTO'
}).addTo(map);

let marcadoresLayer = L.layerGroup().addTo(map);
let idsProcessados = new Set();
let currentLocal = null;
let debounceTimer;

// ELEMENTOS DOM
const inputBusca = document.getElementById('input-busca');
const listaSugestoes = document.getElementById('lista-sugestoes');
const sliderHora = document.querySelector('input[type="range"]');
const inputData = document.getElementById('input-data');


//  AUTOCOMPLETE (NOMINATIM) 
inputBusca.addEventListener('input', () => {
    clearTimeout(debounceTimer);
    const query = inputBusca.value;
    if (query.length < 3) {
        listaSugestoes.classList.add('hidden');
        return;
    }
    debounceTimer = setTimeout(() => buscarEnderecos(query), 500);
});

sliderHora.addEventListener('change', () => {
    const card = document.getElementById('info-card');
    const isCardOpen = card.style.transform === "translateY(0px)" || card.style.transform === "translateY(0)";
    
    if (currentLocal && isCardOpen) {
        console.log("Horário alterado. Reanalisando com a IA...");
        showDetails(currentLocal);
    }
});

inputData.addEventListener('change', () => {
    const card = document.getElementById('info-card');
    const isCardOpen = card.style.transform === "translateY(0px)" || card.style.transform === "translateY(0)";
    if (currentLocal && isCardOpen) {
        console.log("Data alterada. Reanalisando com a IA...");
        showDetails(currentLocal);
    }
});

async function buscarEnderecos(query) {
    const url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query + " Salvador Bahia")}&limit=5`;
    try {
        const response = await fetch(url, { headers: { 'User-Agent': 'OndeEstacionar/1.0' } });
        const data = await response.json();
        exibirSugestoes(data);
    } catch (error) {
        console.error("Erro Autocomplete:", error);
    }
}

function exibirSugestoes(resultados) {
    listaSugestoes.innerHTML = '';
    if (resultados.length === 0) {
        listaSugestoes.classList.add('hidden');
        return;
    }
    resultados.forEach(res => {
        const li = document.createElement('li');
        li.className = "px-4 py-3 hover:bg-orange-50 cursor-pointer text-sm text-gray-700 border-b border-gray-50 last:border-none transition-colors";
        li.innerText = res.display_name;
        li.onclick = () => {
            const lat = parseFloat(res.lat);
            const lon = parseFloat(res.lon);
            map.flyTo([lat, lon], 17);
            inputBusca.value = res.display_name;
            listaSugestoes.classList.add('hidden');
            buscarEstacionamentosReais(lat, lon);
        };
        listaSugestoes.appendChild(li);
    });
    listaSugestoes.classList.remove('hidden');
}

// CARREGAMENTO (BANCO) 
async function carregarZonasAzuisBanco() {
    try {
        const response = await fetch('http://localhost:8000/locais');
        const locais = await response.json();
        locais.forEach(local => {
            const idUnico = `banco-${local.lat}-${local.lng}`;
            if (!idsProcessados.has(idUnico)) {
                adicionarMarcador(local, 'banco');
                idsProcessados.add(idUnico);
            }
        });
    } catch (err) {
        console.error("Erro banco SQLite:", err);
    }
}

function adicionarMarcador(local, origem) {
    const extraClass = origem === 'banco' ? 'marker-banco' : 'marker-real';
    const customIcon = L.divIcon({
        className: 'custom-div-icon',
        html: `<div class="marker-pin ${extraClass}"></div>`,
        iconSize: [30, 42],
        iconAnchor: [15, 42]
    });

    L.marker([local.lat, local.lng], { icon: customIcon })
     .addTo(marcadoresLayer)
     .on('click', () => showDetails(local));
}

// CARD IA 
async function showDetails(local) {
    currentLocal = local;
    const card = document.getElementById('info-card');
    const statusText = document.getElementById('status-text');
    const statusBar = document.getElementById('status-bar');
    const percDisplay = document.getElementById('perc-display');
    const justificativa = document.getElementById('ia-justificativa');

    document.getElementById('place-name').innerText = local.nome;
    
    if (card.style.transform !== "translateY(0px)" && card.style.transform !== "translateY(0)") {
        card.style.transform = "translateY(0)";
    }

    statusText.innerText = "IA reanalisando cenário...";
    statusBar.style.backgroundColor = "#cbd5e1"; 
    
    const horaSelecionada = sliderHora.value;
    const dataSelecionada = inputData.value; 

    try {
        const url = `http://localhost:8000/predict?lat=${local.lat}&lng=${local.lng}&local=${encodeURIComponent(local.nome)}&hora=${horaSelecionada}&data=${dataSelecionada}`;        const res = await fetch(url);
        const data = await res.json();

        percDisplay.innerText = data.percentage + "%";
        statusBar.style.width = data.percentage + "%";
        
        if (data.percentage > 70) {
            statusText.innerText = "Excelente probabilidade";
            statusBar.style.backgroundColor = "#22c55e"; 
        } else if (data.percentage > 35) {
            statusText.innerText = "Probabilidade moderada";
            statusBar.style.backgroundColor = "#f97316"; 
        } else {
            statusText.innerText = "Vagas muito limitadas";
            statusBar.style.backgroundColor = "#ef4444"; 
        }

        justificativa.innerText = data.justificativa || "Análise baseada no fluxo histórico de Salvador.";

    } catch (e) {
        console.error("Erro na predição:", e);
        statusText.innerText = "Erro na análise";
        justificativa.innerText = "Não foi possível contactar a IA.";
    }
}

// UTILITÁRIOS 
function closeCard() {
    document.getElementById('info-card').style.transform = "translateY(150%)";
}

function abrirRota() {
    if (!currentLocal) return;
    window.open(`https://www.google.com/maps/dir/?api=1&destination=${currentLocal.lat},${currentLocal.lng}`, '_blank');
}

function getUserLocation() {
    navigator.geolocation.getCurrentPosition((pos) => {
        const { latitude, longitude } = pos.coords;
        map.flyTo([latitude, longitude], 16);
        L.circleMarker([latitude, longitude], { radius: 8, fillColor: "#3b82f6", color: "#fff", weight: 2, fillOpacity: 1 }).addTo(map);
        buscarEstacionamentosReais(latitude, longitude);
    });
}

window.onload = async () => {
    await carregarZonasAzuisBanco(); 
    const centro = map.getCenter();
    buscarEstacionamentosReais(centro.lat, centro.lng); 
};

map.on('moveend', () => {
    const centro = map.getCenter();
    buscarEstacionamentosReais(centro.lat, centro.lng);
});

document.addEventListener('click', (e) => {
    if (!inputBusca.contains(e.target)) listaSugestoes.classList.add('hidden');
});