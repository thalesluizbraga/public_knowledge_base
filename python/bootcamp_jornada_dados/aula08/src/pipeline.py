#%%
import os
import pandas as pd

def extract_json(path: str) -> list: 
    df_list = []
    for file in os.listdir(path):
        if file.endswith('.json'):
            df = pd.read_json(os.path.join(path, file))
            df_list.append(df)
    return df_list


def concat_json(df_list: list) -> pd.DataFrame:
    df = pd.concat(df_list)
    return df

def calculate_total_sales_col(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']
    return df

def load_df(df: pd.DataFrame, path_output: str ,format_output: list):
    for formato in format_output:
        if formato == 'csv':
            print('Csv file saved successfully.')
            return df.to_csv(f'{path_output}data.csv', index=False)
            
        if formato == 'parquet':
            print('Parquet file saved successfully.')
            return df.to_parquet(f'{path_output}data.parquet', index=False)
            

if __name__ == '__main__':
    path = 'C:/Users/JHS/Documents/repos/public_knwoledge_base/python/bootcamp_jornada_dados/aula08/data'
    path_output = 'C:/Users/JHS/Documents/repos/public_knwoledge_base/python/bootcamp_jornada_dados/aula08/data/'
    df_list = extract_json(path)
    df = concat_json(df_list)
    df = calculate_total_sales_col(df)
    print(load_df(df, path_output, ['parquet'] ))
    
# %%
