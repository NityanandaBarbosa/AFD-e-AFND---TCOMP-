import AFND, AFD

class converter():
    
    def __init__(self, afnd):
        self.afnd = afnd

    def conversao(self):
        afd = AFD.Automato()
        afd.set_alfabeto(self.afnd.alfabeto)
        afd.estados.append(self.afnd.estadoInicial)
        afd.set_estadoInicial(self.afnd.estadoInicial)


    

afnd = AFND.Automato()
afnd.set_alfabeto(['0','1'])
afnd.set_estados(['q1','q2','q3'])
afnd.set_estadoInicial('q1')
afnd.set_estadosFinais(['q2','q3'])
afnd.set_transicoes({'q1':{'0':['q3','q2'],'1':['q1']},'q2':{'0':['q3','q2'],'1':['q1']},'q3':{'0':['q2','q3'],'1':['q1']}}) 

convert = converter(afnd)
