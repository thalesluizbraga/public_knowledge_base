#%% 
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():    
    total = 0

    while True:
        order = input('Order: ').capitalize()

        try:
                
            for item in menu:
                if order == item:
                    total += menu[item]
                    print(f'Total: ${total: .2f}')
            
        except EOFError:
            break
    # Aqui o try/except ficar dentro do loop porque eu quero alimentar um counter que pare so quando a exceçao acontecer

if __name__ == '__main__':
    main()

# %%
