weekdays = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
day_bought = input()
days_to_ship = int(input())

when_bought = weekdays.index(day_bought)

if when_bought + days_to_ship >= len(weekdays):
    arrive = (when_bought + days_to_ship) - len(weekdays)
    print(f'sera entregue {weekdays[arrive]}')
else:
    arrive = when_bought + days_to_ship
    if arrive == when_bought:
        print('chega hoje!')
    else:
        print(f'sera entregue {weekdays[arrive]}')