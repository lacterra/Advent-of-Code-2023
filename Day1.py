import re

#Datei analysieren
Input = open("Input.txt", "r")
Liste = Input.readlines()
AnzahlZeilen = len(Liste)

Summe = 0


for i in range(AnzahlZeilen):
  ZeileAlsString = Liste[i]
  
  ZeileAlsString = ZeileAlsString.replace("\n", "")
  ZeileAlsString = ZeileAlsString.replace("nineight" , "98")
  ZeileAlsString = ZeileAlsString.replace("eightwo" , "82")
  ZeileAlsString = ZeileAlsString.replace("sevenine" , "69")
  ZeileAlsString = ZeileAlsString.replace("fiveight" , "58")
  ZeileAlsString = ZeileAlsString.replace("threeight" , "38")
  ZeileAlsString = ZeileAlsString.replace("twone" , "21")
  ZeileAlsString = ZeileAlsString.replace("oneight" , "18")
  ZeileAlsString = ZeileAlsString.replace("one" , "1")
  ZeileAlsString = ZeileAlsString.replace("two" , "2")
  ZeileAlsString = ZeileAlsString.replace("three" , "3")
  ZeileAlsString = ZeileAlsString.replace("four" , "4")
  ZeileAlsString = ZeileAlsString.replace("five" , "5")
  ZeileAlsString = ZeileAlsString.replace("six" , "6")
  ZeileAlsString = ZeileAlsString.replace("seven" , "7")
  ZeileAlsString = ZeileAlsString.replace("eight" , "8")
  ZeileAlsString = ZeileAlsString.replace("nine" , "9")
  Bereinigt = re.sub("[a-zA-Z]", "",  ZeileAlsString)
  erstesZiffer = Bereinigt[0]
  letzteZiffer = Bereinigt[len(Bereinigt)-1]
  ZweistelligeZahl = erstesZiffer + letzteZiffer
  
  Summe = Summe + int(ZweistelligeZahl)
  
print(Summe)
