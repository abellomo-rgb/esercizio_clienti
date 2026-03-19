import json  # ← Era "mport", manca la "i"

with open ("clienti.json", "r", encoding="utf-8") as f:
    dati = json.load(f)

clienti = dati

def sort_casereccio(items, key="priorita"):
    for i in range(len(items)):
        for j in range(len(items)):
            if int(items[j][key]) < int(items[i][key]):
                temp = items[i]
                items[i] = items[j]
                items[j] = temp
    return items

clienti_sorted = sort_casereccio(clienti, key="priorita")

for persona in clienti_sorted:
    print(f"{persona['nome']} {persona['cognome']} - Priorita: {persona['priorita']}")


    ##cliente piu ricco

    ##vendite