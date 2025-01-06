from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van 4 euro voor {nieuwe_prijs} euro")

aanbieding_1("aardbei", 4, 0.1)
print()
print("------------------------------------------------------------------------------------------------------------------------------------")
print()

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    bedrag_btw = totaal * (btw / 100)
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag_btw} euro btw betaald dient te worden."

inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw = 9

resultaat = inkomsten_totaal(inkomsten, btw)
print(resultaat)
print()
print("------------------------------------------------------------------------------------------------------------------------------------")
print()

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [laagste, hoogste]

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

resultaat = laag_en_hoog(mijn_lijst)
print(resultaat)
print()
print("------------------------------------------------------------------------------------------------------------------------------------")
print()

def gemiddelde(mijn_lijst):
    gemiddelde = sum(mijn_lijst) / len(mijn_lijst)
    return [gemiddelde]

resultaat = gemiddelde(mijn_lijst)
print(f"De gemiddelde inkomsten deze week zijn {resultaat} euro")
print()
print("------------------------------------------------------------------------------------------------------------------------------------")
print()

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]

resultaat = meervoudig(invoer_lijst)
print(resultaat)
print()
print("------------------------------------------------------------------------------------------------------------------------------------")
print()


