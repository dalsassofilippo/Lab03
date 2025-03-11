import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self,language,frase=None):
        self.dizionario=d.Dictionary(language)
        self.frase=frase if frase is not None else []
        self.dizionario.loadDictionary(language)
        self.listaRWL = []
        self.listaRWC =[]
        self.listaRWD = []

    def printDic(self, language):
        self.dizionario.printAll()

    def searchWord(self):
        for p in self.frase:
            if not self.dizionario.dict.__contains__(p.lower()):
                self.listaRWC.append(rw.RichWord(p, False))

        return self.listaRWC

    def searchWordLinear(self):
        for p in self.frase:
            flag=False
            for t in self.dizionario.dict:
                if p.lower()==t.lower():
                    flag=True
                    rw.RichWord(p,True)
            if flag==False:
                self.listaRWL.append(rw.RichWord(p,False))

        return self.listaRWL

    def searchWordDichotomic(self):
        d=self.dizionario.dict.copy()
        inizio=len(d)/2
        for p in self.frase:
            while len(d)==1:
                if p!=d[inizio]:
                    if p<d[inizio]:
                        for t in range(inizio,len(d)):
                            d.pop(t)
                    else:
                        for t in range(0,inizio):
                            d.pop(t)
                    inizio/=2
            if not d.__contains__(p):
                self.listaRWD.append(rw.RichWord(p,False))
            else:
                rw.RichWord(p, True)

        return self.listaRWD