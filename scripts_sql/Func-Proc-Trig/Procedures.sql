-- Procedimento armazenado para excluir consulta
CREATE PROCEDURE ExcluirConsulta
    @ConsultaID INT
AS
BEGIN
    DELETE FROM Consultas
    WHERE ConsultaID = @ConsultaID;
END;
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
END;
GO



-- Procedure para agendar uma consulta
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

    -- Obter IDs de paciente e dentista usando as funções criadas
    SET @PacienteID = dbo.GetPacienteID(@NomePaciente);
    SET @DentistaID = dbo.GetDentistaID(@NomeDentista);

    -- Obter ID do tratamento
    SELECT @TratamentoID = TratamentoID FROM Tratamentos WHERE Descricao = @Tratamento;

    -- Inserir na tabela de Consultas
    INSERT INTO Consultas (PacienteID, DentistaID, DataHora)
    VALUES (@PacienteID, @DentistaID, @DataConsulta);

    -- Exibir mensagem de sucesso
    PRINT 'Consulta agendada com sucesso.';
END;
GO
