# Onde Estacionar | Salvador

### Sistema Inteligente de Predição de Vagas com IA 

O **Onde Estacionar** está sendo projetado para resolver um dos maiores problemas de mobilidade urbana de Salvador: encontrar estacionamento. O sistema utiliza uma base de dados consolidada da **Transalvador** (mais de 15.000 vagas) e utiliza IA para prever a disponibilidade de vagas em tempo real, baseando-se em data, hora e localização.

## Funcionalidades Principais

* **Mapa Interativo:** Renderização dos pontos de Zona Azul via Leaflet.js.
* **Simulação Preditiva:** Seleção de data e hora para prever o fluxo de ocupação.
* **IA (Llama 3.3):** Probabilidade e justificativas geradas por inteligência artificial que explicam o contexto do bairro (ex: eventos, horário comercial, vida noturna).
* **Busca por Endereço:** Integração com Nominatim para localizar ruas em Salvador.
* **Rotas Diretas:** Botão integrado para traçar rota no Google Maps.
---

## Stack 

| Camada | Tecnologia |
| --- | --- |
| **Frontend** | HTML5, Tailwind CSS, JavaScript (ES6), Leaflet.js |
| **Backend** | Python, FastAPI, Uvicorn |
| **IA** | Groq Llama 3.3 API |
| **Banco de Dados** | SQLite (Dados Oficiais Transalvador) |
| **Infraestrutura** | Docker |

---

## Estrutura do Projeto

/
├── backend/
│   ├── main.py             # API FastAPI e lógica de integração com IA
│   ├── data/
│   │   ├── seed.py                   # Script para popular o banco de dados
│   │   └── estacionamentos.db        # Banco SQLite com >15.000 logradouros
├── frontend/
│   ├── index.html          # Interface principal 
│   ├── script.js           # Lógica do mapa e consumo da API
│   ├── manifest.json       # Configurações de PWA
│   └── sw.js               # Service Worker para cache offline
├── Dockerfile              # Configuração de container
└── README.md

---

## Como Rodar o Projeto

### Pré-requisitos
* **Docker** e **Docker Compose** instalados.
* Uma **API KEY do Groq** (Obtenha em [console.groq.com](https://console.groq.com)).

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   cd seu-repositorio


2. **Configure as Variáveis de Ambiente:**
Já tem um arquivo `.env.example` na raiz do projeto:
```env
GROQ_API_KEY=sua_chave_aqui

```


3. **Suba os Containers:**
```bash
docker-compose up --build

```


4. **Acesse no Navegador:**
Abra [http://localhost:8000]()


---

## Base de Dados (Zonas Azuis) e Bahia Park (Privado)

O projeto conta com o mapeamento completo das 6 áreas da Transalvador:
* **Área I:** Cidade Baixa / Comércio.
* **Área II:** Centro / Cidade Alta.
* **Área III:** Pituba / Rio Vermelho / Iguatemi (Maior densidade).
* **Área IV:** Boca do Rio / Imbuí / Patamares.
* **Área V & VI:** Itapuã / Piatã / Stella Maris.

---