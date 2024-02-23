
def calculate_bonus(name, salary):

    try:
        if not isinstance(name, str):
            raise ValueError
        if not isinstance(salary, float):        
            raise ValueError

        for i in bonus.keys(): 
            if 0 < salary <= 2000:
                return salary * (1 + bonus['faixa_1'])
            elif 2000 < salary <= 5000:
                return  salary * (1 + bonus['faixa_2'])
            elif 5000 < salary <= 10000:
                return salary * (1 + bonus['faixa_3'])
            else:
                return salary * (1 + bonus['faixa_4'])
    except: 
        return ValueError



if __name__ == '__main__':
    name = (input('Insert your name: ')).capitalize()
    salary = float(input('Insert your salary: '))
    bonus = {'faixa_1' : 0.5,
             'faixa_2': 1,
             'faixa_3': 1.5,
             'faixa_4': 2  }
    
    print(calculate_bonus(name, salary))




# Colocar try and excepts para os tipos dos dados
    