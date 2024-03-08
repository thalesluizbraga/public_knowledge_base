#%%

# with open read 
# passar para dicionario
# passar tabulate par formatar o dicionario como tabulacao


import sys

def get_arg():

    if len(sys.argv) > 2:
        return 'Too many arguments.'
    elif len(sys.argv) < 2:
        return 'Too few arguments.'
    elif not sys.argv[1].endswith('.csv'):
        return 'Not a CSV file.'
    else:   
        return sys.argv[1]
    
def read_csv():



if __name__ == '__main__':
    arg = get_arg()
    
    
# %%
import csv
from tabulate import tabulate

with open('sicilian.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)


# %%
# conseguir fazer em pandas, pra depois entender o codigo fonte
# da funcao read_csv e replicar no exercicio

import pandas as pd
from tabulate import tabulate
df = pd.read_csv('regular.csv')
df_dict = df.to_dict()

#print(tabulate(df_dict, headers='keys', tablefmt='grid'))
#print(tabulate(df, headers='keys', tablefmt='grid'))


# %%
