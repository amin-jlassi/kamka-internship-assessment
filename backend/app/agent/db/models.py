# app/db/models.py
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "llmdb.sqlite3")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS LLM_PROVIDER (
            id INT PRIMARY KEY ,
            model_name VARCHAR(200)
        );

        INSERT OR IGNORE INTO LLM_PROVIDER (id , model_name)
        VALUES ('1', 'google');
    """)
    conn.commit()
    conn.close()

def get_llm_provider() -> str:
    conn = get_connection()
    row = conn.execute(
        "SELECT model_name FROM LLM_PROVIDER WHERE id = 1"
    ).fetchone()
    conn.close()
    if row : 
        return row["model_name"]
    else : 
        return None
    

def update_llm_provider(model_name: str):
    conn = get_connection()
    conn.execute(
        "UPDATE LLM_PROVIDER SET model_name = (?) WHERE id = 1",
        (model_name,)
    )
    conn.commit()
    conn.close()