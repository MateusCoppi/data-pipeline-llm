# Conexao com o Banco de Dados PostgreSQL

# Import
import psycopg2

def cria_conexao():
    
    # Conecta ao banco de dados PostgreSQL com as credenciais fornecidas
    conn = psycopg2.connect(
        dbname="mydatabase",
        user="admin",
        password="admin",
        host="localhost",
        port="5959"
    )

    return conn