prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}

aanbieding = (prijzen["vanille"]) * 0.8

reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}")
# print(reclame_tekst)

''' 
Bij de huiswerkopgaven staat dat er een rare tekst zou moeten zijn, echter deze zie ik niet,
Mijn antwoord is € 3.2 als ik deze print wat volgens mij correct is.. ? 4x0.8=3.2.
'''

reclame_tekst3 = reclame_tekst.upper()
# print(reclame_tekst3)

reclame_tekst4 = reclame_tekst3.split()
# print(reclame_tekst4)

for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())
