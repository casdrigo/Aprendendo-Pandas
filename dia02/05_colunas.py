#%%
from os import sep
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep =';')
df
# %%
df.shape
# %%
df.info(memory_usage='deep')
# %%
df.dtypes
# %%
renamed_columns = {
                    "QtdePontos":"qtPontos",
                    "DescSistemaOrigem":"SistemaOrigem"
                    
                    }
# df = df.rename(columns =renamed_columns)
df.rename(columns=renamed_columns, inplace=True)    #Mesma coisa que o de cima

df
# %%
# df[["IdCliente", "qtPontos"]]     #só aceita um objeto, portanto é bom passar uma lista

colunas= ["IdCliente", "qtPontos"]  #mesma coisa que o de cima
df[colunas] 
# %%
df[["IdCliente","IdTransacao","qtPontos"]].head()
# %%
colunas = list(df.columns)
colunas.sort()
colunas