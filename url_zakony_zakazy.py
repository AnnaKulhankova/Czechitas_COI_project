#oteviram si soubor ze ktereho cerpam nazvy zakonu a ukladam je do promene
import csv
with open('Seznam_zakonu_ze_zakazu.csv', 'r', encoding = 'utf-8') as zakony_sankce:
    reader = csv.reader(zakony_sankce, delimiter=',')
    zakony = list(reader)

#otviram si soubor do ktereho budu nazvy + vytvorene url adresy zapisovat
soubor_write = open('Zakazy_URL.txt', 'w', encoding = 'utf-8')

#vyzobavam rok a cislo zakona
zakony_split = [zakon[0].split("/") for zakon in zakony]

#vyzobavam nazev zakonu do finalniho souboru
nazvy_zakonu = [zakon[0] for zakon in zakony]

#vytvarim adresy v potrebnem slozeni (www+rok-cislo zakona)
html1 = ['https://www.zakonyprolidi.cz/cs/'+adresa[1]+'-' for adresa in zakony_split]

#vytvarim finalni url adresy + radky pro zapis, tzn. nazev zakona + url adresu a zapisuji do noveho souboru
i = 0
for adresa in html1:
  adresa_final = nazvy_zakonu[i]+'\t'+html1[i]+zakony_split[i][0]+'\n'
  soubor_write.write(adresa_final)
  i +=1