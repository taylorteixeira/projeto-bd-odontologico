-- FUNCION:














-- PROCEDURE:













-- TRIGGER:
--- Ideia para Trigger (teste)
-- A cada geração de consulta o valor de receita é atualizado no insert 

-- CREATE TRIGGER atualizar_valor_receita
-- AFTER INSERT ON Consultas
-- FOR EACH ROW
-- BEGIN
--     DECLARE novo_valor DECIMAL(10, 2);

--     SELECT SUM(r.Valor) INTO novo_valor
--     FROM Receitas r
--     WHERE r.PacienteID = NEW.PacienteID;

--     UPDATE Receitas
--     SET Valor = novo_valor
--     WHERE PacienteID = NEW.PacienteID;
-- END;

-- OU

-- CREATE TRIGGER trg_AfterInsertConsulta_UpdateAgenda
-- ON Consultas
-- AFTER INSERT
-- AS
-- BEGIN
-- -- Declaração de variáveis
-- DECLARE @DentistaID INT, @datahora DATETIME;

-- -- Selecionar os dados da nova consulta inserida
-- SELECT @DentistaID = i.DentistaID, 
--        @DataHora = i.DataHora
-- FROM Inserted i;

-- -- Atualizar a disponibilidade do dentista para FALSE
-- UPDATE Agendas
-- SET Disponivel = 0
-- WHERE DentistaID = @DentistaID AND DataHora = @DataHora;
-- END;

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
(5, 1, '2024-07-12 09:00:00', 'Teste')










