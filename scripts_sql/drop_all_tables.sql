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

SELECT * FROM Pacientes;
SELECT * FROM Dentistas;
SELECT * FROM Consultas;
SELECT * FROM Tratamentos;
SELECT * FROM Prontuarios;
SELECT * FROM Pagamentos;
SELECT * FROM Agendas;
SELECT * FROM Receitas;
GO

DROP FUNCTION FormatarDataHoraBrasileira;
DROP TRIGGER trg_AfterInsertConsultas;
DROP PROCEDURE ExcluirConsulta;
DROP PROCEDURE InserirConsulta;
DROP PROCEDURE AgendarConsulta;
DROP TRIGGER trg_AposInserirConsulta
GO