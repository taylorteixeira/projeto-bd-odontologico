DROP TABLE Pacientes
DROP TABLE Dentistas
DROP TABLE Consultas
DROP TABLE Tratamentos
DROP TABLE Prontuarios
DROP TABLE Pagamentos
DROP TABLE Agendas
DROP TABLE Receitas
go

SELECT * FROM Pacientes
SELECT * FROM Dentistas
SELECT * FROM Consultas
SELECT * FROM Tratamentos
SELECT * FROM Prontuarios
SELECT * FROM Pagamentos
SELECT * FROM Agendas
SELECT * FROM Receitas
go

CREATE TABLE Pacientes (
    PacienteID INT IDENTITY PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    DataNascimento DATE NOT NULL,
    Sexo CHAR(1),
    Endereco VARCHAR(200),
    Telefone VARCHAR(15),
    Email VARCHAR(100)
);

CREATE TABLE Dentistas (
    DentistaID INT IDENTITY PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    CRO VARCHAR(20) NOT NULL UNIQUE,  -- Conselho Regional de Odontologia
    Especialidade VARCHAR(50),
    Telefone VARCHAR(15),
    Email VARCHAR(100)
);

CREATE TABLE Consultas (
    ConsultaID INT IDENTITY PRIMARY KEY,
    PacienteID INT,
    DentistaID INT,
    DataHora DATETIME NOT NULL,
    Motivo VARCHAR(255),
    FOREIGN KEY (PacienteID) REFERENCES Pacientes(PacienteID),
    FOREIGN KEY (DentistaID) REFERENCES Dentistas(DentistaID)
);

CREATE TABLE Tratamentos (
    TratamentoID INT IDENTITY PRIMARY KEY,
    Descricao VARCHAR(255) NOT NULL,
    Custo DECIMAL(10, 2)
);

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

CREATE TABLE Pagamentos (
    PagamentoID INT IDENTITY PRIMARY KEY,
    PacienteID INT,
    Valor DECIMAL(10, 2) NOT NULL,
    DataPagamento DATE NOT NULL,
    MetodoPagamento VARCHAR(50),
    FOREIGN KEY (PacienteID) REFERENCES Pacientes(PacienteID)
);

CREATE TABLE Agendas (
    AgendaID INT IDENTITY PRIMARY KEY,
    DentistaID INT,
    DataHora DATETIME NOT NULL,
    Disponivel bit NOT NULL,
    FOREIGN KEY (DentistaID) REFERENCES Dentistas(DentistaID)
);

CREATE TABLE Receitas (
    ReceitaID INT IDENTITY PRIMARY KEY,
    PacienteID INT,
    Valor DECIMAL(10, 2) NOT NULL,
    DataReceita DATE NOT NULL,
    Descricao VARCHAR(255),
    FOREIGN KEY (PacienteID) REFERENCES Pacientes(PacienteID)
);