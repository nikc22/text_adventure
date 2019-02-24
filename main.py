from room import Room
from character import Enemy, Friend, Nuetral
from item import Item
from backpack import Backpack
import helpers as hlp


def print_score():
    """Prints the players score"""
    print('Scores:')
    print(str(hugs) + ' hugs given')
    print(str(fights) + ' fights won')
    print(str(favours) + ' favours done')


kitchen = Room('Kitchen', 'A dank and dirty room buzzing with flies')
dinning_hall = Room('Dinning Hall', 'A large room with ornate golden decorations on every wall')
ballroom = Room('Ballroom', 'A place where various conspiricies and affairs of the heart were launched, admist dancing and cavorting')
drawing_room = Room('Drawing Room', 'An austere room with large couches dominating the space')
shed = Room('Shed', 'A garden shed full of interesting items')
path = Room('Path', 'A path leading from the house to the stream, lined with trees')
stream = Room('Stream', 'A burbbling little stream, crossed by a bridge to the north')
stream2 = Room('Stream', 'A burbbling little stream, crossed by a bridge to the north')
bridge = Room('Bridge', 'A bridge that to nowhere')
shop = Room('Shop', 'A small shop filled with curious items')
entrance = Room('Entrance', 'A small room with an umbrella stand behind wooden doors that are two stories high')
drive = Room('Driveway', 'A promenade that leads to the carriage way, with buggy near the house, unfortunately wihtout the horse')
games_room = Room('Games Room', 'A place for billiards and discussion after dinner')
stairs = Room('Stairs', 'A grand staircase leading up to the first floor and down to the cellar')
herb_garden = Room('Herb Garden', 'A lovely garden full of fresh Rosemary and Thyme, amongst other things')


kitchen.link_room(dinning_hall, 'south')
kitchen.link_room(shed, 'east')
dinning_hall.link_room(kitchen, 'north')
dinning_hall.link_room(ballroom, 'west')
dinning_hall.link_room(drawing_room, 'south')
drawing_room.link_room(dinning_hall, 'north')
drawing_room.link_room(entrance, 'south')
drawing_room.link_room(games_room, 'west')
ballroom.link_room(dinning_hall, 'east')
ballroom.link_room(games_room, 'south')
games_room.link_room(ballroom, 'north')
games_room.link_room(drawing_room, 'east')
games_room.link_room(stairs, 'south')
shed.link_room(kitchen, 'west')
shed.link_room(path, 'east')
path.link_room(shed, 'west')
path.link_room(stream, 'east')
stream.link_room(path, 'west')
stream.link_room(stream2, 'north')
stream2.link_room(stream, 'south')
stream2.link_room(bridge, 'north')
bridge.link_room(stream2, 'south')
entrance.link_room(drawing_room, 'north')
entrance.link_room(drive, 'south')
entrance.link_room(stairs, "west")
stairs.link_room(games_room, 'north')
stairs.link_room(entrance, 'east')
drive.link_room(entrance, 'north')
drive.link_room(shop, 'south')
shop.link_room(drive, 'north')

path.set_special('climb', 'You climb a tree, but don\'t see much that is special apart from a lake to the north')
stream.set_special('swim', 'You take a refreshing dip in the stream')

# Enemies
dave = Enemy('Dave', 'A smelly grumpy zombie')
dave.set_conversation('Brrlgrh... rgrhl... brains...')
dave.set_weakness('cheese')

jack = Enemy('Jack', 'An enormous fierce rat')
jack.set_conversation('And a fine day it is')
jack.set_weakness('book')

jill = Enemy('Jill', 'A nasty troll')
jill.set_conversation('How much will you pay me to cross the bridge?')
jill.set_weakness('duster')


# Friends
connie = Friend('Connie', 'A friendly skelton')
connie.set_conversation('How are you today?')
connie.set_hint('Dave doesn\'t like cheese.')

jim = Friend('Jim', 'A friendly gardiner')
jim.set_conversation('I hope it doens\'t rain inside again today')
jim.set_hint('Jack doesn\'t like books')

# Neutral
gaylord = Nuetral('Gaylord', 'A Bored Shop keeper')
gaylord.set_conversation('I don\'t have many things to sell, can you bring me some more items for my shop')


cheese = Item('cheese', 'A large and smelly block of cheese', 2.0)
book = Item('book', 'A tome full of wonderous knowledge', 3.0)
breadstick = Item('breadstick', 'A baugette old enough to be used as a weapon', 1.5)
apple_pie = Item('Apple Pie', 'A freshly baked pie made with apples form the orchard', 2.0)
duster = Item('feather duster', 'A moth eaten excuse for a duster', 1.0)

dinning_hall.set_character(dave)
ballroom.set_character(connie)
bridge.set_character(jill)
shed.set_character(jack)
drawing_room.set_character(jim)
shop.set_character(gaylord)

ballroom.set_item(cheese)
dinning_hall.set_item(book)
kitchen.set_item(apple_pie)
games_room.set_item(breadstick)
drawing_room.set_item(duster)

backpack = Backpack(15.0)  # Number determines backpack capacity

current_room = kitchen
dead = False
hugs = 0
fights = 0
favours = 0


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

    # Movement Commands
    if command in ['north', 'south', 'west', 'east', 'n', 's', 'w', 'e']:
        current_room = current_room.move(command)
    elif command == 'climb':
        if current_room.get_special() == 'climb':
            print(current_room.get_special_text())
        else:
            print('There is nothing to climb here')
    elif command == 'swim':
        if current_room.get_special() == 'swim':
            print(current_room.get_special_text())
        else:
            print('There is nothing to swim in here')

    # Character Commands
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

    # Item/Inventory Commands
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

    # Game Commands
    elif command == 'help':
        hlp.help_contents()
    elif command == 'score':
        print_score()
    elif command == 'exit':
        dead = True

    # Don't know/Evrything else Commands
    else:
        print('I don\'t know how to ' + command + '. Try help to see what I know about')

    # Exit and print scores
    if dead:
        print('\nThank you for playing')
        print_score()
