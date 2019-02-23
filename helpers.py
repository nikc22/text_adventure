# Mac command to generte docs:
# python3 -m pydoc -w ./


def help_contents():
    """Lists all of the commands and some text about what they do"""
    print('Commands I know are:')
    print('north, south, west, east - move in that direction')
    print('talk - hear what the room inhabitant has to say')
    print('hug - hug the room inhabitant, be careful not to hug enemies')
    print('take, get - pick up an item')
    print('drop - remove an item from your backpack and leave it in the current room')
    print('inv - display the contents of my backpack')
    print('fight - challenge the room inhabitant to a duel with an item')
    print('hum - a way of waiting for something to happen')
    print('climb - some places have things that you can climb')
    print('score - print the scores so far')
    print('exit - leave the game')
    return True
