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
                        if(transicoes[estado][entrada] not in self.estados):
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

    def aplicacao_transicoes(self, estado_atual,simbolo):
        estado_atual = self.transicoes[estado_atual][simbolo]
        return estado_atual

    def set_string(self, string):
        for simbolo in list(set(string)):
            if(simbolo not in self.alfabeto):
                print("'"+ simbolo +"' nao faz parte do alfabeto")
                return
            
        estado_atual = self.estadoInicial

        for simbolo in string:
            estado_atual = self.aplicacao_transicoes(estado_atual, simbolo)
    
        if(estado_atual in self.estadosFinais):
            print("String aceita")
        else:
            print("String Recusada")

afd = AFD()
afd.set_alfabeto(['0','1'])
afd.set_estados(['q1','q2','q3','q4'])
afd.set_estadoInicial('q1')
afd.set_estadosFinais(['q2','q4'])
afd.set_transicoes({'q1':{'0':'q3','1':'q2'},'q2':{'0':'q1','1':'q4'},'q3':{'0':'q2','1':'q4'},'q4':{'0':'q4','1':'q1'}}) 
afd.set_string('110001')