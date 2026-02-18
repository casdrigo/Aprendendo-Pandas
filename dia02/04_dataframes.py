#%%
import pandas as pd

df_clientes = pd.read_csv('../data/clientes.csv', sep = ";")
df_clientes
# %%
df_clientes.head(n=10)  #Por padrão exibe apenas as 5 primeiras linhas
                        #serve para big data, só para ver se foi importado sem
                        #exigir tanta memoria do pc
# %%
df_clientes.tail()      #Mesma coisa que o head, porém aqui ele mostra os ultimos
                        #padrão tambem é 5, mas pode ser mudado com "n="

# %%
df_clientes.sample(10)  #Significa amostra, serve para ter valores aleatorios
                        #É para se certificar que ta tudo ai, em pontos aleatorios do
                        #arquivo

# %%
df_clientes.shape
# %%
df_clientes.columns
# %%
df_clientes.index
# %%
df_clientes.info(memory_usage='deep')
# %%
df_clientes.dtypes
# %%
