-- Consultas
CREATE NONCLUSTERED INDEX IX_Consultas_DataHora ON Consultas (DataHora);
CREATE NONCLUSTERED INDEX IX_Consultas_PacienteID_DentistaID ON Consultas (PacienteID, DentistaID);

-- Prontuarios
CREATE NONCLUSTERED INDEX IX_Prontuarios_PacienteID_DentistaID_Data ON Prontuarios (PacienteID, DentistaID, Data);
CREATE NONCLUSTERED INDEX IX_Prontuarios_TratamentoID ON Prontuarios (TratamentoID);
CREATE NONCLUSTERED INDEX IX_Prontuarios_DentistaID ON Prontuarios (DentistaID);

-- Receitas
CREATE NONCLUSTERED INDEX IX_Receitas_PacienteID_DataReceita ON Receitas (PacienteID, DataReceita);

-- Paciente
CREATE CLUSTERED INDEX IX_Paciente_PacienteID ON Paciente (PacienteID);

-- dentistas
CREATE CLUSTERED INDEX IX_Dentistas_DentistaID ON Dentistas (DentistaID);
CREATE CLUSTERED INDEX IX_Dentistas_DentistaID ON Dentistas (DentistaID);
CREATE INDEX IX_Dentistas_Nome_Pacientes_Sexo 
ON Dentistas (Nome)
INCLUDE (DentistaID);


-- dentistas +custo
CREATE INDEX IX_Dentistas_Especialidade_Tratamentos_Custo 
ON Dentistas (Especialidade)
INCLUDE (DentistaID);

-- tratamento
CREATE CLUSTERED INDEX IX_Tratamentos_TratamentoID ON Tratamentos (TratamentoID);

