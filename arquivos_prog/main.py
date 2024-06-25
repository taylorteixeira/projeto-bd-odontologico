from conexao_banco import get_connection, salvar_alteracoes, mostrar_dados, tirando_tabela, tirando_todas_as_tabelas, executar_SQL
from conexao_banco import add_agendas, remover_agendas, mostrar_agendas, mudar_agendas
import os
import time
import pyodbc

def main():
    # Conectar com o banco de dados
    connection = get_connection()

    try:
        os.system("cls")
        time.sleep(2)
        print("Bem-vindo ao sistema!\n")
        time.sleep(2)
        os.system("cls")

        while True:
            print("Escolha uma das \033[34mopções\033[0m abaixo:\n\n\033[34m1-\033[0m Adicionar Agendamento\n\033[34m2-\033[0m Remover Agendamento\n\033[34m3-\033[0m Listar Agendamentos\n\033[34m4-\033[0m Mudar Agendamento\n\033[34m5-\033[0m Sair do Sistema\n")
            escolha = int(input("Digite o número da \033[34mopção desejada\033[0m: "))

            match escolha:
                case 1:
                    os.system("cls")
                    print("\033[34m1- Adicionar Agendamento:\033[0m\n")
                    
                    paciente_id = int(input("Digite o código do \033[34mpaciente\033[0m: "))
                    dentista_id = int(input("Digite o código do \033[34mdentista\033[0m: "))
                    data_hora_inicio = input("Digite a data de \033[34minício da consulta\033[0m (yyyy-MM-dd HH:mm:ss): ")
                    data_hora_fim = input("Digite a data de \033[34mfinal da consulta\033[0m (yyyy-MM-dd HH:mm:ss): ")
                    disponivel = int(input("Digite (1) para agendamento disponível e (2) para agendamento indisponível: "))
                    
                    add_agendas(connection, paciente_id, dentista_id, data_hora_inicio, data_hora_fim, disponivel)
                    time.sleep(2)
                    os.system("cls")

                case 2:
                    os.system("cls")
                    print("\033[34m2- Remover Agendamento\033[0m\n")
                    
                    agenda_id = int(input("Digite o \033[34mcódigo do agendamento\033[0m para remover: "))
                    
                    remover_agendas(connection, agenda_id)
                    time.sleep(2)
                    os.system("cls")

                case 3:
                    os.system("cls")
                    print("\033[34m3- Listar Agendamentos:\033[0m\n")
                    mostrar_agendas(connection)
                    input("\nPressione \033[34mEnter\033[0m para continuar...")
                    os.system("cls")

                case 4:
                    os.system("cls")
                    print("\033[34m4- Mudar Agendamento\033[0m\n")

                    agenda_id = int(input("Digite o \033[34mcódigo da agenda\033[0m que você deseja alterar: "))
                    
                    mudarPaciente = int(input("\nVocê deseja alterar o \033[34mpaciente?\033[0m (1) Sim e (2) Não: "))
                    if mudarPaciente == 1:
                        paciente_id = int(input("Digite o código do novo paciente: "))
                    else:
                        paciente_id = None

                    mudarDentista = int(input("\nVocê deseja alterar o \033[34mdentista?\033[0m (1) Sim e (2) Não: "))
                    if mudarDentista == 1:
                        dentista_id = int(input("Digite o código do novo dentista: "))
                    else:
                        dentista_id = None

                    mudarInicio = int(input("\nVocê deseja alterar a \033[34mdata de início?\033[0m (1) Sim e (2) Não: "))
                    if mudarInicio == 1:
                        data_hora_inicio = input("Digite a nova data de início da consulta (yyyy-MM-dd HH:mm:ss): ")
                    else:
                        data_hora_inicio = None

                    mudarFim = int(input("\nVocê deseja alterar a \033[34mdata de fim?\033[0m (1) Sim e (2) Não: "))
                    if mudarFim == 1:
                        data_hora_fim = input("Digite a nova data de fim da consulta (yyyy-MM-dd HH:mm:ss): ")
                    else:
                        data_hora_fim = None

                    mudarDisponibilidade = int(input("\nVocê deseja alterar a \033[34mdisponibilidade?\033[0m (1) Sim e (2) Não: "))
                    if mudarDisponibilidade == 1:
                        disponivel = int(input("Digite a nova disponibilidade: "))
                    else:
                        disponivel = None
                    
                    mudar_agendas(connection, agenda_id, paciente_id, dentista_id, data_hora_inicio, data_hora_fim, disponivel)

                case 5:
                    os.system("cls")
                    print("Saindo do sistema...")
                    time.sleep(2)
                    break

                case _:
                    os.system("cls")
                    print("\033[31mOpção inválida!\033[0m Tente novamente.")
                    time.sleep(2)
                    os.system("cls")

    except pyodbc.Error as e:
        print("Erro: ", e)

    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    main()