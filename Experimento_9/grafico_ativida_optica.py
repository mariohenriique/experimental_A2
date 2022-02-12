import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

arquivo = pd.read_csv('dados.txt')
arquivo = pd.DataFrame(arquivo)
arquivo['d'] = arquivo['d']/100

#linearização
res1 = stats.linregress(arquivo['solu1'],arquivo['d'])
res2 = stats.linregress(arquivo['solu2'],arquivo['d'])
res3 = stats.linregress(arquivo['solu3'],arquivo['d'])

def fazer_grafico(x1,x2,x3,y,titulo,nomeeixox,nomeeixoy,nome_arquivo):
    plt.scatter(x1,y,color = 'black',label = 'Solução 1')
    plt.scatter(x2,y,color = 'red',label = 'Solução 2')
    plt.scatter(x3,y,color = 'blue',label = 'Solução 3')
    plt.plot(x1,res1.intercept + res1.slope*x1,color = 'black',label = 'Regressão Linear 1')
    plt.plot(x2,res2.intercept + res2.slope*x2,color = 'red',label = 'Regressão Linear 2')
    plt.plot(x3,res3.intercept + res3.slope*x3,color = 'blue',label = 'Regressão Linear 3')
    plt.title(titulo) #título
    plt.xlabel(nomeeixox) #título do eixo x
    plt.ylabel(nomeeixoy) #título do eixo y
    plt.legend()
    plt.savefig(nome_arquivo,format='png')
    plt.show()

print(res1.slope)
grafico = fazer_grafico(arquivo['solu1'],arquivo['solu2'],arquivo['solu3'],arquivo['d'],'Polarização X Distância','Ângulo de polarização[°]','Distância [m]','grafico.png')