starts = int(input())
ends = int(input())
leap_years = []
while starts <= ends:
   def check(date):
      if date % 4 == 0 and date % 100 != 0 or date % 400 == 0:
         leap_years.append(date)
   check(starts)
   starts += 1
for x in leap_years:
   print(x)
print(f'bissextos: {len(leap_years)}')