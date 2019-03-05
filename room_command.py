class Room_Command():

    def __init__(self, command_name, command_text):
        """Creates a Room Command, which allows special actions in specific rooms"""
        self.command = command_name
        self.command_text = command_text

    def get_command_text(self):
        return self.command_text

    def set_command_text(self, command_text):
        self.command_text = command_text

    def get_command(self):
        return self.command
