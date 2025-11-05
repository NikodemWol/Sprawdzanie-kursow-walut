import requests
from bs4 import BeautifulSoup
#ściągam link do strony i robie z niego html w zmiennej soup
url = 'https://www.money.pl/pieniadze/nbp/srednie/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


#ściągam wszystkie nazwy walut ze strony i kłade je do listy
waluty=soup.find_all("a", {"class": "sc-18yizqs-0 sUail"})
posortowane_waluty=[waluta.text.strip() for waluta in waluty]
posortowane_waluty=list(dict.fromkeys(posortowane_waluty))



#ściągam przeliczniki walut
spany = soup.find_all("div", {"class": "rt-td"})
posortowane_spany=[span.text.strip() for span in spany]




#tworze tabele sprzedaż i kupno, a później nadaje im elementy
kurs=[]
for i in range(len(posortowane_spany)):
    for j in range(len(posortowane_waluty)):
        if posortowane_spany[i] == posortowane_waluty[j]:
            kurs.append(posortowane_spany[i+2])
            break
maksymalna=0
for i in range(len(posortowane_waluty)):
    if len(posortowane_waluty[i])>maksymalna:
        maksymalna=len(posortowane_waluty[i])
#printuje tabele
print("                    "+"kurs")
for i in range(len(posortowane_waluty)):
    print(posortowane_waluty[i]+ (" " * (maksymalna-len(posortowane_waluty[i])+1)) + kurs[i])

while True:
    try:
        jaka=input("Jeśli szukasz konkretnej waluty to możesz wpisać jej nazwe: ").lower()
        print("           " + "kurs")
        print(jaka+(" " * (maksymalna-len(posortowane_waluty[i])+1))+kurs[posortowane_waluty.index(jaka)])
    except:
        print("Nie znam takiej waluty (sprawdz, czy nie zrobiłeś literówki)")