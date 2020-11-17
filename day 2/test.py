# Exercice 1
list1 = [5, 10, 15, 20, 25, 50, 20]
print(list1.index(20))

list1[list1.index(20)] = 200

print(list1)

# Exercice 2

nombre = int(input('Entrez un nombre : '))
for i in range(1, 13):
    val = nombre * i
    print('{} * {} = {}'.format(nombre, i, val))
# Exercice 3
# Unpack the following tuple into 4 variables

aTuple = (10, 20, 30, 40)
a, b, c, d = aTuple
print(a)
print(b)
print(c)
print(d)
