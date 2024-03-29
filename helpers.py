# Mac command to generte docs:
# python3 -m pydoc -w ./


def help_contents():
    """Lists all of the commands and some text about what they do"""
    print('Commands I know are:')
    print('north, south, west, east, up, down - move in that direction, short command of first letter also available')
    print('talk - hear what the room inhabitant has to say')
    print('hug - hug the room inhabitant, be careful not to hug enemies')
    print('pat - pat the room inhabitant, be careful, some don''t like it (scores as a hug)')
    print('take, get - pick up an item')
    print('give - give an item to somebody else')
    print('drop - remove an item from your backpack and leave it in the current room')
    print('inv - display the contents of my backpack')
    print('fight - challenge the room inhabitant to a duel with an item')
    print('hum - a way of waiting for something to happen')
    print('climb - some places have things that you can climb, including trees')
    print('swim - swim in a body of water')
    print('pick - pick flowers or herbs from this location')
    print('score - print the scores so far')
    print('exit - leave the game')
    return True
