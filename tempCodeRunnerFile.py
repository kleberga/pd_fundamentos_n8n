from fastapi import FastAPI
from gnews import GNews
from pydantic import BaseModel

# Inicializa a aplicação
app = FastAPI()

# Exemplo de rota que recebe um nome e retorna um cálculo ou texto
""" @app.get("/processar/{item_id}")
def ler_item(item_id: int, q: str = None):
    # Aqui você colocaria a lógica do seu código Python
    resultado = item_id * 2
    return {"id_recebido": item_id, "calculo": resultado, "query": q} """

# Criar a estrutura dos dados
class FiltroBusca(BaseModel):
    assunto: str
    ano_ini: int
    mes_ini: int
    dia_ini: int
    ano_fim: int
    mes_fim: int
    dia_fim: int

@app.post("/busca")
def ler_noticias(filtro: FiltroBusca):
    # Inicializa o buscador configurado para o Brasil
    google_news = GNews(language='pt', country='BR')

    # Define o intervalo de datas (Ano, Mês, Dia)
    google_news.start_date = (filtro.ano_ini, filtro.mes_ini, filtro.dia_ini)
    google_news.end_date = (filtro.ano_fim, filtro.mes_fim, filtro.dia_fim)

    # Faz a busca
    noticias = google_news.get_news(filtro.assunto)

    # Definir os veiculos abertos
    veiculos_abertos = ['G1', 'CNN Brasil', 'BBC News Brasil', 'Poder360', 'Agência Brasil', 'band.com.br', 'Portal G7']

    # Filtrar pelos veículos
    noticias_filtradas = [n for n in noticias if n['publisher']['title'] in veiculos_abertos]

    return noticias_filtradas