import pandas as pd
import matplotlib.pylab as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import RFE

base = pd.read_csv('bcdata.sgs.7385.csv', delimiter = ';', header = 0, parse_dates = ['data'],
                index_col = ['data'], squeeze = True)

#Aplica a diferenciação nos dados, e mostra o resultado e gráfico
differenced = base.diff(12)
differenced.head(n = 13)
differenced.plot()

#Remove os valores Nan, e plota o grafico sem os dados NaN
differenced = differenced[12:]
differenced.head(n = 13)
differenced.plot()

#Faz uma nova série temporal(12 meses) para prever a observação corrente
dataframe = pd.DataFrame()
for i in range(12, 0, -1):
    dataframe['t-'+ str(i)] = differenced.shift(i)
    dataframe['t'] = differenced.values
print(dataframe.head(13))
dataframe = dataframe[13:]

#Separação das variáveis independente e dependente para o Random forest
array = dataframe.values
X = array[:, 0:-1]
y = array[:, -1]

#Faz o uso do Random Forest para mostra quais períodos são mais importantes
modelo = RandomForestRegressor(n_estimators = 500, random_state = 1)
modelo.fit(X, y)

#Mostra a importância dos períodos, a segunda é a mais importante
print(modelo.feature_importances_)

#Mostra um gráfico de barra com a importância dos períodos para fazer a previsão
nomes = dataframe.columns.values[0:-1]
barras = [i for i in range (len(nomes))]
plt.figure(figsize = (10, 5))
plt.bar(barras, modelo.feature_importances_)
plt.xticks(barras, nomes)
plt.show()

#O RFE irá selecionar os (4) melhores períodos/atributos
rfe = RFE(RandomForestRegressor(n_estimators = 500, random_state = 1), 4)
fit = rfe.fit(X, y)

#Lista os atributos mais importantes
for i in range(len(fit.support_)):
    if fit.support_[i]:
        print(nomes[i])

'''Ou seja o gráfico mostrou que não é necessário usar todos os dados da série temporal
para prever as previsões futuras. Ou seja, nessa base de dados, basta usar os dados de
4 anos atrás para previsões futuras. Com isso diminui o tempo de processamento da máquina,
tem menos dados para tratar e menos código para fazer.'''