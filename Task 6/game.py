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
        self.phrase = None
        self.name = name
        self.description = description

    def set_conversation(self, phrase: str) -> None:
        """
        Assigns character a phrase
        Args:
            phrase (str): phrase to say
        """
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
        self.name = name

    def get_name(self) -> str:
        """Returns item's name"""
        return self.name

class Phone(Item):
    """
    Item with which you can call taxi or call polica in fight

    Inheritance:
        Item:
    """

    def taxi_call(self, money: int, distance: int) -> bool:
        """
        Retrns True if you have enough money to pay for a ride

        Args:
            money (int): money in wallet
            distance (int): distance to ride

        Returns:
            bool: if you can ride
        """
        print(f"-Allo, you must pay {distance*50} UAH to get to UCU")
        return money >= distance*50

class PepperSpray(Item):
    """
    Item that you can use only 1 time to beat enemies

    Inheritance:
        Item:
    """

    def get_description(self) -> None:
        """Prints description of this item"""
        print("Use pepper spray in fight")

class Advice(Item):
    """
    Item that you can't put in your bag, it's just text

    Attributes:
        name (str): name of item
        advice (str): information that character told you

    Inheritance:
        Item:
    """

    def __init__(self, name: str, advice: str) -> None:
        super().__init__(name)
        self.advice = advice

    def __str__(self) -> str:
        return self.advice

class Wallet(Item):
    """
    Using this item you can store your money or change its amount

    Attributes:
        name (str):
        money (int): your money

    Inheritance:
        Item:
    """

    def __init__(self, name: str, money: int) -> None:
        super().__init__(name)
        self.money = money

    def get_money(self, amount: int) -> None:
        """Increases amount of your money"""
        self.money += amount
        print(f"Now you have {self.money} UAH")

    def spend_money(self, amount: int) -> None:
        """Decreases amount of your money"""
        self.money -= amount
        print(f"Now you have {self.money} UAH")

class Street():
    """
    Room with an enemy and items that you can take

    Attributes:
        name (str):
        description (str):
        adjacent_streets (list): rooms, where youu can
        item (Item): item that yo can take
        character (Character): Character that lives in the room
    """

    def __init__(self, name: str, ucu_distance: int) -> None:
        """Creates object with character and item inside"""
        self.name = name
        self.adjacent_streets = []
        self.character = None
        self.ucu_distance = ucu_distance

    def get_details(self) -> None:
        """Prints details about room"""
        print(self.name)
        print("-"*20)
        if self.adjacent_streets:
            print(f"You are on {self.name}")
            print("\n".join([room[0] for room in self.adjacent_streets]))

    def adjust_street(self, room: object, direction: str) -> None:
        """Add a room to the list of linked rooms"""
        self.adjacent_streets.append([f"The {room.name} is {direction}", room])

    def set_character(self, character: Character) -> None:
        """Adds character to the room"""
        self.character = character

    def get_character(self) -> Character:
        """Returns character from the room"""
        return self.character

    def move(self, direction: str) -> object:
        """Returns linked room in given direction"""
        for room in self.adjacent_streets:
            if direction in room[0]:
                return room[1]

class Enemy(Character):
    """
    Enemy character with which you can fight

    Attributes:
        defeats (int): amount of defeated enemies
        weakness (str): name of object that counters this character

    Inheritance:
        Character:
    """

    def __init__(self, name: str, description: str) -> None:
        super().__init__(name, description)
        self.weaknesses = []

    def set_weakness(self, item: Item) -> None:
        """Assigns a weakness to enemy"""
        self.weaknesses.append(item)

class Lodr(Enemy):
    """
    Enemy character, which you can beat with phone call and earn money for that

    Attributes:
        beatable (bool): if you can defeat this character

    Inheritance:
        Enemy:
    """

    def __init__(self, name: str, description: str) -> None:
        super().__init__(name, description)
        self.beatable = True

    def fight(self, weapon: str) -> int:
        """
        Returns amont of money as a result of fight

        Args:
            weapon (str): item that you use in fight

        Returns:
            int: amount of money as a reward
        """
        if weapon == self.weaknesses[0]:
            print("Police has arrested him and rewarded you with 50 UAH")
            return 50
        elif weapon == self.weaknesses[1]:
            print("He had mask under hood, so you lost")
        return 0

class Zbui(Enemy):
    """
    Enemy character, which you can beat with pepper spray and earn money for that

    Attributes:
        beatable (bool): if you can defeat this character

    Inheritance:
        Enemy:
    """

    def __init__(self, name: str, description: str) -> None:
        super().__init__(name, description)
        self.beatable = True

    def fight(self, weapon: str) -> int:
        """
        Returns amont of money as a result of fight

        Args:
            weapon (str): item that you use in fight

        Returns:
            int: amount of money as a reward
        """
        if weapon == self.weaknesses[0]:
            print("Police is busy")
        elif weapon == self.weaknesses[1]:
            print("You scared him, so he paid you 50 UAH to be safe")
            return 50
        return 0

class Batyar(Enemy):
    """
    The most powerful enemy, that you can't defeat

    Attributes:
        beatable (bool): if this character has any weknesses

    Inheritance:
        Enemy:
    """

    def __init__(self, name: str, description: str) -> None:
        super().__init__(name, description)
        self.beatable = False

class Friend(Character):
    """
    Character that has item, which he can give to you

    Attributes:
        help_cost (int): amount of money to trade for item 
        thing (Item): item to assign

    Inheritance:
        Character:
    """

    def __init__(self, name: str, description: str, help_cost: int) -> None:
        super().__init__(name, description)
        self.help_cost = help_cost
        self.thing = None

    def add_item(self, thing: Item) -> None:
        """Assigns an item to friendly character"""
        self.thing = thing

class Laidak(Friend):
    """
    Friendly class, that will tell you an advice if yo give him money for food

    Inheritance:
        Friend:
    """

    def help_player(self) -> None:
        """Gives you an advice"""
        print(self.thing)

class Kavaler(Friend):
    """
    Friendly character, that will give you pepperspray if you return his lost money

    Inheritance:
        Friend:

    """
    def help_player(self) -> Item:
        """Gives you a pepper spray"""
        print("Thank you. Take this pepper spray, cause it's dangerous at night")
        return self.thing
