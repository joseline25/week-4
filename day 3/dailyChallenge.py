import string

x = list(string.ascii_lowercase)

y = list(string.ascii_uppercase)

message = input('Enter the message to encrypt : ')

tab = list(message)

cipher = ''

"""for i in tab:
    val = x[(x.index(i) + 3 ) % 26]
    cipher = cipher + val
print('The cesar encryption of {} is {}'.format(message, cipher))
"""
print('We are going to proceed to cesar encryption')
choice = int(input('Choose : 1 for left shift and 2 for right shift : '))

if choice == 1:
    for i in tab:
        if i.islower():
            val = x[(x.index(i) - 3) % 26]
            cipher = cipher + val
        else:
            val = y[(y.index(i) - 3) % 26]
            cipher = cipher + val
    print('The cesar encryption of {} is {}'.format(message, cipher))

if choice == 2:
    for i in tab:
        if i.islower():
            val = x[(x.index(i) + 3) % 26]
            cipher = cipher + val
        else:
            val = y[(y.index(i) + 3) % 26]
            cipher = cipher + val
    print('The cesar encryption of {} is {}'.format(message, cipher))

"""
Bonus :

To decrypt a cipher from left shift, use the right shift on the cipher and you will get the clear message

To decrypt a cipher from right shift, use the left shift on the cipher and you will get the clear message
"""
