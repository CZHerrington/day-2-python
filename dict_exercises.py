phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

# Print Elizabeth's phone number.
# Add an entry to the dictionary: Kareem's number is 938-489-1234.
# Delete Alice's phone entry.
# Change Bob's phone number to '968-345-2345'.
# Print all the phone entries.

elizabeth_phone = phonebook_dict['Elizabeth']
print(elizabeth_phone)
phonebook_dict['Kareem'] = '938-489-1234'
del phonebook_dict['Alice']
phonebook_dict['Bob'] = '968-345-2345'

for person in phonebook_dict:
    phone_number = phonebook_dict[person]
    print(person, ' : ', phone_number)