values = []
total = 0
while True:
    donation = int(input())
    if donation > 0:
        values.append(donation)
    else:
        break
for x in values:
    total += x
media = total / len(values)
print(f'MEDIA: {media:.2f}')

for x in values:
    if x < media:
        print(x)
