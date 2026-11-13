from Pannello import PannelloFotovoltaico
from impianto import ImpiantoSolare

def registra_impianto(impianti: list[ImpiantoSolare], impianto: ImpiantoSolare)-> None:
    if impianto in impianti:
        raise ValueError("The implant is already in the list")
    impianti.append(impianto)
    
def cerca_impianto(impianti: list[ImpiantoSolare], codice: str) -> ImpiantoSolare:
    for i in impianti:
        if i.codice.upper() == codice.upper():
            return i
    return None

def riepilogo_impianti(nome_azienda: str, impianti: list[ImpiantoSolare]) -> None:
    print("Riepilogo Impianti dell' azienda: ", nome_azienda)
    for i in impianti:
        print("codice: ",  i.codice)
        print("modello: ", i.modello)
        print("stato: ", i.stato)
        print("potenza totale: ", i.potenza_pannelli())
    
if __name__=="__main__":
    impianti: list[ImpiantoSolare] = []
    impianto1 =  ImpiantoSolare("primo", "modello1", "localita1", 500.5, "OK")
    impianto2 = ImpiantoSolare("secondo", "modello2", "localita2", 600.5, "In progress")
    impianto3 = ImpiantoSolare("terzo", "modello3", "localita3", 700.5, "Alted")
    impianto4 = ImpiantoSolare("quarto", "modello4", "localita4", 800.5, "OK")
    registra_impianto(impianti, impianto1)
    registra_impianto(impianti, impianto2)
    registra_impianto(impianti, impianto3)
    registra_impianto(impianti, impianto4)
    
    pannello1 =  PannelloFotovoltaico("pannello1" ,"modello1", (6.0))
    pannello2 = PannelloFotovoltaico("pannello2" ,"modello2", (7.0))
    pannello3 =  PannelloFotovoltaico("pannello3" ,"modello3", (8.0))
    pannello4 = PannelloFotovoltaico("pannello4" ,"modello4", (9.0))
    pannello5 =  PannelloFotovoltaico("pannello5" ,"modello5", (10.0))
    pannello6 = PannelloFotovoltaico("pannello6" ,"modello6", (11.0))
    pannello7 =  PannelloFotovoltaico("pannello7" ,"modello7", (12.0))
    pannello8 = PannelloFotovoltaico("pannello8" ,"modello8", (57.0))
    impianti[0].aggiungi_pannello(pannello1)
    impianti[0].aggiungi_pannello(pannello2)
    impianti[1].aggiungi_pannello(pannello3)
    impianti[1].aggiungi_pannello(pannello4)
    impianti[2].aggiungi_pannello(pannello5)
    impianti[2].aggiungi_pannello(pannello6)
    impianti[3].aggiungi_pannello(pannello7)
    impianti[3].aggiungi_pannello(pannello8)
        
    riepilogo_impianti("Azienda Pascal", impianti)
    print(cerca_impianto(impianti, "primo"))
    print(cerca_impianto(impianti, "quinto"))
          
    print(impianti[0].cerca_pannello("pannello34450"))
    
    print(impianti[0].pannelli_sotto_potenza, 1000000000.5)
    
    p1 = impianti[0].cerca_pannello("pannello1")
    p2 = impianti[0].rimuovi_pannello("pannello1")
    
    print(p1)
    print(p2)
    
    
    
    
    
    
    