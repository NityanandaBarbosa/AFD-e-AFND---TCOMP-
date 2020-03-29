import AFND, AFD

class convert():
    
    def __init__(self, afnd):
        self.afnd = afnd
        self.afd = AFD.Automato()
        self.afd.set_alfabeto(self.afnd.alfabeto)
        self.conversao()

    def conversao(self):
        self.afd.estados.append([self.afnd.estadoInicial])
        self.afd.estadoInicial = self.afnd.estadoInicial
        saida = []

        quantidade = 0
        controle = False
        while(controle == False):
            saidas = []
            for i in self.afnd.alfabeto:
                if(quantidade == 0):
                    self.afnd.transicoes[self.afd.estadoInicial][i].sort()
                    aux = self.afnd.transicoes[self.afd.estadoInicial][i]
                    if aux not in self.afd.estados:
                        self.afd.estados.append(aux)         
                    saida.append(aux)
                    saidas.append(saida)
                    for j in aux:
                        if j in self.afnd.estadosFinais:
                            if(aux not in self.afd.estadosFinais):
                                #print(aux)
                                self.afd.estadosFinais.append(aux)
                else:
                    vetor = []
                    #print(self.afd.estados, quantidade)
                    for estado in self.afd.estados[quantidade]:
                        for j in self.afnd.transicoes[estado][i]:
                            if j not in vetor:
                                vetor.append(j)
                    vetor.sort()
                    for j in vetor:
                        if j in self.afnd.estadosFinais:
                            if(vetor not in self.afd.estadosFinais):
                                self.afd.estadosFinais.append(vetor)
                    saida.append(vetor)   
                    saidas.append(vetor)
            
            cont = 0
            if(quantidade > 0):
                for j in saidas:
                    if j not in self.afd.estados:
                        #print("entrou")
                        self.afd.estados.append(j)
                    else:
                        #print("contou")
                        cont += 1
                if cont == len(saidas):
                    if(len(saida)/len(self.afd.estados) == len(self.afd.alfabeto)):
                        controle = True     
            if(controle == False):
                quantidade += 1
        
        self.afd.estadoInicial = '0'

        for i in range(len(self.afd.estados)):
            for j in range(len(saida)):
               if saida[j] == self.afd.estados[i]:
                    saida[j] = str(i)
            for j in range(len(self.afd.estadosFinais)):
                if self.afd.estadosFinais[j] == self.afd.estados[i]:
                    self.afd.estadosFinais[j] = str(i)
            self.afd.estados[i] = str(i)

        dic = {}
        count = 0

        for i in self.afd.estados:
            dic[i] = {}
            for j in self.afd.alfabeto:
                dic[i][j] = saida[count]
                count += 1
        self.afd.set_transicoes(dic)

        print(self.afd.estados)
        print(saida)
        print(self.afd.transicoes)
        

    def set_string_all(self, string):
        print("Resultado AFD : ")
        self.afd.set_string(string)
        print("Resultado AFND : ")
        self.afnd.set_string(string)

afnd = AFND.Automato()
afnd.set_alfabeto(['0','1'])
afnd.set_estados(['a','b','c','d','e','f'])
afnd.set_estadoInicial('a')
afnd.set_estadosFinais(['d'])
afnd.set_transicoes({'a': {'0': ['e'], '1': ['b'],'epsilon':[]},
                    'b': {'0': [], '1': ['c'],'epsilon':['d']},
                    'c': {'0': [],'1':['d'],'epsilon':[]},
                    'd': {'0': [], '1': [],'epsilon':[]},
                    'e': {'0': ['f'], '1': [],'epsilon':[]},
                    'f': {'0': ['d'], '1': [],'epsilon':[]}})

convert = convert(afnd)
convert.set_string_all("1")

