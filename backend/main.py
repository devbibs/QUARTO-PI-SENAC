from fastapi import FastAPI
from fastapi import Body
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import os

app = FastAPI(title="TechVagas API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #autorizando qualquer origem a acessar a API somente por questões de teste
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_NAME = os.path.join(os.path.dirname(__file__), "database.db")


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS oportunidades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        tipo TEXT,
        tag TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS perfil (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        bio TEXT,
        nascimento TEXT,
        endereco TEXT,
        contato TEXT,
        interesses TEXT
    )
""")

    
    cursor.execute("SELECT COUNT(*) FROM oportunidades")
    count = cursor.fetchone()[0]

    if count == 0:
        dados_iniciais = [
            ("Desenvolvedor Python", "Vaga", "Backend"),
            ("Curso de IA para Iniciantes", "Curso", "IA"),
            ("Analista de Sistemas", "Vaga", "Sistemas"),
            ("Especialização em Data Science", "Curso", "IA")
        ]

        cursor.executemany(
            "INSERT INTO oportunidades (titulo, tipo, tag) VALUES (?, ?, ?)",
            dados_iniciais
        )

    conn.commit()
    conn.close()


init_db()


@app.get("/oportunidades")
def listar(filtro: str = None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    if filtro:
        cursor.execute("""
        SELECT * FROM oportunidades
        WHERE LOWER(titulo) LIKE ?
        """, ('%' + filtro.lower() + '%',))
    else:
        cursor.execute("SELECT * FROM oportunidades")

    resultados = cursor.fetchall()
    conn.close()

    return [
        {"id": row[0], "titulo": row[1], "tipo": row[2], "tag": row[3]}
        for row in resultados
    ]

    @app.post("/perfil")
    def salvar_perfil(perfil: dict = Body(...)):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM perfil")

        cursor.execute(
            "INSERT INTO perfil (id, nome, bio) VALUES (1, ?, ?)",
            (perfil.get("nome"), perfil.get("bio"))
        )

        conn.commit()
        conn.close()

        return {"status": "ok"}


@app.get("/perfil")
def obter_perfil():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nome, bio, nascimento, endereco, contato, interesses
        FROM perfil WHERE id = 1
    """)
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        return {
            "nome": resultado[0],
            "bio": resultado[1],
            "nascimento": resultado[2],
            "endereco": resultado[3],
            "contato": resultado[4],
            "interesses": resultado[5]
        }

    return {}