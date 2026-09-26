import os

import psycopg
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

with psycopg.connect(database_url) as conexao:
    with conexao.cursor() as cursor:
        cursor.execute("SELECT 1")
        resultado = cursor.fetchone()
        print("Conexão funcionou! Resultado:", resultado)
