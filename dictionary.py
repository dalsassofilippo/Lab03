class Dictionary:
    def __init__(self,nome):
        self.nome = nome
        self._dict = []

    def loadDictionary(self,path):
        try:
            with open(path,"r",encoding="utf-8") as file:
                righe=file.readlines()
                for r in righe:
                    self._dict.append(r.strip())

                file.close()
        except FileNotFoundError:
            print("Nome file ERRATO")
        except Exception as e:
            print("ERRORE durante la lettura del file")

    def printAll(self):
        for r in self._dict:
            print(r)

    @property
    def dict(self):
        return self._dict