import AFND, AFD

class convert():
    
    def __init__(self, afnd):
        self.afnd = afnd
        self.afd = AFD.Automato()
        self.afd.set_alfabeto(self.afnd.alfabeto)
        self.conversao()

    def conversao(self):
        if(self.afnd.estadoInicial == None):
            return
        self.afd.estados.append(self.transicaoEpsilon([self.afnd.estadoInicial]))
        self.afd.estadoInicial = self.transicaoEpsilon([self.afnd.estadoInicial])
        saida = []
        quantidade = 0
        controle = False
        while(controle == False):
            saidas = []
            for i in self.afnd.alfabeto:
                if(i != "epsilon"):
                    #if(quantidade == 0):
                    #    self.afnd.transicoes[self.afd.estadoInicial][i].sort()
                    #    aux = self.afnd.transicoes[self.afd.estadoInicial][i]
                    #    aux = self.transicaoEpsilon(aux)
                    #    if aux not in self.afd.estados:
                    #        self.afd.estados.append(aux)         
                    #    saida.append(aux)
                    #    saidas.append(saida)
                    #    #print(saidas)
                    #    for j in aux:
                    #        if j in self.afnd.estadosFinais:
                    #            if(aux not in self.afd.estadosFinais):
                    #                self.afd.estadosFinais.append(aux)
                    #else:
                    #print(quantidade)
                    #print(self.afd.estados)
                    vetor = []
                    for estado in self.afd.estados[quantidade]:
                        for j in self.afnd.transicoes[estado][i]:
                            if j not in vetor:
                                vetor.append(j)
                    vetor.sort()
                    vetor = self.transicaoEpsilon(vetor)
                    for j in vetor:
                        if j in self.afnd.estadosFinais:
                            if(vetor not in self.afd.estadosFinais):
                                self.afd.estadosFinais.append(vetor)
                    saida.append(vetor)   
                    saidas.append(vetor)

            cont = 0
            if(quantidade >= 0):
                for j in saidas:
                    if j not in self.afd.estados:
                        self.afd.estados.append(j)
                    else:
                        cont += 1
                if cont == len(saidas):
                    if(len(saida)/len(self.afd.estados) == len(self.afd.alfabeto) - 1):
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
            if(i != "epsilon"):
                dic[i] = {}
                for j in self.afd.alfabeto:
                    if(j != "epsilon"):
                        dic[i][j] = saida[count]
                        count += 1
        
        self.afd.set_transicoes(dic)

        #print(self.afd.estados)
        #print(saida)
        #print(self.afd.transicoes)

    def set_string_all(self, string):
        print("Resultado AFD : ")
        self.afd.set_string(string)
        print("Resultado AFND : ")
        self.afnd.set_string(string)

    def transicaoEpsilon(self, aux):
        controle = False
        vetor = []
        for i in aux:
            vetor.append(i)
        for estado in aux:
            for posicao in range(len(self.afnd.transicoes[estado]["epsilon"])):
                novoValor = self.afnd.transicoes[estado]["epsilon"][posicao]
                if(novoValor not in vetor):
                    vetor.append(novoValor)
                if(posicao == len(self.afnd.transicoes[estado]["epsilon"])):
                    controle = True
                while(self.afnd.transicoes[novoValor]["epsilon"] != []):
                    guarda_estado = novoValor
                    for j in range(len(self.afnd.transicoes[novoValor]["epsilon"])):
                        if(j>0):
                            newValor = self.afnd.transicoes[guarda_estado]["epsilon"][j]
                            if(newValor not in vetor):
                                vetor.append(newValor)
                        else:
                            novoValor = self.afnd.transicoes[novoValor]["epsilon"][j]
                            if(novoValor not in vetor):
                                vetor.append(novoValor)
                else:
                    if(controle == False):
                        if(novoValor not in vetor):
                                vetor.append(novoValor)
        return vetor