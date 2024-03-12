#%%
import pandas as pd

class CsvProcessor: # Por convencao, a classe sempre comeca com uma letra maiuscula
    def __init__(self, file_path:str): # definicao do metodo construtor
        self.file_path = file_path # o self sao os parametros que ficam instanciados na classe. Sempre que a classe for chamada, esses metodos vem junto porque foram definidos no proprio construtor.
        self.df = None # aqui por exemplo, vai ser instanciado sempre um df, quando a classe for chamada.


    def load_csv(self):
        self.df = pd.read_csv(self.file_path)   
        return self.df
        

if __name__ == '__main__':
    csv_file = CsvProcessor('C:/Users/Thales/Documents/repos/public_knowledge_base/python/bootcamp_jornada_dados/aula11a12/src/data/pokemon.csv') 
    df = csv_file.load_csv()
    print(df)
        
    
# %%
