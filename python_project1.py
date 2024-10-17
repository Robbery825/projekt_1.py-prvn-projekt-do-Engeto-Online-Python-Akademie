projekt_1.py: První projekt do Engeto Online Python Akademie
author: Robert Svorada
email: robert825
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
registred_user = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
import sys
import getpass
user = input("Zadejte své přihlašovací jméno: ")
password = getpass.getpass("Zadejte svoje heslo: ")
if user in registred_user:
    print(f"Welcome to the app: {user}\nWe have 3 text to be analyzed")
    print(cara)
else: 
    print("Unregistered user, termining the program")
    sys.exit()
vyber = int(input("Zadejte číslo  (1-3): "))
if vyber <1 or vyber > len(TEXTS):
    print("Neplatný výběr. Program končí")
    print(cara)
else:
    print(f"Enter number btw. 1 and 3 to select: {vyber - 0 }")
    print(cara)
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
delka_slov = sorted([len(slovo) for slovo in vybrany_text.split()])
print("Délka slov: ")
for index, delka in enumerate(delka_slov, start=1,):
    print(f"{index}| {"*" * delka} | {delka}")
