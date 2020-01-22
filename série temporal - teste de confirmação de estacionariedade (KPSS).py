''' Alem do teste de estacionariedade do Dickey Fuller, usaremos o teste do KPSS'''

import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.pylab as plt
import numpy as np
from statsmodels.tsa.stattools import kpss

def kpss_test(y):
    #Teste com o KPSS
    print('Resultado com o teste KPSS')
    kpss_teste = kpss(y)
    kpss_saida = pd.Series(kpss_teste[0:4], index = ['Status KPSS', 'Valor p', '# de lags',
                                                     '# de observações' ])
    for k, valor in kpss_teste[3].items():
        kpss_saida[f'Valores críticos ({k})'] = valor
    print(kpss_saida)
    
base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';')

dateparse = lambda dates: pd.datetime.strptime(dates, '%d/%m/%Y')
base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';', dayfirst = True,
                   parse_dates = ['data'], index_col ='data', date_parser = dateparse)

plt.plot(base)

y = base['valor']

kpss_test(y)

y_diff = np.diff(y) #Aplicando a diferenciação de 1ª Ordem
plt.plot(y_diff)
kpss_test(y_diff)

y_diff2 = np.diff(y_diff) #Aplicando a diferenciação de 2ª Ordem
plt.plot(y_diff2)
kpss_test(y_diff2)

''' Mesmo fazendo 2 diferenciações, o valor de p é maior do que 0.05, então a hipótese nula
está mantida, só que diferente do Dickey Fuller a hipótese nula significa que a série é estacionária'''