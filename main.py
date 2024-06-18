# import scriptCRUD as crud
from login import login
from cadastro import cadastro
import os
import time

def main():
    # Exemplo de uso das funções CRUD
    #crud.tirando_todas_as_tabelas()
    #crud.criando_todas_as_tabelas()
    #crud.inserindo_todos_os_dados_iniciais()
    #crud.salvar_alteracoes()
    
    # PARTE 01: LOGIN/CADASTRO NO SISTEMA:

    print("Bem-vindo ao sistema!\n")
    while True:
        login_ou_cadastro = int(input("1- Login\n2- Cadastro\n3- Sair\n\nEscolha uma opção: "))

        if login_ou_cadastro in [1, 2, 3]:
            break
        else:
            time.sleep(1)
            os.system('cls')
            print("Opção inválida, tente novamente.\n")
            time.sleep(1)
            os.system('cls')
            continue

    if login_ou_cadastro == "1":
        resultado_login = login()
        if resultado_login:
            if resultado_login == "Paciente":
                acesso_ao_sistema_paciente = True
            elif resultado_login == "Dentista":
                acesso_ao_sistema_dentista = True
            acesso_ao_sistema = True

    if login_ou_cadastro == "2":
        #Lógica de cadastro
        resultado_cadastro = cadastro() # Ainda não funcional
        if resultado_cadastro:
            acesso_ao_sistema_paciente = True
            acesso_ao_sistema = True

    elif login_ou_cadastro == "3":
        return 

    # PARTE 02: MENU PRINCIPAL DO SISTEMA:

    if acesso_ao_sistema:
        # Menu principal e sistema aqui
        if acesso_ao_sistema_paciente:
            pass
        elif acesso_ao_sistema_dentista:
            pass

    else:
        return 

if __name__ == "__main__":
    main()
