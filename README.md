# Paywall
## Circumventing the paywall on some Italian online newspaper sites

Simple script written in Python3 for circumventing the weak paywall on some Italian online newspaper sites.

### Operations
After lauching the script the CLI ask to insert the URL of the article behind paywall.

```bash
$ paywall_bypass.ph
$ Inserisci URL dell'articolo da leggere: [URL of the blocked article]
```

decode the page to UTF-8 and insert it into a string.

```python
page = r.urlopen(input("Inserisci URL dell'articolo da leggere: "))
string = page.read().decode('utf8')
```

The script estract the text of the article and generate a new HTML file with the text.

```python
text_file = open("paywall.html", "w")
text_file.write("<html><body>"+string[startPos1:startPos2]+"</body></html>")
text_file.close()
```

At the end this new file is opened with a sys call.

```python
os.system("open paywall.html")
```

### Disclaimer
~~Although this script works~~ (now deprecated) bypassing paywalls is illegal, **this script is for academic purpose only**.
