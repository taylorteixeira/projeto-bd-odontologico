from conexao_banco import salvar_alteracoes, mostrar_dados, tirando_tabela, tirando_todas_as_tabelas, executar_SQL
from conexao_banco import add_agendas, remover_agendas, mostrar_agendas, mudar_agendas
import os
import time

def main():
    # Exemplo de uso das funções do arquivo conexao_banco.py
    #tirando_todas_as_tabelas()
    #executar_SQL("CREATE TABLE IF NOT EXISTS dentistas (id INTEGER PRIMARY KEY, nome TEXT, email TEXT, senha TEXT, especialidade TEXT, telefone TEXT, endereco TEXT, cidade TEXT, estado TEXT)")
    #salvar_alteracoes()
    os.system("cls")
    time.sleep(2)
    print("Bem-vindo ao sistema!\n")
    time.sleep(2)
    os.system("cls")

    # PARTE 01: MENU PRINCIPAL DO SISTEMA:

    while True:
        #Sistema aqui 
        print("Escolha uma das opções abaixo:\n1-Adicionar Agendamento\n2-Remover Agendamento\n3-Listar Agendamentos\n4-Mudar Agendamento\n5-Sair do Sistema\n")  
        escolha = int(input("Digite o número da opção desejada: "))

        match escolha:
            case 1:
                os.system("cls")
                print("1-Adicionar Agendamento")
                
                paciente_id = int(input("Digite o codigo do paciente: "))
                dentista_id =  int(input("Digite o codigo do dentista: "))
                data_hora_inicio = input("Digite a data de inicio da consulta (yyyy-MM-dd HH:mm:ss): ")
                data_hora_fim = input("Digite a data de final da consulta (yyyy-MM-dd HH:mm:ss): ")
                disponivel = int(input("Digite (1) para agendamento disponivel e (2) para agendamento indisponivel: "))
                
                add_agendas(paciente_id, dentista_id, data_hora_inicio, data_hora_fim, disponivel)
                time.sleep(2)
                os.system("cls")

            case 2:
                os.system("cls")
                print("2-Remover Agendamento")
                
                agenda_id = int(input("Digite o codigo do agendamento para remover: "))
                
                remover_agendas(agenda_id)
                time.sleep(2)
                os.system("cls")


            case 3:
                os.system("cls")
                print("3-Listar Agendamentos")

                mostrar_agendas()
                input("Pressione qualquer tecla para continuar...")
                os.system("cls")

            case 4:
                os.system("cls")
                print("4-Mudar Agendamento")

                agenda_id = int(input("Digite o codigo da agenda que você deseja alterar: "))
                
                mudarPaciente = int(print("Você deseja alterar o paciente? (1) Sim e (2)Não: "))
                match mudarPaciente:
                    case 1:
                        paciente_id = int(input("Digite o codigo do paciente que você deseja alterar: "))
                    case 2:
                        pass
                    case _:
                        print("opção Invalida")

                mudarDentista = int(print("Você deseja alterar o paciente? (1) Sim e (2)Não: "))
                match mudarDentista:
                    case 1:
                        dentista_id =  int(input("Digite o codigo do dentista que você deseja alterar: "))
                    case 2:
                        pass
                    case _:
                        print("opção Invalida")
                
                mudarInicio = int(print("Você deseja alterar o paciente? (1) Sim e (2)Não: "))
                match mudarInicio:
                    case 1:
                        data_hora_inicio = input("Digite a data de inicio da consulta (yyyy-MM-dd HH:mm:ss) que você deseja alterar:  ")
                    case 2:
                        pass
                    case _:
                        print("opção Invalida")
                
                mudarFim = int(print("Você deseja alterar o paciente? (1) Sim e (2)Não: "))                
                match mudarFim:
                    case 1:
                        data_hora_fim = input("Digite a data de final da consulta (yyyy-MM-dd HH:mm:ss) que você deseja alterar:  ")
                    case 2:
                        pass
                    case _:
                        print("opção Invalida")                
                
                mudarDisponibilidade = int(print("Você deseja alterar o paciente? (1) Sim e (2)Não: "))
                match mudarDisponibilidade:
                    case 1:
                        disponivel = int(input("Digite a disponibilidade para qual você deseja alterar: "))
                    case 2:
                        pass
                    case _:
                        print("opção Invalida")
                
            case 5:
                os.system("cls")
                print("Saindo do sistema...")
                time.sleep(2)
                break

            case _:
                os.system("cls")
                print("Opção inválida! Tente novamente.")
                time.sleep(2)
                os.system("clear")
                continue
        
if __name__ == "__main__":
    main()
