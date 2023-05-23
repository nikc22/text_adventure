class Character():

    def __init__(self, char_name, char_description):
        """Creates a Cahracter"""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Prints the characters name and description"""
        print(self.name + ' is here!')
        print(self.description)

    def set_conversation(self, conversation):
        """Sets the cahracters conversation text"""
        self.conversation = conversation

    def talk(self):
        """Prints the conversation text, if it exists"""
        if self.conversation is not None:
            print("[" + self.name + "] says: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        """Basic fight logic"""
        print(self.name + " doesn't want to fight with you")
        return True

    def give(self, gift_item):
        print(self.name + ' doesn\'t want your ' + gift_item.get_name())
        return False


class Enemy(Character):

    def __init__(self, char_name, char_description):
        """Creates an enemy character"""
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, char_weakness):
        """Sets the enemies weakness"""
        self.weakness = char_weakness

    def get_weakness(self):
        """Returns the enemies weakness"""
        return self.weakness

    def fight(self, combat_item):
        """Fight logic for enemies"""
        if combat_item == self.weakness:
            print('You vanquish ' + self.name + ' with the ' + combat_item)
            return True
        else:
            print(self.name + ' crushes you, puny adventurer')
            return False

    def hug(self):
        """Hugging an enemy results in a fight"""
        self.fight('nothing')
        return False


class Friend(Character):

    def __init__(self, char_name, char_description):
        """Creates a freindly character"""
        super().__init__(char_name, char_description)
        self.hint = None

    def hug(self):
        """Hugs your friend"""
        print(self.name + ' hugs you back')
        return True

    def pat(self):
        """Pats your friend"""
        if self.name == 'oscar':
            print(self.name + ' wags his tail')
        else:
            print(self.name + ' grins')
        return True

    def set_hint(self, friend_hint):
        """Sets the friends hint"""
        self.hint = friend_hint

    def get_hint(self):
        """Returns the friends hint if there is one"""
        if self.hint is not None:
            print("[" + self.name + "] says: " + self.hint)

    def give(self, gift_item):
        print('[' + self.name + '] says: Thank you for the ' + gift_item.get_name())
        return True


class Nuetral(Character):

    def __init__(self, char_name, char_description):
        """Creates a nuetral character"""
        super().__init__(char_name, char_description)

    def hug(self):
        """Hug a Neutral character"""
        print('[' + self.name + '] says: That was akward')
        return True
