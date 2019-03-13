class Room():

    def __init__(self, room_name, room_description):
        """Creates a Room"""
        self.name = room_name
        self.description = room_description
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.special_commands = {}
        self.lock = False
        self.unlock_item = None
        self.lock_text = None

    def set_unlock_item(self, lock_item, lock_status, lock_text):
        """Sets the item used to lock/unlock the room"""
        self.unlock_item = lock_item
        self.lock = lock_status
        self.lock_text = lock_text

    def set_lock_text(self, lock_text):
        """Sets the text to be returned when trying to enter a locked room"""
        self.lock_text = lock_text

    def get_lock_text(self):
        """Gets the text to be returned when trying to enter a locked room"""
        return self.lock_text

    def get_unlock_item(self):
        """Gets the item to be used to unlock the room"""
        return self.unlock_item

    def lock(self, lock_item):
        """Locks the room"""
        if lock_item == self.unlock_item:
            self.lock = True

    def unlock(self, lock_item):
        """Unlocks the Room"""
        if lock_item == self.unlock_item:
            self.lock = False

    def get_lock_status(self):
        """Gets the lock status value (Locked/Unlocked)"""
        return self.lock

    def set_special(self, room_command):
        """Sets a special command for a room"""
        self.special_commands[room_command.get_command()] = room_command

    def get_special(self, command):
        """Returns whether a special command applies to the room"""
        if len(self.special_commands) != 0:
            for ind in self.special_commands:
                comm = self.special_commands[ind]
                if comm.get_command() == command:
                    return True
        else:
            return False
        # return self.special_commands(command)

    def get_special_text(self, command):
        """Returns to text for aspecial command for the room"""
        if len(self.special_commands) != 0:
            for ind in self.special_commands:
                comm = self.special_commands[ind]
                if comm.get_command() == command:
                    return comm.get_command_text()
        else:
            return False

    def get_special_item(self, command):
        """Returns to text for aspecial command for the room"""
        if len(self.special_commands) != 0:
            for ind in self.special_commands:
                comm = self.special_commands[ind]
                if comm.get_command() == command:
                    return comm.get_item()
        else:
            return None

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
        # print('This rooms lock is ' + str(self.get_lock_status()))
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
        elif direction == 'd':
            direction = 'down'
        elif direction == 'u':
            direction = 'up'

        if direction in self.linked_rooms:
            next_room = self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
        if next_room.get_lock_status() is True:
            print("The door is locked, you can't go that way")
            if next_room.get_lock_text() is not None:
                print(next_room.get_lock_text())
            return self
        else:
            return next_room
