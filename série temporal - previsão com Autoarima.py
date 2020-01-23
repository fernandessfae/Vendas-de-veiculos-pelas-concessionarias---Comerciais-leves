import pandas as pd
import matplotlib.pylab as plt

base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';')

dateparse = lambda dates: pd.datetime.strptime(dates, '%d/%m/%Y')
base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';', dayfirst = True,
                   parse_dates = ['data'], index_col ='data', date_parser = dateparse)

base = base.rename({'valor' : 'quantidade veículos'}, axis = 1)
plt.xlabel('Anos')
plt.ylabel('Quantidade de comerciais leves vendidos')
plt.plot(base)

#Utilização do autoarima para a previsão

from pmdarima.arima import auto_arima

stepwise_model = auto_arima(base, start_p = 1, start_q = 1, max_p = 6, max_q = 6,
                            m = 12, start_P = 0, seasonal = True, d = 1, D = 1,
                            erro_action = 'ignore', suppress_warnings = True, stepwise = True)

AIC = stepwise_model.aic()

treino = base.loc['1990-01-01': '2018-12-01']
teste = base.loc['2019-01-01':]

stepwise_model.fit(treino)

ano_futuro = stepwise_model.predict(n_periods = 12)

ano_futuro = pd.DataFrame(ano_futuro, index = teste.index, columns = ['quantidade comerciais leves vendidos']) 

pd.concat([teste, ano_futuro], axis = 1).plot()

pd.concat([base, ano_futuro], axis = 1).plot(linewidth = 3)