from fastapi.responses import RedirectResponse
import uvicorn
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.templating import Jinja2Templates
from babel.numbers import format_currency
from starlette.middleware.sessions import SessionMiddleware
from passlib.context import CryptContext

from repo.categoria_repo import criar_tabela_categorias, obter_categorias_por_pagina
from repo.cliente_repo import criar_tabela_clientes, obter_clientes_por_pagina
from repo.endereco_repo import criar_tabela_enderecos, obter_enderecos_por_pagina
from repo.produto_repo import criar_tabela_produtos, obter_produto_por_id, obter_produtos_por_pagina
from util.auth import SECRET_KEY, autenticar_usuario

criar_tabela_produtos()
criar_tabela_clientes()
criar_tabela_categorias()
criar_tabela_enderecos()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

def format_currency_br(value, currency='BRL', locale='pt_BR'):
    return format_currency(value, currency, locale=locale)

templates.env.filters['format_currency_br'] = format_currency_br

@app.get("/login")
def read_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(
    request: Request, 
    email: str = Form(), 
    senha: str = Form()):
    usuario = autenticar_usuario(email, senha)    
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    request.session["usuario"] = usuario
    return RedirectResponse(url="/", status_code=303)

@app.post("/logout")
async def logout(request: Request):    
    request.session.clear()
    return RedirectResponse(url="/", status_code=303)

@app.get("/")
def read_root(request: Request):
    produtos = obter_produtos_por_pagina(12, 0)
    response = templates.TemplateResponse("index.html", {"request": request, "produtos": produtos})
    return response

@app.get("/produtos/{id}")
def read_produto(request: Request, id: int):
    produto = obter_produto_por_id(id)
    response = templates.TemplateResponse("produto.html", {"request": request, "produto": produto})
    return response

@app.get("/clientes")
def read_clientes(request: Request):
    clientes = obter_clientes_por_pagina(12, 0)
    response = templates.TemplateResponse("clientes.html", {"request": request, "clientes": clientes})
    return response

@app.get("/produtos")
def read_produtos(request: Request):
    produtos = obter_produtos_por_pagina(12, 0)
    response = templates.TemplateResponse("produtos.html", {"request": request, "produtos": produtos})
    return response

@app.get("/categorias")
def read_categorias(request: Request):
    categorias = obter_categorias_por_pagina(12, 0)
    response = templates.TemplateResponse("categorias.html", {"request": request, "categorias": categorias})
    return response

@app.get("/enderecos")
def read_enderecos(request: Request):
    enderecos = obter_enderecos_por_pagina(12, 0)
    response = templates.TemplateResponse("enderecos.html", {"request": request, "enderecos": enderecos})
    return response


if __name__ == "__main__":
    uvicorn.run(app=app, port=8000, reload=True)