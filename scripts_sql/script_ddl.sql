CREATE TABLE Pacientes (
    PacienteID INT IDENTITY PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    DataNascimento DATE NOT NULL,
    Sexo CHAR(1),
    Endereco VARCHAR(200),
    Telefone VARCHAR(15),
    Email VARCHAR(100)
);
GO

CREATE TABLE Dentistas (
    DentistaID INT IDENTITY PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    CRO VARCHAR(20) NOT NULL UNIQUE,
    Especialidade VARCHAR(50),
    Telefone VARCHAR(15),
    Email VARCHAR(100)
);
GO

CREATE TABLE Consultas (
    ConsultaID INT IDENTITY PRIMARY KEY,
    PacienteID INT,
    DentistaID INT,
    DataHora DATETIME NOT NULL,
    Motivo VARCHAR(255),
    FOREIGN KEY (PacienteID) REFERENCES Pacientes(PacienteID),
    FOREIGN KEY (DentistaID) REFERENCES Dentistas(DentistaID)
);
GO

CREATE TABLE Tratamentos (
    TratamentoID INT IDENTITY PRIMARY KEY,
    Descricao VARCHAR(255) NOT NULL,
    Custo DECIMAL(10, 2),
    DuracaoMinutos INT -- Adicionando coluna para tempo de duração do tratamento em minutos
);
GO

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
GO

CREATE TABLE Pagamentos (
    PagamentoID INT IDENTITY PRIMARY KEY,
    PacienteID INT,
    Valor DECIMAL(10, 2) NOT NULL,
    DataPagamento DATE NOT NULL,
    MetodoPagamento VARCHAR(50),
    FOREIGN KEY (PacienteID) REFERENCES Pacientes(PacienteID)
);
GO

CREATE TABLE Agendas (
    AgendaID INT IDENTITY PRIMARY KEY,
    PacienteID INT,
    DentistaID INT,
    DataHoraInicio DATETIME NOT NULL,
    DataHoraFim DATETIME NOT NULL,
    Disponivel BIT NOT NULL,
    FOREIGN KEY (DentistaID) REFERENCES Dentistas(DentistaID),
    FOREIGN KEY (PacienteID) REFERENCES Pacientes(PacienteID)
);
GO

CREATE TABLE Receitas (
    ReceitaID INT IDENTITY PRIMARY KEY,
    PacienteID INT,
    Valor DECIMAL(10, 2) NOT NULL,
    DataReceita DATE NOT NULL,
    Descricao VARCHAR(255),
    FOREIGN KEY (PacienteID) REFERENCES Pacientes(PacienteID)
);
GO
