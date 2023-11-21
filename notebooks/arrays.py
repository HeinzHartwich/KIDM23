# In der Softwareentwicklung treffen wir häufig auf eine Datenmenge gleichen Typs,
# wenn wir z. B. eine Preisliste oder einen Warenkorb betrachten oder das 
# Durchschnittsalter einer Gruppe von Menschen berechnen wollen.
# Die Variable alter: wir speichern in alter das Alter von vielen Schüler:innen einer Klasse.
alter = [19, 22, 24, 29, 23, 17, 25, 22, 18, 18, 26, 24, 22, 21, 19, 27, 25, 24, 21]

# Im folgenden Warenkorb sind die Preise von einigen Produkten hinterlegt:
warenkorb = [12.50, 18.63, 4.76, 12.48, 1.74, 8.37]

# Dieser Variablentyp heißt ARRAY - in Python ist der Name "list". Ein Array kann auf unterschiedliche 
# Arten erstellt werden. Ein Array hat eine öffnende Klammer "[" und eine 
# schließende Klammer "]". Zwischen den Klammern werden die einzelnen Elemente erfasst
# und durch Kommas getrennt. Der Zugriff auf ein Array erfolgt wie beim sequentiellen 
# Datentyp String über den Index. 
# Es folgen Ausgaben der einzelnen Elemente des Warenkorbs:
print(warenkorb[0]), print(warenkorb[1]), print(warenkorb[2]),
# Die Ausgabe der einzelnen Elemente wiederholt sich.

# In der Regel ist es günstig und praktisch für die Verarbeitung 
# von ARRAYS Schleifen zu verwenden:
for i in range(len(warenkorb)):
    print("Indexposition ", i, ":", warenkorb[i])
# for i in range(len(warenkorb)): 
# i ist hier eine Laufvariable, die nach jedem Schleifendurchlauf standardmäßig um eins erhöht wird
# range() gibt an, wie oft die Schleife durchlaufen werden soll. Man kann eine Obergrenze als Zahl einfügen
# oder auch berechnen lassen, wie durch len(warenkorb), wodurch die Anzahl der Elemente in warenkorb
# berechnet wird, hier sind das 6 Elemente. Range verwendet die Obergrenze exklusiv, d. h. i läuft in 
# unserem Beispiel von i = 0 bis i = 6 exklusiv, also wird die Schleife 6 mal durchlaufen. 
# range() kann weitere Werte aufnehmen, siehe file loops.py
# Quellen: https://www.w3schools.com/python/python_for_loops.asp
# oder

# oder auch ...
for x in alter:
    print(x)
# for x in alter: 
# Hier gibt es keine explizit sichtbare Laufvariable! Die Elemente werden alle durchlaufen, dann endet die Schleife.
# Schleifen führen den eingerückten Code aus, siehe file loops.py
i = 0
while i < len(warenkorb):
    print("Indexposition ", i, ":", warenkorb[i])
    i += 1

# Operationen auf Arrays
# Quelle: https://www.w3schools.com/python/python_lists.asp

# Unterschiedliche Variablentypen sind möglich
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
# ... auch gemischt
list4 = [1, "banana", 1.76]

print(list1, list2, list3, list4)

# Eine weitere Liste erstellen. Die Listenelemente müssen in runden Klammern übergeben werden
# note the double round-brackets
list5 = list(("Fred", "Selma", "Barney"))
print(list5)

# Listen verketten
list6 = list2 + list3
print(list6)

# Zugriff auf ein Element:
print(list2[4])
# Listenelement überschreiben
list2[4] = 98
print(list2)

# Listenelemente an Index 2 einfügen
list2 = [1, 5, 7, 9, 3]
list2.insert(2, 37)
print(list2)

# Listenelemente am Ende anhängen
list2 = [1, 5, 7, 9, 3]
list2.append(104)
print(list2)
    
# Listen list2 und liste3 verketten
list2 = [1, 5, 7, 9, 3]
list3 = [4, 8, -3, -9, 14]
list2.extend(list3)
print(list2)
    
# Listenelement löschen
list2 = [1, 5, 7, 5, 3, 9, 3]
list2.remove(5)
print(list2)

# Listenelement löschen
list2 = [1, 5, 7, 5, 3, 9, 3]
del list2[0]
print(list2)


# Lambda - muss man (noch) nicht unbedingt verstehen
list2 = [1, 5, 7, 5, 599, 9, 3]
[print(x) for x in list2]

################################################################################
# Nested Lists
################################################################################
# Eine Liste kann Listen aufnehmen -> nested list
# Diese Listn hier haben keinen tieferen Sinn.
# Es soll der Zugriffsmechanismus verdeutlicht werden:
l1 = [1, 2, "B", 4]
l2 = [5, "A", 7, 8]
l3 = [9, -10.3]

l4 = [l1, l2, l3]
# Gibt die nested List aus
print(l4)
# Gibt das Element an der Indexposition 1 aus.
print(l4[1])
# Sucht das Element an Indexposition 2, und nimmt
# davon das Element an der Indexposition 1; das wäre die -10.3
print(l4[2][1])

# verändern des Elements an Indexposition 1.2, hier die 7
# und überschreibt diese mit der 28 
l4[1][2] = 28
print(l4)

# Ausgabe der Elemente
# Wir nehmen jedes Listenelement einzeln
for liste in l4:
    # Wir greifen auf den Inhalt der Liste zu
    for value in liste:
        print(value)





