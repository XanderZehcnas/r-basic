# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:46:04 2021

@author: Rhiznab
"""

# Data Frames

import pandas as pd

df = pd.read_csv("D:\\Desarrollo\\MyLearning\\R\\data\\medals.csv") # Fichero o URL
print(df.head(8))

# acceder a posiciones determinadas

print(df.loc[[1]]) # Index name
print(df.iloc[[0]]) # Index number

df[12:20] # Un conjunto
df[10:95:5] # De la 10 a la 95 de 5 en 5

# df.Density no va
print(df.Year.mean())
print(df.Year.describe())
print(df.describe())


df2 = pd.read_table("D:\\Desarrollo\\MyLearning\\R\\data\\medals.csv",delimiter=",") # Fichero o URL
print(df2.head())


# Crear DF

import numpy as np
df = pd.DataFrame({
    'A': np.random.rand(10),
    'B': np.random.rand(10),
    'C': np.random.rand(10)
})
print(df.mean())
print(df.mean(axis='columns'))

df2 = pd.DataFrame({
    'key' : ['A','B','C','A','B','C'],
    'values': range(6)
    },columns = ['key','values'])

print(df2)

print(df2.groupby('key').mean())

# Manipulación de Dataframes - aggregate

df = pd.DataFrame({
        'key' : ['A','B','C','A','B','C'],
        'value1' : range(6),
        'value2' : np.random.randint(0,100,6)
    })
print(df)

print(df.groupby('key').aggregate(['min',np.median,np.mean,max]))

print(df.groupby('key').aggregate({
    'value1' : [min,np.mean],
    'value2': max
    }))

## Filter
print(df.groupby('key').std())

def filter_func(x):
    return x['value2'].std()>20

print("Mostrnado un display de datos y opciones:")
display(df,df.groupby('key').std(),df.groupby('key').filter(filter_func))

## Transform
print(df.groupby('key').transform(lambda x: x - x.mean()))

## Apply
def norm_by_col2(x):
    x['value1'] /= x['value2'].sum()
    return x
print(df.groupby('key').apply(norm_by_col2))

## División de datos por columnas

L = [0,1,0,1,2,0]
print(df.groupby(L).sum()) # String o vector de valores sirve para agrupar.

print ("MAPPING.............")
df2 = df.set_index('key')
print (df2)
mapping = {
    'A':'vowel',
    'B':'consonant',
    'C':'consonant'
    }
print(df2.groupby(mapping).sum())

print(df2.groupby(str.lower).mean())

print(df2.groupby([str.lower,mapping]).mean())

print("Gráficos desde data frames y exportación")

years = [year for year in range(1900,2020)]
deads = [round(y+np.random.uniform(0,100) - 1850) for y in years]
df = pd.DataFrame({
    'year': years,
    'deads': deads
    })
print(df.head())
my_plot = df.plot(x="year",y="deads",figsize=(10,8), kind="scatter")
my_fig= my_plot.get_figure()
my_fig.savefig("D:\\Desarrollo\\MyLearning\\R\\data\\df_plot.png")
