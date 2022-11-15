all_donations = []
total_amount = 0
while True:
    donation = float(input())
    if donation != -1:
        all_donations.append(donation)
    else:
        break

for x in all_donations:
    total_amount += x

print(f'VC$ {total_amount:.2f}')
print(f'R$ {(total_amount * 2.5):.2f}')