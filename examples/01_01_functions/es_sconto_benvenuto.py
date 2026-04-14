def applica_sconto_benvenuto(prezzo_iniziale,prezzo_maglia):
    return prezzo_iniziale-5
prezzo_maglia= 55
prezzo_pantalone= 65
prezzo_calze= 15
prezzo_scarpe= 105
x= input("cosa vuoi comprare?")
if x=="maglia":
    prezzo_finale= applica_sconto_benvenuto(prezzo_iniziale,prezzo_maglia)