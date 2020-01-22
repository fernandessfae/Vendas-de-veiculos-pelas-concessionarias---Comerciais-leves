import pandas as pd
import matplotlib.pylab as plt
import numpy as np

base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';')

dateparse = lambda dates: pd.datetime.strptime(dates, '%d/%m/%Y')
base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';', dayfirst = True,
                   parse_dates = ['data'], index_col ='data', date_parser = dateparse)

#Fazer o teste de estacionaridade da série temporal

from statsmodels.tsa.stattools import adfuller

X = base['valor']
resultado = adfuller(X)
print(f'ADF Estatísticas: {resultado[0]}')
print(f'Valor de P: {resultado[1]}')
print('Valores críticos: ')
for k, valor in resultado[4].items():
    print(f'\t{k}: {valor:.3f}')

''' Como o valor de P > 0.05, aqui comprova que a série não é estacionária.
    Vale ressaltar que pelo gráfico da série temporal já percebe-se que a série
    não é estacionária, porém é interessante fazer o teste para corroboração.'''