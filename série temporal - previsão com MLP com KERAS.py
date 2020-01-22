import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#Função para a preparação de dados para o modelo MLP
def preparacao_dados(data, lags = 1):
    X, y = [], []
    for row in range(len(data) - lags - 1):
        a = data[row:(row + lags), 0]
        X.append(a)
        y.append(data[row + lags, 0])
    return np.array(X), np.array(y)

base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';', parse_dates = True, index_col = 0)
data = base.values
np.random.seed(3)

#Conversão dos números para o MLP Keras
data = data.astype('float32')

#Separação dos dados em 75/25
treino = data[0:270, :]
teste = data[270:, :]

lags = 1
X_treino, y_treino = preparacao_dados(treino, lags)
X_teste, y_teste = preparacao_dados(teste, lags)
y_verdade = y_teste

#Geração do gráfico com os dados originais e os dados com lags
plt.figure(figsize = (10, 5))
plt.plot(y_teste, label = 'Dados Originais | y ou t+1', color = 'blue')
plt.plot(X_teste, label = 'Dados Passados | X ou t', color = 'orange')
plt.legend(loc = 'upper right')
plt.title('Dados passado de um Período')
plt.show()

#Criação do MLP
mlp = Sequential()
mlp.add(Dense(3, input_dim = lags, activation = 'relu'))
mlp.add(Dense(1))
mlp.compile(loss = 'mean_squared_error', optimizer = 'adam')
mlp.fit(X_treino, y_treino, epochs = 200, batch_size = 2, verbose = 2)

#Avaliação da performance do modelo criado
treino_score = mlp.evaluate(X_treino, y_treino, verbose = 0)
print(f'Pontuação de Treino: {round(treino_score, 2)} MSE ({round(math.sqrt(treino_score), 2)} RMSE)')
teste_score = mlp.evaluate(X_teste, y_teste, verbose = 0)
print(f'Pontuação de Teste: {round(teste_score, 2)} MSE ({round(math.sqrt(teste_score), 2)} RMSE)')

predicao_treino = mlp.predict(X_treino)
predicao_teste = mlp.predict(X_teste)

predicao_treino_plot = np.empty_like(data)
predicao_treino_plot[:, :] = np.nan
predicao_treino_plot[lags: len(predicao_treino) + lags, :] = predicao_treino

predicao_teste_plot = np.empty_like(data)
predicao_teste_plot[:, :] = np.nan
predicao_teste_plot[len(predicao_treino) + (lags * 2) + 1: len(data) - 1, :] = predicao_teste

plt.figure(figsize = (10, 5))
plt.plot(data, label = 'Observado', color = 'red')
plt.plot(predicao_treino_plot, label = 'Previsão para os dados de treino', color = 'orange', alpha = 0.05)
plt.plot(predicao_teste_plot, label = 'Previsão para os dados de teste', color = 'black')
plt.legend(loc = 'best')
plt.title('Previsão com Rede Neural Artificial (MLP)')
plt.show()

''' Como observado no gráfico, os dados dados de treinamento e teste ficaram superajustado,
podendo acarretar num problema de overfitting. Assim mostra que essa rede neural, nesses ajustes,
não serve para fazer um previsão futura confiável. '''