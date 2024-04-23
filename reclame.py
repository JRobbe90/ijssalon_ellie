from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    korting = prijs * (1 - korting)
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:.2f} voor {korting:.2f} euro.")

aanbieding_1(f"aardbei", 4, 0.1)

inkomsten = [220, 430, 125, 160, 205, 90, 345]

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten) * (1 - btw)
    return totaal

totaal_inkomsten = inkomsten_totaal(inkomsten, 0)
btw = inkomsten_totaal(inkomsten, 0.91)
print(f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {btw:.2f} euro btw betaald dient te worden.")


def laag_en_hoog(mijn_lijst):
    laag = min(inkomsten)
    hoog = max(inkomsten)
    return laag, hoog

resultaat = laag_en_hoog(inkomsten)
print(list(resultaat))

def gemiddelde(mijn_lijst):
    totaal = sum(inkomsten)
    weekgemiddelde = totaal / (len(inkomsten))
    return weekgemiddelde

weekgemiddelde = gemiddelde(inkomsten)
print(f"De gemiddelde inkomsten deze week zijn {weekgemiddelde:.2f} euro.")

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]

def meervoudig(invoer_lijst):
    laag, hoog = laag_en_hoog(invoer_lijst)
    return [laag, hoog]

resultaten = meervoudig(invoer_lijst)
print(resultaten)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer