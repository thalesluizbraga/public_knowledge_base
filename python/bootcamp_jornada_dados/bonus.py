# Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas


def get_name():
    while True:
        try:
            name = input('Insert your name: ').strip().capitalize()
            if name:
                return name
            elif len(name) == 0:
                return 'Name cannot be empty.'
        except ValueError:
            return 'Invalid name. Please enter a valid name'

def get_salary():
    while True:
        try:
            salary = float(input('Insert your salary: '))
            if salary > 0:
                return salary
            else:
                return 'Salary must be greater than zero.'
        except ValueError:
            return 'Invalid salary. Please enter a valid number.'

def calculate_bonus(salary: float, bonus: dict):
    if 0 < salary <= 2000:
        return salary * (1 + bonus['faixa_1'])
    elif 2000 < salary <= 5000:
        return  salary * (1 + bonus['faixa_2'])
    elif 5000 < salary <= 10000:
        return salary * (1 + bonus['faixa_3'])
    else:
        return salary * (1 + bonus['faixa_4'])        

if __name__ == '__main__':
    bonus = {'faixa_1': 0.5, 'faixa_2': 1, 'faixa_3': 1.5, 'faixa_4': 2}
    name = get_name()
    salary = get_salary()
    bonus_amount = calculate_bonus(salary, bonus)
    print(f'{name}, your bonus amount is: ${bonus_amount}')
