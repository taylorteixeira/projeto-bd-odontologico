# import scriptCRUD as crud
from login import login
from cadastro import cadastro

def main():
    # Exemplo de uso das funções CRUD
    #crud.tirando_todas_as_tabelas()
    #crud.criando_todas_as_tabelas()
    #crud.inserindo_todos_os_dados_iniciais()
    #crud.salvar_alteracoes()
    
    # PARTE 01: LOGIN/CADASTRO NO SISTEMA:

    print("Bem-vindo ao sistema!\n")
    login_ou_cadastro = input("1- Login\n2- Cadastro\n3- Sair\n\nEscolha uma opção: ")

    if login_ou_cadastro == "1":
        resultado_login = login()
        if resultado_login:
            print("\nBem-vindo ao sistema!")
            acesso_ao_sistema = True

    if login_ou_cadastro == "2":
        #Lógica de cadastro
        resultado_cadastro = cadastro() # Ainda não funcional
        if resultado_cadastro:
            print("\nBem-vindo ao sistema!")
            acesso_ao_sistema = True

    elif login_ou_cadastro == "3":
        return ''

    # PARTE 02: MENU PRINCIPAL DO SISTEMA:

    if acesso_ao_sistema:
        # Menu principal e sistema aqui
        pass

    else:
        # Quebrar codigo aqui
        pass
        


if __name__ == "__main__":
    main()
