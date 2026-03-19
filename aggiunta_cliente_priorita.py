import json

with open ("clienti.json", "r", encoding="utf-8") as f:
    dati = json.load(f)

clienti = dati

# Aggiungere il nuovo cliente PRIMA di ordinare
nuovo_cliente = {
    "nome": "Nuovo",
    "cognome": "Cliente",
    "eta": 19,
    "patrimonio": 100,
    "priorita": 6
}

clienti.append(nuovo_cliente)

def sort_casereccio(items, key="priorita"):
    for i in range(len(items)):
        for j in range(len(items)):
            if int(items[j][key]) < int(items[i][key]):
                temp = items[i]
                items[i] = items[j]
                items[j] = temp
    return items

clienti_sorted = sort_casereccio(clienti, key="priorita")

#for persona in clienti_sorted:
   # print(f"{persona['nome']} {persona['cognome']} - Priorita: {persona['priorita']}")

def cliente_piu_ricco(lista):
    return max(lista, key = lambda x:x["patrimonio"])
    
cliente_piu_ricco(clienti_sorted)
print(cliente_piu_ricco[0])