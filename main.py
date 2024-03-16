import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = int(input())

    # Add input control here!
    def controlloInput(input):
        parola = input.replace(" ", "")
        if parola.isalpha() == False:
            raise ValueError

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        txtIn = input()
        controlloInput(txtIn)
        t.handleAdd(txtIn.lower())
    elif int(txtIn) == 2:
        print("Ok, quale parola devo cercare?")
        txtIn = input()
        controlloInput(txtIn)
        t.handleTranslate(txtIn.lower())
    elif int(txtIn) == 3:
        print("Ok, quale wildcard devo cercare?")
        txtIn = input()
        t.handleWildCard(txtIn.lower())
    elif int(txtIn) == 4:
        t.printAll()
    elif int(txtIn) == 5:
        break


