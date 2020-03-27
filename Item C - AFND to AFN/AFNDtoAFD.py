import AFND, AFD

class converter():
    
    def __init__(self, afnd):
        self.afnd = afnd
        self.afd = AFD.Automato()

    def conversao(self):
        self.afd.set_alfabeto(self.afnd.alfabeto)
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
                                print(aux)
                                self.afd.estadosFinais.append(aux)
                else:
                    vetor = []
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
                        print("entrou")
                        self.afd.estados.append(j)
                    else:
                        print("contou")
                        cont += 1
                if cont == len(self.afd.estados):
                    controle = True     
            if(controle == False):
                quantidade += 1
            print("Finais")
            print(self.afd.estadosFinais)
            print()


afnd = AFND.Automato()
afnd.set_alfabeto(['0','1'])
afnd.set_estados(['q1','q2','q3'])
afnd.set_estadoInicial('q1')
afnd.set_estadosFinais(['q2','q3'])
afnd.set_transicoes({'q1':{'0':['q3','q2'],'1':['q1']},'q2':{'0':['q3','q2'],'1':['q1']},'q3':{'0':['q2','q3'],'1':['q1']}}) 

convert = converter(afnd)
convert.conversao()
