"""Module that makes a game chaser"""

class Room():
    """class for a rooms"""
    def __init__(self, name, character=None):
        """
        Initializes attributes for class. 
        """
        self.name = name
        self.description = ''
        self.direction = ''
        self.character = character
        self.item = None
        self.rooms = []
        self.roomsdict = dict()
        
    def set_description(self, description):
        """
        Sets a description.
        """
        self.description = description
        return self.description

    def link_room(self,other_room, direction):
        
        self.roomsdict[direction] = other_room
        self.rooms.append(f'The{other_room.name} is {direction}')

    def set_character(self, character):
        """
        Sets a character for the location.
        """
        self.character = character

    def set_item(self, item):
        """
        Sets an item for the location.
        """
        self.item = item

    def get_item(self):
        """
        Gets an item for the location.
        """
        return self.item
  
    def get_character(self):
        return self.character

    def get_details(self):
        print(f"""
{self.name}
--------------------
{self.description}""")
        for room in self.rooms:
            print(room)

    def move(self, command):
        """
        Lets player move from the location.
        """
        return self.roomsdict[command]


    
        
class Enemy:
    """class for an enemy"""
    defeats = 0
    def __init__(self, name, description):
        """
        Initializes attributes for class. 
        """
        self.name = name
        self.description = description
        self.conversation = ''
        self.weakness = ''
    
    def fight(self, item):
        """
        Lets character fight with the enemy.
        """
        if self.weakness == item:
            Enemy.defeats += 1
        return self.weakness == item

    def get_defeated(self):
        """
        Returns points from different defeats
        """
        return Enemy.defeats

    def set_conversation(self, conversation):
        """
        Sets a conversation for a mob.
        """
        self.conversation = conversation

    def set_weakness(self, weakness):
        """
        Sets a conversation for a mob.
        """
        self.weakness = weakness

    def describe(self):
        """
        Describes a character.
        """
        print(f"""
{self.name} is here!
{self.description}
""")

    def talk(self):
        """
        Simmulate conversation to the player.
        """
        print(f'[{self.name} says]: {self.conversation}')


class Item:
    """class for a item"""
    def __init__(self, name):
        """
        Initializes attributes for class. 
        """
        self.name = name
        self.description = ''
    def set_description(self, description):
        """
        Sets a description.
        """
        self.description = description


    def get_name(self):
        """
        Gets a name.
        """
        return self.name

    def describe(self):
        """
        Prints a description.
        """
        print(f"""
The {self.name} is here - {self.description}
""")

