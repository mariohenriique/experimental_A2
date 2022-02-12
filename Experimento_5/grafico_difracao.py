import pandas as pd
import matplotlib.pyplot as plt
import math

def ler_arquivo(nome_arquivo):
    arquivo = pd.read_csv(nome_arquivo)
    arquivo = pd.DataFrame(arquivo)
    arquivo['tempo'] = (arquivo['tempo']-123.5)/10
    return(arquivo)

def normalize(x):
    return [(x[n] - min(x)) / (max(x) - 
           min(x)) for n in range(len(x))]

arquivo = ler_arquivo('Fenda dupla a de 0p04 mm e d de 0p250 mm - 10 sec por cm - D de 165 cm')
arquivo['intensidade'] = normalize(arquivo['intensidade'])


x1 = []
ydupla = []
ysimples = []
Io = 1
a = 5*10**(-5)
X = 1
D = 0.18
d = 1/300
comprimentodeonda = 632.8*10**(-9)

tamanho = 2479

for i in range(len(arquivo['tempo'])):
    x1.append((i-200)*math.pi*0.001)

for i in range(len(x1)):
    if x1[i]==0:
        x1[i] = 0.0002
    ydupla.append(Io*math.sin(math.pi*a*math.sin(x1[i])/(comprimentodeonda))**2*(math.cos(math.pi*d*math.sin(x1[i])/(comprimentodeonda)))**2/(math.pi*a*math.sin(x1[i])/(comprimentodeonda))**2)
    ysimples.append(Io*math.sin(math.pi*a*math.sin(x1[i])/(comprimentodeonda))**2/(math.pi*a*math.sin(x1[i])/(comprimentodeonda))**2)

def fazer_grafico(x,y,int,titulo,nomeeixox,nomeeixoy,nome_arquivo):
    plt.plot(x,y,'red',label = 'Experimental') #plotar o gráfico
    plt.plot(x1,int,'black',label = 'Teórico')
    plt.title(titulo) #título
    plt.legend()
    #plt.xlim(-0.05,0.05)
    plt.xlabel(nomeeixox) #título do eixo x
    plt.ylabel(nomeeixoy) #título do eixo y
    plt.savefig(nome_arquivo,format='png')
    plt.show()

grafico = fazer_grafico(arquivo['tempo'],arquivo['intensidade'],ysimples,'Fenda simples','Theta (rad)','Intensidade normalizada','fenda_simples_experimental.png')
grafico1 = fazer_grafico(arquivo['tempo'],arquivo['intensidade'],ydupla,'Fenda dupla 300 linhas','Posição (m)','Intensidade normalizada','fenda_dupla_300_experimental.png')
grafico2 = fazer_grafico(arquivo['tempo'],arquivo['intensidade'],ydupla,'Fenda dupla 600 linhas','Theta (rad)','Intensidade normalizada','fenda_dupla_600_experimental.png')
grafico3 = fazer_grafico(arquivo['tempo'],arquivo['intensidade'],ysimples,'Fenda simples','Theta (rad)','Intensidade normalizada','fenda_simples_teorico.png')
grafico4 = fazer_grafico(arquivo['tempo'],arquivo['intensidade'],ydupla,'Fenda dupla 300 linhas','Posição (m)','Intensidade normalizada','fenda_dupla_300_teorico.png')
grafico5 = fazer_grafico(arquivo['tempo'],arquivo['intensidade'],ydupla,'Fenda dupla 600 linhas','Theta (rad)','Intensidade normalizada','fenda_dupla_600_teorico.png')