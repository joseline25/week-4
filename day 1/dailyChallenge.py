# Daily Challenge : Build Up A String

import random

"""phrase = input('Entrez un phrase de 10 caractères exactement')

if len(phrase)< 10:
    print('string not long enough')
elif len(phrase)>10:
    print('string too long')
else:
    print('{} and {}'.format(phrase[:1], phrase[9:10]))


cons = input('Enter a sentence')
for i in range(len(cons)+1):
    print(cons[:i]) """

sent = input('Enter a sentence')
b = ''.join(random.sample(sent,len(sent)))

print(b)
