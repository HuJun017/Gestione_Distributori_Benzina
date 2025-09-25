from serbatoio import Serbatoio

class Distributore(Serbatoio):
    def __init__(self, id_distributore, nome, provincia, lat, lon,
                 capienza_benzina, capienza_diesel,
                 prezzo_benzina, prezzo_diesel, numero_pompe):

        super().__init__(capienza_benzina, 0, 0, 0, 0)

        self.id = id_distributore
        self.nome = nome
        self.provincia = provincia
        self.lat = lat
        self.lon = lon

        self.capienza_benzina = capienza_benzina
        self.capienza_diesel = capienza_diesel

        # inizialmente pieni
        self.volume_benzina = capienza_benzina
        self.volume_diesel = capienza_diesel

        self.prezzo_benzina = prezzo_benzina
        self.prezzo_diesel = prezzo_diesel
        self.numero_pompe = numero_pompe

        self.venduti_benzina = 0
        self.venduti_diesel = 0
        self.incasso = 0

    def stato(self):
        """Restituisce tutte le informazioni del distributore"""
        return {
            "id": self.id,
            "nome": self.nome,
            "provincia": self.provincia,
            "coordinate": (self.lat, self.lon),
            "benzina_disponibile": self.volume_benzina,
            "diesel_disponibile": self.volume_diesel,
            "prezzo_benzina": self.prezzo_benzina,
            "prezzo_diesel": self.prezzo_diesel,
            "numero_pompe": self.numero_pompe,
            "litri_benzina_venduti": self.venduti_benzina,
            "litri_diesel_venduti": self.venduti_diesel,
            "incasso": self.incasso
        }

    def cambia_prezzo(self, tipo, nuovo_prezzo):
        """Aggiorna il prezzo di un carburante."""
        if tipo == "benzina":
            self.prezzo_benzina = nuovo_prezzo
        elif tipo == "diesel":
            self.prezzo_diesel = nuovo_prezzo
        else:
            raise ValueError("Tipo carburante non valido. Usa 'benzina' o 'diesel'.")

    def eroga_carburante(self, tipo, litri):
        """Eroga una quantità di carburante, se disponibile."""
        if litri <= 0:
            raise ValueError("La quantità deve essere positiva.")

        if tipo == "benzina":
            if self.volume_benzina >= litri:
                self.volume_benzina -= litri
                self.venduti_benzina += litri
                self.incasso += litri * self.prezzo_benzina
                return True
            else:
                return False

        elif tipo == "diesel":
            if self.volume_diesel >= litri:
                self.volume_diesel -= litri
                self.venduti_diesel += litri
                self.incasso += litri * self.prezzo_diesel
                return True
            else:
                return False

        else:
            raise ValueError("Tipo carburante non valido. Usa 'benzina' o 'diesel'.")
