-- Remover tabelas se existirem
DROP TABLE IF EXISTS Pacientes;
DROP TABLE IF EXISTS Dentistas;
DROP TABLE IF EXISTS Consultas;
DROP TABLE IF EXISTS Tratamentos;
DROP TABLE IF EXISTS Prontuarios;
DROP TABLE IF EXISTS Pagamentos;
DROP TABLE IF EXISTS Agendas;
DROP TABLE IF EXISTS Receitas;
GO

-- Criação das tabelas
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
    Custo DECIMAL(10, 2)
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

-- Inserção de dados nas tabelas
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
GO

INSERT INTO Dentistas (Nome, CRO, Especialidade, Telefone, Email) VALUES
('Dr. Fernando Almeida', 'SP12345', 'Ortodontia', '11987654322', 'fernando.almeida@clinica.com'),
('Dra. Paula Souza', 'SP54321', 'Endodontia', '11987654323', 'paula.souza@clinica.com'),
('Dr. Ricardo Lima', 'SP67890', 'Periodontia', '11987654324', 'ricardo.lima@clinica.com'),
('Dra. Juliana Mendes', 'SP09876', 'Odontopediatria', '11987654325', 'juliana.mendes@clinica.com'),
('Dr. Gustavo Ferreira', 'SP13579', 'Implantodontia', '11987654326', 'gustavo.ferreira@clinica.com'),
('Dra. Mariana Lima', 'SP24680', 'Prótese Dentária', '11987654327', 'mariana.lima@clinica.com'),
('Dr. Rafael Moreira', 'SP97531', 'Dentística', '11987654328', 'rafael.moreira@clinica.com'),
('Dra. Sofia Costa', 'SP86420', 'Patologia Bucal', '11987654329', 'sofia.costa@clinica.com');
GO

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
GO

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
GO

INSERT INTO Prontuarios (PacienteID, DentistaID, Data, Diagnostico, TratamentoID, Observacoes) VALUES
(1, 1, '2024-06-12 09:00:00', 'Boa saúde bucal', 1, 'Paciente em boas condições.'),
(2, 2, '2024-06-12 10:00:00', 'Cárie dentária', 2, 'Recomendada realização de canal.'),
(3, 3, '2024-06-12 11:00:00', 'Gengivite', 3, 'Necessária extração de dente.'),
(4, 4, '2024-06-12 14:00:00', 'Boa saúde bucal', 1, 'Paciente em boas condições.'),
(5, 5, '2024-06-12 15:00:00', 'Perda de dente', 5, 'Recomendada colocação de implante.'),
(6, 6, '2024-06-13 09:30:00', 'Dente quebrado', 6, 'Necessária colocação de prótese.'),
(7, 7, '2024-06-13 10:30:00', 'Cárie dentária', 7, 'Recomendada restauração.'),
(8, 8, '2024-06-13 11:30:00', 'Lesão na boca', 8, 'Tratamento necessário para gengivite.'),
(9, 1, '2024-06-14 09:00:00', 'Boa saúde bucal', 1, 'Paciente em boas condições.'),
(10, 2, '2024-06-14 10:00:00', 'Cárie dentária', 2, 'Recomendada realização de canal.');
GO

INSERT INTO Pagamentos (PacienteID, Valor, DataPagamento, MetodoPagamento) VALUES
(1, 200.00, '2024-06-12', 'Cartão de Crédito'),
(2, 800.00, '2024-06-12', 'Dinheiro'),
(3, 300.00, '2024-06-12', 'Cartão de Débito'),
(4, 200.00, '2024-06-12', 'Cartão de Crédito'),
(5, 3000.00, '2024-06-12', 'Transferência Bancária'),
(6, 2500.00, '2024-06-13', 'Cartão de Crédito'),
(7, 500.00, '2024-06-13', 'Cartão de Débito'),
(8, 600.00, '2024-06-13', 'Dinheiro'),
(9, 200.00, '2024-06-14', 'Cartão de Crédito'),
(10, 800.00, '2024-06-14', 'Dinheiro');
GO

INSERT INTO Agendas (PacienteID, DentistaID, DataHoraInicio, DataHoraFim, Disponivel) VALUES
(1, 1, '2024-06-12 09:00:00', '2024-06-12 09:30:00', 0),
(2, 2, '2024-06-12 10:00:00', '2024-06-12 10:30:00', 0),
(3, 3, '2024-06-12 11:00:00', '2024-06-12 11:30:00', 0),
(4, 4, '2024-06-12 14:00:00', '2024-06-12 14:30:00', 0),
(5, 5, '2024-06-12 15:00:00', '2024-06-12 15:30:00', 0),
(6, 6, '2024-06-13 09:30:00', '2024-06-13 10:00:00', 0),
(7, 7, '2024-06-13 10:30:00', '2024-06-13 11:00:00', 0),
(8, 8, '2024-06-13 11:30:00', '2024-06-13 12:00:00', 0),
(9, 1, '2024-06-14 09:00:00', '2024-06-14 09:30:00', 0),
(10, 2, '2024-06-14 10:00:00', '2024-06-14 10:30:00', 0);
GO

INSERT INTO Receitas (PacienteID, Valor, DataReceita, Descricao) VALUES
(1, 100.00, '2024-06-12', 'Consulta de rotina'),
(2, 150.00, '2024-06-12', 'Canal Radicular'),
(3, 200.00, '2024-06-12', 'Extração de Dente'),
(4, 250.00, '2024-06-12', 'Consulta de rotina'),
(5, 300.00, '2024-06-12', 'Implante Dentário'),
(6, 350.00, '2024-06-13', 'Prótese Dentária'),
(7, 400.00, '2024-06-13', 'Restauração Dental'),
(8, 450.00, '2024-06-13', 'Tratamento de Gengivite'),
(9, 500.00, '2024-06-14', 'Consulta de rotina'),
(10, 550.00, '2024-06-14', 'Canal Radicular');
GO

-- Consultas para os relatórios solicitados

-- Relatório de Prontuários de Pacientes
SELECT p.Nome AS NomePaciente, d.Nome AS NomeDentista, pr.Data, pr.Diagnostico, t.Descricao AS Tratamento, pr.Observacoes
FROM Prontuarios pr
JOIN Pacientes p ON pr.PacienteID = p.PacienteID
JOIN Dentistas d ON pr.DentistaID = d.DentistaID
JOIN Tratamentos t ON pr.TratamentoID = t.TratamentoID;
GO

-- Relatório de Pagamentos por Paciente
SELECT p.Nome AS NomePaciente, pg.Valor, pg.DataPagamento, pg.MetodoPagamento
FROM Pagamentos pg
JOIN Pacientes p ON pg.PacienteID = p.PacienteID;
GO

-- Relatório de Agendas por Dentista
SELECT d.Nome AS NomeDentista, a.DataHoraInicio, a.DataHoraFim, a.Disponivel
FROM Agendas a
JOIN Dentistas d ON a.DentistaID = d.DentistaID
WHERE a.Disponivel = 0;
GO

-- Relatório de Receitas por Data
SELECT r.DataReceita, SUM(r.Valor) AS ReceitaTotal
FROM Receitas r
GROUP BY r.DataReceita;
GO

-- Criação de um trigger para a tabela Consultas que automaticamente insere um registro na tabela Agendas quando uma nova consulta é marcada
CREATE TRIGGER trg_AfterInsertConsultas
ON Consultas
AFTER INSERT
AS
BEGIN
    DECLARE @PacienteID INT, @DentistaID INT, @DataHora DATETIME;
    
    SELECT @PacienteID = i.PacienteID, @DentistaID = i.DentistaID, @DataHora = i.DataHora
    FROM inserted i;
    
    INSERT INTO Agendas (PacienteID, DentistaID, DataHoraInicio, DataHoraFim, Disponivel)
    VALUES (@PacienteID, @DentistaID, @DataHora, DATEADD(MINUTE, 30, @DataHora), 0);
END;
GO

SELECT * FROM Agendas
SELECT * FROM Consultas

INSERT INTO Consultas (PacienteID, DentistaID, DataHora, Motivo) VALUES
(5, 1, '2024-07-12 09:00:00', 'Teste')
