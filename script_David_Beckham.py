import requests
from bs4 import BeautifulSoup

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>David Backham</title>
<head>
<body>
    {}
</body>
</html>
'''

response = requests.get("https://en.wikipedia.org/wiki/David_Beckham")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    spans = soup.find_all("table", class_="infobox biography vcard")
    test = spans[0]
    with open("index.html", "w", encoding="utf=8") as f:
        f.write(HTML_TEMPLATE.format(test))
else:
    print("failed")
