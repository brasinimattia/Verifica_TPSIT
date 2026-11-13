from Pannello import PannelloFotovoltaico
class ImpiantoSolare:
    def __init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str) -> None:
        self.codice = codice
        self.modello = modello
        self.localita = localita
        self.potenza_massima_kw = potenza_massima_kw
        self.stato = stato
        self.pannelli: list[PannelloFotovoltaico]
        
    def aggiungi_pannello(self, pannello: PannelloFotovoltaico) -> None:
        self.pannelli.append(pannello)
        
    def potenza_pannelli(self)->float:
        potenza_tot = 0
        for p in self.pannelli:
            potenza_tot += p.potenza_kw
            
        return potenza_tot
    
    def cerca_pannello(self, codice:str) -> PannelloFotovoltaico:
        for p in self.pannelli:
            if p.codice == codice:
                return p
        return None
    
    def rimuovi_pannello(self, codice:str) -> PannelloFotovoltaico:
        pannello: PannelloFotovoltaico
        for p in self.pannelli:
            if p.codice == codice:
                pannello = p
                self.pannelli.remove(p)
                return pannello
        return None
    
    