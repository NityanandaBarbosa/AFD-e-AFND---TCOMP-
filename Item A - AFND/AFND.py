class estado:
    def __init__(self):
        self.name = None
        self.proxEstado = None
        self.anteriorEstado = None

    def get_proxEstado(self):
        return self.proxEstado
    
    def set_proxEstado(self, prox):
        self.proxEstado = prox

    def get_anteriorEstado(self):
        return self.anteriorEstado
    
    def set_anteriorEstado(self, anterior):
        self.anteriorEstado = anterior

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
        else:
            print("Funções de transições fora do Padrao de um AFD")

    def laco_transicoes(self,simbolo):
        estado = self.primeiro_estado
        aux_inicio = None
        aux_fim = None
        while estado.get_proxEstado() != None:
            aux1, aux2 = self.aplicacao_transicoes(simbolo, estado)
            if((aux_inicio and aux_inicio) == None):
                aux_inicio = aux1
                aux_fim = aux2
            else:
                aux_fim.set_proxEstado(aux1)
                aux1.set_anteriorEstado(aux_fim)
                aux_fim = aux2
            estado = estado.get_proxEstado()
        else: 
            aux1, aux2 = self.aplicacao_transicoes(simbolo, estado)
            if((aux1 and aux2) != None):
                if((aux_inicio and aux_fim) == None):
                    aux_inicio = aux1
                    aux_fim = aux2
                else:
                    aux_fim.set_proxEstado(aux1)
                    aux1.set_anteriorEstado(aux_fim)
                    aux_fim = aux2
        if((aux_inicio and aux_fim) != None):
            estado.set_proxEstado(aux_inicio)
            aux_inicio.set_anteriorEstado(estado)
            self.ultimo_estado = aux_fim
        

    def aplicacao_transicoes(self, simbolo,estado_atual):    
        aux_inicio = None
        aux_fim = None
        estados = estado_atual.name

        for i in range(len(self.transicoes[estados][simbolo])):
            if(i == 0):
                estado_atual.name = self.transicoes[estados][simbolo][i]
            else:
                novoEstado = estado()
                novoEstado.name = self.transicoes[estados][simbolo][i]
                if((aux_inicio and aux_fim) == None):
                    aux_inicio = novoEstado
                    aux_fim = novoEstado
                else:
                    aux_fim.set_proxEstado(novoEstado)
                    novoEstado.set_anteriorEstado(aux_fim)
                    aux_fim = novoEstado
                self.quantidade_estados += 1
        if(len(self.transicoes[estados][simbolo]) == 0):
            self.entrada_sem_saida(estado_atual)
        return aux_inicio, aux_fim

    def entrada_sem_saida(self, estado):
        if(estado == self.primeiro_estado):
            self.primeiro_estado = self.primeiro_estado.get_proxEstado()
        elif(estado == self.ultimo_estado):
            self.ultimo_estado = self.ultimo_estado.get_anteriorEstado()
            self.ultimo_estado.set_proxEstado(None)
        else:
            estado1 = estado.get_anteriorEstado()
            estado2 = estado.get_proxEstado()
            estado1.set_proxEstado(estado2)
            estado2.set_anteriorEstado(estado1)
        self.quantidade_estados += -1

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
        
        estado_atual = self.primeiro_estado

        if(estado_atual != None):
            while(estado_atual.get_proxEstado() != None):
                if(self.verificacao_automato(estado_atual.name) == True):
                    self.end()
                    return
                estado_atual = estado_atual.get_proxEstado()
            else:
                if(self.verificacao_automato(estado_atual.name) == True):
                    self.end()
                    return
                else:
                    print("String Recusada\n")
                    self.end()
        else:
            print("String Recusada")
            self.end()
        
    def verificacao_automato(self, estado):
        if(estado in self.estadosFinais):
            print("String Aceito\n")
            return True

    def end(self):
        self.primeiro_estado = None
        self.ultimo_estado = None
        self.quantidade_estados = 0

afd = AFND()
afd.set_alfabeto(['0','1'])
afd.set_estados(['q1','q2','q3'])
afd.set_estadoInicial('q1')
afd.set_estadosFinais(['q2','q3'])
afd.set_transicoes({'q1':{'0':['q3','q2'],'1':['q1']},'q2':{'0':['q3','q2'],'1':['q1']},'q3':{'0':['q2','q3'],'1':['q1']}}) 
afd.set_string('001')
afd.set_string('00')