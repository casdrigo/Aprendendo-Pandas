#%%
import pandas as pd
#%%

dump_barragem = pd.read_csv('../data/dump_barragem_telix.csv', sep =",")
df = pd.DataFrame(dump_barragem)
df

#%%
df.to_csv('../data/exercicio/dump_barragem_telix1.csv') #salvando 1 modificação


# %%

df[df.duplicated()]
# %%
df_sem_duplicatas = df.drop_duplicates()
df_sem_duplicatas
#%%
df_sem_duplicatas.to_csv('../data/exercicio/dump_barragem_telix2-semDuplicatas.csv')
# %%
