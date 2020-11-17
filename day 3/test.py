my_dict  = {
    'nom' : 'Youego',
    'prenom' : 'Joseline',
    'age' : 25,
    'genre' : 'feminin'
}

print(my_dict['age'])

etudiant = {
    'nom': 'joseline',
    'age': 27,
    'notes': [19, 18, 20],
    'enfant': {
        'nom': 'elsa',
        'age': 3
    }
}
print(etudiant['nom'])
print(etudiant['notes'][1])
print(etudiant['enfant']['age'])

personne = {
            'nom' : 'jojo', 'age' : 27}

cour = {
    'titre': 'Python',
    'duree': 3
}

travail = {
    'intitulé': 'developeur',
    'lieu': 'bastos'
}
liste = [personne, cour , travail]

print(liste[1]['duree'])

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}

del sampleDict['name']

del sampleDict['salary']

print(sampleDict)

print([i for i in range(0, 101) if i % 3 == 0])

for letter in 'Leonardo':
    if letter == 'a':
        continue
    print(letter, end='')
