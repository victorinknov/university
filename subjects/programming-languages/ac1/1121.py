import math

price = float(input())
quantity = int(input())

value = price * quantity
print(f'%.2f' %value)

fixed_discount = value * 0.1
amount_discount = quantity * (value * 0.01)
final_value = value - (fixed_discount + amount_discount)
print(f'%.2f' %final_value)