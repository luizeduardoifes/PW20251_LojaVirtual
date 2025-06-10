CREATE_TABLE_CLIENTE = """
CREATE TABLE IF NOT EXISTS Cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    telefone TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    data_nascimento TEXT NOT NULL,
    senha_hash TEXT NOT NULL);
"""

INSERT_CLIENTE = """
INSERT INTO Cliente (nome, cpf, telefone, email, data_nascimento, senha_hash)
VALUES (?, ?, ?, ?, ?, ?);
"""

UPDATE_CLIENTE = """
UPDATE Cliente
SET nome = ?, cpf = ?, telefone = ?, email = ?, data_nascimento = ?, senha_hash = ?
WHERE id = ?;
"""

DELETE_CLIENTE = """
DELETE FROM Cliente
WHERE id = ?;
"""

GET_CLIENTE_BY_ID = """
SELECT id, nome, cpf, telefone, email, data_nascimento, senha_hash
FROM Cliente
WHERE id = ?;
"""

GET_CLIENTE_BY_EMAIL = """
SELECT id, nome, cpf, telefone, email, data_nascimento
FROM Cliente
WHERE email = ?;
"""

GET_CLIENTES_BY_PAGE = """
SELECT id, nome, cpf, telefone, email, data_nascimento, senha_hash
FROM Cliente
ORDER BY nome ASC
LIMIT ? OFFSET ?;
"""