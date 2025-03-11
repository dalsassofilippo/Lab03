import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.language="" # GLI PASSI IL RIFERIMENTO ALLA CARTELLA DOVE SONO CONTENUTI I FILE

    def handleSentence(self, txtIn, language):

        lingua=f"{language[0].upper()}{language[1:len(language)]}"
        self.language=f"./resources/{lingua}.txt"
        parole=replaceChars(txtIn).strip().split(" ")
        multi=md.MultiDictionary(self.language,parole)

        print("______________________________\n")
        print("Using contains")
        t1=time.time()
        listaSbagliate1=multi.searchWord()
        if len(listaSbagliate1) == 0:
            if language == "italian":
                print("Nessuna parola sbagliata!")
            elif language == "english":
                print("All words are correct!")
            else:
                print("Todo correcto!")
        else:
            for x in listaSbagliate1:
                print(x.__str__())
        t2=time.time()
        print(t2-t1)
        print("______________________________\n")
        print("Using Linear search")
        print()
        t3=time.time()
        listaSbagliate=multi.searchWordLinear()
        if len(listaSbagliate) == 0:
            if language == "italian":
                print("Nessuna parola sbagliata!")
            elif language == "english":
                print("All words are correct!")
            else:
                print("Todo correcto!")
        else:
            for r in listaSbagliate:
                print(r.__str__())
        t4=time.time()
        print(t4-t3)
        print("______________________________\n")
        print("Using Dichotomic search")
        print()
        t5=time.time()
        listaSbagliate2=multi.searchWordDichotomic()
        if len(listaSbagliate2) == 0:
            if language == "italian":
                print("Nessuna parola sbagliata!")
            elif language == "english":
                print("All words are correct!")
            else:
                print("Todo correcto!")
        else:
            for r in listaSbagliate:
                print(r.__str__())
        t6=time.time()
        print(t6-t5)


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~?'"
    for c in chars:
        text = text.replace(c, "")
    return text