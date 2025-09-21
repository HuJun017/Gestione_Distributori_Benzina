class Distributore:
    def __init__(self, id_distributore, nome, provincia, lat, lon,
                 capienza_benzina, capienza_diesel,
                 prezzo_benzina, prezzo_diesel, numero_pompe):

        self.id = id_distributore
        self.nome = nome
        self.provincia = provincia
        self.lat = lat
        self.lon = lon

        self.capienza_benzina = capienza_benzina
        self.capienza_diesel = capienza_diesel

        self.volume_benzina = capienza_benzina
        self.volume_diesel = capienza_diesel

        self.prezzo_benzina = prezzo_benzina
        self.prezzo_diesel = prezzo_diesel
        self.numero_pompe = numero_pompe

        self.venduti_benzina = 0
        self.venduti_diesel = 0
        self.incasso = 0

    def stato(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "provincia": self.provincia,
            "coordinate": (self.lat, self.lon),
            "litri_benzina_venduti": self.venduti_benzina,
            "litri_diesel_venduti": self.venduti_diesel,
            "incasso": self.incasso,
            "benzina_disponibile": self.volume_benzina,
            "diesel_disponibile": self.volume_diesel,
            "prezzo_benzina": self.prezzo_benzina,
            "prezzo_diesel": self.prezzo_diesel,
        }

    def cambia_prezzo(self, tipo, nuovo_prezzo):
        if tipo == "benzina":
            self.prezzo_benzina = nuovo_prezzo
        elif tipo == "diesel":
            self.prezzo_diesel = nuovo_prezzo
