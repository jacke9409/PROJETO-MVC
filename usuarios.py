from app.database import Session, engine, Base
from app.models.usuario import Usuario
from app.auth import hash_senha

Usuarios = [
    {
        "nome": "Admin",
        "email": "admin@teste.com",
        "senha": "admin1234"
    },
    {
        "nome": "Gabriel",
        "email": "gabriel@admin.com",
        "senha": "gabriel1234",
        "role": "admin",
    },
]

def criar_usuarios():
    db = Session()
    try:
        for usuario in Usuarios:
            existente = db.query(Usuario).filter_by(email = usuario["email"]).first()

            if existente:
                print(f"Já existe esse email: {usuario['email']} no banco.")
                continue
            else:
                novo_usuario = Usuario(
                    nome = usuario["nome"],
                    email = usuario["email"],
                    senha_hash = hash_senha(usuario["senha"]),
                    role = usuario.get("role", "user"), # .get evita erro caso o "role" não exista
                )
                db.add(novo_usuario)
        
        db.commit()
        print(f"Usuarios cadastrados com sucesso!")
    except Exception as erro:
        db.rollback()
        print(erro)
    finally:
        db.close()