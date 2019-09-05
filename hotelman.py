db = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}
# db operations
def add_guests(floor, room, occupants):
    if floor not in db:
        db[floor] = {}

    if room not in db[floor]:
        db[floor][room] = occupants
        print("Your room number is %s!" % (str(room)), db)
    else:
        print("Guests already checked in to that room!")

def remove_guests(floor, room):
    if floor in db:
        print('floor exists..')
        if room in db[floor]:
            print('room occupied...')
            del db[floor][room]
        print("thank you, you are checked out of room %s" % (str(room)))

# utility fxns
def check_room_free(floor, room):
    if str(floor) not in db or str(room) not in db[str(floor)]:
        return True
    else:
        return False

# menu option prompts
def prompt_guests(num):
    guests = []
    i = 0

    while i < num:
        guest = input("what is the name of guest number " + str(i + 1) + "?: ")
        guests.append(guest)
        i += 1
    return guests

def prompt_checkin():
    floor = input("which floor would you like?: ")
    room = str(floor) + input("which room would you like?: ")

    if check_room_free(floor, room):
        guest_count = int(input("How many guests will be staying?: "))
        if guest_count < 1:
            print('there needs to be at least one guest!')
            exit
        guests = prompt_guests(guest_count)
        add_guests(floor, room, guests)

def prompt_checkout():
    room = str(input("what was your room number?: "))
    floor = str(room[0])

    print('remove: ', floor, room)
    remove_guests(floor, room)



# main prompt
def menu():
    run = True
    while run:
        option = int(input('1. Check in\n2. Check out\n3. Dump database\n4. Exit program\n> '))
        if option == 1:
            prompt_checkin()

        if option == 2:
            prompt_checkout()

        if option == 3:
            print(db)

        if option == 4:
            run = False

        if option > 4:
            print('selection must be one of the available options')

menu()
# make main loop that calls menu fxn, script style