-- índices utilizados na consulta 2
-- Receitas (já criado anteriormente em index 1)
-- CREATE NONCLUSTERED INDEX IX_Receitas_PacienteID_DataReceita ON Receitas (PacienteID, DataReceita);

-- Paciente
CREATE CLUSTERED INDEX IX_Paciente_PacienteID ON Paciente (PacienteID);

-- Prontuarios
CREATE NONCLUSTERED INDEX IX_Prontuarios_TratamentoID ON Prontuarios (TratamentoID);
CREATE NONCLUSTERED INDEX IX_Prontuarios_DentistaID ON Prontuarios (DentistaID);