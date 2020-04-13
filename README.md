## Autômato finito determinístico - AFD

- Primeiro é necessário instânciar o AFD.

```py
        afd = Automato()
```
- O alfabeto dever ser passado por meio de um vetor, caracteres repetidos serão ignorados.

```py
        afd.set_alfabeto(['0','1']) 
```
- O conjunto de estados devem ser passados por meio de um vetor, estados repetidos serão ignorados.

```py   
        afd.set_estados(['q1','q2','q3','q4'])
```
- O estado inicial deve está contido nos estados e deve ser passado como uma string.

```py
        afd.set_estadoInicial('q1')
```
- O conjunto de estados finais devem ser passados por meio de um vetor, estados não contidos no conjunto de estados ou estados repetidos serão ignorado.

```py   
        afd.set_estadosFinais(['q2','q4'])
```
- As funções de transição deve ser passadas por meio de um dicionário que conterá os estados e esses estados devem ter um dicionário que terá suas entradas contidas no alfabeto e suas respectivas saidas.

```py    
        afd.set_transicoes({'q1':{'0':'q3','1':'q2'},
                            'q2':{'0':'q1','1':'q4'},
                            'q3':{'0':'q2','1':'q4'},
                            'q4':{'0':'q4','1':'q1'}}) 
```
- A string que será testado não pode conter caracteres que diferentes do alfabeto.

```py
        afd.set_string('110') #String Aceita
        afd.set_string('110001') #String Recusada
```

## Autômato finito não-determinístico - AFND

- Primeiro é necessário instânciar o AFND.

```py
        afnd = Automato()
```
- O alfabeto dever ser passado por meio de um vetor, caracteres repitidos serão ignorados.

```py
        afnd.set_alfabeto(['0','1']) 
```
- O conjunto de estados devem ser passados por meio de um vetor, estados repetidos serão ignorados.

```py   
        afnd.set_estados(['a','b','c','d','e','f'])
```
- O estado inicial deve está contido nos estados e deve ser passado como uma string.

```py
        afnd.set_estadoInicial('a')
```
- O conjunto de estados finais devem ser passados por meio de um vetor, estados não contidos no conjunto de estados ou estados repetidos serão ignorado.

```py   
        afnd.set_estadosFinais(['a','c','f'])
```
- As funções de transição deve ser passadas por meio de um dicionário que conterá os estados e esses estados devem ter um dicionário que terá suas entradas contidas no alfabeto e suas respectivas saidas dentro de um vetor.

```py    
        afnd.set_transicoes({'a': {'0': ['f'], '1': ['b'],'epsilon':[]},
                             'b': {'0': [], '1': ['b'],'epsilon':['e']},
                             'c': {'0': [],'1':['d'],'epsilon':[]},
                             'd': {'0': [], '1': ['f'],'epsilon':[]},
                             'e': {'0': [], '1': ["c"],'epsilon':['c']},
                             'f': {'0': ['f'], '1': ["c"],'epsilon':['a']}})  
```
- A string que será testado não pode conter caracteres que diferentes do alfabeto.

```py
        afnd.set_string("1")  #String Recusada
        afnd.set_string("10") #String Aceita
```

## AFND to AFD

- Deve se seguir todos etapas de "configuração" já descritas de um AFND menos a de set_string.

```py
        afnd = AFND.Automato()
```
```py
        afnd.set_alfabeto(['0','1'])
```
```py
        afnd.set_estados(['a','b','c','d','e','f'])
```

```py
        afnd.set_estadoInicial('a')
```

```py  
        afnd.set_estadosFinais(['d'])
```
```py
        afnd.set_transicoes({'a': {'0': ['e'], '1': ['b'],'epsilon':[]},
                             'b': {'0': [], '1': ['c'],'epsilon':['d']},
                             'c': {'0': [],'1':['d'],'epsilon':[]},
                             'd': {'0': [], '1': [],'epsilon':[]},
                             'e': {'0': ['f'], '1': [],'epsilon':['b','c']},
                             'f': {'0': ['d'], '1': [],'epsilon':[]}})
```
- Instanciar convert passando como parâmetro o AFND.

```py
        convert = convert(afnd)
```

- Setar uma string que será testada no AFND e no AFD gerado.

```py
        convert.set_string_all("101")

        #Result :
                Resultado AFD : 
                String Recusada
                Resultado AFND : 
                String Recusada
```