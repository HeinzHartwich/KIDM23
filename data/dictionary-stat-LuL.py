# Verwenden Sie diese Liste, um den Überblick behalten zu können ...
products = [["ProductID", "ProductName", "SupplierID", "CategoryID", "Unit", "Price"],
            [1, "Chais", 1, 1, "10 boxes x 20 bags", 18],
            [2, "Chang", 1, 1, "24 - 12 oz bottles", 19],
            [3, "Aniseed Syrup", 1, 2, "12 - 550 ml bottles", 10],
            [4, "Chef Anton's Cajun Seasoning", 2, 2, "48 - 6 oz jars", 22],
            [5, "Chef Anton's Gumbo Mix", 2, 2, "36 boxes", 21.35]]

# Importieren Sie diese Liste, um mit ALLEN Datensätzen arbeiten zu können ...
# Dazu löschen Sie in der folgenden Zeile das Zeichen "#" vor dem Schlüsselwort from
# from products_list import products

# Dictionary initialisieren
statistic = {"count": 0, "sum": 0}

# 1: Anzahl Sets
statistic["count"] = len(products[1:])

# 2: Summe bilden
for set in products[1:]:
    statistic["sum"] += set[5]

# Dictionary: average als Key hinzufügen
# 3: average berechnen
statistic["average"] = statistic["sum"] / statistic["count"]

# Ausgabe Dictionary
# print(statistic) -- siehe weiter unten in __main__

# BEGIN --- Aufgabe 1:
# BEGIN --- Hilfsmittel
from operator import itemgetter
# Liste nach Attribut-Index sortieren lassen
def sortListByIndex(products, index):
     # nach Attribut index sortierte Liste zurückgeben
     # Code-Demo siehe unten
     return sorted(products, key=itemgetter(index))
# END --- Hilfsmittel



# Aufgabe 1.1
# Wandeln Sie den Code für Anzahl Datensätze und Summe über das Index-Feld in Funktionen um.
# Code siehe oben, unter # 2 und # 3.

# Aufgabe 1.2
# Erweitern Sie das Dictionary um dden key average.
# Implementieren Sie die Funktionen dazu.

def calcAverage():
    average = 0
    return average

# Aufgabe 1.3
# Erweitern Sie das Dictionary um die Keys min und max.
# Implementieren Sie die Funktionen dazu.
# Hinweis: in wie weit können die Aufgaben 1.4 und 1.5 Ihnen dabei helfen
# die Aufgabe 1.3 zu lösen?

def calcMin(products, index):
    # min = 0
    return numFlops(products, index, 1)[0]

def calcMax(products, index):
    # max = 0
    return numTops(products, index, 1)[0]

# Aufgabe 1.4
# Erweitern Sie das Dictionary um den Key Tops.
# Sortieren Sie zunächst die Liste mit der Hilfsfunktion.
# numTops(products, 5, 3): liefert die 3 teuersten Artikel, absteigend sortiert
def numTops(products, index, count):
    tops = []
    if count <= len(products):
        tops = sortListByIndex(products[1:], 5)
        tops.reverse()
        return tops[0:count]
    else:
        return None

# Aufgabe 1.5
# Erweitern Sie das Dictionary um den Key Flops.
# Sortieren Sie zunächst die Liste mit der Hilfsfunktion.
# numFlops(products, 5, 3): liefert die 3 billigsten Artikel, aufsteigend sortiert
def numFlops(products, index, count):
    flops = []
    if count <= len(products):
        flops = sortListByIndex(products[1:], 5)
        return flops[0:count]
    else:
        return None

# END --- Aufgabe:

if __name__ == "__main__":
    #print(statistic)
    # BEGIN : Hier folgt ein DemoCode für sortListByIndex ------
    # Die Funktion sortListByIndex() soll nicht mehr direkt aufgerufen werden, sondern wird
    # von numTops() und numFlops() gekappselt werden.
    # Wenn Sie die numTops und numFlops implementiert haben löschen Sie die nächsten Zeilen
    """ products_sorted = sortListByIndex(products[1:], 5)
    print(products_sorted)
    products_sorted.reverse()
    print(products_sorted)
    # END : DemoCode für sortListByIndex ------

    """

    statistic["tops"] = numTops(products[1:], 5, 3)
    statistic["flops"] = numFlops(products[1:], 5, 3)

    statistic["min"]= calcMin(products, 5)
    statistic["max"] = calcMax(products, 5)

    # Ausgabe der Statistik
    #print(statistic)
    for key, value in statistic.items():
        print(key, ": ", value)


