CREATE FUNCTION FormatarDataHoraBrasileira(@datahora datetime)
RETURNS NVARCHAR(100)
AS
BEGIN
    DECLARE @data_formatada NVARCHAR(100);

    SELECT @data_formatada = CONVERT(NVARCHAR, DATEPART(day, @datahora)) + ' de ' + 
                             CASE DATEPART(month, @datahora)
                                 WHEN 1 THEN 'janeiro' WHEN 2 THEN 'fevereiro' WHEN 3 THEN 'março' 
                                 WHEN 4 THEN 'abril' WHEN 5 THEN 'maio' WHEN 6 THEN 'junho' 
                                 WHEN 7 THEN 'julho' WHEN 8 THEN 'agosto' WHEN 9 THEN 'setembro' 
                                 WHEN 10 THEN 'outubro' WHEN 11 THEN 'novembro' WHEN 12 THEN 'dezembro'
                             END + ' de ' + 
                             CONVERT(NVARCHAR, DATEPART(year, @datahora)) + ' às ' + 
                             CONVERT(NVARCHAR, DATEPART(hour, @datahora)) + ':' + 
                             RIGHT('0' + CONVERT(NVARCHAR, DATEPART(minute, @datahora)), 2);

    RETURN @data_formatada;
END;
GO

-- Trigger para inserir automaticamente na tabela Agendas
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

-- Procedimento armazenado para excluir consulta
CREATE PROCEDURE ExcluirConsulta
    @ConsultaID INT
AS
BEGIN
    DELETE FROM Consultas
    WHERE ConsultaID = @ConsultaID;
END;
GO

CREATE FUNCTION ConsultasComNomes()
RETURNS TABLE
AS
RETURN
(
    SELECT 
        C.ConsultaID,
        C.PacienteID,
        P.Nome AS NomePaciente,
        C.DentistaID,
        D.Nome AS NomeDentista,
        dbo.FormatarDataHoraBrasileira(C.DataHora) AS DataHoraFormatada,
        C.Motivo
    FROM Consultas C
    INNER JOIN Pacientes P ON C.PacienteID = P.PacienteID
    INNER JOIN Dentistas D ON C.DentistaID = D.DentistaID
);
GO

CREATE PROCEDURE InserirConsulta
    @NomePaciente VARCHAR(100),
    @NomeDentista VARCHAR(100),
    @DataHora DATETIME,
    @Motivo VARCHAR(255)
AS
BEGIN
    DECLARE @PacienteID INT;
    DECLARE @DentistaID INT;

    -- Obter PacienteID pelo Nome do Paciente
    SELECT @PacienteID = PacienteID
    FROM Pacientes
    WHERE Nome = @NomePaciente;

    -- Obter DentistaID pelo Nome do Dentista
    SELECT @DentistaID = DentistaID
    FROM Dentistas
    WHERE Nome = @NomeDentista;

    -- Inserir a consulta com os IDs obtidos
    INSERT INTO Consultas (PacienteID, DentistaID, DataHora, Motivo)
    VALUES (@PacienteID, @DentistaID, @DataHora, @Motivo);

    -- Retornar os dados da consulta recém-inserida com nomes
    SELECT *
    FROM ConsultasComNomes()
    WHERE ConsultaID = SCOPE_IDENTITY(); -- SCOPE_IDENTITY() retorna o ID da consulta inserida
END;

---- nova proc para atender o tratamento
CREATE PROCEDURE AgendarConsulta (
    @NomePaciente NVARCHAR(100),
    @NomeDentista NVARCHAR(100),
    @DataConsulta DATETIME,
    @Tratamento NVARCHAR(100)
)
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @PacienteID INT, @DentistaID INT, @TratamentoID INT;

    -- Função para obter o ID do paciente pelo nome
    CREATE FUNCTION dbo.GetPacienteID (@Nome NVARCHAR(100))
    RETURNS INT
    AS
    BEGIN
        DECLARE @ID INT;
        SELECT @ID = PacienteID FROM Pacientes WHERE Nome = @Nome;
        RETURN @ID;
    END;

    -- Função para obter o ID do dentista pelo nome
    CREATE FUNCTION dbo.GetDentistaID (@Nome NVARCHAR(100))
    RETURNS INT
    AS
    BEGIN
        DECLARE @ID INT;
        SELECT @ID = DentistaID FROM Dentistas WHERE Nome = @Nome;
        RETURN @ID;
    END;

    -- Obter IDs de paciente e dentista
    SET @PacienteID = dbo.GetPacienteID(@NomePaciente);
    SET @DentistaID = dbo.GetDentistaID(@NomeDentista);

    -- Obter ID do tratamento
    SELECT @TratamentoID = TratamentoID FROM Tratamentos WHERE Descricao = @Tratamento;

    -- Inserir na tabela de Consultas
    INSERT INTO Consultas (PacienteID, DentistaID, DataHora, Descricao)
    VALUES (@PacienteID, @DentistaID, @DataConsulta, @Tratamento);

    -- Exibir mensagem de sucesso
    PRINT 'Consulta agendada com sucesso.';
END;

------------------
-- Primeiro, criamos a trigger
CREATE TRIGGER trg_ApósInserirConsulta
ON Consultas
AFTER INSERT
AS
BEGIN
    DECLARE @ConsultaID INT, @DataInicio DATETIME, @DuracaoMinutos INT;

    -- Obtém o ID da consulta inserida
    SELECT @ConsultaID = inserted.ConsultaID
    FROM inserted;

    -- Obtém a data e a duração do tratamento da consulta inserida
    SELECT @DataInicio = c.DataHora,
           @DuracaoMinutos = t.DuracaoEmMinutos
    FROM inserted i
    INNER JOIN Consultas c ON i.ConsultaID = c.ConsultaID
    INNER JOIN Tratamentos t ON c.Descricao = t.Descricao;

    -- Calcula a data final baseada na duração do tratamento
    DECLARE @DataFim DATETIME;
    SET @DataFim = DATEADD(MINUTE, @DuracaoMinutos, @DataInicio);

    -- Insere na tabela de Agendas
    INSERT INTO Agendas (PacienteID, DentistaID, DataHoraInicio, DataHoraFim, Disponivel)
    SELECT c.PacienteID, c.DentistaID, @DataInicio, @DataFim, 0
    FROM Consultas c
    WHERE c.ConsultaID = @ConsultaID;

END;

