num = int(input())
counter = 1
while counter <= 10:
    if 0 <= num <= 10:
        last = num * counter
        print(f'{num} x {counter} = {last}')
        counter += 1