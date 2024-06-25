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

DROP FUNCTION IF EXISTS FormatarDataHoraBrasileira;
DROP TRIGGER IF EXISTS trg_AfterInsertConsultas;
DROP PROCEDURE IF EXISTS ExcluirConsulta;
DROP PROCEDURE IF EXISTS InserirConsulta;
DROP PROCEDURE IF EXISTS AgendarConsulta;
DROP TRIGGER IF EXISTS trg_AposInserirConsulta
GO