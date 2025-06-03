from data.database import obter_conexao
from sql.categoria_sql import *
from models.categoria import Categoria

def criar_tabela_categorias() -> bool:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(CREATE_TABLE_CATEGORIA)
        return (cursor.rowcount > 0)



def inserir_categoria(categoria: Categoria) -> Categoria:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(INSERT_CATEGORIA, 
            (categoria.nome))
        categoria.id = cursor.lastrowid
        return categoria

def atualizar_categoria(categoria: Categoria) -> bool:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(UPDATE_CATEGORIA, 
            (categoria.nome, categoria.id))
        return (cursor.rowcount > 0)

def excluir_categoria(id: int) -> bool:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(DELETE_CATEGORIA, (id,))
        return (cursor.rowcount > 0)

def obter_categoria_por_id(id: int) -> Categoria:
    with obter_conexao() as conexao:
        cursor = conexao.cursor()
        cursor.execute(GET_CATEGORIA_BY_ID, (id,))
        resultado = cursor.fetchone()
        if resultado:
            return Categoria(
                id=resultado["id"],
                nome=resultado["nome"])
        return None

def obter_categorias_por_pagina(numero_pagina: int, tamanho_pagina: int) -> list[Categoria]:
    with obter_conexao() as conexao:
        limite = tamanho_pagina
        offset = (numero_pagina - 1) * tamanho_pagina
        cursor = conexao.cursor()
        cursor.execute(GET_CATEGORIAS_BY_PAGE, (limite, offset))
        resultados = cursor.fetchall()
        return [Categoria(
            id=resultado["id"],
            nome=resultado["nome"]) 
            for resultado in resultados]