import sqlite3

def get_contexto():
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contexto')
    contexto = cursor.fetchall()
    conn.close()
    return contexto

def get_historico():
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM historico')
    historico = cursor.fetchall()
    conn.close()
    return historico
