db = {}

# add guest
# remove guest

def add_guests(floor, room, occupants):
    if floor not in db:
        db[floor] = {}

    if room not in db[floor]:
        db[floor][room] = occupants
        print("added!", db)
    else:
        Exception("Guests already checked in to that room! [this code should not be reached]")

def remove_guests(floor, room):
    if room not in db[floor]:
        Exception('No one is checked in to that room! [this code should not be reached]')
    del db[floor][room]

def check_room_free(floor, room):
    if floor not in db or room not in db[floor]:
        return True
    else:
        return False

def prompt_guests(num):
    guests = []
    i = 0

    while i < num:
        guest = input("what is the name of guest number " + str(i + 1) + "?: ")
        guests.append(guest)
        i += 1
    return guests


def prompt_checkin():
    floor = int(input("which floor would you like?: "))
    room = int(input("which room would you like?: "))

    if check_room_free(floor, room):
        guest_count = int(input("How many guests will be staying?: "))
        guests = prompt_guests(guest_count)
        add_guests(floor, room, guests)

prompt_checkin()