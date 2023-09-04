import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

r=requests.get("https://easy-polish.com/pl/tornadot/texget.html?exerciseid=vzxgdnmrjq")
s= BeautifulSoup(r.text, features="html.parser")
with open('downloaded.html', 'w', encoding="utf-8") as file:
    file.write(s.prettify())
a= s.select(".overword") #tak jest w html'u oznaczona klasa słów ktore chce pobrac
zbiór=[]
for b in a:
    zbiór.append(b.text)
#zbiór= list(zbiór)
czy=('tak')
while (czy=='tak'):
    życia=12
    x=('')
    litera=("")
    lista=[]
    słowo= random.choice(zbiór)
    słowo = (słowo.lower())
    słowo = (słowo.strip())
    while ((słowo.isalpha() == False) or (len(słowo)<3)):
        słowo = random.choice(zbiór)
    for d in range (0, len(słowo)):
        sys.stdout.write("_ ")
        x+=('_')
    print("  <-długość słowa: ", len(słowo))
    print("ilość żyć: ", życia)
    while litera != słowo:
        if życia == 0:
            print("trup!\n słowo o które chodziło to: ", słowo)
            break
        b = ("")
        litera = input("Wpisz literę lub docelowe hasło: ")
        litera=(litera.lower())
        if (len(litera)!= 1)  and (len(litera) != len(słowo)) or (litera.isalpha() ==False) or (litera in lista):
            print ('coś poszło nie tak!')
            continue
        elif (litera in słowo):
                for a in range (0, len(słowo)):
                    if słowo[a] == litera:
                      x=x[0:a] + litera + x[a+1:]
                      lista += litera
                      print("Wykorzystane litery: ", lista)
                    else:
                        continue
                print(x)
        else:
            życia-=1
            lista += litera
            print("nie ma \n pozostałe życia:", życia, "\n Wykorzystane litery: ", lista)
    else:
        print("gratulacje! udało Ci sie nie zdechnąć człowieka")
    czy= input('czy chcesz zagrać jeszcze raz? (tak/nie)\n')