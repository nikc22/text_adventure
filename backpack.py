class Backpack():

    def __init__(self, capacity):
        """Creates a Backpack, setting the max capacity"""
        self.items = {}
        self.weight = 0
        self.max_weight = capacity

    def get_inventory(self):
        """Prints the inventory in the backpack"""
        if len(self.items) == 0:
            print('There is nothing in your backpack')
        else:
            for ind in self.items:
                item = self.items[ind]
                print(item.get_name() + ' (' + str(item.get_weight()) + ')')
            print('Your backpack weighs ' + str(self.weight))
        print('The capcity of your backpack is ' + str(self.max_weight))

    def add_item(self, item):
        """Adds an Item to the backpack, if there is capacity"""
        if self.get_weight() + item.get_weight() <= self.max_weight:
            self.items[item.get_name()] = item
            self.weight += item.get_weight()
            return True
        else:
            return False

    def drop_item(self, item):
        """Removes an item fromt the Backapack"""
        ind = self.items[item]
        self.items[item] = None
        self.weight -= ind.get_weight()
        return ind

    def get_weight(self):
        """Returns the weight of items in the backpack"""
        return self.weight

    def get_items(self):
        """Returns the items, allowing for searching int he list of items"""
        return self.items
