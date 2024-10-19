projekt_1.py: První projekt do Engeto Online Python Akademie
author: Robert Svorada
email: robert825seznam.cz
discord: strejdabob.
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

vybrany_text = TEXTS
cara = "-" * 40
registered_user = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
import sys
user = input("Zadejte své přihlašovací jméno: ")
password = input("Zadejte svoje heslo: ")
print(f"username: {user}")
print(f"password: {password}")
print(cara)
if user in registered_user and registered_user[user] == password:
    print(f"Welcome to the app: {user}\nWe have {len(TEXTS)} texts to be analyzed.")
    print(cara)
else: 
    print("Unregistered user, terminating the program.")
    sys.exit()
    print(cara)

while True:
    vstup = input("Zadejte číslo (1-3): ")  

    if vstup.strip() == "":
        print("Vstup nemůže být prázdný. Zkuste to znovu.")
        continue

    if vstup.isdigit():
        vyber = int(vstup)
    else:
        print("Neplatný vstup. Zadejte pouze celé číslo.")
        continue  
    if vyber < 1 or vyber > 3:
        print("Neplatný výběr. Vstup musí být v rozsahu 1 - 3.")
    else:
        print(f"Enter a number btw. 1 and {len(TEXTS)} to select: {vyber}")  
        print(cara)
        break



vybrany_text = TEXTS[vyber - 1]
pocet_slov = len(vybrany_text.split()) 
print(f"There are {pocet_slov} words in the text.")
pocet_velkych_pismen = sum(1 for slovo in vybrany_text.split() if slovo.istitle())
print(f"There are {pocet_velkych_pismen} titlecase words.")
pocet_velkych_pismen2 = sum(1 for slovo in vybrany_text.split() if slovo.isupper() and slovo.isalpha())
print(f"There are {pocet_velkych_pismen2} uppercase words.")
pocet_malym_pismem = sum(1 for slovo in vybrany_text.split() if slovo.islower())
print(f"There are {pocet_malym_pismem} lowercase in words")
pocet_cisel = sum(1 for cislo in vybrany_text.split() if cislo.isdigit()) 
print(f"There are {pocet_cisel} numeric string.")
suma= sum(int(cislo) for cislo in vybrany_text.split() if cislo.isdigit())
print(f"The sum of all the the numbers {suma}.")
print(cara)
print("LEN| OCCURENCES |NR.")
print(cara)



slova = vybrany_text.split()
delka_slov = {}

for slovo in slova:
    delka = len(slovo.strip(",."))
    if delka in delka_slov:
        delka_slov[delka] += 1
    else:
        delka_slov[delka] = 1
mdelka = max(delka_slov.keys())
for delka in range(1, mdelka + 1):
    pocet = delka_slov.get(delka, 0)
    print(f"{delka:<2} | {'*' * pocet:<12} | {pocet}")

