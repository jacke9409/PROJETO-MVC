from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func #pega a data atual (func)
#preciso importar do database, a classe Base que tem la, pra ca
#mas preciso ver aonde ele está, dentro de app então:
from app.database import Base

class Usuario(Base):
    __tablename__= "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)

    nome = Column(String(100), nullable=False)

    email= Column(String(100), unique=True, index=True, nullable=False)

    senha_hash = Column(String(225), nullable=False)

    # perfil do usuário:admin ou operador
    role = Column(String(20), nullable=False, default="operador")

    # para saber se o usuário está ativo ou não 
    ativo = Column(Boolean, nullable=False, default=True)
    #preenchimento automatico pelo banco de dados ao criar o registro
    criado_em = Column(DateTime, server_default=func.now())