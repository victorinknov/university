given_number = int(input())
pseudo_alphabet = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = list(pseudo_alphabet)
str = ''
counter = 1
 
while counter <= given_number:
   print(str.ljust(counter, alphabet[counter]))
   counter += 1