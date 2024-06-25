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
GO
