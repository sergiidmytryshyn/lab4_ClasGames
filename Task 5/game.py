"""Module with definitions of classes needed for gameplay"""

class Character():
    """
    Object with which tou can interact
    Attributes:
        phrase (str): phrase that character can say
        name (str): charactesrs name
        description (str): description of character
    """

    def __init__(self, name: str, description: str) -> None:
        """Creates an object of class Character"""
        self.phrase = None
        self.name = name
        self.description = description

    def set_conversation(self, phrase: str) -> None:
        """Assigns character a phrase"""
        self.phrase = phrase

    def describe(self) -> str:
        """Prints character's description"""
        print(f"The {self.name} is here!\n{self.description}")

    def talk(self) -> str:
        """Prints chracter's phrase"""
        print(f"[{self.name} says]: {self.phrase}")

class Item():
    """
    Item that you can find in the room and take it to fight enemies 
    Attributes:
        name (str): name of item
        description (str): description of item
    """

    def __init__(self, name: str) -> None:
        """Creates item object"""
        self.name = name
        self.description = None

    def set_description(self, description: str) -> None:
        """Assigns a description to item"""
        self.description = description

    def describe(self) -> str:
        """Prints item's description"""
        print(f"The [{self.name}] is here - {self.description}")

    def get_name(self) -> str:
        """Returns item's name"""
        return self.name

class Enemy(Character):
    """
    Enemy character with which you can fight
    Attributes:
        defeats (int): amount of defeated enemies
        weakness (str): name of object that counters this character
    Inheritance:
        Character:
    """

    defeats = 0
    def __init__(self, name: str, description: str) -> None:
        """Creates enemy character"""
        super().__init__(name, description)
        self.weakness = None

    def set_weakness(self, item: Item) -> None:
        """Assigns a weakness to enemy"""
        self.weakness = item

    def fight(self, fight_with: str) -> bool:
        """Checks if your item is enemy's weakness"""
        return fight_with == self.weakness

    def get_defeated(self) -> int:
        """Increases amount of defeated enemies"""
        Enemy.defeats += 1
        return Enemy.defeats

class Room():
    """
    Room with an enemy and items that you can take
    Attributes:
        name (str):
        description (str):
        linked_rooms (list): rooms, where youu can
        item (Item): item that yo can take
        character (Character): Character that lives in the room
    """

    def __init__(self, name: str) -> None:
        """Creates object with character and item inside"""
        self.name = name
        self.description = None
        self.linked_rooms = []
        self.item = None
        self.character = None

    def set_description(self, description: str) -> None:
        """Sets description of room"""
        self.description = description

    def get_details(self) -> None:
        """Prints details about room"""
        print(self.name)
        print("-"*20)
        if self.linked_rooms:
            print(f"{self.description}")
            print("\n".join([room[0] for room in self.linked_rooms]))

    def link_room(self, room: object, direction: str) -> None:
        """Add a room to the list of linked rooms"""
        self.linked_rooms.append([f"The {room.name} is {direction}", room])

    def set_character(self, character: Character) -> None:
        """Adds character to the room"""
        self.character = character

    def get_character(self) -> Character:
        """Returns character from the room"""
        return self.character

    def set_item(self, item: Item) -> None:
        """Places item in the room"""
        self.item = item

    def get_item(self) -> Item:
        """Returns item from the room"""
        return self.item

    def move(self, direction: str) -> object:
        """Returns linked room in given direction"""
        for room in self.linked_rooms:
            if direction in room[0]:
                return room[1]

# class Friend(Character):
#     """Unused class"""
#     pass
