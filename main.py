import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!
    if txtIn.isdigit():
        if int(txtIn) == 1:
            print("Inserisci la tua frase in Italiano\n")
            frase = input()
            sc.handleSentence(frase,"italian")

        if int(txtIn) == 2:
            print("Inserisci la tua frase in Inglese\n")
            frase = input()
            sc.handleSentence(frase,"english")

        if int(txtIn) == 3:
            print("Inserisci la tua frase in Spagnolo\n")
            frase = input()
            sc.handleSentence(frase,"spanish")

        if int(txtIn) == 4:
            print()
            print("Programma terminato con successo!")
            break
    else:
        print("ERRORE: inserire un numero compreso tra 1 e 4")


