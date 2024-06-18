import pyodbc
import os
import time

# Conectar ao banco de dados
def connect(connection_string):
    return pyodbc.connect(connection_string)

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost,1433;"
    "UID=sa;"
    "PWD=Passw0rd;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

connection = connect(connection_string)
time.sleep(2)
os.system('cls')

# Criando o cursor para manipular o banco de dados
cursor = connection.cursor()

def login():
    x = 3
    while x > 0:

        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        
        cursor.execute("SELECT * FROM Pacientes WHERE Email = ? AND Senha = ?", (email, senha))
        paciente = cursor.fetchone()
        
        if paciente:
            print("Login bem-sucedido para paciente")
            return "Paciente"
        
        cursor.execute("SELECT * FROM Dentistas WHERE Email = ? AND Senha = ?", (email, senha))
        dentista = cursor.fetchone()
        
        if dentista:
            print("Login bem-sucedido para dentista")
            return "Dentista"
        
        else: 
            x -= 1
            print(f"Email ou senha incorretos, você ainda possui {x} tentativas.")
    
    print("Número de tentativas excedido")
    return False
    

