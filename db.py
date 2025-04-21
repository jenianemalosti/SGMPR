import oracledb

# Função de conexão com o banco de dados
def conectar_oracle():
    dsn = oracledb.makedsn('localhost', '1521', service_name='xe')
    conn = oracledb.connect(user='system', password='1234', dsn=dsn)

    # Verificando o usuário conectado
    cursor = conn.cursor()
    cursor.execute("SELECT user FROM dual")
    user = cursor.fetchone()[0]
    print(f"Conectado como: {user}")  # Exibe o usuário com o qual está conectado
    cursor.close()  # Não se esqueça de fechar o cursor
    return conn


# Testando a conexão
conn = conectar_oracle()
