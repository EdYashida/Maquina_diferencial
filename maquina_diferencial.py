
def resultado(dif,i):

    if dif[i][-1] == dif[-1][-1]: #para quando encontra o ultimo "diferente"(coluna)
        return dif[i][-1]
    else :
        return dif[i][-1] - resultado(dif,i+1) #retorna diferença

    #faz a diferença do ultimo valor da linha anterior à ela por ela
    #precisa fazer de 2 em 2!
    #pega o resultado da diferença e faz pelo outro
    #o faz até tirar a diferença pela linha 0
    #retorna resultado
    return 1

def babbage(eixo_y):
    n = len(eixo_y) #4
    tabela = [eixo_y] #primeira linha são os resultados
    for i in range(n - 1): #0 até 3         numero de linhas, 3
        linha = []
        for j in range(n - i - 1): #4-i-1       define n de valores na linha
            v = tabela[i][j] - tabela[i][j + 1] #define valor pela diferença de 2 seguidos da linha anterior
            linha.append(v) #adiciona valor à linha
        tabela.append(linha) #adiciona linha à tabela
    return tabela


def polinomio(x, coeficientes, grau):
    soma = 0
    i = 0
    while (i <= grau):
        soma += coeficientes[i] * (x ** (grau - i))
        i += 1
    return soma


coeficientes = list()
grau = int(input('Deseja inserir um polinômio de qual grau? ')) #insere grau do polinomio
grauaux = grau


for i in range(0,grau+1):
    valor = int(input(f'Insira o digito de grau {grauaux}: '))
    grauaux-=1
    coeficientes.append(valor) #a cada valor inserido, grau reduz em 1
#coeficientes = [2, -2, 3, 2]
#grau = len(coeficientes) - 1


eixo_x = list() #obtem informação sobre os valores de entrada (x)
xinicial = float(input('Qual o valor inicial? '))
xpasso = float(input('Qual o incremento desse valor? '))
x=xinicial #será incrementado


print('-'*30)
resultadodesejado = float(input('Deseja resultado para qual valor?(deve estar até o 100º passo incremental) '))
print('-'*30)


for i in range(0,100): #preenche entrada
    eixo_x.append(x) #adiciona o x atual
    x+=xpasso #obtem o próximo x
    if x==resultadodesejado: #para de adicionar entrada após adicionar o valor cujo resultado eh desejado
        break
    if i==99 and x !=resultadodesejado: #caso entrada não esteja no padrão
        print('A entrada não está no formato da progressão de x!')
        exit()


eixo_y = [polinomio(x, coeficientes, grau) for x in eixo_x]


diffs = babbage(eixo_y)
print(f'Entrada(x): {eixo_x}')
print(f'Pn(x): {eixo_y}')
print('')

print("tabela de diferenças :")
for c, linha in enumerate(diffs):
    if c == 0:
        print(f"Pn(x): {linha}")
    else:
        print(f"dif {c-1}: {linha}")

#Mostra o resultado desejado
print(f'\nO resultado para a entrada {resultadodesejado}, considerando o polinômio ',end='')
for i,v in enumerate(coeficientes):
    if v>=0 and i!=0 and i+1!=len(coeficientes):
        print(f'+{v}x^{grau-i}',end='')
    if v>=0 and i==0:
        print(f'{v}x^{grau-i}',end='')
    if v<0:
        print(f'{v}x^{grau-i}',end='')
    if i+1==len(coeficientes):
        if v>=0:
            print(f'+{v}',end=' é ')
        if v<0:
            print(v,end=' é ')

#chama função pra retornar resultado
res = resultado(diffs,0)
print(res)
