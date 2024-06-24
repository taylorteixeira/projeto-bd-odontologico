-- índices utilizados na consulta 4
-- consulta (já criado em index 1)
-- CREATE INDEX IX_Consultas_DataHora ON Consultas (DataHora);

-- pacientes (já criado em index 2)
-- CREATE CLUSTERED INDEX IX_Pacientes_PacienteID ON Pacientes (PacienteID);

-- dentistas
CREATE CLUSTERED INDEX IX_Dentistas_DentistaID ON Dentistas (DentistaID);

CREATE INDEX IX_Dentistas_Nome_Pacientes_Sexo 
ON Dentistas (Nome)
INCLUDE (DentistaID);

-- Este índice cobre a coluna Sexo da tabela Pacientes
