# Program bude obsahovat
# 1) vyžádání si od uživatele přihlašovací jméno a heslo
# 2) zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů
# 3) pokud je registrovaný, pozdraví jej a umožní mu analyzovat texty
# 4) pokud není registrovaný, upozorní jej a ukončí program
# 5) registrovaní uživatelé
# user  password

# bob   123
# ann   pass123
# mike  password123
# liz   pass123

# 6) pokud uživatel vybere takové číslo textu, které není v zadání, 
#    program jej upozorní a skončí
# 7) pokud program zadá jiný vstup než číslo, program jej rovněž upozorní 
#    a skončí
# 8) statistiky - počet slov začínajících velkým písmenem
#               - počet slov psaných velkými písmeny
#               - počet slov psaných malými písmeny 
#               - počet čísel(ne cifer)
#               - sumu všech čísel(ne cifer) v textu

"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Juryca
email: adruj@seznam.cz
"""
import sys

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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
cara = "-" * 75
print(cara)
print("Vítejte v programu textový analyzátor, zadejte přihlašovací jméno a heslo")
print(cara)
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
zadane_jmeno = input("Zadejte jméno: ")
zadane_heslo = input("Zadejte heslo: ")

if zadane_jmeno in users and users[zadane_jmeno] == zadane_heslo:
    print("Vítej v aplikaci", zadane_jmeno.capitalize(), "!")
    print(cara)
    cislo_vstup = input("Který odstavec ze 3 si přejete analyzovat? Zadejte číslo od 1 do 3.\n")
    print(cara)
    if cislo_vstup.isdigit():
        cislo = int(cislo_vstup)
        if 1 <= cislo <= 3:
            vybrany_odstavec = TEXTS[cislo - 1]
            pocet_slov = len(vybrany_odstavec.split())
            print(f"There are {pocet_slov} words in the selected text.")

            pocet_titlecase_slov = 0
            pocet_upercase_slov = 0
            pocet_lowercase_slov = 0

            for slovo in vybrany_odstavec.split():
                if slovo and slovo[0].isupper() and slovo != "US":
                    pocet_titlecase_slov += 1
                if slovo.isupper() and slovo.isalpha():
                    pocet_upercase_slov += 1
                if slovo.islower():
                    pocet_lowercase_slov += 1

            print(f"There are {pocet_titlecase_slov} titlecase words.")
            print(f"There are {pocet_upercase_slov} uppercase words.")
            print(f"There are {pocet_lowercase_slov} lowercase words.")

            pocet_isdigit_cisel = 0
            slova = vybrany_odstavec.split()
            cisla = [int(slovo) for slovo in slova if slovo.isdigit()]
            pocet_isdigit_cisel = len(cisla)
            print(f"There are {pocet_isdigit_cisel} numeric strings.")
            print(f"The sum of all the numbers {sum(cisla)}")
            print(cara)

            cisty_odstavec = vybrany_odstavec.replace(',', '').replace('.', '')

            slova = cisty_odstavec.split()
            delky_slov = [len(slovo) for slovo in slova]

            kategorie = {}
            for delka in delky_slov:
                if delka not in kategorie:
                    kategorie[delka] = 0
                kategorie[delka] += 1

            print("\nLEN| OCCURENCES        |NR.")
            print(cara)
            for delka in sorted(kategorie.keys()):
                hvezdicky = '*' * kategorie[delka]
                print(f"{delka:<3}| {hvezdicky:<17} |{kategorie[delka]}")

        else:
            print("Invalid paragraph number")
            sys.exit()
    else:
        print("Invalid input. Please enter a number")
        sys.exit()
else:
    print("unregistered user, terminating the program..")
    sys.exit()






        
            
        


