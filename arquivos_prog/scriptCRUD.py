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
    "PWD=YourComplexPassword123!;"  # Substitua pela sua senha real
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

try:
    # Conectar com o banco de dados
    connection = pyodbc.connect(connection_string)

    # Criando o cursor para manipular o connection de dados
    cursor = connection.cursor()

    # ------------------------- FUNÇÕES -------------------------#

    def salvar_alteracoes():
        connection.commit()

    def mostrar_dados(tabela):
        cursor.execute(f'SELECT * FROM {tabela}')
        resultados = cursor.fetchall()
        # Salvar os resultados em uma lista de listas
        lista_de_listas = [list(row) for row in resultados]

        # Exibir os resultados
        for lista in lista_de_listas:
            print(lista)

    # ---------------------- CREATE TABLES ----------------------#

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
        ('Dr. Fernando Almeida', 'SP12345', 'Ortodontia', '11987654321', 'dr.fernando.almeida@gmail.com'),
        ('Dra. Camila Silva', 'SP54321', 'Endodontia', '11976543210', 'dra.camila.silva@gmail.com'),
        ('Dr. Ricardo Mendes', 'SP67890', 'Implantodontia', '11965432109', 'dr.ricardo.mendes@gmail.com'),
        ('Dra. Juliana Santos', 'SP09876', 'Prótese Dentária', '11954321098', 'dra.juliana.santos@gmail.com'),
        ('Dr. Paulo Oliveira', 'SP11223', 'Periodontia', '11943210987', 'dr.paulo.oliveira@gmail.com');
        ''')

    def inserindo_dados_iniciais_consultas():
        cursor.execute('''
        INSERT INTO Consultas (PacienteID, DentistaID, DataHora, Motivo) VALUES
        (1, 1, '2023-05-10 09:00', 'Avaliação inicial'),
        (2, 2, '2023-05-11 10:00', 'Tratamento de canal'),
        (3, 3, '2023-05-12 11:00', 'Implante dentário'),
        (4, 4, '2023-05-13 14:00', 'Prótese dentária'),
        (5, 5, '2023-05-14 15:00', 'Limpeza'),
        (6, 1, '2023-05-15 09:00', 'Aparelho ortodôntico'),
        (7, 2, '2023-05-16 10:00', 'Tratamento de canal'),
        (8, 3, '2023-05-17 11:00', 'Implante dentário'),
        (9, 4, '2023-05-18 14:00', 'Prótese dentária'),
        (10, 5, '2023-05-19 15:00', 'Limpeza');
        ''')

    def inserindo_dados_iniciais_tratamentos():
        cursor.execute('''
        INSERT INTO Tratamentos (Descricao, Custo) VALUES
        ('Tratamento de Canal', 1200.00),
        ('Implante Dentário', 3500.00),
        ('Prótese Dentária', 1500.00),
        ('Aparelho Ortodôntico', 2500.00),
        ('Limpeza', 200.00);
        ''')

    def inserindo_dados_iniciais_prontuarios():
        cursor.execute('''
        INSERT INTO Prontuarios (PacienteID, DentistaID, Data, Diagnostico, TratamentoID, Observacoes) VALUES
        (1, 1, '2023-05-10', 'Cárie em dente molar', 1, 'Paciente deverá retornar em 1 mês'),
        (2, 2, '2023-05-11', 'Necrose pulpar', 1, 'Canal finalizado com sucesso'),
        (3, 3, '2023-05-12', 'Perda de dente', 2, 'Implante realizado'),
        (4, 4, '2023-05-13', 'Fratura dentária', 3, 'Prótese instalada'),
        (5, 5, '2023-05-14', 'Gengivite', 5, 'Recomendado uso de antisséptico bucal'),
        (6, 1, '2023-05-15', 'Mordida cruzada', 4, 'Aparelho instalado'),
        (7, 2, '2023-05-16', 'Cárie profunda', 1, 'Tratamento de canal realizado'),
        (8, 3, '2023-05-17', 'Ausência de dente', 2, 'Implante realizado com sucesso'),
        (9, 4, '2023-05-18', 'Desgaste dentário', 3, 'Prótese colocada'),
        (10, 5, '2023-05-19', 'Tártaro', 5, 'Limpeza realizada, paciente orientado sobre higiene bucal');
        ''')

    def inserindo_dados_iniciais_pagamentos():
        cursor.execute('''
        INSERT INTO Pagamentos (PacienteID, Valor, DataPagamento, MetodoPagamento) VALUES
        (1, 1200.00, '2023-05-10', 'Cartão de Crédito'),
        (2, 1500.00, '2023-05-11', 'Boleto Bancário'),
        (3, 3500.00, '2023-05-12', 'Transferência Bancária'),
        (4, 200.00, '2023-05-13', 'Dinheiro'),
        (5, 2500.00, '2023-05-14', 'Cartão de Débito'),
        (6, 1200.00, '2023-05-15', 'Cartão de Crédito'),
        (7, 1500.00, '2023-05-16', 'Boleto Bancário'),
        (8, 3500.00, '2023-05-17', 'Transferência Bancária'),
        (9, 200.00, '2023-05-18', 'Dinheiro'),
        (10, 2500.00, '2023-05-19', 'Cartão de Débito');
        ''')

    def inserindo_dados_iniciais_agendas():
        cursor.execute('''
        INSERT INTO Agendas (DentistaID, DataHora, Disponivel) VALUES
        (1, '2023-05-10 09:00', 0),
        (2, '2023-05-11 10:00', 0),
        (3, '2023-05-12 11:00', 0),
        (4, '2023-05-13 14:00', 0),
        (5, '2023-05-14 15:00', 0),
        (1, '2023-05-15 09:00', 0),
        (2, '2023-05-16 10:00', 0),
        (3, '2023-05-17 11:00', 0),
        (4, '2023-05-18 14:00', 0),
        (5, '2023-05-19 15:00', 0);
        ''')

    def inserindo_dados_iniciais_receitas():
        cursor.execute('''
        INSERT INTO Receitas (PacienteID, Valor, DataReceita, Descricao) VALUES
        (1, 1200.00, '2023-05-10', 'Receita 1'),
        (2, 1500.00, '2023-05-11', 'Receita 2'),
        (3, 3500.00, '2023-05-12', 'Receita 3'),
        (4, 200.00, '2023-05-13', 'Receita 4'),
        (5, 2500.00, '2023-05-14', 'Receita 5'),
        (6, 1200.00, '2023-05-15', 'Receita 6'),
        (7, 1500.00, '2023-05-16', 'Receita 7'),
        (8, 3500.00, '2023-05-17', 'Receita 8'),
        (9, 200.00, '2023-05-18', 'Receita 9'),
        (10, 2500.00, '2023-05-19', 'Receita 10');
        ''')

    # ---------------------- DELETE TABLES ----------------------#

    def tirando_todas_as_tabelas():
        cursor.execute('DROP TABLE IF EXISTS Pacientes')
        cursor.execute('DROP TABLE IF EXISTS Dentistas')
        cursor.execute('DROP TABLE IF EXISTS Consultas')
        cursor.execute('DROP TABLE IF EXISTS Tratamentos')
        cursor.execute('DROP TABLE IF EXISTS Prontuarios')
        cursor.execute('DROP TABLE IF EXISTS Pagamentos')
        cursor.execute('DROP TABLE IF EXISTS Agendas')
        cursor.execute('DROP TABLE IF EXISTS Receitas')

    def tirando_tabela(tabela):
        cursor.execute(f'DROP TABLE {tabela}')

    # -------------------- RODANDO CÓDIGO -----------------------#

    # Utilize as funções abaixo para rodar o código

    # mostrar_dados('Pacientes')

    # -------------------------------------------------------#

except pyodbc.Error as e:
    print("Error: ", e)
finally:
    if 'connection' in locals():
        connection.close()
