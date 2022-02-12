import math
import random
import pandas as pd
import matplotlib.pyplot as plt

alpha_aleatorio = []
intensidade_paralelo = []
intensidade_perpendicular = []
n = 1.01

for i in range(3000):
    a = random.uniform(0,90)
    b = a*math.pi/180
    alpha_aleatorio.append(a)
alpha_aleatorio.sort()

for i in range(len(alpha_aleatorio)):
    b = alpha_aleatorio[i]*math.pi/180
    intensidade_perpendicular.append((math.sqrt((n**2)-(math.sin(b))**2)-math.cos(b)**2)/((n**2)-1))
    intensidade_paralelo.append((n**2*(math.cos(b))-(math.sqrt((n**2-(math.sin(b))**2))))/((n**2*(math.cos(b)))+(math.sqrt((n**2)-((math.sin(b))**2)))))

arquivo = pd.read_csv('Intensidade_referencia_minimo.txt')
arquivo = pd.DataFrame(arquivo)
arquivo['num'] = (arquivo['Intensidade'])/28

arquivo2 = pd.read_csv('Intensidade_referencia_minimo.txt')
arquivo2 = pd.DataFrame(arquivo2)
arquivo2['num'] = (arquivo2['Intensidade'])/64

def fazer_grafico(xmin,ymin,xmax,ymax,xexperimentlamax,yexperimentalmax,xexperimentlamin,yexperimentalmin,titulo,nomeeixoy,nomeeixox,nome_arquivo):
    plt.plot(xmin,ymin,label = 'teórico') #plotar o gráfico
    plt.plot(xmax,ymax,label = 'teórico')
    plt.scatter(xexperimentlamin,yexperimentalmin,color = 'black',label = 'perpendicular')
    plt.scatter(xexperimentlamax,yexperimentalmax,color = 'red',label = 'paralelo')
    plt.title(titulo) #título
    plt.xlabel(nomeeixox) #título do eixo x
    plt.ylabel(nomeeixoy) #título do eixo y
    plt.legend()
    plt.savefig(nome_arquivo,format='png')
    plt.show()

grafico = fazer_grafico(alpha_aleatorio,intensidade_perpendicular,
alpha_aleatorio,intensidade_paralelo,
arquivo['alpha'],arquivo['num'],
arquivo2['alpha'],arquivo2['num'],'Coeficiente de reflexão X Ângulo de reflexão','Coeficiente de reflexão','Ângulo de incidência (°)','grafico.png')