class estado:
    def __init__(self):
        self.name = None
        self.proxEstado = None

    def get_proxEstado(self):
        return self.proxEstado
    
    def set_proxEstado(self, prox):
        self.proxEstado = prox

class AFND:
    def __init__(self):
        self.alfabeto = []
        self.transicoes = {}
        self.estados = []
        self.estadoInicial = None
        self.estadosFinais = []
        self.primeiro_estado = None
        self.ultimo_estado = None
        self.quantidade_estados = 0
    
    def verificar_repitidos(self, dados):
        vetor = []
        for i in dados:
            if(i not in vetor):
                vetor.append(i)
        return vetor

    def set_alfabeto(self, alfabeto):
        self.alfabeto = self.verificar_repitidos(alfabeto)

    def set_estados(self, estados):
        self.estados = self.verificar_repitidos(estados)
        self.estados.sort()
    
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
        estados_transições = []

        for estado in transicoes:
            check_estados = []; estados_transições.append(estado)
            if(estado not in check_estados and estado in self.estados):
                check_estados.append(estado); check_alfabeto = []
                for entrada in transicoes[estado]:
                    check_alfabeto.append(entrada)
                    if(entrada in self.alfabeto):
                        for i in transicoes[estado][entrada]:
                            if(i not in self.estados):
                                return False
                    else:
                        return False  
                check_alfabeto.sort()
                if(check_alfabeto != self.alfabeto):
                    return False           
            else:
                return False
        
        estados_transições.sort()
        if(estados_transições != self.estados):
            return False
        return True

    def set_transicoes(self, transicoes):
        if(self.verificar_transicoes(transicoes) == True):
            self.transicoes = transicoes
            print(self.transicoes)
        else:
            print("Funções de transições fora do Padrao de um AFD")

    def laco_transicoes(self,simbolo):
        estado = self.primeiro_estado
        aux_inicio = None
        aux_fim = None
        while estado.get_proxEstado != None:
            aux1, aux2 = self.aplicacao_transicoes(simbolo, estado)
            if((aux_inicio and aux_inicio) == None):
                aux_inicio = aux1
                aux_fim = aux2
            else:
                aux_fim.set_proxEstado(aux1)
                aux_fim = aux2
            estado = estado.get_proxEstado()
        else:
            aux_inicio, aux_fim = self.aplicacao_transicoes(simbolo, estado)
        estado.set_proxEstado(aux_inicio)
        self.ultimo_estado = aux_fim

    def aplicacao_transicoes(self, simbolo,estado_atual):    
        aux_inicio = None
        aux_fim = None
        for estado in self.transicoes:
            if(estado == estado_atual.name):
                for entrada in self.transicoes[estado]:
                    if(entrada == simbolo):
                        for i in range(len(self.transicoes[estado][entrada])):
                            if(i == 0):
                                estado_atual.name = self.transicoes[estado][entrada][i]
                            else:
                                novoEstado = estado()
                                if((aux_inicio and aux_fim) == None):
                                    aux_inicio = novoEstado
                                    aux_fim = novoEstado
                                else:
                                    aux_fim.set_proxEstado(novoEstado)
                                    aux_fim = novoEstado
                        return aux_inicio, aux_fim

    def set_string(self, string):
        for simbolo in list(set(string)):
            if(simbolo not in self.alfabeto):
                print("'"+ simbolo +"' nao faz parte do alfabeto")
                return
            
        if(self.quantidade_estados == 0):
            novoEstado = estado()
            novoEstado.name = self.estadoInicial
            self.primeiro_estado = novoEstado
            self.ultimo_estado = novoEstado
            self.quantidade_estados += 1

        for simbolo in string:
            self.laco_transicoes(simbolo)
    
        #if(estado_atual in self.estadosFinais):
        #    print("aceito")
        #else:
        #    print("Recusado")

afd = AFND()
afd.set_alfabeto(['0','1'])
afd.set_estados(['q1','q2','q3'])
afd.set_estadoInicial('q1')
afd.set_estadosFinais(['q2','q2'])
afd.set_transicoes({'q1':{'0':['q3','q1'],'1':['q2']},'q2':{'0':['q1','q3'],'1':['q2']},'q3':{'0':['q2'],'1':[]}}) 
afd.set_string('110')