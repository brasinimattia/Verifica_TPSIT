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
    
    for i in range(1,5):
        pannello1 =  PannelloFotovoltaico(f"pannello{i}" ,f"modello{i}", (5.0 + i))
        pannello2 = PannelloFotovoltaico(f"pannello{i+10}" ,f"modello{i+10}", (5.0 + i+10))
        impianti[i].aggiungi_pannello(pannello1)
        impianti[i].aggiungi_pannello(pannello2)
        
    riepilogo_impianti(impianti)
    print(cerca_impianto(impianti, "primo"))
    print(cerca_impianto(impianti, "quinto"))
          
    print(impianti[1].cerca_pannello("pannello34450"))
    
    print(impianti[1].pannelli_sotto_potenza, 1000000000.5)
    
    p = impianti[1].cerca_pannello("pannello1")
    p = impianti[1].rimuovi_pannello("pannello1")
    
    
    
    