'''Aqui iremos fazer um teste de tendência da série temporal, utilizando o Mann-Kendall'''

import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.pylab as plt
import pymannkendall

def mk_test(y):
    #teste de mann-kendall
    print('Resultado do Teste Mann-Kendall')
    mkteste = pymannkendall.hamed_rao_modification_test(y)
    mksaida = pd.Series(mkteste[0:9], index = ['Movimento Tendência', 'Há Tendência?', 'Valor p', 'Teste normalizado',
                                               'Coeficiente Kendall', 'Mand-Kendall Score', 'Variância S', 'Sen Slope'])
    print(mksaida)

base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';')

dateparse = lambda dates: pd.datetime.strptime(dates, '%d/%m/%Y')
base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';', dayfirst = True,
                   parse_dates = ['data'], index_col ='data', date_parser = dateparse)

plt.plot(base)

y = base['valor']

mk_test(y)

'''Como o valor de p é menor do que 0.05, a hipótese nula é rejeitada, e confirma
a tendência da série temporal. '''