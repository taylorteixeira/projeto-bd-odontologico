-- índices utilizados na consulta 3
-- dentista
CREATE CLUSTERED INDEX IX_Dentistas_DentistaID ON Dentistas (DentistaID);

-- prontuário ((já criado anteriormente em index 2))
-- CREATE NONCLUSTERED INDEX IX_Prontuarios_DentistaID_TratamentoID ON Prontuarios (DentistaID, TratamentoID);
-- CREATE INDEX IX_Prontuarios_Data ON Prontuarios (Data);


-- tratamento
CREATE CLUSTERED INDEX IX_Tratamentos_TratamentoID ON Tratamentos (TratamentoID);

-- dentistas +custo
CREATE INDEX IX_Dentistas_Especialidade_Tratamentos_Custo 
ON Dentistas (Especialidade)
INCLUDE (DentistaID);

