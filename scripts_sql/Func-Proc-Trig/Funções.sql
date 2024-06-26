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



-- Função para obter o ID do paciente pelo nome
CREATE FUNCTION dbo.GetPacienteID (@Nome NVARCHAR(100))
RETURNS INT
AS
BEGIN
    DECLARE @ID INT;
    SELECT @ID = PacienteID FROM Pacientes WHERE Nome = @Nome;
    RETURN @ID;
END;
GO



-- Função para obter o ID do dentista pelo nome
CREATE FUNCTION dbo.GetDentistaID (@Nome NVARCHAR(100))
RETURNS INT
AS
BEGIN
    DECLARE @ID INT;
    SELECT @ID = DentistaID FROM Dentistas WHERE Nome = @Nome;
    RETURN @ID;
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