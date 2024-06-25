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
            print("Escolha uma das opções abaixo:\n\n1-Adicionar Agendamento\n2-Remover Agendamento\n3-Listar Agendamentos\n4-Mudar Agendamento\n5-Sair do Sistema\n")
            escolha = int(input("Digite o número da opção desejada: "))

            match escolha:
                case 1:
                    os.system("cls")
                    print("1-Adicionar Agendamento\n")
                    
                    paciente_id = int(input("Digite o código do paciente: "))
                    dentista_id = int(input("Digite o código do dentista: "))
                    data_hora_inicio = input("Digite a data de início da consulta (yyyy-MM-dd HH:mm:ss): ")
                    data_hora_fim = input("Digite a data de final da consulta (yyyy-MM-dd HH:mm:ss): ")
                    disponivel = int(input("Digite (1) para agendamento disponível e (2) para agendamento indisponível: "))
                    
                    add_agendas(connection, paciente_id, dentista_id, data_hora_inicio, data_hora_fim, disponivel)
                    time.sleep(2)
                    os.system("cls")

                case 2:
                    os.system("cls")
                    print("2-Remover Agendamento\n")
                    
                    agenda_id = int(input("Digite o código do agendamento para remover: "))
                    
                    remover_agendas(connection, agenda_id)
                    time.sleep(2)
                    os.system("cls")

                case 3:
                    os.system("cls")
                    print("3-Listar Agendamentos:\n")
                    mostrar_agendas(connection)
                    input("\nPressione Enter para continuar...")
                    os.system("cls")

                case 4:
                    os.system("cls")
                    print("4-Mudar Agendamento\n")

                    agenda_id = int(input("Digite o código da agenda que você deseja alterar: "))
                    
                    mudarPaciente = int(input("Você deseja alterar o paciente? (1) Sim e (2) Não: "))
                    if mudarPaciente == 1:
                        paciente_id = int(input("Digite o código do paciente que você deseja alterar: "))
                    else:
                        paciente_id = None

                    mudarDentista = int(input("\nVocê deseja alterar o dentista? (1) Sim e (2) Não: "))
                    if mudarDentista == 1:
                        dentista_id = int(input("Digite o código do dentista que você deseja alterar: "))
                    else:
                        dentista_id = None

                    mudarInicio = int(input("\nVocê deseja alterar a data de início? (1) Sim e (2) Não: "))
                    if mudarInicio == 1:
                        data_hora_inicio = input("Digite a data de início da consulta (yyyy-MM-dd HH:mm:ss): ")
                    else:
                        data_hora_inicio = None

                    mudarFim = int(input("\nVocê deseja alterar a data de fim? (1) Sim e (2) Não: "))
                    if mudarFim == 1:
                        data_hora_fim = input("Digite a data de fim da consulta (yyyy-MM-dd HH:mm:ss): ")
                    else:
                        data_hora_fim = None

                    mudarDisponibilidade = int(input("\nVocê deseja alterar a disponibilidade? (1) Sim e (2) Não: "))
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
                    print("Opção inválida! Tente novamente.")
                    time.sleep(2)
                    os.system("cls")

    except pyodbc.Error as e:
        print("Erro: ", e)

    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    main()