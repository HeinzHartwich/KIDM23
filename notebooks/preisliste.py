warenkorb = [12.50, 18.63, 4.76, 12.48, 1.74, 8.37]
#alter = [19, 22, 24, 29, 23, 17, 25, 22, 18, 18, 26, 24, 22, 21, 19, 27, 25, 24, 21]
alter = [40, 20]

def calcMean(liste):
    # summe initialisieren
    summe = 0
    # Länge der Liste berechnen. Wieviele Elemente gibt es?
    size = len(liste)
    # durch die Liste iterieren
    for element in liste:
        summe = summe + element       
    mean = summe / size
    return mean
   
if __name__ == "__main__":

    print( calcMean(warenkorb) )
    print( calcMean(alter) )

