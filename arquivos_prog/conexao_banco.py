import pyodbc
from tabulate import tabulate

# Define a string de conexão
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost,1433;" #Verificar se a porta é essa
    "DATABASE=odontodb;"
    "UID=SA;" #Verificar o nome do banco
    "PWD=reallyStrongPwd123;"  # Substitua pela sua senha do banco
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)


def get_connection():
    return pyodbc.connect(connection_string)

# Publicar mudança no banco
def salvar_alteracoes(connection):
    connection.commit()

# Mostrar tabelas
def mostrar_dados(connection, tabela):
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {tabela}')
    resultados = cursor.fetchall()
    lista_de_listas = [list(row) for row in resultados]
    for lista in lista_de_listas:
        print(lista)

# Drop All
def tirando_todas_as_tabelas(connection):
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS Pacientes')
    cursor.execute('DROP TABLE IF EXISTS Dentistas')
    cursor.execute('DROP TABLE IF EXISTS Consultas')
    cursor.execute('DROP TABLE IF EXISTS Tratamentos')
    cursor.execute('DROP TABLE IF EXISTS Prontuarios')
    cursor.execute('DROP TABLE IF EXISTS Pagamentos')
    cursor.execute('DROP TABLE IF EXISTS Agendas')
    cursor.execute('DROP TABLE IF EXISTS Receitas')
    salvar_alteracoes(connection)

# Drop "Tabela"
def tirando_tabela(connection, tabela):
    cursor = connection.cursor()
    cursor.execute(f'DROP TABLE {tabela}')
    salvar_alteracoes(connection)

# Executar SQL
def executar_SQL(connection, SQL):
    cursor = connection.cursor()
    cursor.execute(SQL)
    salvar_alteracoes(connection)

# Adicionando Agendamentos
def add_agendas(connection, paciente_id, dentista_id, data_hora_inicio, data_hora_fim, disponivel):
    cursor = connection.cursor()
    query = '''
    INSERT INTO Agendas (PacienteID, DentistaID, DataHoraInicio, DataHoraFim, Disponivel)
    VALUES (?, ?, ?, ?, ?)
    '''
    cursor.execute(query, (paciente_id, dentista_id, data_hora_inicio, data_hora_fim, disponivel))
    salvar_alteracoes(connection)
    print("\n\033[92mAgendamento adicionado com sucesso.\033[0m")

# Removendo Agendas
def remover_agendas(connection, agenda_id):
    cursor = connection.cursor()
    query = '''
    DELETE FROM Agendas WHERE AgendaID = ?
    '''
    cursor.execute(query, (agenda_id,))
    salvar_alteracoes(connection)
    print("\n\033[92mAgendamento removido com sucesso.\033[0m")

# Mostrar Agendas
def mostrar_agendas(connection):
    cursor = connection.cursor()
    query = '''
    SELECT AgendaID, PacienteID, DentistaID, DataHoraInicio, DataHoraFim, Disponivel FROM Agendas
    '''
    cursor.execute(query)
    rows = cursor.fetchall()
    headers = ["AgendaID", "PacienteID", "DentistaID", "DataHoraInicio", "DataHoraFim", "Disponibilidade"]
    table = tabulate(rows, headers, tablefmt="grid")
    print(table)

# Atualizar valores das Agendas
def mudar_agendas(connection, agenda_id, paciente_id=None, dentista_id=None, data_hora_inicio=None, data_hora_fim=None, disponivel=None):
    cursor = connection.cursor()
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
    salvar_alteracoes(connection)
    print("\n\033[92mAgendamento alterado com sucesso.\033[0m")