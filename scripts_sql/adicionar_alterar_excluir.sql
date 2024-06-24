-- add consulta
INSERT INTO Consultas (PacienteID, DentistaID, DataHora, Motivo) VALUES
(20, 1, '2024-12-01 13:30:00', 'Consulta de rotina');
GO

-- updt
UPDATE Consultas
SET DataHora = '2024-12-04 13:30:00'
WHERE ConsultaID = 1;
GO

-- del
DELETE FROM Consultas
WHERE PacienteID = 20;
GO