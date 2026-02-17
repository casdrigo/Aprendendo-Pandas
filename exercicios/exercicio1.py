#%%
import pandas as pd
#%%

dump_barragem = pd.read_csv('../data/dump_barragem_telix.csv', sep =",")
df = pd.DataFrame(dump_barragem)
df

#%%
df.to_csv('../data/exercicio/dump_barragem_telix1.csv') #salvando 1 modificação


# %%

df_sem_duplicatas = pd.DataFrame(df).drop_duplicates(keep=False)

df_sem_duplicatas