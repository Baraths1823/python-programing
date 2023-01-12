a=input('enter a word: ')
print('Vowels: ')
for i in a:
   if i in "AEIOUaeiou":
      print(i, end=' ')
print('\nConsonants: ')
for i in a:
   if i not in "AEIOUaeiou ":
      print(i, end=' ')
