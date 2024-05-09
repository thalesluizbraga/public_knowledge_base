#%%
import pandas as pd

# %%

data_familia = {'nome':['thales_luiz', 'thaian_luiz', 'maria_lais'],
            'idade':[29,27,26]}

df_familia = pd.DataFrame(data_familia)


# Usandoa  funcao get_first dentro do apply
def get_first(name):
    return name.split('_')[0]

df_familia['primeiro_nome'] = df_familia['nome'].apply(get_first)
df_familia


# %%

dict_rfv = {'nome':['thales', 'thaian', 'maria lais'],
          'recencia':[10,12,16],
          'frequencia':[10,20,14],
          'valor':[1000,2000,1500]}
df_rfv = pd.DataFrame(dict_rfv)

def rfv(row):
    nota = 0

    if row['recencia'] <= 10:
        nota += 10
    elif 10 < row['recencia'] >= 15:
        nota += 15
    elif 15 < row['recencia'] >= 20:
        nota += 20
    
    if row['frequencia'] <= 10:
        nota += 10
    elif 10 < row['frequencia'] >= 15:
        nota += 15
    elif 15 < row['frequencia'] >= 20:
        nota += 20
    
    if row['valor'] <= 1000:
        nota += 10
    elif 1000 < row['recencia'] >= 1500:
        nota += 15
    elif 1500 < row['recencia'] >= 2000:
        nota += 20
    
    return nota


df_rfv['rfv'] = df_rfv.apply(rfv, axis=1)
df_rfv.sort_values('rfv', ascending=False)

# %%
