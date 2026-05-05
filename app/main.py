from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import  HTMLResponse, RedirectResponse
from app.controllers import auth_controller
app = FastAPI(title="sistema estoque")

# configurar o fastapi para servir os arquivos estáticos (css, js, imagens)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

# incluir os routers dos controllers
app.include_router(auth_controller.router)
