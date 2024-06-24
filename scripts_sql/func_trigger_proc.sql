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

--DECLARE @datahora DATETIME = '2024-06-24 15:30:00';
--SELECT dbo.FormatarDataHoraBrasileira(@datahora) AS DataHoraFormatada;

-------------------------------------------------------------------------------------------------------

CREATE PROCEDURE ExcluirConsulta
    @ConsultaID INT
AS
BEGIN
    DELETE FROM Consultas
    WHERE ConsultaID = @ConsultaID;
END;
GO

--INSERT INTO Consultas (PacienteID, DentistaID, DataHora, Motivo)
--VALUES (1, 1, '2024-06-24 15:30:00', 'Consulta de teste');

--SELECT * FROM Consultas WHERE PacienteID = 1 AND DentistaID = 1 AND DataHora = '2024-06-24 15:30:00';

--EXEC ExcluirConsulta @ConsultaID = (SELECT ConsultaID FROM Consultas WHERE PacienteID = 1 AND DentistaID = 1 AND DataHora = '2024-06-24 15:30:00');

--SELECT * FROM Consultas WHERE PacienteID = 1 AND DentistaID = 1 AND DataHora = '2024-06-24 15:30:00';


-------------------------------------------------------------------------------------------------------

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

--SELECT * FROM dbo.ConsultasComNomes();
-------------------------------------------------------------------------------------------------------

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

    -- Inserir a consulta
    INSERT INTO Consultas (PacienteID, DentistaID, DataHora, Motivo)
    VALUES (@PacienteID, @DentistaID, @DataHora, @Motivo);
END;
GO

--INSERT INTO Pacientes (Nome) VALUES ('Paciente de Teste');
--INSERT INTO Dentistas (Nome) VALUES ('Dentista de Teste');

-- Testar o procedimento InserirConsulta
--EXEC InserirConsulta @NomePaciente = 'Paciente de Teste', 
                    --@NomeDentista = 'Dentista de Teste', 
                    --@DataHora = '2024-06-25 10:00:00', 
                    --@Motivo = 'Consulta de Teste';

--SELECT * FROM Consultas WHERE PacienteID = (SELECT PacienteID FROM Pacientes WHERE Nome = 'Paciente de Teste')
                        --AND DentistaID = (SELECT DentistaID FROM Dentistas WHERE Nome = 'Dentista de Teste')
                        --AND DataHora = '2024-06-25 10:00:00';

-------------------------------------------------------------------------------------------------------

CREATE TRIGGER tg_validar_dados
ON Consultas
FOR INSERT
AS
BEGIN
    DECLARE @PacienteID INT;
    DECLARE @DentistaID INT;
    DECLARE @DataHora DATETIME;

    SELECT @PacienteID = i.PacienteID, @DentistaID = i.DentistaID, @DataHora = i.DataHora
    FROM inserted i;

    -- Verificar se o paciente existe
    IF NOT EXISTS (SELECT 1 FROM Pacientes WHERE PacienteID = @PacienteID)
    BEGIN
        RAISERROR ('Paciente não encontrado!', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END;

    -- Verificar se o dentista existe
    IF NOT EXISTS (SELECT 1 FROM Dentistas WHERE DentistaID = @DentistaID)
    BEGIN
        RAISERROR ('Dentista não encontrado!', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END;

    -- Verificar se o dentista está disponível no horário marcado
    IF EXISTS (
        SELECT 1 FROM Consultas
        WHERE DentistaID = @DentistaID
          AND DataHora = @DataHora
    )
    BEGIN
        RAISERROR ('O dentista não está disponível nesse horário!', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END;
END;
GO