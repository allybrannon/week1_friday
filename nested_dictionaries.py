ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
#exercise 1: write python expression that gets the email address of Ramit
print(ramit['email'])

#exercise 2: write python expression that gets the first of Ramit's interests
print(ramit['interests'][0])

#exercise 3: write python expression that gets the email address of Jasmine
print(ramit['friends'][0]['email'])

#exercise 4: write python expression that gets the second of Jan's two interests
print(ramit['friends'][1]['interests'][1])
