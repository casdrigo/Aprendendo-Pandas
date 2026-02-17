#%%
import pandas as pd
#%%

dump_barragem = pd.read_csv('../data/dump_barragem_telix.csv', sep =",")
df = pd.DataFrame(dump_barragem)
df.to_csv('../data/exercicio/dump_barragem_telix1.csv') #salvando 1 modificação


# %%
