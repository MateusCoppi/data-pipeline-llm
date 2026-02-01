# Pipeline de Carga de Dados

# Imports
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# Cria o motor de conexão
engine = create_engine('postgresql+psycopg2://admin:admin@localhost:5959/mydatabase')

print("\nIniciando o Processo de Carga dos Dados!\n")

# Função para carregar dados dos arquivos CSV para o PostgreSQL no schema especificado
def carrega_dados(csv_file, table_name, schema):

    # Bloco try/except
    try:

        # Lê o arquivo CSV
        df = pd.read_csv(csv_file)

        # Executa SQL a partir do dataframe do Pandas
        df.to_sql(table_name, engine, schema = schema, if_exists = 'append', index = False)
        print(f"Dados do arquivo {csv_file} foram inseridos na tabela {schema}.{table_name}.")

    except Exception as e:
        print(f"Erro ao inserir dados do arquivo {csv_file} na tabela {schema}.{table_name}: {e}")

# Carregamento dos dados no schema 'lab'
carrega_dados('../data_src/clientes.csv', 'clientes', 'lab')
carrega_dados('../data_src/produtos.csv', 'produtos', 'lab')
carrega_dados('../data_src/compras.csv', 'compras', 'lab')

print("\nCarga Executada com Sucesso!\n")



