class Room_Command():

    def __init__(self, command_name, command_text):
        """Creates a Room Command, which allows special actions in specific rooms"""
        self.command = command_name
        self.command_text = command_text
        self.item = None

    def get_command_text(self):
        """Get the text for the command"""
        return self.command_text

    def set_command_text(self, command_text):
        """Set the text for the command"""
        self.command_text = command_text

    def get_command(self):
        """Get the text for the command name"""
        return self.command

    def set_item(self, room_item):
        """Places an item for the room command"""
        self.item = room_item

    def get_item(self):
        """Returns the item for the room command"""
        return self.item
