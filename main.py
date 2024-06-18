import scriptCRUD as crud
import login as login

def main():
    # Exemplo de uso das funções CRUD
    #crud.drop_all_tables()
    #crud.criando_todas_as_tabelas()
    #crud.inserindo_todos_os_dados_iniciais()
    #crud.salvar_alteracoes()

    # Exemplo de uso da função de login
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    resultado_login = login.login(email, senha)
    print(resultado_login)

if __name__ == "__main__":
    main()
