"""{
"60-",
"40-59",
"30-39",
"18-29",
"18<"

}"""

import json 

with open ("clienti.json", "r", encoding="utf-8") as f:
    dati = json.load(f)
    clienti=dati["dati"]

def estrazione_fasce_eta(lista_clienti):
    diz= {
        "60-":list(),
        "40-59":list(),
        "30-39":list(),
        "18-29":list(),
        "18<":list()
    }

    for elem in lista_clienti:

        if elem["eta"]>=60:
            diz["60-"].append(elem)

        elif elem["eta"]>=40 and elem["eta"]<60:
            diz["40-59"].append(elem)
        elif elem["eta"]>=30 and elem["eta"]<40:

            diz["30-39"].append(elem)
        elif elem["eta"]>=18 and elem["eta"]<30:

            diz["18-29"].append(elem)
        elif elem["eta"]<18:

            diz["18<"].append(elem)
    return diz
    

print(estrazione_fasce_eta(clienti))       ###funziona
