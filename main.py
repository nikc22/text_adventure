from room import Room
from character import Enemy, Friend
from item import Item
from backpack import Backpack
import helpers as hlp

kitchen = Room('Kitchen', 'A dank and dirty room buzzing with flies')
dinning_hall = Room('Dinning Hall', 'A large room with ornate golden decorations on every wall')
ballroom = Room('Ballroom', 'A place where various conspiricies and affairs of the heart were launched, admist dancing and cavorting')
drawing_room = Room('Drawing Room', 'An austere room with large couches dominating the space')
shed = Room('Shed', 'A garden shed full of interesting items')
path = Room('Path', 'A path leading from the house to the stream')
stream = Room('Stream', 'A burbbling little stream, crossed by a bridge to the north')
stream2 = Room('Stream', 'A burbbling little stream, crossed by a bridge to the north')
bridge = Room('Bridge', 'A bridge that to nowhere')

kitchen.link_room(dinning_hall, "south")
kitchen.link_room(shed, 'east')
dinning_hall.link_room(kitchen, "north")
dinning_hall.link_room(ballroom, "west")
dinning_hall.link_room(drawing_room, "south")
drawing_room.link_room(dinning_hall, "north")
ballroom.link_room(dinning_hall, "east")
shed.link_room(kitchen, 'west')
shed.link_room(path, 'east')
path.link_room(shed, 'west')
path.link_room(stream, 'east')
stream.link_room(path, 'west')
stream.link_room(stream2, 'north')
stream2.link_room(stream2, 'south')
stream2.link_room(bridge, 'north')
bridge.link_room(stream2, 'south')

dave = Enemy('Dave', 'A smelly grumpy zombie')
dave.set_conversation('Brrlgrh... rgrhl... brains...')
dave.set_weakness('cheese')

jack = Enemy('Jack', 'An enormous fierce rat')
jack.set_conversation('And a fine day it is')
jack.set_weakness('book')

jill = Enemy('Jill', 'A nasty troll')
jill.set_conversation('How much will you pay me to cross the bridge?')
jill.set_weakness('duster')

connie = Friend('Connie', 'A friendly skelton')
connie.set_conversation('How are you today?')
connie.set_hint('Dave doesn\'t like cheese.')

jim = Friend('Jim', 'A friendly servant')
jim.set_conversation('I hope it doens\'t rain inside again today')
jim.set_hint('Jack doesn\'t like books')

cheese = Item('cheese', 'A large and smelly block of cheese', 2.0)
book = Item('book', 'A tome full of wonderous knowledge', 3.0)
breadstick = Item('breadstick', 'A baugette old enough to be used as a weapon', 1.5)
duster = Item('feather duster', 'A moth eaten excuse for a duster', 1.0)

dinning_hall.set_character(dave)
ballroom.set_character(connie)
bridge.set_character(jill)
shed.set_character(jack)
drawing_room.set_character(jim)

ballroom.set_item(cheese)
dinning_hall.set_item(book)
kitchen.set_item(breadstick)
drawing_room.set_item(duster)

backpack = Backpack(15.0)

current_room = kitchen
dead = False
hugs = 0
fights = 0


print('Welcome to a little adventure')
print('Enter the direction you want to move in or help to see what else I can do')
while not dead:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ['north', 'south', 'west', 'east', 'n', 's', 'w', 'e']:
        current_room = current_room.move(command)
    elif command == 'talk':
        inhabitant.talk()
    elif command == 'hum':
        if isinstance(inhabitant, Friend):
            inhabitant.get_hint()
        else:
            inhabitant.talk()
    elif command == 'fight':
        print('What would you like to fight with?')
        fight_item = input('+ ')
        if fight_item in backpack.get_items():
            if inhabitant.fight(fight_item) is False:
                dead = True
            else:
                current_room.character = None
                fights += 1
        else:
            print('You don\'t have a ' + fight_item + ' in your backpack')
    elif command == 'hug':
        if inhabitant.hug() is False:
            dead = True
        else:
            hugs += 1
    elif command in ('take', 'get'):
        if current_room.item is None:
            print('Nothing to take')
        else:
            if backpack.add_item(item) is True:
                current_room.item = None
                print('The ' + item.get_name() + ' is now in your backpack')
            else:
                print('The ' + item.get_name() + ' didn\'t fit in your backpack, maybe you need to drop an item')
    elif command == 'drop':
        if current_room.item is None:
            print('What would you like to drop?')
            drop_item = input('+ ')
            if drop_item in backpack.get_items():
                current_room.item = backpack.drop_item(drop_item)
            else:
                print('You don\'t have a ' + drop_item + ' in your backpack')
        else:
            print('There is already an item in this room, you\'ll need to drop it somewhere else')
    elif command == 'inv':
        backpack.get_inventory()
    elif command == 'help':
        hlp.help_contents()
    elif command == 'exit':
        dead = True
    else:
        print('I don\'t know how to ' + command + '. Try help to see what I know about')

    if dead:
        print('\nThank you for playing')
        print('Scores:')
        print(str(hugs) + ' hugs given')
        print(str(fights) + ' fights won')
