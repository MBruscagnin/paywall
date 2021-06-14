import urllib.request as r
page = r.urlopen('https://nuovavenezia.gelocal.it/venezia/cronaca/2021/06/12/news/blitz-della-finanza-in-centro-a-venezia-bancarelle-nel-mirino-scattano-sequestri-di-prodotti-e-maxi-multe-1.40381982')
# @return prima posizione marker di inizio
string = page.read().decode('utf8')
startPos1 = string.find("<!--  -->")

# @return ultima posiione marker di inizio
endPos1 = string.rfind("<!--  -->")

# @return prima posizione marker di fine
startPos2 = string.find("<!--  -->", endPos1)

text_file = open("paywall.html", "w")
text_file.write(string)
text_file.close()


# print("<html><body>"+string[startPos1:startPos2]+"</body></html>")
