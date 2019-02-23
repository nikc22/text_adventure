class Room():

    def __init__(self, room_name, room_description):
        """Creates a Room"""
        self.name = room_name
        self.description = room_description
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.special = None

    def set_special(self, special_thing):
        """Sets the command that is special for a room"""
        self.special = special_thing

    def get_special(self):
        """Returns to special command for the room"""
        return self.special

    def set_character(self, room_character):
        """Places a character in the room"""
        self.character = room_character

    def get_character(self):
        """Returns the character"""
        return self.character

    def set_item(self, room_item):
        """Places an item in the room"""
        self.item = room_item

    def get_item(self):
        """Returns the item in the room"""
        return self.item

    def set_description(self, room_description):
        """Sets a string containing the description of the room"""
        self.description = room_description

    def get_description(self):
        """Returns a string containing the description of the room"""
        return self.description

    def set_name(self, room_name):
        """Sets the Room name"""
        self.name = room_name

    def get_name(self):
        """Returns the rooom name"""
        return self.name

    def describe(self):
        """Prints the room description"""
        print(self.description)

    def link_room(self, room_to_link, direction):
        """Links one room to another room, in one direction"""
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        """Prints the room details"""
        print("The " + self.get_name())
        print("-------------------")
        print(self.get_description())
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        """Moves the cahracter from one room to another, if they're linked"""
        if direction == 'n':
            direction = 'north'
        elif direction == 's':
            direction = 'south'
        elif direction == 'w':
            direction = 'west'
        elif direction == 'e':
            direction = 'east'
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
