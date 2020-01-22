''' Como o teste de estacionariedade confirmou que a série temporal não é
estacionária, teremos que fazer uma transformação na série temporal, para
depois aplicarmos, novamente, o teste de estacionaridade de Dickey-Fuller.'''

import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.pylab as plt
import numpy as np
from statsmodels.tsa.stattools import adfuller

def adf_teste(y):
    #Perfomance do teste ADF
    print('Resultado do teste Dickey-Fuller:')
    df_teste = adfuller(y, autolag = 'AIC')
    df_saida = pd.Series(df_teste[0:4], index = ['Teste', 'Valor p', '# de lags', '# de observações'])
    for k, valor in df_teste[4].items():
        df_saida[f'Valores críticos ({k})'] = valor
    print(df_saida)

base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';')

dateparse = lambda dates: pd.datetime.strptime(dates, '%d/%m/%Y')
base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';', dayfirst = True,
                   parse_dates = ['data'], index_col ='data', date_parser = dateparse)

plt.plot(base)

y = base['valor']

adf_teste(y)

y_diff = np.diff(y) #Aplicando a diferenciação de 1ª Ordem

plt.plot(y_diff)

adf_teste(y_diff)

plt.figure(figsize = (10, 5))
plt.subplot(2, 1, 1)
plt.title('Antes da diferenciação de 1ª Ordem')
plt.plot(base)

plt.subplot(2, 1, 2)
plt.title('Depois da diferenciação de 1ª Ordem')
plt.plot(y_diff)
plt.tight_layout()

''' Após aplicar a diferenciação de 1ª ordem, a série temporal não-estacionária
virou estacionária, e aplicando o teste de Dickey-Fuller confirmou que o valor p < 0.05,
rejeitando a hipótese nula e confirmando a estacionariedade para a série temporal.'''