def berechne_MwSt(betrag, mwst):
    if betrag < 0 or mwst < 0:
        return "keine Berechnung möglich - negative Werte"

    return betrag * mwst

def berechne_Brutto(betrag, mwst):
    if betrag < 0 or mwst < 0:
        return "keine Berechnung möglich - negative Werte"

    return betrag * (1 + mwst)

def berechne_Netto(betrag, mwst):
    if betrag < 0 or mwst < 0:
        return "keine Berechnung möglich - negative Werte"

    return betrag / (1 + mwst)




if __name__ == "__main__":

    betrag = float(input("Geben Sie den Betrag ein: "))
    mwst = float(input("Geben Sie den Mehrwertsteuersatz ein: "))
    print(berechne_MwSt(betrag, mwst))
    print(berechne_Netto(betrag, mwst))