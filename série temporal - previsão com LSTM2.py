import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

base = pd.read_csv('bcdata.sgs.7385.csv', sep = ';')

#Separação dos dados de treinamento e teste
base_treinamento = base.iloc[0:270, 1:2].values
base_teste = base.iloc[270:360, 1:2].values

#Normalização dos dados de treinamento
normalizador = MinMaxScaler()
base_treinamento_normalizada = normalizador.fit_transform(base_treinamento)

#Separação dos elementos que irão a previsão e a quantidade real de caminhões para a rede neural LSTM
previsores = []
qt_real = []
for i in range(24, 270):
    previsores.append(base_treinamento_normalizada[i-24:i, 0])
    qt_real.append(base_treinamento_normalizada[i, 0])
previsores, qt_real = np.array(previsores), np.array(qt_real)
previsores = np.reshape(previsores, (previsores.shape[0], previsores.shape[1], 1))

#Criação da rede neural LSTM e treinamento com os dados de treinamento
regressor = Sequential()
regressor.add(LSTM(units = 100, return_sequences = True, input_shape = (previsores.shape[1], 1)))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))
regressor.add(Dense(units = 1, activation = 'sigmoid'))
regressor.compile(optimizer = 'rmsprop', loss = 'mean_squared_error', metrics = ['mean_absolute_error'])
regressor.fit(previsores, qt_real, epochs = 100, batch_size = 48)

entradas = base[len(base) - len(base_teste) - 24:].values
entradas = np.delete(entradas, 0, 1)
entradas = normalizador.transform(entradas)

X_teste = []
for i in range(24, 114):
    X_teste.append(entradas[i-24:i, 0])
X_teste = np.array(X_teste)
X_teste = np.reshape(X_teste, (X_teste.shape[0], X_teste.shape[1], 1))

previsoes = regressor.predict(X_teste)
previsoes = normalizador.inverse_transform(previsoes)

previsoes.mean()
base_teste.mean()

#Criação do gráfico de previsão
plt.figure(figsize = (10, 5))
plt.plot(base_teste, color = 'red', label = 'quantidade total vendida (real)')
plt.plot(previsoes, color = 'blue', label = 'quantidade total vendida (previsto)')
plt.title('Previsão quantidade de comerciais leves totais vendidos')
plt.xlabel('Anos')
plt.ylabel('Quantidade de comerciais leves totais vendidos')
plt.show()