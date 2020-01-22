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
