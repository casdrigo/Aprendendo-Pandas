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

#%%
df_limpo['Fator Correção'] = [0]
#%%
dicionario_fatores = {
    'Piezometro' : 1.05,
    'Nivel': 1.00
}

df_limpo['fator_correcao'] = df_limpo['tipo_sensor'].map(dicionario_fatores)
df_limpo

#%%
df_real = df_limpo
df_real.to_csv('../data/exercicio/dump_barragem_telix4-leiturareal.csv')
#%%
import pandas as pd
df = pd.read_csv('../data/exercicio/dump_barragem_telix4-leiturareal.csv')
df
#%%
df['leitura_real'] = (df['leitura_mm']) * (df['fator_correcao'])
# %%
import numpy as np

#%%
condicao_PiezometroOk = (df['tipo_sensor'] == 'Piezometro') & (df['bateria_v'] >= 3.5)
condicao_nivelOk      = (df['tipo_sensor'] == 'Nivel') & (df['bateria_v'] >= 12.0)
df['alerta_bateria']  = np.where(condicao_nivelOk | condicao_PiezometroOk, 'OK', 'Trocar')  
df

#%%
valor_maximo = df.loc[df['id_sensor'] == 'NA-01', 'leitura_real'].max()
valor_maximo