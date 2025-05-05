# Constante para criar a tabela Produto
CREATE_TABLE_PRODUTO = """
CREATE TABLE IF NOT EXISTS Produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL,
    imagem TEXT NOT NULL
);
"""

# Constante para inserir um novo produto
INSERT_PRODUTO = """
INSERT INTO Produto (nome, descricao, preco, estoque, imagem) 
VALUES (?, ?, ?, ?, ?);
"""

# Constante para atualizar um produto existente
UPDATE_PRODUTO = """
UPDATE Produto 
SET nome = ?, descricao = ?, preco = ?, estoque = ?, imagem = ?
WHERE id = ?;
"""

# Constante para excluir um produto pelo ID
DELETE_PRODUTO = """
DELETE FROM Produto 
WHERE id = ?;
"""

# Constante para obter um produto pelo ID
GET_PRODUTO_BY_ID = """
SELECT id, nome, descricao, preco, estoque, imagem
FROM Produto 
WHERE id = ?;
"""

# Constante para obter produtos por página (com paginação)
GET_PRODUTOS_BY_PAGE = """
SELECT id, nome, descricao, preco, estoque, imagem
FROM Produto
ORDER BY nome ASC 
LIMIT ? OFFSET ?;
"""