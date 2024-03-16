import re
class Dictionary:
    def __init__(self):
        self.dizionario = {}


    def addWord(self, parola, traduzione):
        self.dizionario[parola.lower()] = traduzione.lower()

    def translate(self, parola):
        return self.dizionario[parola.lower()]

    def translateWordWildCard(self, wildCard):
        wildCard = wildCard.replace("?", ".")
        conta = 0
        sb = []

        for w in self.listaChiavi():
            if re.search(wildCard,w):
                conta+=1
                sb.append(self.dizionario.get(w))
        if conta == 0:
            return None
        else:  return sb

    def listaChiavi(self):
        return self.dizionario.keys()

    def printAll(self):
        for key, value in self.dizionario.items(): #per scorrere sia le chiavi, sia i valori di un dizionario
            parolaAliena = key
            traduzione = value
            print(f"Parola Aliena:{parolaAliena}, Traduzione:{traduzione}\n")
