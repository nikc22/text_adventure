from room import Room
from character import Enemy, Friend, Nuetral
from item import Item
from backpack import Backpack
from room_command import Room_Command
import helpers as hlp


def print_score():
    """Prints the players score"""
    print('Scores:')
    print(str(hugs) + ' hugs given')
    print(str(fights) + ' fights won')
    print(str(favours) + ' favours done')


# Ground Floor
kitchen = Room('Kitchen', 'A dank and dirty room buzzing with flies')
dinning_hall = Room('Dinning Hall', 'A large room with ornate golden decorations on every wall')
ballroom = Room('Ballroom', 'A place where various conspiricies and affairs of the heart were launched, admist dancing and cavorting')
ballroom_2 = Room('Ballroom', 'A place where various conspiricies and affairs of the heart were launched, admist dancing and cavorting')
drawing_room = Room('Drawing Room', 'An austere room with large couches dominating the space')
entrance = Room('Entrance', 'A small room with an umbrella stand behind wooden doors that are two stories high')
games_room = Room('Games Room', 'A place for billiards and discussion after dinner')
stairs = Room('Stairs', 'A grand staircase leading up to the first floor and down to the cellar')

# 1st Floor
stairs_1 = Room('Stairs', 'A grand staircase leading down to the ground floor')
bed_1 = Room('Bed 1', 'A bedroom with a quilt that matches the curtains, full of flowers')
bed_2 = Room('Bed 2', 'A bedroom with interesting furniture')
master_1 = Room('Master Bedroom - Southern End', 'A large space dominated by an ornate bed')
master_2 = Room('Master Bedroom - Northern End', 'A large space dominated by an ornate bed')
library = Room('Library', 'A room full of books and comfortable chairs, in which to read them')
bathroom = Room('Bathroom', 'A room with a lovely free standing bath and a pile of big thick towels')
linen_cupboard = Room('Linen Cupboard', 'A space filled with a range of items designed to keep the house running')
balcony_1 = Room('Balcony', 'Looking out over the orchard a gardens')
balcony_2 = Room('Balcony', 'Looking out over the orchard a gardens')
hall1 = Room('Hall', 'A room that connects other rooms on the first floor')
hall2 = Room('Hall', 'A room that connects other rooms on the first floor')
hall3 = Room('Hall', 'A room that connects other rooms on the first floor')
hall4 = Room('Hall', 'A room that connects other rooms on the first floor')

# Cellar
stairs_d = Room('Stairs', 'A grand staircase leading up to the ground floor')
wine_cellar = Room('Wine Cellar', 'A room full of slowly aging bottles of wine and slight musty smell')
larder = Room('Larder', 'A room full of the dried goods that keep keeps the kitchen supplied')

shed = Room('Shed', 'A garden shed full of interesting items')
path = Room('Path', 'A path leading from the house to the stream, lined with trees. There are flowers here')
stream = Room('Stream', 'A burbbling little stream, crossed by a bridge to the north. There are flowers here')
stream2 = Room('Stream', 'A burbbling little stream, crossed by a bridge to the north. There are flowers here')
bridge = Room('Bridge', 'A bridge that to nowhere')
general_store = Room('General Store', 'A small shop filled with curious items')
drive = Room('Driveway', 'A promenade that leads to the carriage way, with buggy near the house, unfortunately wihtout the horse')
herb_garden = Room('Herb Garden', 'A lovely garden full of fresh Rosemary and Thyme, amongst other things')
carriageway = Room('Carriage Way', 'A road way that leads from the village to destinations unknown')
carriageway2 = Room('Carriage Way', 'A road way that leads from the village to destinations unknown')
carriageway3 = Room('Carriage Way', 'A road way that leads from the village to destinations unknown')
carriageway4 = Room('Carriage Way', 'A road way that leads from the village to destinations unknown')
carriageway5 = Room('Carriage Way', 'A road way that leads from the village to destinations unknown')
carriageway6 = Room('Carriage Way', 'A road way that leads from the village to destinations unknown')
carriageway7 = Room('Carriage Way', 'A road way that leads from the village to destinations unknown')
carriageway8 = Room('Carriage Way', 'A road way that leads from the village to destinations unknown')
carriageway9 = Room('Carriage Way', 'A road way that leads from the village to destinations unknown')
carriageway10 = Room('Carriage Way', 'A road way that leads from the village to destinations unknown')
carriagewaybridge = Room('Carriage Way Bridge', 'A bridge that links the carriage way, with the village on one side')
mainstreet = Room('Main Street', 'The main street of the village')
mainstreet2 = Room('Main Street', 'The main street of the village')
bigstreet = Room('Big Street', 'The secondary street of the village')
bigstreet2 = Room('Big Street', 'The secondary street of the village')
school_room = Room('School Room', 'A classroom full of students, listening to Laura tell them about coding Raspberry Pi''s')

# Locks
bathroom.set_unlock_item('House Key', True, 'The lady of the house is using the bathroom')

# House
# Ground floor
kitchen.link_room(dinning_hall, 'south')
kitchen.link_room(shed, 'east')
kitchen.link_room(herb_garden, 'north')
herb_garden.link_room(kitchen, 'south')
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
entrance.link_room(drawing_room, 'north')
entrance.link_room(drive, 'south')
entrance.link_room(stairs, "west")
stairs.link_room(games_room, 'north')
stairs.link_room(entrance, 'east')
stairs.link_room(stairs_d, "down")
stairs.link_room(stairs_1, "up")


# Cellar
stairs_d.link_room(stairs, "up")
stairs_d.link_room(wine_cellar, "north")
wine_cellar.link_room(stairs_d, "south")
wine_cellar.link_room(larder, "east")
larder.link_room(wine_cellar, "west")

# First Floor
stairs_1.link_room(stairs, "down")
stairs_1.link_room(hall1, "east")
hall1.link_room(stairs_1, "west")
hall1.link_room(hall2, "north")
hall1.link_room(master_1, "east")
hall2.link_room(hall1, "south")
hall2.link_room(hall3, "north")
hall2.link_room(bed_1, "west")
hall2.link_room(master_2, "east")
hall3.link_room(hall2, "south")
hall3.link_room(hall4, "north")
hall3.link_room(library, "west")
hall3.link_room(bathroom, "east")
hall4.link_room(hall3, "south")
hall4.link_room(bed_2, "west")
hall4.link_room(linen_cupboard, "east")
master_1.link_room(hall1, "west")
master_1.link_room(balcony_1, "east")
master_1.link_room(master_2, "north")
master_2.link_room(hall2, "west")
master_2.link_room(balcony_2, "east")
master_2.link_room(master_1, "south")
bed_1.link_room(hall2, "east")
bed_2.link_room(hall4, "east")
linen_cupboard.link_room(hall4, "west")
balcony_1.link_room(master_1, "west")
balcony_2.link_room(master_2, "west")
bathroom.link_room(hall3, "west")
library.link_room(hall3, "east")


shed.link_room(kitchen, 'west')
shed.link_room(path, 'east')
path.link_room(shed, 'west')
path.link_room(stream, 'east')
stream.link_room(path, 'west')
stream.link_room(stream2, 'north')
stream2.link_room(stream, 'south')
stream2.link_room(bridge, 'north')
bridge.link_room(stream2, 'south')
drive.link_room(entrance, 'north')
drive.link_room(carriageway, 'south')
carriageway.link_room(drive, 'north')
carriageway.link_room(carriageway2, 'east')
carriageway2.link_room(carriageway, 'west')
carriageway2.link_room(carriageway3, 'east')
carriageway3.link_room(carriageway2, 'west')
carriageway3.link_room(carriagewaybridge, 'east')
carriagewaybridge.link_room(carriageway3, 'west')
carriagewaybridge.link_room(carriageway4, 'east')
carriageway4.link_room(carriagewaybridge, 'west')
carriageway4.link_room(carriageway5, 'east')
carriageway5.link_room(carriageway4, 'west')
carriageway5.link_room(carriageway6, 'east')
carriageway6.link_room(carriageway5, 'west')
carriageway6.link_room(carriageway7, 'east')
carriageway7.link_room(carriageway6, 'west')
carriageway7.link_room(carriageway8, 'east')
carriageway8.link_room(carriageway7, 'west')
carriageway8.link_room(carriageway9, 'east')
carriageway9.link_room(carriageway8, 'west')
carriageway9.link_room(carriageway10, 'east')
carriageway10.link_room(carriageway9, 'west')

# Village
carriageway6.link_room(mainstreet, 'north')
carriageway9.link_room(bigstreet, 'north')
mainstreet.link_room(carriageway6, 'south')
mainstreet.link_room(mainstreet2, 'north')
mainstreet2.link_room(mainstreet, 'south')
bigstreet.link_room(carriageway9, 'south')
bigstreet.link_room(bigstreet2, 'north')
bigstreet2.link_room(bigstreet, 'south')
mainstreet.link_room(general_store, 'west')
general_store.link_room(mainstreet, 'east')
bigstreet.link_room(school_room, 'east')
school_room.link_room(bigstreet, 'west')

# Special Commands

path_climb = Room_Command('climb', 'You climb a tree, but don\'t see much that is special apart from a lake to the north')
path_pick = Room_Command('pick', 'You pick some flowers and try and put them in your bacpack')
stream_swim = Room_Command('swim', 'You take a refreshing dip in the stream')
stream_pick = Room_Command('pick', 'You pick some flowers, although they wilt in your hand as you pick them')
herb_garden_pick = Room_Command('pick', 'You pick some herbs and try and put them in your bacpack')

path.set_special(path_climb)
path.set_special(path_pick)
stream.set_special(stream_swim)
stream2.set_special(stream_swim)
stream.set_special(stream_pick)
stream2.set_special(stream_pick)
herb_garden.set_special(herb_garden_pick)

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

oscar = Friend('Oscar', 'A friendly little white dog with a very waggy tail')
oscar.set_conversation('Where''s my treat human')
oscar.set_hint('I''ll guard the treat cupboard for you')


# Neutral
gaylord = Nuetral('Gaylord', 'A Bored Shop keeper')
gaylord.set_conversation('I don\'t have many things to sell, can you bring me some more items for my shop')


cheese = Item('cheese', 'A large and smelly block of cheese', 2.0)
book = Item('book', 'A tome full of wonderous knowledge', 3.0)
breadstick = Item('breadstick', 'A baugette old enough to be used as a weapon', 1.5)
apple_pie = Item('Apple Pie', 'A freshly baked pie made with apples form the orchard', 2.0)
duster = Item('feather duster', 'A moth eaten excuse for a duster', 1.0)
flower = Item('flowers', 'A bunch of lovely daisies', 0.5)
herb = Item('herbs', 'A bunch of Rosemary and Thyme', 0.5)

kitchen.set_character(oscar)
dinning_hall.set_character(dave)
ballroom.set_character(connie)
bridge.set_character(jill)
shed.set_character(jack)
drawing_room.set_character(jim)
general_store.set_character(gaylord)

ballroom.set_item(cheese)
dinning_hall.set_item(book)
kitchen.set_item(apple_pie)
games_room.set_item(breadstick)
drawing_room.set_item(duster)

# Special Command Items
path_pick.set_item(flower)
herb_garden_pick.set_item(herb)

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
    if command in ['north', 'south', 'west', 'east', 'n', 's', 'w', 'e', 'down', 'up', 'd', 'u']:
        current_room = current_room.move(command)

    # Room commands
    elif command in ('pick', 'climb', 'swim'):
        if current_room.get_special(command) is True:
            print(current_room.get_special_text(command))
            item = current_room.get_special_item(command)
            if item is not None:
                if backpack.add_item(item) is True:
                    print('The ' + item.get_name() + ' is now in your backpack')
                else:
                    print('The ' + item.get_name() + ' didn\'t fit in your backpack, maybe you need to drop an item')
                    # drop item if it doesn't fit, when rooms can have multiple items
        else:
            if command == 'pick':
                print('There is nothing to pick here')
            elif command == 'climb':
                print('There is nothing to climb here')
            elif command == 'swim':
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
    elif command == 'give':
        print('What would you like to give?')
        gift_item = input('+ ')
        if gift_item in backpack.get_items():
            item = backpack.drop_item(gift_item)
            if inhabitant.give(item) is True:
                favours += 1
            else:
                if current_room.item is None:
                    current_room.item = item
                else:
                    backpack.add_item(item)
        else:
            print('You don\'t have a ' + gift_item + ' in your backpack')
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
