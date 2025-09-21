import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Monitoraggio Distributori Iperstaroil")

# 0. Elenco distributori
if st.button("Mostra tutti i distributori"):
    data = requests.get(f"{API_URL}/distributori").json()
    st.table(data)

# 1. Livello per provincia
provincia = st.text_input("Provincia")
if st.button("Mostra livello provincia"):
    data = requests.get(f"{API_URL}/distributori/provincia/{provincia}").json()
    st.json(data)

# 2. Livello distributore specifico
id_dist = st.number_input("ID Distributore", step=1)
if st.button("Mostra livello distributore"):
    data = requests.get(f"{API_URL}/distributori/{id_dist}").json()
    st.json(data)

# Cambio prezzo
prov = st.text_input("Provincia per cambio prezzo")
tipo = st.selectbox("Tipo carburante", ["benzina", "diesel"])
nuovo_prezzo = st.number_input("Nuovo prezzo", step=0.01, format="%.2f")
if st.button("Aggiorna prezzi"):
    data = requests.post(f"{API_URL}/distributori/prezzo/{prov}", 
                         params={"tipo": tipo, "nuovo_prezzo": nuovo_prezzo}).json()
    st.json(data)

# 3. Mappa distributori
if st.button("Mostra distributori su mappa"):
    data = requests.get(f"{API_URL}/distributori").json()
    st.map({"lat": [d["coordinate"][0] for d in data],
            "lon": [d["coordinate"][1] for d in data]})
