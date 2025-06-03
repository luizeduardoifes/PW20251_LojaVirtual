import sqlite3

def obter_conexao():
    conexao = sqlite3.connect('dados.db')
    conexao.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conexao