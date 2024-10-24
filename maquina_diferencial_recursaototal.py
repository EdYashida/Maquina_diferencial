from maquina_diferencial import linha


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

def babbage(eixo_y,i,j,tabela,linha):
    n = len(eixo_y)

    if i==n-1:
        l=preenchelinha(i,j,n,tabela,linha) #faz a lista de diferença mais distante
        tabela.append(l) #insere a linha na tabela
        return tabela

    else:
        babbage(eixo_y, i+1, j, tabela) #incrementa i+1 anté ele ser igual à n-1
                                        #i referencia a linha/ lista de diferença
        l=preenchelinha(i,j,n,tabela,linha) #faz a lista de diferença com incide igual i+1
        return tabela


def preenchelinha(i,j,n,tabela,linha):  #lida com o laço de j
    if j==n-i-1:
        v = tabela[i][j] - tabela[i][j + 1]  # define valor pela diferença de 2 seguidos da linha anterior
        linha.append(v)  # adiciona valor à linha
        return linha     # retorna linha
    else:
        preenchelinha(i,j+1,n,tabela,linha) #vai pros elementos sucessores da lista de diferença
        v = tabela[i][j] - tabela[i][j + 1]
        linha.append(v)  #adiciona na mesma linha
        return linha


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

tabela = [eixo_y]  # primeira linha são os resultados
                    # cria uma tabela quando chama pela primeira vez apenas
                    # cria fora pra só instanciar uma vez
linha = list()      #mesma coisa
diffs = babbage(eixo_y,0,0, tabela,list)
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
