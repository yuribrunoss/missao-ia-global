import os

import psycopg
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

with psycopg.connect(database_url) as conexao:
    with conexao.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                nome TEXT NOT NULL,
                ativo BOOLEAN NOT NULL DEFAULT TRUE
            )
        """)
        print("Tabela criada!")
