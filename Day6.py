###############################
# Author: Timon Paech
# Datum: 2024-02-09
#
# Titel: Advent of Code - Day 6
# Aufgabe:  Prüfe Passwörter auf Anzahl des Vorkommen von Buchstaben 
#          
# 
#
#
# Lösung: - Datei Zeilenweise einlesen
#         - Prüfpasswort, Minimum, Maximum, Prüfbuchstabe und Buschstabenanzahl ermitteln
#         - Passwort auf Anzahl des Prüf-Buchstaben validieren
#         - Summierung der Buchstabenanzahl valider Passwörter
###############################

def Program():
  Summe = 0

  #Datei einlesen
  Input = open("Day6Input.txt", "r")

  #Ziele in Liste speichern
  Liste = Input.readlines()

  #Länge der Liste ermitteln
  AnzahlZeilen = len(Liste)

  #Umbrüche entfernen
  for i in range(AnzahlZeilen):
    ZeileAlsString = Liste[i]

    #Umbrüchen entfernen
    ZeileAlsString = ZeileAlsString.replace("\n", "")

    #Zerschneiden in mehrere Teile
    Schnitt = ZeileAlsString.split("-")

    #Minimum Buchstabenanzahl ermitteln
    Minimum = int(Schnitt[0])

    Schnitt2 = Schnitt[1].split(" ")

    #Maximum Buchstabenanzahl ermitteln
    Maximum = int(Schnitt2[0])

    #Prüf-Buchstabe ermitteln
    Buchstabe = Schnitt2[1].replace(":", "")

    #Prüfpasswort ermitteln
    Passwort = Schnitt2[2]

    #Prüfe Passwort auf Anzahl Prüf-Buchstabe
    BuchstabenAnzahl = Passwort.count(Buchstabe)

    #wenn Buchstabenanzahl zwischen Minimum und Maximum liegt, dann Buchstabenzahl summieren  
    if BuchstabenAnzahl >= Minimum and BuchstabenAnzahl <= Maximum:
      print("+ Passort: ", Passwort, " min:", Minimum, " max:", Maximum, " Buchstabe:", Buchstabe, " Anzahl:", BuchstabenAnzahl)
      Summe = Summe + 1
    else:
      print("  Passort: ", Passwort, " min:", Minimum, " max:", Maximum, " Buchstabe:", Buchstabe, " Anzahl:", BuchstabenAnzahl)

  print(Summe)
