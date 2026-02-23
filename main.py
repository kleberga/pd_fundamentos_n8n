from fastapi import FastAPI
from pydantic import BaseModel
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Criar a estrutura dos dados
class FiltroBusca(BaseModel):
    assunto: str
    data_ini: str
    data_fim: str

@app.post("/busca")
def busca_noticias(filtro: FiltroBusca):
    url = "https://newsapi.org/v2/everything" 
    params = { "q": filtro.assunto, "from": filtro.data_ini, "to": filtro.data_fim, "apiKey": os.getenv("NEWS_API") }

    response = requests.get(url, params=params)

    data = response.json()

    return data