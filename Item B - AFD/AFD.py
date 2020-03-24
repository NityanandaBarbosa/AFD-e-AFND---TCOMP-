class AFD:
    def __init__(self):
        self.alfabeto = []
        self.transicoes = {}
        self.estados = []
        self.estadoInicial = None
        self.estadosFinais = []
    
    def verificar_repitidos(self, dados):
        vetor = []
        for i in dados:
            if(i not in vetor):
                vetor.append(i)
            else:
                pass
                #print("Repitido, será ignorado")
        return vetor

    def set_alfabeto(self, alfabeto):
        self.alfabeto = self.verificar_repitidos(alfabeto)

    def set_estados(self, estados):
        self.estados = self.verificar_repitidos(estados)
    
    def set_estadoInicial(self, estado):
        if estado in self.estados:
            self.estadoInicial = estado
    
    def set_estadosFinais(self, estados):
        estados = self.verificar_repitidos(estados)
        for i in estados:
            if i in self.estados:
                self.estadosFinais.append(i)
        #print(self.estadosFinais)
    
    def verificar_transicoes(self, transicoes):
        control = False
        for i in transicoes:
            test = []
            if((i not in test and i in self.estados) and control == False):
                test.append(i)
                for j in transicoes[i]:
                    if(j in self.alfabeto):
                        if(transicoes[i][j] not in self.estados):
                            control = True
                            return False
                    else:
                        control = True
                        return False
            else:
                return False
        return True

    def set_transicoes(self, transicoes):
        if(self.verificar_transicoes(transicoes) == True):
            self.transicoes = transicoes

afd = AFD()
afd.set_alfabeto(['0','1'])
afd.set_estados(['q1','q2',])
afd.set_estadosFinais(['q2'])
afd.set_transicoes({'q1':{'5':'q0','0':'q1'},'q2':{'0':'q1','1':'q2'}})