#mijn_functie 1
def mijn_functie_1(argumenten):
    return [x**2 for x in argumenten]

argumenten = (2, 4, 10, 12)
resultaat = mijn_functie_1(argumenten)
print(resultaat) 
print()
print("------------------------------------------------------------------------------------------------------------------------------------")
print()
#mijn_functie 2
def mijn_functie_2(a, b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a + b)
    uitvoer_lijst.append(a - b)
    uitvoer_lijst.append(a * b)
    uitvoer_lijst.append(a / b)
    return uitvoer_lijst

a = [12, 12, 10, 100]
b = [3, 2, 5, 20]

for i in range(len(a)):
    resultaat = mijn_functie_2(a[i], b[i])
    print(f"{resultaat}")
print()
print("------------------------------------------------------------------------------------------------------------------------------------")
print()