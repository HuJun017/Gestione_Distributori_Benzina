class Serbatoio:
    def __init__(self, capienza, altezza, lunghezza, larghezza, liquido_interno):
        if capienza <= 0:
            raise ValueError("CapacityValue must be higher than 0")
        self.capienza = capienza
        self.altezza = altezza
        self.lunghezza = lunghezza
        self.larghezza = larghezza
        self.liquido_interno = liquido_interno
        self.volume = 0  # inizialmente vuoto

    # Riempire serbatoio (aggiunge volume)
    def riempire(self, volume):
        if self.volume + volume > self.capienza:
            return False
        self.volume += volume
        return True

    # Svuotare serbatoio
    def svuotare(self):
        volume_svuotato = self.volume   # <----- serve per dire di quanto liquido è stato svuotato il serbatoio
        self.volume = 0
        return volume_svuotato

    # Controllo liquido interno
    def check_liquido(self):
        return self.liquido_interno

    # Controllo volume attuale
    def check_volume(self):
        return self.volume

    # Controllo dimensioni
    def check_dimensioni(self):
        return self.altezza, self.lunghezza, self.larghezza