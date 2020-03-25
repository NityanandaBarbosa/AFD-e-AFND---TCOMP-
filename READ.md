## Autômato finito determinístico - AFD

- Primeiro é necessário instânciar o AFD.

```py
        afd = AFD()
```
- O alfabeto de ver ser passado por meio de um vetor, caracteres repitidos serão ignorados.

```py
        afd.set_alfabeto(['0','1']) 
```
- O conjunto de estados devem ser passados por meio de um vetor, estados repitidos serão ignorados.

```py   
        afd.set_estados(['q1','q2','q3','q4'])
```
- O estado inicial deve está contido nos estados e deve ser passado como uma string.

```py
        afd.set_estadoInicial('q1')
```
- O conjunto de estados finais devem ser passados por meio de um vetor, estados não contigos no conjunto de estados ou estados repitido serão ignorado.

```py   
        afd.set_estadosFinais(['q2','q4'])
```
- As funções de transição deve ser passadas por meio de um dicionario que conterá os estados e esses estados devem ter um dicionario que terá suas entradas contidas no alfabeto e suas respectivas saidas.

```py    
        afd.set_transicoes({'q1':{'0':'q3','1':'q2'},'q2':{'0':'q1','1':'q4'},'q3':{'0':'q2','1':'q4'},'q4':{'0':'q4','1':'q1'}}) 
```
- A string que será testado não pode conter caracteres que diferentes do alfabeto.

```py
        afd.set_string('110') #String Aceita
        afd.set_string('110001') #String Recusada
```

## Autômato finito não-determinístico - AFND

- Primeiro é necessário instânciar o AFD.

```py
        afnd = AFND()
```
- O alfabeto de ver ser passado por meio de um vetor, caracteres repitidos serão ignorados.

```py
        afnd.set_alfabeto(['0','1']) 
```
- O conjunto de estados devem ser passados por meio de um vetor, estados repitidos serão ignorados.

```py   
        afnd.set_estados(['q1','q2','q3','q4'])
```
- O estado inicial deve está contido nos estados e deve ser passado como uma string.

```py
        afnd.set_estadoInicial('q1')
```
- O conjunto de estados finais devem ser passados por meio de um vetor, estados não contigos no conjunto de estados ou estados repitido serão ignorado.

```py   
        afnd.set_estadosFinais(['q2','q4'])
```
- As funções de transição deve ser passadas por meio de um dicionario que conterá os estados e esses estados devem ter um dicionario que terá suas entradas contidas no alfabeto e suas respectivas saidas dentro de um vetor.

```py    
        afnd.set_transicoes({'q1':{'0':['q3','q2'],'1':['q1']},'q2':{'0':['q3','q2'],'1':['q1']},'q3':{'0':['q2','q3'],'1':['q1']}})  
```
- A string que será testado não pode conter caracteres que diferentes do alfabeto.

```py
        afnd.set_string('001') #String Recusada
        afnd.set_string('00') #String Aceita
```