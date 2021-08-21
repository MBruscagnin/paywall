import os
import urllib.request as r
page = r.urlopen(input("Inserisci URL dell'articolo de LA NUOVA VENEZIA da leggere: "))

#string = input("Inserisci URL dell'articolo da leggere: ")
string = page.read().decode('utf8')

# @return prima posizione marker di inizio
startPos1 = string.find("<!-- ZEPHR_FEATURE ql_nuovavenezia_article -->")

# @return ultima posizione marker di inizio
endPos1 = string.rfind("<!-- ZEPHR_FEATURE ql_nuovavenezia_article -->")

# @return prima posizione marker di fine
startPos2 = string.find("<!-- ZEPHR_FEATURE_END ql_nuovavenezia_article -->", endPos1)

text_file = open("paywall.html", "w")
text_file.write("<html><body>"+string[startPos1:startPos2]+"</body></html>")
text_file.close()

os.system("open paywall.html")
