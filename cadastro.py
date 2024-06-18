# import scriptCRUD as crud
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

def cadastro():
    #adicionar logica de cadastro
    pass