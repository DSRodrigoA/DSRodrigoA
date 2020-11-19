# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 09:51:58 2020

@author: Homemachine
"""
# Definição das bibliotecas utilizadas

import numpy as np
import pandas as pd
import plotly
import plotly.graph_objects as go
import plotly.offline as pyoff
import matplotlib.pyplot as plt
import plotly.offline as pyoff
import plotly.graph_objs as go
from datetime import datetime, timedelta
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from platform import python_version
python_version()


pd.set_option('display.precision', 3)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
pd.set_option('display.min_rows', 40)
pd.set_option('display.date_dayfirst',True)

#pd.get_option()
#pd.reset_option('display.max_rows')

#__________________________________________________________________

# Leitura do Dataset

dataset = pd.read_csv('D:/Google Drive/portfolioDS/mbasket_analytics/data/retail.csv', header = 0, encoding = 'unicode_escape')


# Exploração do Raw Dataset

dataset

dataset.columns

dataset.head(5)

dataset.shape

dataset.describe()

dataset.info()

dataset
from platform import python_version
python_version()
#.size()

# dataset.loc[dataset.NomeProduto.str.contains('Br', regex=True)]


dataset[['Pais','NumeroFatura']].nunique()

#df.rename(columns={'ConvertedComp': 'SalaryUSD'}, inplace=True)

dataset.loc(['NomeProduto'] == *?*)

#Numero de notas por Pais

dataset['Pais'].unique()

dataset[['Pais','NumeroFatura']].groupby(['Pais']).nunique()

(dataset[['Pais','NumeroFatura']].groupby('Pais').nunique()).plot(kind='bar',figsize=(10,7))



dataset.dtypes

dataset['Quantidade'].nlargest(10)
dataset['ValorUnitario'].nlargest(10)

dataset.sort_values(by=['Quantidade', 'ValorUnitario'], ascending=[True, False])


#Função head em modo 'Transpose" para visualizar as colunas como linhas

dataset.head(5).T

# Trabalhando com Datas

##Convertendo a coluna DataVenda para DateTime
dataset.DataVenda = pd.to_datetime(dataset.DataVenda,dayfirst='True', yearfirst='False')

print('Data Mínima:', dataset['DataVenda'].min())
print('Data Máxima:', dataset['DataVenda'].max())
print('Data Máxima:', dataset['data'].max())

dataset['d_mes'] = dataset['DataVenda'].map(lambda date: date.month)
dataset['d_dia'] = dataset['DataVenda'].map(lambda date: date.day)

#dataset["data"] = dataset["DataVenda"].dt.strftime("%d/%m/%Y")
#dataset["hora"] = dataset["DataVenda"].dt.strftime("%H:%M")
#dataset = dataset.drop(columns=['data'])
#dataset["data"] = dataset["DataVenda"].dt.date

dataset


# Contar valores 'Nulos'

dataset.isnull().sum()

print(dataset.isnull().sum() / len(dataset) * 100)





# Limpeza do Dataset
## Criação da coluna Total

dataset['Faturamento'] = dataset['Quantidade'] * dataset['ValorUnitario']

dataset.describe()


dataset.loc[(dataset['Quantidade'] <= 0)]

dataset.loc[(dataset['ValorUnitario'] <= 0)]

dataset.loc[(dataset['Faturamento'] <= 0)]

cleaner_total = dataset.loc[(dataset['Faturamento'] <= 0)]

cleaner_total


ds1 = dataset.drop(cleaner_total.index)

ds1.loc[(ds1['Faturamento'] <= 0)]

ds1.describe()

ds1 = ds1.drop(columns='CodigoProduto')

ds1


#Tratando a coluna Quantidade devido Outliers

ds1.sort_values(['Quantidade'], ascending = False)

ds1['Quantidade'].mean()

print((ds1.loc[ds1['Quantidade'] > 1000]))

cleaner_quantidade = (ds1.loc[ds1['Quantidade'] > 1000])

cleaner_quantidade

ds1 = ds1.drop(cleaner_quantidade.index)

ds1.describe()



# Faturamento Mensal
ds1_faturamento = ds1.groupby(['d_mes']).agg({'Faturamento': sum}).reset_index()

ds1_faturamento



## Plot do Faturamento Mensal
plot_data = [go.Scatter(x = ds1_faturamento['d_mes'], 
                        y = ds1_faturamento['Faturamento'],)]

# Layout
plot_layout = go.Layout(xaxis = {"type": "category"}, 
                        title = 'Faturamento Mensal')

# Plot da figura
fig = go.Figure(data = plot_data, layout = plot_layout)

pyoff.iplot(fig)






## Convertendo as colunas e valores numéricos para categóricos, tipo 'string'
---
dataset['NumeroFatura'] = dataset['NumeroFatura'].astype('str')

dataset['IdCliente'] = dataset['IdCliente'].astype('str')

dataset.dtypes
---
# Exploração do Dataset limpo


# Testes estatísticos - Itensets mais frequentes e menos frequentes

# Criação e transformação do Dataframe Pivot para Apriori

ds1_pivot = ds1.pivot_table(index = ['NumeroFatura'], columns = ['NomeProduto'], values = 'Quantidade')

ds1_pivot = ds1_pivot.fillna(0)

ds1_pivot = ds1_pivot.set_index('NumeroFatura')



def my_encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
    
cesta1 = ds1_pivot.applymap(my_encode_units)

cesta1.head(2)








# Definição dos parâmetros

# Aplicação do Algoritimo Apriori e Association Rules 

itemset1 = apriori(cesta1, min_support=0.02, use_colnames=True)

itemset1



# Criação da lista de Regras de Associação com o método association_rules

regras = association_rules(itemset1, metric="confidence", min_threshold=0.5)


regras



# Possíveis Filtros 
regras[regras['antecedents'] == {'ALARM CLOCK BAKELIKE PINK'}]

## Criar uma Feature para aumentar o alcance dos filtros
at least 2 antecedents
a confidence > 0.75
a lift score > 1.2
We could compute the antecedent length as follows:

rules["antecedent_len"] = rules["antecedents"].apply(lambda x: len(x))
rules


regras[ (regras['antecedent_len'] >= 2) &
       (regras['confidence'] > 0.75) &
       (regras['lift'] > 1.2) ]

regras[(regras['confidence'] < 0.6) & 
       (regras['support'] < 0.03) ]  



# Interpretação dos resultados

# Plot dos Resultados

# Exportação dos Outputs Datasets para integração do PowerBI

# Possibilidades de Automatizar processos

