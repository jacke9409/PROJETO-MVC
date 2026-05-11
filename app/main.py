from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import  HTMLResponse, RedirectResponse
from app.auth import get_usuario_opcional
from app.controllers import auth_controller
app = FastAPI(title="sistema estoque")

# configurar o fastapi para servir os arquivos estáticos (css, js, imagens)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

# incluir os routers dos controllers
app.include_router(auth_controller.router)

# tela inicial do sistema
@app.get("/")
def home(
    request: Request, 
    usuario_logado= Depends(get_usuario_opcional)
    ):

    if usuario_logado is None:
        return templates.TemplateResponse(
            request,
            "index.html", 
            {"request": request})
    
    # exibir a tela principal com os dados do usuario logado
    return templates.TemplateResponse(
        request,
        "home.html",
        {"request": request,
        "usuario": usuario_logado})