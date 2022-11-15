debit = int(input())
payment = int(input())
many_payments = 0
while debit != 0:
   many_payments += 1
   print(f'pagamento: {many_payments}')
   print(f'antes = {debit}')
   debit = debit - payment
   if debit < 0:
      debit = 0
   print(f'depois = {debit}')
   print('-----')