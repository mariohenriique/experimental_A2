import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def fazer_grafico(txt,titulo,nomeeixoy,nomeeixox,nome_arquivo):
    arquivo = pd.read_table(txt)
    arquivo = pd.DataFrame(arquivo)
    x = arquivo['Tempo']
    y = arquivo['Posicao']
    plt.scatter(x,y, s= 5.) #plotar o gráfico
    plt.title(titulo) #título
    plt.xlabel(nomeeixox) #título do eixo x
    plt.ylabel(nomeeixoy) #título do eixo y
    plt.savefig(nome_arquivo,format='png')
    plt.show()

grafico1 = fazer_grafico('oscilador x3-01-12-experimento1-mais amortecimento.txt','Oscilador mais amortecimento','posição (m)', 'tempo (s)','mais_amortecimento.png')
grafico2 = fazer_grafico('oscilador x3-01-12-experimento1-menos amortecimento.txt','Oscilador menos amortecimento','posição (m)', 'tempo (s)','menos_amortecimento.png')


arquivo = pd.read_table('oscilador x3-01-12-experimento1-mais amortecimento.txt')
arquivo = pd.DataFrame(arquivo)

def verifica_ponto_inflexao (inflexao):
    maior = []
    menor = []
#percorri a lista do segundo item até o penúltimo e adicionei em outras listas
    for i in range(1, len(inflexao) - 1):
        if inflexao[i] < inflexao[i + 1] and inflexao[i] <= inflexao[i - 1] and inflexao[i]<inflexao[i+2] and inflexao[i]<=inflexao[i-2]and inflexao[i]<inflexao[i+3] and inflexao[i]<=inflexao[i-3]:
            menor.append(inflexao[i])
        
        elif inflexao[i] > inflexao[i + 1] and inflexao[i] >= inflexao[i - 1]and inflexao[i]>inflexao[i+2] and inflexao[i]>=inflexao[i-2]and inflexao[i]>inflexao[i+3] and inflexao[i]>=inflexao[i-3]:
            maior.append(inflexao[i])
#toda vez que fazer uma funçao tem q definir o que me retorna
    return maior, menor

mais_amortecimento = verifica_ponto_inflexao(arquivo['Posicao'])
maior = mais_amortecimento[0]
menor = mais_amortecimento[1]
print(menor,len(menor),maior,len(maior))