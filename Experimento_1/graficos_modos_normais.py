import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def fazer_grafico(txt,titulo,nomeeixoy,nomeeixox,nome_arquivo):
    arquivo = pd.read_table(txt)
    arquivo = pd.DataFrame(arquivo)
    x = arquivo['Tempo']
    y = arquivo['Posicao']
    plt.plot(x,y) #plotar o gráfico
    plt.title(titulo) #título
    plt.xlabel(nomeeixox) #título do eixo x
    plt.ylabel(nomeeixoy) #título do eixo y
    plt.savefig(nome_arquivo,format='png')
    plt.show()

grafico1 = fazer_grafico('pendulo E1.txt','pendulo simples','posição (m)', 'tempo (s)','pendulo_simples.png')
grafico2 = fazer_grafico('mola E2.txt','massa mola','posição (m)', 'tempo (s)','massa_mola.png')
grafico3 = fazer_grafico('modo anti simetrico E3.txt','modo anti simétrico','posição (m)', 'tempo (s)','modo_anti_simetrico.png')
grafico4 = fazer_grafico('moso simetrico E4.txt','modo simétrico','posição (m)', 'tempo (s)','modo_simetrico.png')
grafico5 = fazer_grafico('batimento E5.txt','batimento','posição (m)', 'tempo (s)','batimento.png')
grafico6 = fazer_grafico('batimento-mola grande E5 extra.txt','batimento','posição (m)', 'tempo (s)','batimento_extra.png')