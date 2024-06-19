from conexao_banco import salvar_alteracoes, mostrar_dados, tirando_tabela, tirando_todas_as_tabelas, executar_SQL
import conexao_banco
# import pyodbc
import os
import time

# Conectar ao banco de dados
# def connect(connection_string):
#     return pyodbc.connect(connection_string)

# connection_string = (
#     "DRIVER={ODBC Driver 17 for SQL Server};"
#     "SERVER=localhost,1433;"
#     "UID=sa;"
#     "PWD=Passw0rd;"
#     "Encrypt=yes;"
#     "TrustServerCertificate=yes;"
# )

# connection = connect(connection_string)

time.sleep(1)
os.system('cls')

# Criando o cursor para manipular o banco de dados
# cursor = connection.cursor()

def login():
    x = 3
    while x > 0:

        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        
        executar_SQL(f"SELECT * FROM Pacientes WHERE Email = {email} AND Senha = {senha}")
        paciente = conexao_banco.cursor.fetchone()
        
        if paciente:
            print("Login bem-sucedido para paciente")
            return "Paciente"
        
        executar_SQL(f"SELECT * FROM Dentistas WHERE Email = {email} AND Senha = {senha}")
        dentista = conexao_banco.cursor.fetchone()
        
        if dentista:
            print("Login bem-sucedido para dentista")
            return "Dentista"
        
        else: 
            x -= 1
            print(f"Email ou senha incorretos, você ainda possui {x} tentativas.")
    
    print("Número de tentativas excedido")
    return False
