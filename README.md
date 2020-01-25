# Vendas de veiculos pelas concessionárias - Comerciais leves
Conceito: Valor da produção de veículos comerciais leves no País. Refletem o desempenho das vendas das empresas associadas a(o): estoque e venda de veículos pelas concessionárias produção e vendas de veículos e congêneres produção e vendas de motociclos.<br/>
Fonte: Federação Nacional da Distribuição de Veículos Automotores<br/>
Link do dataset: http://dados.gov.br/dataset/7385-vendas-de-veiculos-pelas-concessionarias-comerciais-leves

## A ideia é tentar ver se existe alguma série temporal (com tendência e sazionalidade), a partir desses dados obtidos, e fazer previsões futuras.

**Gráfico dos dados originais**

![Figure_1](https://user-images.githubusercontent.com/48027825/72921975-fe254e80-3d2a-11ea-920e-a2a878171df5.png)

**Gráfico da tendência, sazonalidade e resíduo**

![Figure_2](https://user-images.githubusercontent.com/48027825/72921976-febde500-3d2a-11ea-9d99-5f0cea8aa155.png)

**Gráfico da série temporal, com diferenciação, para o teste de estacionariedade**

![Figure_1](https://user-images.githubusercontent.com/48027825/72922996-df27bc00-3d2c-11ea-8fea-93608a334ab1.png)

**Gráfico da importância dos períodos para previsões futuras**

![Figure_1](https://user-images.githubusercontent.com/48027825/72928353-9543d380-3d36-11ea-929f-5dd5ede4cc9c.png)

- Testes de confirmação de estacionariedade

**Dickey Fuller e KPSS**

Resultado do teste Dickey-Fuller:<br/>
Teste                      -3.289543<br/>
Valor p                     0.015352 (Rejeição da hipótese nula)<br/>
 de lags                    13.000000<br/>
 de observações             345.000000<br/>
Valores críticos (1%)      -3.449447<br/>
Valores críticos (5%)      -2.869954<br/>
Valores críticos (10%)     -2.571253<br/>

H0 = A série não é estacionária. <br/>
H1 = A série é estacionária.

Resultado com o teste KPSS<br/>
Status KPSS                                                        0.0232085<br/>
Valor p                                                                  0.1 (Adoção da hipótese nula)<br/>
 de lags                                                                 17<br/>
 de observações          
Valores críticos (10%)                                                 0.347<br/>
Valores críticos (5%)                                                  0.463<br/>
Valores críticos (2.5%)                                                0.574<br/>
Valores críticos (1%)                                                  0.739

H0 = A série é estacionária. <br/>
H1 = A série apresenta raiz unitária.

- Teste de  confirmação de tendência

**Teste de Mann-Kendall**

Resultado do Teste Mann-Kendall<br/>
Movimento Tendência     increasing<br/>
Há Tendência?                 True<br/>
Valor p                9.07964e-06<br/>
Teste normalizado          4.43801<br/>
Coeficiente Kendall        0.55489<br/>
Mand-Kendall Score           35857<br/>
Variância S            6.52752e+07<br/>
Sen Slope                  79.4129

H0 = As observações da série são independentes e identicamente distribuídas. (Não há tendência)<br/>
H1 = As observações da série possuem tendência monotônica no tempo. (Há tendência)

- Aqui estão a previsão da série temporal utilizando alguns métodos

**1) Holt Winters**

- Sem amortização da série temporal (Método aditivo)

![Figure_1](https://user-images.githubusercontent.com/48027825/72924275-683ff280-3d2f-11ea-8539-ef102d511866.png)
![Figure_2](https://user-images.githubusercontent.com/48027825/72924276-683ff280-3d2f-11ea-816b-f766502fb941.png)

- Com amortização da série temporal (Método multiplicativo)

![Figure_1](https://user-images.githubusercontent.com/48027825/72924734-311e1100-3d30-11ea-92b1-2d18c9a2d70c.png)
![Figure_2](https://user-images.githubusercontent.com/48027825/72924735-311e1100-3d30-11ea-81e1-468d55584f2c.png)

**2) Redes Neurais (MLP com KERAS)**

![Figure_1](https://user-images.githubusercontent.com/48027825/72929894-801c7400-3d39-11ea-98c8-8ae62c0a0ed3.png)

**3) AUTO Arima**

- Dados Originais (azul) x Dados Previsão (laranja)

![Figure_1](https://user-images.githubusercontent.com/48027825/72951107-0fdb1600-3d6c-11ea-93ec-d995b4914a57.png)
![Figure_2](https://user-images.githubusercontent.com/48027825/72951108-0fdb1600-3d6c-11ea-8b88-ebe8f07cc7b7.png)

**4) Rede Neurais (LSTM)**

- Dados Originais (vermelho) x Dados Previsão (azul)

![Figure_1](https://user-images.githubusercontent.com/48027825/73115345-7181b880-3f03-11ea-8413-38a49b1b2110.png)
