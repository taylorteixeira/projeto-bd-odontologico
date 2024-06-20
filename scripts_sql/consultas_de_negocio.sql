---1. Total de receitas por dentista em um determinado período, incluindo número de consultas e custo total dos tratamentos realizados.

WITH ConsultaDetalhes AS (
SELECT
c.DentistaID,
COUNT(c.ConsultaID) AS NumeroDeConsultas,
SUM(t.Custo) AS CustoTotalTratamentos,
SUM(r.Valor) AS ReceitaTotal
FROM
Consultas c
LEFT JOIN
Prontuarios p ON c.PacienteID = p.PacienteID AND c.DentistaID = p.DentistaID AND c.DataHora = p.Data
LEFT JOIN
Tratamentos t ON p.TratamentoID = t.TratamentoID
LEFT JOIN
Receitas r ON c.PacienteID = r.PacienteID AND CAST(c.DataHora AS DATE) = r.DataReceita
WHERE
c.DataHora BETWEEN '2024-06-01' AND '2024-06-30'
GROUP BY
c.DentistaID
)
SELECT
d.Nome AS Dentista,
cd.NumeroDeConsultas,
cd.CustoTotalTratamentos,
cd.ReceitaTotal
FROM
Dentistas d
INNER JOIN
ConsultaDetalhes cd ON d.DentistaID = cd.DentistaID
ORDER BY
cd.ReceitaTotal DESC;
GO
---2. Pacientes que mais gastaram em tratamentos nos últimos três meses, incluindo detalhes do tratamento e o dentista responsável.
WITH GastosPacientes AS (
SELECT
r.PacienteID,
SUM(r.Valor) AS GastoTotal
FROM
Receitas r
WHERE
r.DataReceita BETWEEN DATEADD(MONTH, -3, GETDATE()) AND GETDATE()
GROUP BY
r.PacienteID
)
SELECT
p.Nome AS Paciente,
gp.GastoTotal,
t.Descricao AS Tratamento,
d.Nome AS Dentista,
pr.Data
FROM
GastosPacientes gp
INNER JOIN
Pacientes p ON gp.PacienteID = p.PacienteID
INNER JOIN
Prontuarios pr ON p.PacienteID = pr.PacienteID
INNER JOIN
Tratamentos t ON pr.TratamentoID = t.TratamentoID
INNER JOIN
Dentistas d ON pr.DentistaID = d.DentistaID
WHERE
pr.Data BETWEEN DATEADD(MONTH, -3, GETDATE()) AND GETDATE()
ORDER BY
gp.GastoTotal DESC;
GO
---3. Média de custo dos tratamentos por especialidade dos dentistas, considerando apenas os tratamentos realizados no último ano.
SELECT
d.Especialidade,
AVG(t.Custo) AS MediaCustoTratamento
FROM
Dentistas d
INNER JOIN
Prontuarios p ON d.DentistaID = p.DentistaID
INNER JOIN
Tratamentos t ON p.TratamentoID = t.TratamentoID
WHERE
p.Data BETWEEN DATEADD(YEAR, -1, GETDATE()) AND GETDATE()
GROUP BY
d.Especialidade
ORDER BY
MediaCustoTratamento DESC;
GO
---4. Pacientes atendidos por cada dentista, divididos por sexo, nos últimos seis meses.
SELECT
d.Nome AS Dentista,
p.Sexo,
COUNT(c.ConsultaID) AS NumeroDePacientes
FROM
Consultas c
INNER JOIN
Pacientes p ON c.PacienteID = p.PacienteID
INNER JOIN
Dentistas d ON c.DentistaID = d.DentistaID
WHERE
c.DataHora BETWEEN DATEADD(MONTH, -6, GETDATE()) AND GETDATE()
GROUP BY
d.Nome, p.Sexo
ORDER BY
d.Nome, p.Sexo;
GO