-------------------------------------------------------------------------
no vscode para instalar todas as bibliotecas, no terminal:
pip install -r requirements.txt, pedir pra instalar o ambiente, fala q n
--------------------------------------------------------------------------
<!-- iniciar alembic -->

python -m alembic init migrations

<!-- gerar a migration -->

bash
python -m alembic revision --autogenerate -m "criar tabela usuarios"

<!-- aplicar a migration -->
python -m alembic upgrade head