import sqlite3
import os

DB_PATH = "/app/data/estacionamentos.db"

def seed_data():
    print(f"--- Iniciando População do Banco ---")
    
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute('DROP TABLE IF EXISTS locais') 
        cursor.execute('''
            CREATE TABLE locais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                lat REAL NOT NULL,
                lng REAL NOT NULL,
                tipo TEXT
            )
        ''')
        
        bahia_park = [
            ('Pituba Parque Center (Bahia Park)', -12.9957687, -38.4672895, 'Privado'),
            ('Rua João das Botas (Bahia Park)',-12.9910604, -38.5204521, 'Privado'),
            ('Cei Clínica Medica (Bahia Park)', -12.9702204, -38.5005504, 'Privado'),
            ('Hospital Aristides Maltez (HAM) (Bahia Park)', -12.9907812, -38.4859478, 'Privado'),
            ('Bahia Marina (Bahia Park)', -12.979939, -38.5194797, 'Privado'),
            ('Shopping Cidade (Bahia Park)',-12.9956307, -38.4691764, 'Privado'),
            ('Edificio Suarez Trade Center (Bahia Park)', -12.978765, -38.4617217, 'Privado'),
            ('Rua do Paraíso (Bahia Park)', -12.9797614, -38.5125382, 'Privado'),
            ('Associação Comercial da Bahia (Bahia Park)', -12.9701334, -38.5107379, 'Privado'),
            ('Centro Odontomédico Itamaraty (Bahia Park)', -12.9992881, -38.5052997, 'Privado'),
            ('Parque da Cidade Joventino Silva (Bahia Park)', -12.9964227, -38.4736252, 'Privado'),
            ('Hospital Santa Izabel (Bahia Park)', -12.9711147, -38.5029406, 'Privado'),
            ('Condomínio Edifício Empresarial Convention Center (Bahia Park)', -12.9880825, -38.4718088, 'Privado'),
            ('Fiesta Bahia Hotel (Bahia Park)', -12.9975694, -38.4648943, 'Privado'),
            ('Max Center (Bahia Park)', -12.9961359, -38.4653762, 'Privado'),
            ('Hospital Santa Luzia (Bahia Park)', -12.9748786, -38.5021322, 'Privado'),
            ('Yacht Clube da Bahia (Bahia Park)', -13.0003123, -38.5306621, 'Privado'),
            ('ITC Salvador (Bahia Park)', -12.935377, -38.392347, 'Privado'),
            ('Edificio NEO (Bahia Park)', -12.9977219, -38.461273, 'Privado'),
            ('Hospital Aeroporto (Bahia Park)', -12.9018988, -38.3332003, 'Privado'),
            ('Estacionamento Bahia Park (Bahia Park)', -12.992593, -38.5197435, 'Privado'),
            ('Clube Bahiano de Tênis (Bahia Park)', -13.0017518, -38.5262069, 'Privado'),
            ('Igreja e Mosteiro de São Bento (Bahia Park)', -12.9788842, -38.5142426, 'Privado'),
            ('Shopping Center Lapar (Bahia Park)', -12.9828516, -38.5141532, 'Privado'),
            ('Mercado do Rio Vermelho - Ceasinha (Bahia Park)', -13.0022815, -38.482351, 'Privado'),
            ('Civil Towers (Bahia Park)', -12.9892295, -38.4487622, 'Privado'),
            ('Centro Empresarial Iguatemi (Bahia Park)', -12.9798547, -38.46309, 'Privado'),
            ('Bradesco (Bahia Park)', -12.9964667, -38.4643143, 'Privado')
        ]
        # Dados Oficiais de Salvador (Principais áreas de Zona Azul)
        zonas_azuis_salvador = [
            # ÁREA I - CIDADE BAIXA / COMÉRCIO 
            ('Rua da Conceição da Praia (315 vagas)', -12.9754, -38.5146, 'Zona Azul'),
            ('Avenida da França (749 vagas)', -12.9675, -38.5128, 'Zona Azul'),
            ('Avenida Estados Unidos (463 vagas)', -12.9708, -38.5125, 'Zona Azul'),
            ('Avenida Jequitaia (172 vagas)', -12.9558, -38.4985, 'Zona Azul'),
            ('Avenida Fernandes da Cunha (136 vagas)', -12.9358, -38.5025, 'Zona Azul'),
            ('Rua da Noruega (77 vagas)', -12.9715, -38.5115, 'Zona Azul'),
            ('Praça Irmã Dulce (104 vagas)', -12.9248, -38.5042, 'Zona Azul'),
            ('Rua Torquato Bahia (109 vagas)', -12.9742, -38.5128, 'Zona Azul'),
            ('Largo de Água de Meninos (204 vagas)', -12.9515, -38.4955, 'Zona Azul'),
            ('Rua Barão de Cotegipe (110 vagas)', -12.9395, -38.5038, 'Zona Azul'),
            ('Rua Portugal (80 vagas)', -12.9725, -38.5122, 'Zona Azul'),
            ('Avenida Eng. Oscar Pontes (98 vagas)', -12.9625, -38.5055, 'Zona Azul'),
            ('Largo da Calçada (50 vagas)', -12.9385, -38.5015, 'Zona Azul'),
            ('Rua da Polônia (74 vagas)', -12.9728, -38.5112, 'Zona Azul'),
            ('Rua do Imperador (72 vagas)', -12.9654, -38.5082, 'Zona Azul'),
            ('Largo da Baixa do Bonfim (82 vagas)', -12.9235, -38.5085, 'Zona Azul'),
            ('Rua Comendador Bastos (65 vagas)', -12.9315, -38.5015, 'Zona Azul'),
            ('Rua Agrário de Menezes (70 vagas)', -12.9305, -38.5025, 'Zona Azul'),
            ('Rua Conselheiro Dantas (49 vagas)', -12.9735, -38.5135, 'Zona Azul'),
            ('Praça Marechal Deodoro (49 vagas)', -12.9755, -38.5125, 'Zona Azul'),
            ('Largo do Cais do Ouro (40 vagas)', -12.9685, -38.5105, 'Zona Azul'),
            ('Rua da Holanda (46 vagas)', -12.9718, -38.5108, 'Zona Azul'),
            ('Rua dos Ourives (25 vagas)', -12.9745, -38.5115, 'Zona Azul'),
            ('Ladeira do Bonfim (25 vagas)', -12.9225, -38.5075, 'Zona Azul'),
            ('Rua Teodózio Rodrigues de Faria (23 vagas)', -12.9215, -38.5065, 'Zona Azul'),

            # ÁREA II - CIDADE ALTA / CENTRO 
            ('Rua Comendador Bernardo Catarino (24 vagas)', -13.0031, -38.5298, 'Zona Azul'),
            ('Rua Dom Marcos Teixeira (10 vagas)', -13.0041, -38.5285, 'Zona Azul'),
            ('Rua Professor Lemos Brito (9 vagas)', -13.0051, -38.5281, 'Zona Azul'),
            ('Travessa Marquês de Leão (15 vagas)', -13.0061, -38.5281, 'Zona Azul'),
            ('Rua Miguel Burnier (10 vagas)', -13.0071, -38.5261, 'Zona Azul'),
            ('Rua Leoni Ramos (13 vagas)', -13.0081, -38.5251, 'Zona Azul'),
            ('Rua Professor Fernando Luz (19 vagas)', -13.0015, -38.5241, 'Zona Azul'),
            ('Rua Barão de Sergy (12 vagas)', -13.0025, -38.5231, 'Zona Azul'),
            ('Rua do Forte de São Diogo (24 vagas)', -13.0035, -38.5331, 'Zona Azul'),
            ('Rua Macapá (65 vagas)', -13.0045, -38.4981, 'Zona Azul'),
            ('Rua do Tingui (35 vagas)', -12.9775, -38.5061, 'Zona Azul'),
            ('Rua da Mangueira (36 vagas)', -12.9785, -38.5051, 'Zona Azul'),
            ('Praça Duque de Caxias (23 vagas)', -12.9865, -38.5171, 'Zona Azul'),
            ('Rua do Salete (15 vagas)', -12.9855, -38.5131, 'Zona Azul'),
            ('Rua da Mouraria (122 vagas)', -12.9795, -38.5111, 'Zona Azul'),
            ('Travessa Corneta Lopes (9 vagas)', -12.9805, -38.5101, 'Zona Azul'),
            ('Praça Almirante Paula Guimarães (62 vagas)', -13.0011, -38.5191, 'Zona Azul'),
            ('Rua Marechal Floriano (125 vagas)', -12.9935, -38.5195, 'Zona Azul'),
            ('Avenida Araújo Pinho (88 vagas)', -12.9925, -38.5205, 'Zona Azul'),
            ('Rua Pedro Lessa (21 vagas)', -13.0021, -38.5215, 'Zona Azul'),
            ('Rua Moreira de Pinho (31 vagas)', -13.0011, -38.5225, 'Zona Azul'),
            ('Avenida José Joaquim Seabra (135 vagas)', -12.9765, -38.5085, 'Zona Azul'),
            ('Rua Pe Agostinho Gomes (11 vagas)', -12.9755, -38.5075, 'Zona Azul'),
            ('Rua do Tabuão (25 vagas)', -12.9735, -38.5085, 'Zona Azul'),
            ('Rua General Argolo (44 vagas)', -12.9725, -38.5065, 'Zona Azul'),
            ('Rua Djalma Dutra (24 vagas)', -12.9695, -38.5035, 'Zona Azul'),
            ('Rua Professor Hugo Balthazar da Silveira (78 vagas)', -12.9685, -38.5025, 'Zona Azul'),
            ('Avenida Presidente Costa e Silva (82 vagas)', -12.9785, -38.5025, 'Zona Azul'),
            ('Rua Santa Clara (36 vagas)', -12.9795, -38.5015, 'Zona Azul'),
            ('Avenida Vasco da Gama (120 vagas)', -12.9922, -38.5035, 'Zona Azul'),
            ('Avenida Mário Leal Ferreira (50 vagas)', -12.9815, -38.4895, 'Zona Azul'),
            ('Rua Professora Anfrísia Santiago (40 vagas)', -12.9791, -38.5041, 'Zona Azul'),
            ('Avenida Presidente Castelo Branco (110 vagas)', -12.9671, -38.5051, 'Zona Azul'),
            ('Travessa Marquês de Barbacena (83 vagas)', -12.9721, -38.5091, 'Zona Azul'),
            ('Ladeira da Fonte das Pedras (31 vagas)', -12.9791, -38.5021, 'Zona Azul'),
            ('Rua Politeama (23 vagas)', -12.9855, -38.5185, 'Zona Azul'),
            ('Largo do Campo Grande (99 vagas)', -12.9841, -38.5195, 'Zona Azul'),
            ('Largo Terreiro de Jesus (24 vagas)', -12.9722, -38.5105, 'Zona Azul'),
            ('Ladeira da Praça (80 vagas)', -12.9761, -38.5125, 'Zona Azul'),
            ('Avenida Almirante Marques de Leão (159 vagas)', -13.0041, -38.5285, 'Zona Azul'),
            ('Rua Airosa Galvão (20 vagas)', -13.0031, -38.5255, 'Zona Azul'),
            ('Rua Alfredo Magalhães (18 vagas)', -13.0021, -38.5275, 'Zona Azul'),
            ('Avenida Princesa Leopoldina (101 vagas)', -12.9975, -38.5245, 'Zona Azul'),
            ('Rua Professor Sabino Silva (336 vagas)', -13.0045, -38.5185, 'Zona Azul'),
            ('Avenida Anita Garibaldi (258 vagas)', -13.0025, -38.5085, 'Zona Azul'),
            ('Rua Eduardo José dos Santos (25 vagas)', -12.9985, -38.4915, 'Zona Azul'),
            ('Avenida Vale dos Barris (110 vagas)', -12.9885, -38.5125, 'Zona Azul'),
            ('Rua Professor Américo Simas (35 vagas)', -12.9725, -38.5015, 'Zona Azul'),
            ('Rua Comendador José Alves Ferreira (55 vagas)', -12.9915, -38.5235, 'Zona Azul'),
            ('Avenida Professor Paulo Almeida (30 vagas)', -12.9895, -38.5215, 'Zona Azul'),
            ('Rua José Leonídio de Sena (21 vagas)', -12.9655, -38.5035, 'Zona Azul'),
            ('Rua Professor Aristides Novis (150 vagas)', -13.0035, -38.5105, 'Zona Azul'),
            ('Avenida Reitor Miguel Calmon (70 vagas)', -12.9945, -38.5135, 'Zona Azul'),
            ('Travessa Marquês de Caravelas (150 vagas)', -13.0025, -38.5275, 'Zona Azul'),
            ('Praça Santo Antônio da Barra (24 vagas)', -13.0035, -38.5315, 'Zona Azul'),
            ('Rua Dias D’Ávila (7 vagas)', -13.0025, -38.5305, 'Zona Azul'),
            ('Rua Deocleciano Barreto (30 vagas)', -12.9965, -38.5255, 'Zona Azul'),
            ('Rua do Cabral (40 vagas)', -12.9745, -38.5075, 'Zona Azul'),
            ('Rua do Limoeiro (42 vagas)', -12.9705, -38.5085, 'Zona Azul'),
            ('Ladeira dos Galés (50 vagas)', -12.9685, -38.5045, 'Zona Azul'),
            ('Ladeira de Nazaré (40 vagas)', -12.9735, -38.5055, 'Zona Azul'),
            ('Rua Nossa Senhora de Fátima (40 vagas)', -12.9945, -38.5105, 'Zona Azul'),
            ('Avenida Oceânica (152 vagas)', -13.0085, -38.5225, 'Zona Azul'),
            ('Praça Tarquínio Gonzaga (20 vagas)', -13.0075, -38.5215, 'Zona Azul'),
            ('Forte de São Pedro (38 vagas)', -12.9865, -38.5205, 'Zona Azul'),
            ('Avenida Sete de Setembro (141 vagas)', -12.9835, -38.5215, 'Zona Azul'),
            ('Ladeira da Montanha (39 vagas)', -12.9775, -38.5145, 'Zona Azul'),
            ('Ladeira de Santana (17 vagas)', -12.9765, -38.5085, 'Zona Azul'),
            ('Rua General Labatut (30 vagas)', -12.9875, -38.5185, 'Zona Azul'),
            ('Rua São Raimundo (27 vagas)', -12.9885, -38.5145, 'Zona Azul'),
            ('Rua Carlos Gomes (30 vagas)', -12.9815, -38.5155, 'Zona Azul'),
            ('Praça General Inocêncio Galvão (61 vagas)', -12.9775, -38.5095, 'Zona Azul'),
            ('Rua do Paraíso (32 vagas)', -12.9815, -38.5125, 'Zona Azul'),
            ('Rua Dr. Arlindo de Assis (143 vagas)', -12.9955, -38.5115, 'Zona Azul'),
            ('Praça Castro Alves (11 vagas)', -12.9785, -38.5155, 'Zona Azul'),
            ('Rua Frei Vicente (18 vagas)', -12.9725, -38.5095, 'Zona Azul'),
            ('Praça Conselheiro Almeida Couto (45 vagas)', -12.9735, -38.5035, 'Zona Azul'),
            ('Rua Afonso Celso (38 vagas)', -13.0045, -38.5275, 'Zona Azul'),

            # ÁREA III - PITUBA / RIO VERMELHO / IGUATEMI 
            ('Avenida Tancredo Neves (204 vagas)', -12.9811, -38.4522, 'Zona Azul'),
            ('Rua Alceu Amoroso Lima (71 vagas)', -12.9822, -38.4533, 'Zona Azul'),
            ('Rua Guedes Cabral (25 vagas)', -13.0145, -38.4891, 'Zona Azul'),
            ('Rua Borges dos Reis (117 vagas)', -13.0132, -38.4888, 'Zona Azul'),
            ('Avenida Juracy Magalhães Júnior (725 vagas)', -12.9922, -38.4711, 'Zona Azul'),
            ('Praça Caramuru (136 vagas)', -13.0125, -38.4862, 'Zona Azul'),
            ('Largo da Mariquita (42 vagas)', -13.0138, -38.4875, 'Zona Azul'),
            ('Avenida Antônio Carlos Magalhães (606 vagas)', -12.9855, -38.4588, 'Zona Azul'),
            ('Rua do Meio (28 vagas)', -13.0115, -38.4855, 'Zona Azul'),
            ('Avenida Manoel Dias da Silva (60 vagas)', -12.9995, -38.4615, 'Zona Azul'),
            ('Rua Rio de Janeiro (125 vagas)', -12.9925, -38.4555, 'Zona Azul'),
            ('Rua das Hortênsias (212 vagas)', -12.9915, -38.4595, 'Zona Azul'),
            ('Avenida Professor Magalhães Neto (192 vagas)', -12.9885, -38.4455, 'Zona Azul'),
            ('Rua Clara Nunes (35 vagas)', -12.9875, -38.4485, 'Zona Azul'),
            ('Rua Minas Gerais (285 vagas)', -12.9945, -38.4585, 'Zona Azul'),
            ('Avenida Miguel Navarro y Cañizares (238 vagas)', -12.9965, -38.4625, 'Zona Azul'),
            ('Rua São Paulo (38 vagas)', -12.9955, -38.4605, 'Zona Azul'),
            ('Rua Alexandre Herculano (50 vagas)', -12.9935, -38.4615, 'Zona Azul'),
            ('Rua Professor Leopoldo Amaral (32 vagas)', -12.9925, -38.4635, 'Zona Azul'),
            ('Alameda Benevento (28 vagas)', -12.9845, -38.4495, 'Zona Azul'),
            ('Rua Edith Mendes da Gama e Abreu (40 vagas)', -12.9855, -38.4515, 'Zona Azul'),
            ('Rua Coronel Almerindo Rehem (97 vagas)', -12.9835, -38.4515, 'Zona Azul'),
            ('Rua Soldado Luis Gonzaga das Virgens (25 vagas)', -12.9825, -38.4505, 'Zona Azul'),
            ('Rua da Alfazema (19 vagas)', -12.9815, -38.4495, 'Zona Azul'),
            ('Rua João Gomes (13 vagas)', -13.0125, -38.4905, 'Zona Azul'),
            ('Praça Brigadeiro Faria Rocha (16 vagas)', -13.0115, -38.4915, 'Zona Azul'),
            ('Travessa Basílio de Magalhães (10 vagas)', -13.0105, -38.4925, 'Zona Azul'),
            ('Rua Vieira Lopes (9 vagas)', -13.0115, -38.4885, 'Zona Azul'),
            ('Rua Doutor Eduardo Bahiana (147 vagas)', -12.9905, -38.4435, 'Zona Azul'),
            ('Rua Manoel Filomeno de Miranda (37 vagas)', -12.9895, -38.4425, 'Zona Azul'),
            ('Rua Professor Carlos Sá (18 vagas)', -12.9885, -38.4435, 'Zona Azul'),
            ('Travessa Magno Valente (15 vagas)', -12.9875, -38.4415, 'Zona Azul'),
            ('Rua Desembargador Álvaro Clemente de Oliveira (71 vagas)', -12.9865, -38.4425, 'Zona Azul'),
            ('Rua Magno Valente (151 vagas)', -12.9875, -38.4405, 'Zona Azul'),
            ('Alameda dos Eucaliptos (38 vagas)', -12.9855, -38.4455, 'Zona Azul'),
            ('Rua Frederico Simões (111 vagas)', -12.9815, -38.4505, 'Zona Azul'),
            ('Alameda dos Umbuzeiros (96 vagas)', -12.9845, -38.4465, 'Zona Azul'),
            ('Rua Anísio Teixeira (149 vagas)', -12.9895, -38.4555, 'Zona Azul'),
            ('Acesso dos Rodoviários (29 vagas)', -12.9795, -38.4595, 'Zona Azul'),
            ('Jardim dos Namorados (761 vagas)', -12.9935, -38.4425, 'Zona Azul'),
            ('Rua Canavieiras (20 vagas)', -13.0085, -38.4855, 'Zona Azul'),
            ('Rua Potiguares (50 vagas)', -13.0075, -38.4845, 'Zona Azul'),
            ('Rua Itabuna (120 vagas)', -13.0065, -38.4835, 'Zona Azul'),
            ('Praça Carlos Batalha (10 vagas)', -13.0055, -38.4825, 'Zona Azul'),
            ('Rua Ilhéus (110 vagas)', -13.0045, -38.4815, 'Zona Azul'),
            ('Rua José Taboada Vidal (10 vagas)', -13.0035, -38.4805, 'Zona Azul'),
            ('Rua da Fonte do Boi (60 vagas)', -13.0115, -38.4865, 'Zona Azul'),
            ('Travessa Álvaro Clemente (9 vagas)', -12.9865, -38.4435, 'Zona Azul'),
            ('Rua Itatuba (32 vagas)', -13.0055, -38.4805, 'Zona Azul'),
            ('Rua Juazeiro (60 vagas)', -13.0045, -38.4795, 'Zona Azul'),
            ('Rua Alagoinhas (120 vagas)', -13.0035, -38.4785, 'Zona Azul'),
            ('Rua Paraíba (9 vagas)', -12.9985, -38.4575, 'Zona Azul'),
            ('Rua Piauí (23 vagas)', -12.9975, -38.4565, 'Zona Azul'),
            ('Rua Goiás (18 vagas)', -12.9965, -38.4555, 'Zona Azul'),

            # ÁREA IV - PITUAÇU / BOCA DO RIO / IMBUI 
            ('Avenida Jorge Amado (20 vagas)', -12.9655, -38.4185, 'Zona Azul'),
            ('Rua das Araras (83 vagas)', -12.9642, -38.4231, 'Zona Azul'),
            ('Rua Alberto Fiuza (180 vagas)', -12.9668, -38.4255, 'Zona Azul'),
            ('Rua Adhemar Pinheiro Lemos (275 vagas)', -12.9725, -38.4155, 'Zona Azul'),
            ('Avenida Octávio Mangabeira - Orla (1.476 vagas)', -12.9755, -38.4125, 'Zona Azul'),
            ('Rua Padre Casimiro Quiroga (185 vagas)', -12.9655, -38.4285, 'Zona Azul'),
            ('Rua Doutor José Peroba (57 vagas)', -12.9785, -38.4415, 'Zona Azul'),
            ('Rua Manoel Antônio Galvão (208 vagas)', -12.9555, -38.4015, 'Zona Azul'),
            ('Travessa Jardim de Alá (297 vagas)', -12.9915, -38.4355, 'Zona Azul'),
            ('Loteamento Patamares (193 vagas)', -12.9455, -38.3885, 'Zona Azul'),
            ('Avenida Luís Viana - Paralela (103 vagas)', -12.9485, -38.4125, 'Zona Azul'),
            ('Avenida Professor Pinto de Aguiar (183 vagas)', -12.9415, -38.3995, 'Zona Azul'),

            ('Avenida Octávio Mangabeira - Piatã (357 vagas)', -12.9525, -38.3755, 'Zona Azul'),
            ('Alameda Praia de Piatã (350 vagas)', -12.9495, -38.3685, 'Zona Azul'),
            ('Rua Aristides Milton (106 vagas)', -12.9455, -38.3585, 'Zona Azul'),
            ('Rua Mamede Paes Mendonça (34 vagas)', -12.9432, -38.3565, 'Zona Azul'),
            ('Rua Zitelmann de Oliva (40 vagas)', -12.9472, -38.3605, 'Zona Azul'),
            
            # STELLA MARIS / PRAIA DO FLAMENGO
            ('Alameda Mar del Plata (108 vagas)', -12.9355, -38.3285, 'Zona Azul'),
            ('Alameda Cabo Frio (197 vagas)', -12.9315, -38.3225, 'Zona Azul'),
            ('Rua Renato Berbert de Castro (80 vagas)', -12.9335, -38.3245, 'Zona Azul'),
            ('Rua Professor Antonio Augusto Machado (25 vagas)', -12.9385, -38.3355, 'Zona Azul'),
            ('Rua Hamilton Drummond Frank (30 vagas)', -12.9395, -38.3315, 'Zona Azul'),
            ('Alameda Bora Bora (30 vagas)', -12.9405, -38.3305, 'Zona Azul'),
            ('Alameda Martinica (26 vagas)', -12.9415, -38.3295, 'Zona Azul'),
            ('Rua Engenheiro Oswaldo Augusto da Silva (24 vagas)', -12.9425, -38.3275, 'Zona Azul'),
            ('Rua Itamari (21 vagas)', -12.9375, -38.3345, 'Zona Azul'),
            
            # LOGRADOUROS COMPLEMENTARES 
            ('Rua Cesar Reis Filho (14 vagas)', -12.9445, -38.3315, 'Zona Azul'),
            ('Rua Mario Gusmão (14 vagas)', -12.9452, -38.3325, 'Zona Azul'),
            ('Rua Dom Thomaz Murphy (14 vagas)', -12.9458, -38.3335, 'Zona Azul'),
            ('Rua Des. Antonio Herculano (14 vagas)', -12.9465, -38.3345, 'Zona Azul'),
            ('Rua Prof. Dalmo Pontual (30 vagas)', -12.9485, -38.3355, 'Zona Azul')
        ]
        

        cursor.execute("DELETE FROM locais")
        
        cursor.executemany(
            'INSERT INTO locais (nome, lat, lng, tipo) VALUES (?, ?, ?, ?)', bahia_park +
            zonas_azuis_salvador
        )
        
        conn.commit()
        conn.close()
        print(f"✅ SUCESSO: {len(bahia_park)} locais do Bahia Park e {len(zonas_azuis_salvador)} áreas de Salvador inseridos em {DB_PATH}")
        
    except Exception as e:
        print(f"❌ ERRO CRÍTICO: {e}")

if __name__ == "__main__":
    seed_data()