from data.database import obter_conexao
from sql.categoria_sql import *
from models.categoria_model import Categoria

def criar_tabela_categorias():
    """Cria a tabela Categoria se ela não existir."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(CREATE_TABLE_CATEGORIA)
    conexao.commit()
    conexao.close()

def inserir_categoria(categoria: Categoria) -> Categoria:
    """Insere uma nova categoria no banco de dados."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(INSERT_CATEGORIA, (categoria.nome,))
    categoria.id = cursor.lastrowid
    conexao.commit()
    conexao.close()
    return categoria

def atualizar_categoria(categoria: Categoria) -> bool:
    """Atualiza uma categoria existente no banco de dados."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(UPDATE_CATEGORIA, (categoria.nome, categoria.id))
    conexao.commit()
    conexao.close()
    return (cursor.rowcount > 0)

def excluir_categoria(id: int) -> bool:
    """Exclui uma categoria do banco de dados pelo ID."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(DELETE_CATEGORIA, (id,))
    conexao.commit()
    conexao.close()
    return (cursor.rowcount > 0)

def obter_categoria_por_id(id: int) -> Categoria:
    """Obtém uma categoria pelo ID."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(GET_CATEGORIA_BY_ID, (id,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        return Categoria(id=resultado[0], nome=resultado[1])
    return None

def obter_categorias_por_pagina(limite: int, offset: int) -> list[Categoria]:
    """Obtém uma lista de categorias com paginação."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(GET_CATEGORIAS_BY_PAGE, (limite, offset))
    resultados = cursor.fetchall()
    conexao.close()
    return [Categoria(id=resultado[0], nome=resultado[1]) for resultado in resultados]