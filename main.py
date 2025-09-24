# main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dati import distributori

app = FastAPI()

# Alias città → nome completo
CITTA_ALIAS = {
    "monaco": "Monaco di Baviera",
    "monaco di baviera": "Monaco di Baviera",
    "mosca": "Mosca",
    "san pietroburgo": "San Pietroburgo",
    "pietrogrado": "San Pietroburgo",
    "pietroburgo": "San Pietroburgo",
    "volgograd": "Volgograd",
    "varsavia": "Varsavia",
    "parigi": "Parigi",
    "londra": "Londra",
    "stalingrado": "Volgograd",
    "krakau": "Cracovia",
    "krakow": "Cracovia"
}

# -- API esistenti ----------------------------------------------------------
@app.get("/distributori")
def elenco_distributori():
    return sorted([d.stato() for d in distributori], key=lambda x: x["id"])

@app.get("/distributori/provincia/{provincia}")
def livello_provincia(provincia: str):
    # Normalizza alias
    provincia_norm = CITTA_ALIAS.get(provincia.lower(), provincia)
    return [d.stato() for d in distributori if d.provincia.lower() == provincia_norm.lower()]

@app.get("/distributori/{id_distributore}")
def livello_distributore(id_distributore: int):
    for d in distributori:
        if d.id == id_distributore:
            return d.stato()
    return {"errore": "Distributore non trovato"}

@app.post("/distributori/prezzo/{provincia}")
def cambia_prezzo_provincia(provincia: str, tipo: str, nuovo_prezzo: float):
    provincia_norm = CITTA_ALIAS.get(provincia.lower(), provincia)
    modificati = []
    for d in distributori:
        if d.provincia.lower() == provincia_norm.lower():
            d.cambia_prezzo(tipo, nuovo_prezzo)
            modificati.append(d.stato())
    return modificati  # ritorna lista di distributori aggiornati

# -- Serve la pagina HTML (frontend) ---------------------------------------
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def pagina_home(request: Request):
    """
    Restituisce la pagina web principale.
    La pagina farà richieste JS alle API per mostrare dati e mappa.
    """
    return templates.TemplateResponse("index.html", {"request": request})
