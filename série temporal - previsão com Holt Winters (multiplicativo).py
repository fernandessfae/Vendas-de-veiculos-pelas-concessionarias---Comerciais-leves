import pandas as pd
import matplotlib.pylab as plt

base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';')

dateparse = lambda dates: pd.datetime.strptime(dates, '%d/%m/%Y')
base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';', dayfirst = True,
                   parse_dates = ['data'], index_col ='data', date_parser = dateparse)

from statsmodels.tsa.api import ExponentialSmoothing

fit1 = ExponentialSmoothing(base, seasonal_periods = 12, trend = 'multiplicative', seasonal = 'multiplicative').fit(use_boxcox = True)

plt.figure(figsize = (10, 5))
plt.xlabel('Anos')
plt.ylabel('Quantidade de comerciais leves vendidos')
fit1.fittedvalues.plot(style = '--', color = 'red')

plt.figure(figsize = (10, 5))
plt.xlabel('Anos')
plt.ylabel('Quantidade de comerciais leves vendidos(previsão)')
fit1.forecast(24).plot(style = '--', marker = 'o', color = 'black', label = 'Previsão', legend = True)

plt.figure(figsize = (10, 5))
plt.xlabel('Anos')
plt.ylabel('Quantidade de comerciais leves vendidos')
fit1.fittedvalues.plot(style = '--', color = 'red', legend = True, label = 'Dados Originais')
fit1.forecast(24).plot(style = '--', color = 'black', legend = True, label = 'Previsão')