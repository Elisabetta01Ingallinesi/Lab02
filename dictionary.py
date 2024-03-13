class Dictionary:
    def __init__(self):
        self.dizionario = {}


    def addWord(self, parola, traduzione):
        self.dizionario[parola.lower()] = traduzione.lower()

    def translate(self, parola):
        return self.dizionario[parola.lower()]

    def translateWordWildCard(self):
        pass

    def listaChiavi(self):
        return self.dizionario.keys()
