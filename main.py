# main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dati import distributori

app = FastAPI()

# -- API esistenti ----------------------------------------------------------
@app.get("/distributori")
def elenco_distributori():
    return sorted([d.stato() for d in distributori], key=lambda x: x["id"])

@app.get("/distributori/provincia/{provincia}")
def livello_provincia(provincia: str):
    return [d.stato() for d in distributori if d.provincia.lower() == provincia.lower()]

@app.get("/distributori/{id_distributore}")
def livello_distributore(id_distributore: int):
    for d in distributori:
        if d.id == id_distributore:
            return d.stato()
    return {"errore": "Distributore non trovato"}

@app.post("/distributori/prezzo/{provincia}")
def cambia_prezzo_provincia(provincia: str, tipo: str, nuovo_prezzo: float):
    count = 0
    for d in distributori:
        if d.provincia.lower() == provincia.lower():
            d.cambia_prezzo(tipo, nuovo_prezzo)
            count += 1
    return {
        "provincia": provincia,
        "tipo": tipo,
        "nuovo_prezzo": nuovo_prezzo,
        "distributori_aggiornati": count
    }

# -- Serve la pagina HTML (frontend) ---------------------------------------
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def pagina_home(request: Request):
    """
    Restituisce la pagina web principale.
    La pagina farà richieste JS alle API per mostrare dati e mappa.
    """
    return templates.TemplateResponse("index.html", {"request": request})
