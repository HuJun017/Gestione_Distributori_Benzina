from fastapi import FastAPI
from dati import distributori

app = FastAPI()

# 0. Elenco ordinato per ID
@app.get("/distributori")
def elenco_distributori():
    return sorted([d.stato() for d in distributori], key=lambda x: x["id"])

# 1. Livello carburante per provincia
@app.get("/distributori/provincia/{provincia}")
def livello_provincia(provincia: str):
    return [d.stato() for d in distributori if d.provincia.lower() == provincia.lower()]

# 2. Livello carburante distributore specifico
@app.get("/distributori/{id_distributore}")
def livello_distributore(id_distributore: int):
    for d in distributori:
        if d.id == id_distributore:
            return d.stato()
    return {"errore": "Distributore non trovato"}

# Cambio prezzo per tutti i distributori di una provincia
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
