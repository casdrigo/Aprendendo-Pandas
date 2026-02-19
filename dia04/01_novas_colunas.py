#%%
import pandas as pd
df = pd.read_csv("../data/clientes.csv", sep = ";")
df.head()

#%%
df["pontos_100"] = df['qtdePontos'] + 100
df
#%%
df.head()

