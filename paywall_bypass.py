import os
import urllib.request as r
page = r.urlopen(input("Inserisci URL dell'articolo de LA NUOVA VENEZIA da leggere: "))

# @return prima posizione marker di inizio
string = page.read().decode('utf8')
#string = input("Inserisci URL dell'articolo da leggere: ")
startPos1 = string.find("<!--  -->")

# @return ultima posizione marker di inizio
endPos1 = string.rfind("<!--  -->")

# @return prima posizione marker di fine
startPos2 = string.find("<!--  -->", endPos1)

text_file = open("paywall.html", "w")
text_file.write("<html><body>"+string[startPos1:startPos2]+"</body></html>")
text_file.close()

os.system("open paywall.html")
