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
