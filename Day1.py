###############################
# Author: Timon Paech
# Datum: 2024-01-05
#
# Titel: Advent of Code - Day 1
# Aufgabe: Zweistellige Zahlen aus Input Text pro Zeile ermittel und summieren
# 
# Lösung: - Daten zeilenweise einlesen
#          - Daten in Liste speichern
#          - Unnötige Zeichen per Regex entfernen
#          - Zahlen pro Zeile ermitteln und summieren
###############################

import re

def Program():

  #Datei einlesen
  Input = open("Day1Input.txt", "r")
  
  #Ziele in Liste speichern
  Liste = Input.readlines()

  #Länge der Liste ermitteln
  AnzahlZeilen = len(Liste)
  
  Summe = 0

  #alle Zeilen durchgehen
  for i in range(AnzahlZeilen):
    ZeileAlsString = Liste[i]

    #Umbrüchen entfernen
    ZeileAlsString = ZeileAlsString.replace("\n", "")

    #zweistellige Zahlenwerte (als String) mit doppelt verwendeten Buchstaben in Zahlen umwandel
    ZeileAlsString = ZeileAlsString.replace("nineight" , "98")
    ZeileAlsString = ZeileAlsString.replace("eightwo" , "82")
    ZeileAlsString = ZeileAlsString.replace("sevenine" , "69")
    ZeileAlsString = ZeileAlsString.replace("fiveight" , "58")
    ZeileAlsString = ZeileAlsString.replace("threeight" , "38")
    ZeileAlsString = ZeileAlsString.replace("twone" , "21")
    ZeileAlsString = ZeileAlsString.replace("oneight" , "18")

    #einstellige Zahlenwerte in Zahlen umwandeln
    ZeileAlsString = ZeileAlsString.replace("one" , "1")
    ZeileAlsString = ZeileAlsString.replace("two" , "2")
    ZeileAlsString = ZeileAlsString.replace("three" , "3")
    ZeileAlsString = ZeileAlsString.replace("four" , "4")
    ZeileAlsString = ZeileAlsString.replace("five" , "5")
    ZeileAlsString = ZeileAlsString.replace("six" , "6")
    ZeileAlsString = ZeileAlsString.replace("seven" , "7")
    ZeileAlsString = ZeileAlsString.replace("eight" , "8")
    ZeileAlsString = ZeileAlsString.replace("nine" , "9")

    #sonstige Buchstaben aus String entfernen
    Bereinigt = re.sub("[a-zA-Z]", "",  ZeileAlsString)

    #erste Ziffer im String ermitteln
    erstesZiffer = Bereinigt[0]

    #letzte Ziffer im String ermitteln
    letzteZiffer = Bereinigt[len(Bereinigt)-1]

    #zweistellige Zahl aus erster und letzter Ziffer ermitteln
    ZweistelligeZahl = erstesZiffer + letzteZiffer

    #Summe aller zweistelligen Zahlen ermitteln
    Summe = Summe + int(ZweistelligeZahl)
  
  print(Summe)



