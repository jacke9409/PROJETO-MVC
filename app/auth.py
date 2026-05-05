# Hash e veroficação de senha com bcrypt
# geração de token JWT para autenticação
# leitura e validação de token vindo do cookie
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import requests, HTTPException, status
from dotenv import load_dotenv
import os
# carregar variáveis de ambiente do .env
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# cRyptContext para hash de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# função para gerar hash de senha
def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash: str) -> bool:
    return pwd_context.verify(senha, hash)

# funções do token
def criar_token(data: dict):
    paylod = data.copy()

    # define quando o token expira
    expira = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    paylod.update({"exp": expira})

    # criar o token
    token = jwt.encode(paylod, SECRET_KEY, algorithm=ALGORITHM)
    return token
def decodificar_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
    # dependenciais do fastapi para lidar com erros de autenticação

def get_usuario_logado(request: requests.Request):
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de autenticação não encontrado")
    try:
        payload = decodificar_token(token)
        email = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token de autenticação inválido"
                )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de autenticação inválido"
        )
    