# ----------------------- IMPORTAÇÕES -----------------------#

#cmd: pip install pyodbc
import pyodbc

# ----------------------- FUNDAMENTOS -----------------------#

#comando 'pyodbc.connect' para conectar com o banco de dados
#exemplo: connection = pyodbc.connect('bancodedados.db') ou pyodbc.connect(algumaconexao)

#comando 'cursor' para manipular o banco de dados, sempre que chamar o cursor, ele chamará o banco de dados
#exemplo: cursor = connection.cursor()

#comando 'connection.commit()' para salvar as alterações
#exemplo: connection.commit()

#comando 'cursor.fetchall()' para pegar todos os dados
#exemplo: print(cursor.fetchall())

#comando 'cursor.execute' para executar comandos SQL
#exemplo: cursor.execute("CREATE TABLE table (coluna1 typecoluna1, coluna2 typecoluna2, coluna3 typecoluna3)")

#comando 'connection.close()' para fechar o banco de dados ao final do código
#exemplo: connection.close()

# ------------------------- INÍCIO --------------------------#

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost,1433;" #Verificar se a porta é essa
    "UID=sa;" #Verificar o nome do banco
    "PWD=Passw0rd;"  # Substitua pela sua senha do banco
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

try:
    # Conectar com o banco de dados
    connection = pyodbc.connect(connection_string)

    # Criando o cursor para manipular o connection de dados
    cursor = connection.cursor()

    # ------------------------- FUNÇÕES -------------------------#
    #Publicar mudança no banco
    def salvar_alteracoes():
        connection.commit()

    #Mostrar tabelas
    def mostrar_dados(tabela):
        cursor.execute(f'SELECT * FROM {tabela}')
        resultados = cursor.fetchall()
        # Salvar os resultados em uma lista de listas
        lista_de_listas = [list(row) for row in resultados]

        # Exibir os resultados
        for lista in lista_de_listas:
            print(lista)

    #Drop All
    def tirando_todas_as_tabelas():
        cursor.execute('DROP TABLE IF EXISTS Pacientes')
        cursor.execute('DROP TABLE IF EXISTS Dentistas')
        cursor.execute('DROP TABLE IF EXISTS Consultas')
        cursor.execute('DROP TABLE IF EXISTS Tratamentos')
        cursor.execute('DROP TABLE IF EXISTS Prontuarios')
        cursor.execute('DROP TABLE IF EXISTS Pagamentos')
        cursor.execute('DROP TABLE IF EXISTS Agendas')
        cursor.execute('DROP TABLE IF EXISTS Receitas')
        salvar_alteracoes()

    #Drop "Tabela"
    def tirando_tabela(tabela):
        cursor.execute(f'DROP TABLE {tabela}')
        salvar_alteracoes()

    #Executar SQL
    def executar_SQL(SQL):
        cursor.execute(SQL)
        salvar_alteracoes()

    # ------------------------- AGENDAS -------------------------#

    #Adicionando Agendamentos
    def add_agendas(paciente_id, dentista_id, data_hora_inicio, data_hora_fim, disponivel):
        query = '''
        INSERT INTO Agendas (PacienteID, DentistaID, DataHoraInicio, DataHoraFim, Disponivel)
        VALUES (?, ?, ?, ?, ?)
        '''
        cursor.execute(query, (paciente_id, dentista_id, data_hora_inicio, data_hora_fim, disponivel))
        salvar_alteracoes()
        print("Agendamento adicionado com sucesso.")

    #Removendo Agendas
    def remover_agendas(agenda_id):
        query = '''
        DELETE FROM Agendas WHERE AgendaID = ?
        '''
        cursor.execute(query, (agenda_id,))
        salvar_alteracoes()
        print("Agendamento removido com sucesso.")

    #Mostrar Agendas
    def mostrar_agendas():
        query = '''
        SELECT AgendaID, PacienteID, DentistaID, DataHoraInicio, DataHoraFim, Disponivel FROM Agendas
        '''
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    #Atualizar valores das Agendas
    def mudar_agendas(agenda_id, paciente_id=None, dentista_id=None, data_hora_inicio=None, data_hora_fim=None, disponivel=None):
        query = '''
        UPDATE Agendas
        SET PacienteID = COALESCE(?, PacienteID),
            DentistaID = COALESCE(?, DentistaID),
            DataHoraInicio = COALESCE(?, DataHoraInicio),
            DataHoraFim = COALESCE(?, DataHoraFim),
            Disponivel = COALESCE(?, Disponivel)
        WHERE AgendaID = ?
        '''
        cursor.execute(query, (paciente_id, dentista_id, data_hora_inicio, data_hora_fim, disponivel, agenda_id))
        salvar_alteracoes()
        print("Agendamento alterado com sucesso.")
    # -------------------------------------------------------#

except pyodbc.Error as e:
    print("Error: ", e)

finally:
    if 'connection' in locals():
        connection.close()
