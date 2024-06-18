--- Ideia para Trigger (teste)
A cada geração de consulta o valor de receita é atualizado no insert 

CREATE TRIGGER atualizar_valor_receita
AFTER INSERT ON Consultas
FOR EACH ROW
BEGIN
    DECLARE novo_valor DECIMAL(10, 2);

    SELECT SUM(r.Valor) INTO novo_valor
    FROM Receitas r
    WHERE r.PacienteID = NEW.PacienteID;

    UPDATE Receitas
    SET Valor = novo_valor
    WHERE PacienteID = NEW.PacienteID;
END;
