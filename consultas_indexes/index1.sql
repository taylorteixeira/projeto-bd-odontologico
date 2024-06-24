-- Consultas
CREATE NONCLUSTERED INDEX IX_Consultas_DataHora ON Consultas (DataHora);
CREATE NONCLUSTERED INDEX IX_Consultas_PacienteID_DentistaID ON Consultas (PacienteID, DentistaID);

-- Prontuarios
CREATE NONCLUSTERED INDEX IX_Prontuarios_PacienteID_DentistaID_Data ON Prontuarios (PacienteID, DentistaID, Data);

-- Receitas
CREATE NONCLUSTERED INDEX IX_Receitas_PacienteID_DataReceita ON Receitas (PacienteID, DataReceita);
