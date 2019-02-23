class Item():

    def __init__(self, item_name, item_description, item_weight):
        """Creates an Item"""
        self.name = item_name
        self.description = item_description
        self.weight = item_weight

    def set_description(self, item_description):
        """Sets the items description"""
        self.description = item_description

    def get_description(self):
        """Returns the items description"""
        return self.description

    def set_name(self, item_name):
        """Sets the items name"""
        self.name = item_name

    def get_name(self):
        """Returns the items name"""
        return self.name

    def set_weight(self, item_weight):
        """Sets the items weight"""
        self.name = item_weight

    def get_weight(self):
        """Returns the items weight"""
        return self.weight

    def describe(self):
        """Prints the items name and description"""
        print("The [" + self.name + "] is here - " + self.description)
