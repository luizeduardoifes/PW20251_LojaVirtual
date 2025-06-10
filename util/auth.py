from typing import Optional
from fastapi import HTTPException, Request
import hashlib

from models.usuario import Usuario
from repo import cliente_repo



SECRET_KEY="cae3def7c5c8f5c07613a742c1c5435076ccf0777c259796ad1653c0fd5dfdd7"

def hash_senha(senha: str) -> str:
    return hashlib.sha256(senha.encode()).hexdigest()

def verificar_senha(senha_normal: str, senha_hashed: str) -> bool:
    return hash_senha(senha_normal) == senha_hashed

def autenticar_usuario(email: str, senha: str):
    usuario = cliente_repo.obter_cliente_por_email(email)
    if not usuario or not verificar_senha(senha, usuario.senha_hash):
        return None
    return usuario

def obter_usuario_logado(request: Request) -> Optional[Usuario]:
    usuario = request.session.get("usuario")
    if not usuario:
        raise HTTPException(status_code=401, detail="Não autenticado")
    
    return usuario

print("senha do usuario:", hash_senha("123456"))