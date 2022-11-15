starts = int(input())
ends = int(input())
prime_numbers = []

def isprime(num):
  for n in range(2, int(num ** 0.5) + 1):
    if num % n == 0:
      return False
  return True

while starts <= ends:
  if isprime(starts) == True:
    prime_numbers.append(starts)
  starts += 1

if starts != ends <= 5000:
  if len(prime_numbers) != 0 and prime_numbers[0] == 1:
    prime_numbers.pop(0)
  for x in prime_numbers:
    print(x)
  print(f'primos: {len(prime_numbers)}')