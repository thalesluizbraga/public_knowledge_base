#%%
import datetime
import sqlalchemy
from tqdm import tqdm


# %%
def dates_to_list(dt_start, dt_stop):
    date_start = datetime.datetime.strptime(dt_start, '%Y-%m-%d')
    date_stop = datetime.datetime.strptime(dt_stop, '%Y-%m-%d')
    days = (date_stop - date_start).days
    dates = [(date_start + datetime.timedelta(i)).strftime('%Y-%m-%d') for i in range (days + 1)] 
    # Estou passando uma lista de datas pra variavel dates. Entao em vez de criar uma funçao 
    # com o metodo append pra jogar as datas na variavel eu ja crio a variavel direto, com o loop for
    # e tudo caindo na lista

    return dates

dates_to_list('2021-10-01','2021-10-01')


def backfill(query, engine, dt_start, dt_stop):
    dates = dates_to_list(dt_start, dt_stop)
    for d in tqdm(dates):
        process_date(query, d, engine)

def import_file(path):
    with open(path, 'r') as open_file:
        file = open_file.read()
    return file

def process_date(query, date, engine):
    delete = "delete from tb_book_players where dtRef = '{date}'"
    engine.execute(delete)
    query = query.format(date = date)    
    engine.execute(query)    

# %%
engine = sqlalchemy.create_engine('sqlite:///gc.db')

query = import_file('gc_query.sql')

dt_start = input('Entre com uma data de inicio:')
dt_stop = input('Entre com uma data final:')

backfill(query, engine, dt_start, dt_stop)


# %%




# %%

# %%
