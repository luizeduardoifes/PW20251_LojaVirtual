from data.database import obter_conexao
from sql.endereco_sql import *
from models.endereco import Endereco

def criar_tabela_enderecos():
    """Cria a tabela Endereco se ela não existir."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(CREATE_TABLE_ENDERECO)
    conexao.commit()
    conexao.close()

def inserir_endereco(endereco: Endereco) -> Endereco:
    """Insere um novo endereco no banco de dados."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(INSERT_ENDERECO, 
        (endereco.logradouro, endereco.numero, endereco.complemento, endereco.bairro, endereco.cidade, endereco.uf, endereco.cep))
    endereco.id = cursor.lastrowid
    conexao.commit()
    conexao.close()
    return endereco

def atualizar_endereco(endereco: Endereco) -> bool:
    """Atualiza um endereco existente no banco de dados."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(UPDATE_ENDERECO, 
        (endereco.logradouro, endereco.numero, endereco.complemento, endereco.bairro, endereco.cidade, endereco.uf, endereco.cep, endereco.id))
    conexao.commit()
    conexao.close()
    return (cursor.rowcount > 0)

def excluir_endereco(id: int) -> bool:
    """Exclui um endereco do banco de dados pelo ID."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(DELETE_ENDERECO, (id,))
    conexao.commit()
    conexao.close()
    return (cursor.rowcount > 0)

def obter_endereco_por_id(id: int) -> Endereco:
    """Obtém um endereco do banco de dados pelo ID."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(GET_ENDERECO_BY_ID, (id,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        return Endereco(*resultado)
    return None

def obter_enderecos_por_pagina(limite: int, offset: int) -> list[Endereco]:
    """Obtém uma lista de enderecos do banco de dados com base na paginação."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(GET_ENDERECOS_BY_PAGE, (limite, offset))
    resultados = cursor.fetchall()
    conexao.close()
    return [Endereco(*resultado) for resultado in resultados]