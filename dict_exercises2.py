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

# Write a python expression that gets the email address of Ramit.
# Write a python expression that gets the first of Ramit's interests.
# Write a python expression that gets the email address of Jasmine.
# Write a python expression that gets the second of Jan's two interests.

email = ramit['email']

first_interest = ramit['interests'][0]

def get_email(name):
    friend_list = ramit['friends']
    for friend in friend_list:
        # in a production environment there would obviously be error catching and type checking
        if name == friend['name']:
            return friend['email']

print(email)
print(first_interest)
print(get_email('Jasmine'))