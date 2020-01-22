import pandas as pd
import matplotlib.pylab as plt
from statsmodels.tsa.seasonal import seasonal_decompose

base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';')

dateparse = lambda dates: pd.datetime.strptime(dates, '%d/%m/%Y')
base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';', dayfirst = True,
                   parse_dates = ['data'], index_col ='data', date_parser = dateparse)

ts = base['valor']

plt.figure(figsize = (10, 5))
plt.xlabel('Anos')
plt.ylabel('Quantidade de comerciais leves vendidos')
plt.plot(ts)

decomposicao = seasonal_decompose(ts)
tendencia = decomposicao.trend
sazonal = decomposicao.seasonal
residuo = decomposicao.resid

plt.plot(tendencia)
plt.plot(sazonal)
plt.plot(residuo)

plt.figure(figsize = (10, 5))
plt.subplot(4, 1, 1)
plt.plot(ts, label = 'Original')
plt.legend(loc = 'best')

plt.subplot(4, 1, 2)
plt.plot(tendencia, label = 'Tendência')
plt.legend(loc = 'best')

plt.subplot(4, 1, 3)
plt.plot(sazonal, label = 'Sazonalidade')
plt.legend(loc = 'best')

plt.subplot(4, 1, 4)
plt.plot(residuo, label = 'Residuo')
plt.legend(loc = 'best')
plt.tight_layout()