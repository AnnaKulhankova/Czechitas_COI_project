#oteviram si soubor ze ktereho cerpam nazvy zakonu a ukladam je do promene
soubor_read =  open('Seznam_zakonu_ze_sankci.txt', 'r', encoding = 'utf-8')
zakony = [radek for radek in soubor_read]
soubor_read.close()

#otviram si soubor do ktereho budu nazvy + vytvorene url adresy zapisovat
soubor_write = open('Sankce_URL.txt', 'w', encoding = 'utf-8')

#vyzobavam si z nazvu potrebny rok a cislo zakonu, ktere potrebuju k vytvoreni url adresy
zakony_strip = [zakon.strip() for zakon in zakony]
zakony_split = [zakon.split("/") for zakon in zakony_strip]
zakony_replace = [radek[0].replace("Zák. ", "") for radek in zakony_split]

#vytvarim prvni cast adres v potrebnem slozeni (www+rok- zakona)
html1 = ['https://www.zakonyprolidi.cz/cs/'+adresa[1]+'-' for adresa in zakony_split]

#vytvarim finalni url adresy + radky pro zapis, tzn. nazev zakona + url adresu a zapisuji do noveho souboru
i = 0
for adresa in html1:
  adresa_final = zakony_strip[i]+'\t'+html1[i]+zakony_replace[i]+'\n'
  soubor_write.write(adresa_final)
  i += 1
  
soubor_write.close()