n1 = float(input())
n2 = float(input())
m = (n1 + n2) / 2

if m >= 6:
    print('aprovado')

if m < 6:
    if ((n1 + 10) / 2) >= 6:
        print('talvez com a sub')
    else:
        print('reprovado')