import pyodbc

# Defina a string de conexão
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost,1433;"
    "UID=sa;"
    "PWD=YourComplexPassword123!;"  # Substitua pela sua senha
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

# Conectar ao banco de dados
try:
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    print("Conexão estabelecida com sucesso!")

    def salvar_alteracoes():
     connection.commit()
    #banco.commit() para salvar as alterações


    # Função para mostrar os dados da tabela caso existe alguma requisição de leitura com SELECT
    def mostrar_dados():
        print(cursor.fetchall()) 
    #fetchall() pega todos os dados


    # Criando a tabela
    def criar_tabela():
        cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
        salvar_alteracoes()
        print('Tabela criada com sucesso!')
    #cursor.execute("CREATE TABLE table (coluna1 typecoluna1, coluna2 typecoluna2, coluna3 typecoluna3)")


    # Inserindo dados na tabela
    def inserir_dados(nome, idade, email):
        cursor.execute(f"INSERT INTO pessoas VALUES ('{nome}', {idade}, '{email}')")
        salvar_alteracoes()
        print('Dados inseridos com sucesso!')
    #cursor.execute("INSERT INTO table VALUES ('valor1', valor2, 'valor3')")


    # Deletar tabela
    def deletar_tabela(table):
        cursor.execute(f"DROP TABLE {table}")
        salvar_alteracoes()
        print('Tabela deletada com sucesso!')


    # Deletar dados da tabela
    def deletar_dados(table, coluna, valor):
        cursor.execute(f"DELETE FROM {table} WHERE {coluna} = '{valor}'")
        salvar_alteracoes()
        print('Dados deletados com sucesso!')


    # Atualizar dados da tabela
    def atualizar_dados(table, coluna, valor, coluna2, valor2):
        cursor.execute(f"UPDATE {table} SET {coluna} = '{valor}' WHERE {coluna2} = '{valor2}'")
        salvar_alteracoes()
        print('Dados atualizados com sucesso!')


    # Mostrar o nome das tabelas
    def mostrar_nome_tabelas():
        cursor.execute("SELECT name FROM master WHERE type='table'")
        print(cursor.fetchall())
        
    # ------------------------- EXECUÇÃO -------------------------#

    #inserir_dados('Miguel', 18, 'miguelrossifermo05@gmail.com')
    inserir_dados('Maria', 20, 'mariasilva@email.com')

    deletar_dados('pessoas', 'nome', 'Maria')

    # Lendo os dados da tabela
    cursor.execute("SELECT * FROM pessoas")

    # Mostrando os dados
    mostrar_dados()


except pyodbc.Error as ex:
    print("Erro ao conectar ao banco de dados:", ex)

finally:
    # Fechar a conexão
    if cursor:
        cursor.close()
    if connection:
        connection.close()
