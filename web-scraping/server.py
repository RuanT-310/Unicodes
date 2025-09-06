from fastapi import FastAPI
from pydantic import BaseModel
from extracting_service import extracting_service
app = FastAPI()

class LoginData(BaseModel):
    usuario: str
    senha: str

@app.post("/login-and-scrape/")
def login_and_scrape(data: LoginData):
    """
    Realiza o login e raspa uma página protegida.

    Args:
        data (LoginData): Um objeto contendo 'usuario' e 'senha'.
    
    Returns:
        dict: Um dicionário com a mensagem de sucesso e o conteúdo raspado.
    """
    html = extracting_service(data)
    return {"status":"success","message":"Login e scraping concluídos!","html":html}