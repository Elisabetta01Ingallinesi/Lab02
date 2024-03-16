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
        print("4. Stampa tutto il dizionario")
        print("5. Exit")


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

        if parola.lower() not in self.dizionario.listaChiavi():
            traduzioni = ""
            for i in range(1,len(campi)):
                traduzioni += " " + campi[i]
            self.dizionario.addWord(parola, traduzioni)
            print("Aggiunta/e")
        else:
            campi.pop(0)
            risultato = self.dizionario.translate(parola)
            ris = risultato.split(" ")
            daScrivere = []
            for k in ris:
                daScrivere.append(k)
            for k in ris:
                for t in campi:
                    if k == t:
                        print("Traduzione già presente")
                        return
            for t in campi:
                daScrivere.append(t)
            traduzioni = ""
            for i in range(1, len(daScrivere)):
                traduzioni += " " + daScrivere[i]
            self.dizionario.addWord(parola, traduzioni)
            print("Aggiunta/e")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        if query.lower() in self.dizionario.listaChiavi():
            print(f"La traduzione della parola cercata è{self.dizionario.translate(query)}")
        else:
            print("La parola che hai cercato non c'è")


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        traduzioni = self.dizionario.translateWordWildCard(query)
        if traduzioni == None:
            print("WildCard non trovata")
        else:
            for element in traduzioni:
                print(element)

    def printAll(self):
        self.dizionario.printAll()