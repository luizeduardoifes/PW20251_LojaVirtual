from fastapi import HTTPException, Request
from passlib.context import CryptContext

from models.usuario import Usuario

SECRET_KEY="cae3def7c5c8f5c07613a742c1c5435076ccf0777c259796ad1653c0fd5dfdd7"

criptografia = CryptContext(schemes=["bcrypt"], deprecated="auto")

db_usuarios = {
    "admin@email.com": {
        "nome": "Admnistrador do Sistema",
        "email": "admin@email.com",
        "senha_hashed": criptografia.hash("admin123"),
        "perfis": ["admin", "user"]
    },
    "usuario@email.com": {
        "nome": "Usuário do Sistema",
        "email": "usuario@email.com",
        "senha_hashed": criptografia.hash("user123"),
        "perfis": ["user"]
    }
}

def verificar_senha(senha_normal: str, senha_hashed: str) -> bool:
    return criptografia.verify(senha_normal, senha_hashed)

def autenticar_usuario(usuario: str, senha: str):
    usuario = db_usuarios.get(usuario)
    if not usuario or not verificar_senha(senha, usuario["senha_hashed"]):
        return None
    return usuario

def obter_usuario_logado(request: Request):
    usuario = request.session.get("usuario")
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autenticado")
    usuario = db_usuarios.get(usuario)
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return Usuario(nome=usuario["nome"], email=usuario["email"], senha_hash=usuario["senha_hashed"])