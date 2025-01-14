import csv 
with open ('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key, value])

from helper import *
from presentatie import *

inkomsten = {
    "aardbeien-ijs-totaal" : 1000
    "vanille-ijs-totaal" : 2000
    "chocolade-ijs-totaal" : 1500
    "waterijsjes-totaal" : 750
}

totaal_inkomsten = som(inkomsten)

def presenteer(inkomsten, totaal_inkomsten):
    for item, waarde in inkomsten.items():
        print(f"{item}-totaal : {waarde} euro")
    print("=" * 25)
    print(f"totaal : {totaal_inkomsten} euro")

totaal_inkomsten = sum(inkomsten.values())

presenteer(inkomsten, totaal_inkomsten)