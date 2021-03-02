import urllib.request
import json
import datetime

x = datetime.datetime.now()
year = (x.strftime("%Y"))
month = (x.strftime("%m"))
day = (x.strftime("%d"))


# αυτη επιστρεφει ποιο ήταν το πρώτο draw id της ημερας, δηλαδη την πρώτη κλήρωση
def first_draw():
    url = "https://api.opap.gr/draws/v3.0/1100/draw-date/{}-{}-1/{}-{}-{}".format(year, month, year, month, day)
    r = urllib.request.urlopen(url)
    html = r.read()
    html = html.decode()  # μετατρεπει τα bites σε string
    data = json.loads(html, strict=False)  # παρε html και μετετρεψετην σε ενα λεξικο, αρα το data ειναι λεξικο
    return data[0]  # το data[0] είναι τα η λιστα με τα αποτελεσματα της πρώτης κλήρωσης


draw = first_draw()
url = "https://api.opap.gr/draws/v3.0/1100/{}".format(draw)  # αυτο θα επιστρεψει τα winning numbers της συγκεκριμενης κληρωσης
r = urllib.request.urlopen(url)
html = r.read()
html = html.decode()  # μετατρεπει τα bites σε string
data = json.loads(html, strict=False)  # παρε html και μετετρεψετην σε ενα λεξικο, αρα το data ειναι λεξικο
numbers = []
for draw in data["content"]:
    numbers.append(draw["winningNumbers"]["list"])


total_numbers = day*20  # έχουμε 20 winning numbers την κάθε μέρα
count = []
for i in total_numbers:
    if i == numbers[i]:
        count[i] = count[i] + 1

for i in total_numbers:
    percentage = count[i]/total_numbers
    print(percentage)