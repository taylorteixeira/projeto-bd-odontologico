# ----------------------- IMPORTAÇÕES -----------------------#

#cmd: pip install pyodbc
import pyodbc

# ----------------------- FUNDAMENTOS -----------------------#

#comando 'pyodbc.connect' para conectar com o banco de dados
#exemplo: connection = pyodbc.connect('bancodedados.db') ou pyodbc.connect(algumaconexao)

#comando 'cursor' para manipular o banco de dados, sempre que chamar o cursor, ele chamará o banco de dados
#exemplo: cursor = connection.cursor()

#comando 'connection.commit()' para salvar as alterações
#exemplo: connection.commit()

#comando 'cursor.fetchall()' para pegar todos os dados
#exemplo: print(cursor.fetchall())

#comando 'cursor.execute' para executar comandos SQL
#exemplo: cursor.execute("CREATE TABLE table (coluna1 typecoluna1, coluna2 typecoluna2, coluna3 typecoluna3)")

#comando 'connection.close()' para fechar o banco de dados ao final do código
#exemplo: connection.close()

# ------------------------- INÍCIO --------------------------#

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost,1433;"
    "UID=sa;"
    "PWD=YourComplexPassword123!;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

# Conectar com o banco de dados/ Criar o banco de dados
connection = pyodbc.connect(connection_string)

# Criando o cursor para manipular o connection de dados
cursor = connection.cursor()

# ------------------------- FUNÇÕES -------------------------#

def salvar_alteracoes():
    connection.commit()

def mostrar_dados():
    # print(cursor.fetchall()) 
    resultados = cursor.fetchall()
    # Salvar os resultados em uma lista de listas
    lista_de_listas = [list(row) for row in resultados]

    # Exibir os resultados
    for lista in lista_de_listas:
        print(lista)

# ---------------------- CREATE TABLES ----------------------#


# Função para criar todas as tabelas ao mesmo tempo, caso queira criar uma tabela específica, basta chamar a função específica
def criando_todas_as_tabelas():
    criando_tabela_pacientes()
    criando_tabela_dentistas()
    criando_tabela_consultas()
    criando_tabela_tratamentos()
    criando_tabela_prontuarios()
    criando_tabela_pagamentos()
    criando_tabela_agendas()
    criando_tabela_receitas()


def criando_tabela_pacientes():
    cursor.execute('''
    CREATE TABLE Pacientes (
    PacienteID INT IDENTITY PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    DataNascimento DATE NOT NULL,
    Sexo CHAR(1),
    Endereco VARCHAR(200),
    Telefone VARCHAR(15),
    Email VARCHAR(100)
);
''')   
    
def criando_tabela_dentistas(): 
    cursor.execute('''
    CREATE TABLE Dentistas (
    DentistaID INT IDENTITY PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    CRO VARCHAR(20) NOT NULL UNIQUE,  -- Conselho Regional de Odontologia
    Especialidade VARCHAR(50),
    Telefone VARCHAR(15),
    Email VARCHAR(100)
);
''')
    
def criando_tabela_consultas():
    cursor.execute('''
    CREATE TABLE Consultas (
    ConsultaID INT IDENTITY PRIMARY KEY,
    PacienteID INT,
    DentistaID INT,
    DataHora DATETIME NOT NULL,
    Motivo VARCHAR(255),
    FOREIGN KEY (PacienteID) REFERENCES Pacientes(PacienteID),
    FOREIGN KEY (DentistaID) REFERENCES Dentistas(DentistaID)
);
''')

def criando_tabela_tratamentos():
    cursor.execute('''
    CREATE TABLE Tratamentos (
    TratamentoID INT IDENTITY PRIMARY KEY,
    Descricao VARCHAR(255) NOT NULL,
    Custo DECIMAL(10, 2)
);
''')

def criando_tabela_prontuarios():
    cursor.execute('''
    CREATE TABLE Prontuarios (
    ProntuarioID INT IDENTITY PRIMARY KEY,
    PacienteID INT,
    DentistaID INT,
    Data DATETIME NOT NULL,
    Diagnostico VARCHAR(255),
    TratamentoID INT,
    Observacoes TEXT,
    FOREIGN KEY (PacienteID) REFERENCES Pacientes(PacienteID),
    FOREIGN KEY (DentistaID) REFERENCES Dentistas(DentistaID),
    FOREIGN KEY (TratamentoID) REFERENCES Tratamentos(TratamentoID)
);
''')

def criando_tabela_pagamentos():
    cursor.execute('''
    CREATE TABLE Pagamentos (
    PagamentoID INT IDENTITY PRIMARY KEY,
    PacienteID INT,
    Valor DECIMAL(10, 2) NOT NULL,
    DataPagamento DATE NOT NULL,
    MetodoPagamento VARCHAR(50),
    FOREIGN KEY (PacienteID) REFERENCES Pacientes(PacienteID)
);
''')

def criando_tabela_agendas():
    cursor.execute('''
    CREATE TABLE Agendas (
    AgendaID INT IDENTITY PRIMARY KEY,
    DentistaID INT,
    DataHora DATETIME NOT NULL,
    Disponivel bit NOT NULL,
    FOREIGN KEY (DentistaID) REFERENCES Dentistas(DentistaID)
);
''')

def criando_tabela_receitas():
    cursor.execute('''
    CREATE TABLE Receitas (
    ReceitaID INT IDENTITY PRIMARY KEY,
    PacienteID INT,
    Valor DECIMAL(10, 2) NOT NULL,
    DataReceita DATE NOT NULL,
    Descricao VARCHAR(255),
    FOREIGN KEY (PacienteID) REFERENCES Pacientes(PacienteID)
);
''')


# -------------------- INSERT INTO TABLES --------------------#


# Função para inserir todos os dados iniciais ao mesmo tempo, caso queira inserir dados em uma tabela específica, basta chamar a função específica
def inserindo_todos_os_dados_iniciais():
    inserindo_dados_iniciais_pacientes()
    inserindo_dados_iniciais_dentistas()
    inserindo_dados_iniciais_consultas()
    inserindo_dados_iniciais_tratamentos()
    inserindo_dados_iniciais_prontuarios()
    inserindo_dados_iniciais_pagamentos()
    inserindo_dados_iniciais_agendas()
    inserindo_dados_iniciais_receitas()


def inserindo_dados_iniciais_pacientes():
    cursor.execute('''
    INSERT INTO Pacientes (Nome, DataNascimento, Sexo, Endereco, Telefone, Email) VALUES
    ('João Silva', '1985-06-15', 'M', 'Rua das Flores, 123', '11987654321', 'joao.silva@gmail.com'),
    ('Maria Oliveira', '1990-04-25', 'F', 'Av. Paulista, 456', '11976543210', 'maria.oliveira@gmail.com'),
    ('Carlos Santos', '1978-11-30', 'M', 'Rua das Laranjeiras, 789', '11965432109', 'carlos.santos@gmail.com'),
    ('Ana Costa', '1982-08-20', 'F', 'Rua dos Pinheiros, 101', '11954321098', 'ana.costa@gmail.com'),
    ('Pedro Martins', '1995-12-10', 'M', 'Rua da Glória, 202', '11943210987', 'pedro.martins@gmail.com'),
    ('Fernanda Almeida', '1986-07-11', 'F', 'Rua dos Jacarandás, 321', '11932109876', 'fernanda.almeida@gmail.com'),
    ('Paulo Rodrigues', '1975-05-09', 'M', 'Av. Liberdade, 654', '11921098765', 'paulo.rodrigues@gmail.com'),
    ('Clara Mendes', '1992-03-17', 'F', 'Rua das Palmeiras, 888', '11910987654', 'clara.mendes@gmail.com'),
    ('Ricardo Pereira', '1988-12-22', 'M', 'Rua dos Lírios, 777', '11909876543', 'ricardo.pereira@gmail.com'),
    ('Juliana Freitas', '1991-11-19', 'F', 'Rua das Rosas, 999', '11998765432', 'juliana.freitas@gmail.com');
    ''')

def inserindo_dados_iniciais_dentistas():
    cursor.execute('''
    INSERT INTO Dentistas (Nome, CRO, Especialidade, Telefone, Email) VALUES
    ('Dr. Fernando Almeida', 'SP12345', 'Ortodontia', '11987654322', 'fernando.almeida@clinica.com'),
    ('Dra. Paula Souza', 'SP54321', 'Endodontia', '11987654323', 'paula.souza@clinica.com'),
    ('Dr. Ricardo Lima', 'SP67890', 'Periodontia', '11987654324', 'ricardo.lima@clinica.com'),
    ('Dra. Juliana Mendes', 'SP09876', 'Odontopediatria', '11987654325', 'juliana.mendes@clinica.com'),
    ('Dr. Gustavo Ferreira', 'SP13579', 'Implantodontia', '11987654326', 'gustavo.ferreira@clinica.com'),
    ('Dra. Mariana Lima', 'SP24680', 'Prótese Dentária', '11987654327', 'mariana.lima@clinica.com'),
    ('Dr. Rafael Moreira', 'SP97531', 'Dentística', '11987654328', 'rafael.moreira@clinica.com'),
    ('Dra. Sofia Costa', 'SP86420', 'Patologia Bucal', '11987654329', 'sofia.costa@clinica.com');
    ''')

def inserindo_dados_iniciais_consultas():
    cursor.execute('''      
    INSERT INTO Consultas (PacienteID, DentistaID, DataHora, Motivo) VALUES
    (1, 1, '2024-06-12 09:00:00', 'Consulta de rotina'),
    (2, 2, '2024-06-12 10:00:00', 'Dor de dente'),
    (3, 3, '2024-06-12 11:00:00', 'Gengivite'),
    (4, 4, '2024-06-12 14:00:00', 'Consulta de rotina'),
    (5, 5, '2024-06-12 15:00:00', 'Implante dentário'),
    (6, 6, '2024-06-13 09:30:00', 'Prótese dentária'),
    (7, 7, '2024-06-13 10:30:00', 'Restauração dental'),
    (8, 8, '2024-06-13 11:30:00', 'Lesão na boca'),
    (9, 1, '2024-06-14 09:00:00', 'Consulta de rotina'),
    (10, 2, '2024-06-14 10:00:00', 'Dor de dente');
    ''')

def inserindo_dados_iniciais_tratamentos():
    cursor.execute('''
    INSERT INTO Tratamentos (Descricao, Custo) VALUES
    ('Limpeza Dentária', 200.00),
    ('Canal Radicular', 800.00),
    ('Extração de Dente', 300.00),
    ('Clareamento Dental', 1000.00),
    ('Implante Dentário', 3000.00),
    ('Prótese Dentária', 2500.00),
    ('Restauração Dental', 500.00),
    ('Tratamento de Gengivite', 600.00),
    ('Ortodontia (Aparelho)', 3500.00),
    ('Odontopediatria (Consulta)', 150.00);
    ''')

def inserindo_dados_iniciais_prontuarios():
    cursor.execute('''
    INSERT INTO Prontuarios (PacienteID, DentistaID, Data, Diagnostico, TratamentoID, Observacoes) VALUES
    (1, 1, '2024-06-12 09:00:00', 'Boa saúde bucal', 1, 'Paciente em boas condições.'),
    (2, 2, '2024-06-12 10:00:00', 'Cárie dentária', 2, 'Recomendada realização de canal.'),
    (3, 3, '2024-06-12 11:00:00', 'Gengivite', 3, 'Necessária extração de dente.'),
    (4, 4, '2024-06-12 14:00:00', 'Boa saúde bucal', 1, 'Paciente em boas condições.'),
    (5, 5, '2024-06-12 15:00:00', 'Perda de dente', 5, 'Realizar implante dentário.'),
    (6, 6, '2024-06-13 09:30:00', 'Dente quebrado', 6, 'Colocar prótese.'),
    (7, 7, '2024-06-13 10:30:00', 'Cárie', 7, 'Restauração necessária.'),
    (8, 8, '2024-06-13 11:30:00', 'Lesão benigna', 8, 'Acompanhamento.'),
    (9, 1, '2024-06-14 09:00:00', 'Boa saúde bucal', 1, 'Paciente em boas condições.'),
    (10, 2, '2024-06-14 10:00:00', 'Cárie dentária', 2, 'Recomendada realização de canal.');
    ''')

def inserindo_dados_iniciais_pagamentos():
    cursor.execute('''
    INSERT INTO Pagamentos (PacienteID, Valor, DataPagamento, MetodoPagamento) VALUES
    (1, 200.00, '2024-06-12', 'Cartão de Crédito'),
    (2, 800.00, '2024-06-12', 'Dinheiro'),
    (3, 300.00, '2024-06-12', 'Cartão de Débito'),
    (4, 200.00, '2024-06-12', 'Cartão de Crédito'),
    (5, 3000.00, '2024-06-12', 'Transferência Bancária'),
    (6, 2500.00, '2024-06-13', 'Cartão de Crédito'),
    (7, 500.00, '2024-06-13', 'Dinheiro'),
    (8, 600.00, '2024-06-13', 'Cartão de Débito'),
    (9, 200.00, '2024-06-14', 'Cartão de Crédito'),
    (10, 800.00, '2024-06-14', 'Dinheiro');
    ''')

def inserindo_dados_iniciais_agendas():
    cursor.execute('''
    INSERT INTO Agendas (DentistaID, DataHora, Disponivel) VALUES
    (1, '2024-06-13 09:00:00', 0),
    (2, '2024-06-13 10:00:00', 1),
    (3, '2024-06-13 11:00:00', 1),
    (4, '2024-06-13 14:00:00', 0),
    (5, '2024-06-13 15:00:00', 0),
    (6, '2024-06-14 09:30:00', 1),
    (7, '2024-06-14 10:30:00', 1),
    (8, '2024-06-14 11:30:00', 1),
    (1, '2024-06-15 09:00:00', 1),
    (2, '2024-06-15 10:00:00', 1);
    ''')

def inserindo_dados_iniciais_receitas():
    cursor.execute('''
    INSERT INTO Receitas (PacienteID, Valor, DataReceita, Descricao) VALUES
    (1, 200.00, '2024-06-12', 'Limpeza Dentária'),
    (2, 800.00, '2024-06-12', 'Tratamento de Canal'),
    (3, 300.00, '2024-06-12', 'Extração de Dente'),
    (4, 200.00, '2024-06-12', 'Limpeza Dentária'),
    (5, 3000.00, '2024-06-12', 'Implante Dentário'),
    (6, 2500.00, '2024-06-13', 'Prótese Dentária'),
    (7, 500.00, '2024-06-13', 'Restauração Dental'),
    (8, 600.00, '2024-06-13', 'Tratamento de Gengivite'),
    (9, 200.00, '2024-06-14', 'Limpeza Dentária'),
    (10, 800.00, '2024-06-14', 'Tratamento de Canal');
    ''')


# ---------------------- DELETE TABLES ----------------------#


def tirando_tabelas(tabela):
    cursor.execute(f'''
    DROP TABLE {tabela}
''')


# ------------------- UTILIZAÇÃO DE COMANDOS ----------------#

#Utilize os comandos aqui

# criando_tabela_agendas()
# inserindo_dados_iniciais_agendas()

# tirando_tabelas("agendas")







# ------------------- EXECUÇÃO E FECHAMENTO ------------------#

salvar_alteracoes()

connection.close()

#=============================================================#
#=============================================================#
