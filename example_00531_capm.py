
#coding=utf-8
#Implementiere einen Rentenrechner
#Anfangskapital: 100
#Zinsen: 6%
#Laufzeit: Jahre
#Formel für die Zinseszinsrechnung: Anfangskapital * ((1+(Zinsatz/100)) ^ jeweiligen Jahre)
#Anfangskapital*math.pow(Zinsen,1)

"""
Ergebnis:
Anfangskapital:  100
Zinssatz:  6.0
Veranlagungszeitraum:  5
Kapital im Jahr 1 : 106.0
Kapital im Jahr 2 : 112.36
Kapital im Jahr 3 : 119.1016
Kapital im Jahr 4 : 126.247696
Kapital im Jahr 5 : 133.82255776
"""


import math

kapital = 100 #100.0 #Startkapital
zinssatz = 6.0 #Zinssatz in Prozent
jahre = 5 #Laufzeit in Jahren
print("Ergebnis :\n")
print("Anfangskapital: "+str(kapital)+" €")
print("Zinssatz: "+str(zinssatz)+" Prozent")
print("Veranlagungszeitraum : "+str(jahre)+" Jahre")

n = 1


while n <= jahre:
    zinsfaktor = (1+(zinssatz/100))
    #print("Kapital im Jahr "+str(n)+" :")
    print("Kapital im Jahr ", n, " : ",   kapital*math.pow(zinsfaktor, n), "€")
    n = n + 1






