from database import obter_conexao
from produto_sql import *
from produto import Produto

def criar_tabela():
    """Cria a tabela Produto se ela não existir."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(CREATE_TABLE_PRODUTO)
    conexao.commit()
    conexao.close()

def inserir_produto(produto: Produto) -> Produto:
    """Insere um novo produto no banco de dados."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(INSERT_PRODUTO, 
        (produto.nome, produto.descricao, produto.preco, produto.estoque, produto.imagem))
    produto.id = cursor.lastrowid
    conexao.commit()
    conexao.close()
    return produto

def atualizar_produto(produto: Produto) -> bool:
    """Atualiza um produto existente no banco de dados."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(UPDATE_PRODUTO, 
        (produto.nome, produto.descricao, produto.preco, produto.estoque, produto.imagem, produto.id))
    conexao.commit()
    conexao.close()
    return (cursor.rowcount > 0)

def excluir_produto(id: int) -> bool:
    """Exclui um produto do banco de dados pelo ID."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(DELETE_PRODUTO, (id,))
    conexao.commit()
    conexao.close()
    return (cursor.rowcount > 0)

def obter_produto_por_id(id: int) -> Produto:
    """Obtém um produto pelo ID."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(GET_PRODUTO_BY_ID, (id,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        return Produto(
            id=resultado[0],
            nome=resultado[1],
            descricao=resultado[2],
            preco=resultado[3],
            estoque=resultado[4],
            imagem=resultado[5]
        )
    return None

def obter_produtos_por_pagina(limite: int, offset: int) -> list[Produto]:
    """Obtém uma lista de produtos com paginação."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(GET_PRODUTOS_BY_PAGE, (limite, offset))
    resultados = cursor.fetchall()
    conexao.close()
    return [Produto(
        id=resultado[0],
        nome=resultado[1],
        descricao=resultado[2],
        preco=resultado[3],
        estoque=resultado[4],
        imagem=resultado[5]
    ) for resultado in resultados]