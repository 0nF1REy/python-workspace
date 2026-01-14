"""
# Análise de Vendas de Supermercado

## 1. Importação de Dados
"""

import numpy as np  # álgebra linear
import pandas as pd  # processamento de dados, I/O de arquivos CSV
import seaborn as sns
import matplotlib.pyplot as plt
import os

DATA_PATH = os.path.join("..", "..", "data", "external", "supermarket_sales.csv")

sales = pd.read_csv(DATA_PATH)

sales.head()

sales.info()

"""Por inspeção, o tipo de dados 'Date' é um objeto, precisamos convertê-lo para datetime

## 2. Tratamento de Datas e Horários
"""

sales['date'] = pd.to_datetime(sales['Date'])

sales['date'].dtype

type(sales['date'])

sales['date'] = pd.to_datetime(sales['date'])

sales['day'] = (sales['date']).dt.day
sales['month'] = (sales['date']).dt.month
sales['year'] = (sales['date']).dt.year

sales['Time'] = pd.to_datetime(sales['Time'])

sales['Hour'] = (sales['Time']).dt.hour # tipo(sales['Time'])

"""Vamos ver as horas únicas de vendas neste conjunto de dados"""

sales['Hour'].nunique()  # nos dá o número de horas únicas

sales['Hour'].unique()

"""## 3. Estatísticas Descritivas e Categorias"""

sales.describe()

""" Vamos encontrar o número de valores únicos em colunas com tipo de dados objeto"""

categorical_columns = [cname for cname in sales.columns if sales[cname].dtype == "object"]

categorical_columns

print("Valores únicos em Filial: {0}".format(len(sales['Branch'].unique().tolist())))
print("Valores únicos em Cidade: {0}".format(len(sales['City'].unique().tolist())))
print("Valores únicos em Tipo de Cliente: {0}".format(len(sales['Customer type'].unique().tolist())))
print("Valores únicos em Gênero: {0}".format(len(sales['Gender'].unique().tolist())))
print("Valores únicos em Linha de Produto: {0}".format(len(sales['Product line'].unique().tolist())))
print("Valores únicos em Forma de Pagamento: {0}".format(len(sales['Payment'].unique().tolist())))

"""## 4. Análise por Gênero e Filial"""

sns.set(style="darkgrid") # estilo do fundo do gráfico com grade
genderCount = sns.countplot(x="Gender", data=sales).set_title("Contagem por Gênero")

sns.boxplot(x="Branch", y="Rating", data=sales).set_title("Avaliações por Filial")

"""A filial B tem a menor avaliação entre todas as filiais

## 5. Análise de Vendas Temporais

*Vendas por hora na empresa* A maioria dos itens foi vendida por volta das 14:00 horas de tempo local
"""

genderCount = sns.lineplot(x="Hour", y="Quantity", data=sales).set_title("Vendas de Produtos por Hora")

"""Abaixo podemos ver como a quantidade de vendas de cada filial se parece por hora de forma mensal"""

genderCount  = sns.relplot(x="Hour",  y = 'Quantity', col= 'month' , row= 'Branch', kind="line", hue="Gender", style="Gender", data =sales)

""" Abaixo podemos ver as vendas de cada filial por hora de forma mensal"""

genderCount  = sns.relplot(x="Hour",  y = 'Total', col= 'month' , row= 'Branch', estimator = None, kind="line", data =sales)

sales['Rating'].unique()

ageDisSpend = sns.lineplot(x="Total", y = "Rating", data =sales)

"""## 6. Análise de Produtos

Vamos examinar o desempenho de vários produtos.
"""

sns.boxenplot(y = 'Product line', x = 'Quantity', data=sales )

"""A partir do visual acima, Saúde e Beleza, Acessórios eletrônicos, Casa e estilo de vida, Esportes e viagens têm vendas de quantidade média melhor do que alimentos e bebidas, bem como acessórios de moda."""

sns.countplot(y = 'Product line', data=sales, order = sales['Product line'].value_counts().index )

"""A imagem acima mostra o tipo de item de linha de produto mais vendido no conjunto de dados fornecido. Acessórios de Moda é o mais alto, enquanto Saúde e Beleza é o mais baixo"""

sns.boxenplot(y = 'Product line', x = 'Total', data=sales )

sns.stripplot(y = 'Product line', x = 'Total', hue = 'Gender', data=sales )

sns.relplot(y = 'Product line', x = 'gross income', data=sales )

sns.boxenplot(y = 'Product line', x = 'Rating', data=sales )

"""Alimentos e Bebidas têm a avaliação média mais alta, enquanto Esportes e Viagens têm a mais baixa

Vamos ver quando os clientes compram certos produtos nas várias filiais.
"""

productCount  = sns.relplot(x="Hour",  y = 'Quantity', col= 'Product line' , row= 'Branch', estimator = None, kind="line", data =sales)

"""Pelos gráficos acima, podemos ver que as vendas de alimentos e bebidas geralmente são altas em todas as três filiais à noite, especialmente por volta das 19:00

## 7. Canal de Pagamento

Vamos ver como os clientes fazem pagamento neste negócio
"""

sns.countplot(x="Payment", data=sales).set_title("Canal de Pagamento")

"""A maioria dos clientes paga através de Carteira Eletrônica e Pagamento em Dinheiro, enquanto menos de 40 por cento deles pagam com cartão de crédito. Gostaríamos também de ver esta distribuição de tipo de pagamento em todas as filiais"""

sns.countplot(x="Payment", hue="Branch", data=sales).set_title("Canal de Pagamento por Filial")

"""## 8. Análise de Clientes

Por inspeção, existem dois tipos de clientes. Membros e Normais. Vamos ver quantos existem e onde estão
"""

sales['Customer type'].nunique()

sns.countplot(x="Customer type", data=sales).set_title("Tipo de Cliente")

sns.countplot(x="Customer type", hue="Branch", data=sales).set_title("Tipo de Cliente por Filial")

"""## 9. O tipo de cliente influencia as vendas?"""

sales.groupby(['Customer type']).agg({'Total': 'sum'})

sns.barplot(x="Customer type", y="Total", estimator = sum, data=sales)

"""O tipo de cliente influencia a avaliação do cliente? Vamos descobrir"""

sns.swarmplot(x="Customer type", y="Rating", hue="City", data=sales).set_title("Tipo de Cliente")

"""Com o uso de buscas no Google, foi possível obter a latitude e a longitude de cada cidade.

## 10. Mapeamento e Correlações
"""

long = {"Yangon": 16.8661, "Naypyitaw": 19.7633, "Mandalay": 21.9588 }
lat = {"Yangon": 96.1951, "Naypyitaw": 96.0785, "Mandalay": 96.0891 }
for set in sales:
    sales['long'] = sales['City'].map(long)
    sales['lat'] = sales['City'].map(lat)

sns.scatterplot(x="long",  y = "lat",size = "Total", data =sales, legend = "brief").set_title("Tipo de Cliente")

sns.relplot(x="Total",  y = "Quantity", data =sales)