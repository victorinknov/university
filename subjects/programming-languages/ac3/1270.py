first_number = int(input())
second_number = int(input())

if second_number < first_number:
    print('Nenhuma tabuada no intervalo!')
else:
    while first_number <= second_number:
        counter = 1
        while counter <= 10:
            print(f'{first_number} x {counter} = {first_number * counter}')
            counter += 1
        print('----------')
        first_number += 1
