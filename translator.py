import dictionary
class Translator:

    def __init__(self):
        self.dizionario = dictionary.Dictionary()

    def printMenu(self):
        print("---------------------------")
        print("Transaltor Alien-Italian")
        print("---------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Exit")


    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        infile=open(dict, "r", encoding = "utf-8")
        riga = infile.readline()
        while riga!='':
            campi = riga.split(" ")
            self.dizionario.addWord(campi[0].rstrip(), campi[1].rstrip())
            riga = infile.readline()
        infile.close()


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        campi = entry.split(" ")
        parola = campi[0]
        traduzione = campi[1]
        if parola.lower() not in self.dizionario.listaChiavi():
            self.dizionario.addWord(parola, traduzione)
            print("Aggiunta")
        else:
            print("Parola già presente")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        if query.lower() in self.dizionario.listaChiavi():
            print(f"La traduzione della parola cercata è {self.dizionario.translate(query)}")
        else:
            print("La parola che hai cercato non c'è")


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass