num = int(input())

if num % 2 == 0:
    even = num + 2
    odd = num - 1
else:
    even = num + 1
    odd = num - 2

print(f'{odd} {even}')