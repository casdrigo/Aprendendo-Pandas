#%%
import pandas as pd
#%%

dump_barragem = pd.read_csv('../data/dump_barragem_telix.csv', sep =",")
df = pd.DataFrame(dump_barragem)
df

#%%
df.to_csv('../data/exercicio/dump_barragem_telix1.csv') #salvando 1 modificação


# %%

df[df.duplicated()]     #mostra somente as duplicatas
# %%
df_sem_duplicatas = df.drop_duplicates()
df_sem_duplicatas
#%%
df_sem_duplicatas.to_csv('../data/exercicio/dump_barragem_telix2-semDuplicatas.csv')
# %%
df_sem_duplicatas = df_sem_duplicatas[df_sem_duplicatas.status != 'OFFLINE']
#acima estou dizendo que quero que a dfSemDuplicatas seja igual a mesma porém com a coluna
#status sendo diferente de offline

df_sem_duplicatas
# %%
df_limpo = df_sem_duplicatas.dropna(subset=['leitura_mm'])
df_limpo
# %%
df_limpo.to_csv('../data/exercicio/dump_barragem_telix3-limpoSemLeiturasNulas.csv')

#%%

df_limpo = pd.read_csv('../data/exercicio/dump_barragem_telix3-limpoSemLeiturasNulas.csv')
df_limpo