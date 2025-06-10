from dataclasses import dataclass
import datetime
from typing import Optional


@dataclass
class Cliente:
    id: int
    nome: str
    cpf: str
    telefone: str
    email: str    
    data_nascimento: datetime
    senha_hash: Optional[str]
    