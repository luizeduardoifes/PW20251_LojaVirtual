from fastapi import Request, HTTPException
from passlib.context import CryptContext

SECRET_KEY = "9471ca5ca862aea6c3c7f9518239c613ce5cfe60bcd7782e0baaad0e9086c4e6"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
    

def authenticate_user(username: str, password: str):
    # user = fake_users_db.get(username)
    # if not user or not verify_password(password, user["hashed_password"]):
    #     return None
    # return user
    pass

def get_current_user(request: Request):
    """Dependency para verificar se o usuário está logado"""
    username = request.session.get("user")
    if not username:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # user = fake_users_db.get(username)
    # if not user:
    #     raise HTTPException(status_code=401, detail="User not found")
    
    # return User(username=user["username"], email=user["email"])