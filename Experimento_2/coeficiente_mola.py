import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

arquivo = pd.DataFrame(pd.read_table('medida da constante elastica.txt'))
arquivo['x'] = arquivo['x']*0.01
arquivo['m'] = arquivo['m']*0.001


x = arquivo['x']
y = arquivo['m']
res = stats.linregress(x, y)

def fazer_grafico(titulo,nomeeixoy,nomeeixox,nome_arquivo):
    plt.scatter(x,y) #plotar o gráfico
    plt.plot(x, res.intercept + res.slope*x, 'r', label='fitted line')
    plt.title(titulo) #título
    plt.xlabel(nomeeixox) #título do eixo x
    plt.ylabel(nomeeixoy) #título do eixo y
    plt.savefig(nome_arquivo,format='png')
    plt.show()

print(9.78*res.slope, 0.05*res.stderr)
grafico = fazer_grafico('Constante elástica da mola','massa (kg)','deformação (m)','mola.png')