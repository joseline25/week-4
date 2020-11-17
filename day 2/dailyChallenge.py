# Ask a user for his birthdate (specify the format, for example: DD/MM/YYYY) and then

# Display him a little cake

import calendar

entree = input('Enter your age in the format DD/MM/YYYY : ')
age = 2020 - int(entree[6:])
long = list(str(age))
last = int(long[-1])

if last % 2 == 0:
    print('{}{}{}{}'.format(' '*4, '_'*5, 'i'*last, '_'*4))
else:
    print('{}{}{}{}'.format(' '*4, '_'*5, 'i'*last, '_'*5))

print('{}{}{}{}{}{}'.format(' '*3, '|', ' '*((last-1)//2), ':H:a:p:p:y:', ' '*((last - 1)//2), '|'))
if last % 2 == 0:
    print('{}{}{}{}{}{}{}'.format(' ', '_'*2, '|', '_'*(last + 9), '|', '_'*2, ' '))
    print('{}{}{}'.format('|', '^'*(last + 15), '|'))
else:
    print('{}{}{}{}{}{}{}'.format(' ', '_'*2, '|', '_'*(last + 10), '|', '_'*2, ' '))
    print('{}{}{}'.format('|', '^'*(last + 16), '|'))

print('{}{}{}{}{}'.format('|', ' '*((last-1)//2), ':B:i:r:t:h:d:a:y:', ' '*((last-1)//2), '|'))
if last % 2 == 0:
    print('{}{}{}'.format('|', ' '*(15 + last), '|'))
    print('{}'.format('~'*(17 + last)))
else:
    print('{}{}{}'.format('|', ' '*(16 + last), '|'))
    print('{}'.format('~'*(18 + last)))
