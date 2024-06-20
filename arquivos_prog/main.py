from conexao_banco import salvar_alteracoes, mostrar_dados, tirando_tabela, tirando_todas_as_tabelas, executar_SQL
import os
import time

def main():
    # Exemplo de uso das funções do arquivo conexao_banco.py
    #tirando_todas_as_tabelas()
    #executar_SQL("CREATE TABLE IF NOT EXISTS dentistas (id INTEGER PRIMARY KEY, nome TEXT, email TEXT, senha TEXT, especialidade TEXT, telefone TEXT, endereco TEXT, cidade TEXT, estado TEXT)")
    #salvar_alteracoes()
    time.sleep(1)
    print("Bem-vindo ao sistema!\n")
    time.sleep(1)

    # PARTE 01: MENU PRINCIPAL DO SISTEMA:

    while True:
        #Sistema aqui 
        print("Escolha uma das opções abaixo:\n1-Adicionar Agendamento\n2-Remover Agendamento\n3-Listar Agendamentos\n4-Mudar Agendamento\n5-Sair do Sistema\n")  
        escolha = int(input("Digite o número da opção desejada: "))

        if escolha == 1:
            # Lógica para adicionar agendamento
            pass
        elif escolha == 2:
            # Lógica para remover agendamento
            pass
        elif escolha == 3:
            # Lógica para listar agendamentos
            pass
        elif escolha == 4:
            # Lógica para mudar agendamento
            pass
        elif escolha == 5:
            print("Saindo do sistema...")
            time.sleep(2)
            break
        else:
            print("Opção inválida! Tente novamente.")
            time.sleep(2)
            os.system("clear")
            continue
        

if __name__ == "__main__":
    main()
