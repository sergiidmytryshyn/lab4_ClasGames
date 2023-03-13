"""Module with main game loop"""

import game


opera = game.Street("Opera", 5)
mitskevycha = game.Street("Mitskevycha square",4)
romana = game.Street("Kn'az'a Romana", 3)
franka = game.Street("Ivana Franka", 2)
park = game.Street("Stryiskyi park", 1)

opera.adjust_street(mitskevycha, "ucu")
mitskevycha.adjust_street(opera, "centre")
mitskevycha.adjust_street(romana, "ucu")
romana.adjust_street(mitskevycha, "centre")
romana.adjust_street(franka, "ucu")
franka.adjust_street(romana, "centre")
franka.adjust_street(park, "ucu")
park.adjust_street(franka, "centre")


advice = game.Advice("Advice", "Be careful in park")

pepper_spray = game.PepperSpray("pepperspray")

phone = game.Phone("phone")

wallet = game.Wallet("wallet", 15)


laidak = game.Laidak("Laidak", "Oh, you met here homeless man", 15)
laidak.set_conversation("I need 15 UAH to buy a hotdog. In exchange i will give yo an advice")
laidak.add_item(advice)

opera.set_character(laidak)


kavaler = game.Kavaler("Kavaler",\
"Oh, two people walked through, and you found 50 UAH.\nTake it and go or help?", 50)
kavaler.set_conversation("Hello, I've lost 50 UAH, haven't u seen it")
kavaler.add_item(pepper_spray)

mitskevycha.set_character(kavaler)


lodr = game.Lodr("Lodr", "Some suspicious man in a hood")
lodr.set_weakness("phone")
lodr.set_weakness("pepperspray")
lodr.set_conversation("...")

romana.set_character(lodr)

zbui = game.Zbui("Zbui", "What a giant man, looks like he approaches")
zbui.set_weakness("phone")
zbui.set_weakness("pepperspray")
zbui.set_conversation("You think that you are stronger, c'mon, I'll show you")

franka.set_character(zbui)

batyar = game.Batyar("Batyar", "You were catched by madman called Orest The Wild")
batyar.set_conversation("Ha-ha-ha you lost")

park.set_character(batyar)


backpack = []
backpack.append(phone)
backpack.append(wallet)


current_room = opera

DEAD = False

print("""Hello, you were in theatre and now you have to get to Colegium.
It is late, so there are no buses. You can go by foot or taxi.
You have only 15 UAH, but it is not enough for such long taxi drive,
so you should go closer to UCU, to make your ride cheaper.\n
""")

print("""Use commands below to play my game:
'talk' - talk to character
'help' - help friendly character
'fight' - fight enemy
'take' - take something from ground
'ucu' - go closer to UCU
'centre' - go closer to centre
'taxi' - call taxi to get home safely
"""
    )
while not DEAD:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("->")

    if command in ["ucu", "centre"]:
        # Move in the given direction
        if isinstance(current_room.get_character(), game.Enemy):
            # You lose if you try to escape from enemy
            attacker = current_room.get_character().name
            print(f"Oh no, you tried to escape, but {attacker} attacked you")
            print("You lost")
            DEAD = True
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        fighting = True
        while fighting:
            #
            if isinstance(inhabitant, game.Enemy):
                # Fight with the inhabitant, if there is one
                weapons = [item.name for item in backpack]
                print(f"You have {weapons} in your backpack")
                print("What will you fight with?")
                fight_with = input()
                # Do I have this item?
                if fight_with in weapons:
                    # Get money if you win
                    result = inhabitant.fight(fight_with)
                    if result:
                        print("Hooray, you won the fight!")
                        wallet.get_money(result)
                    # Game ends if you lose
                    else:
                        print("Oh, you lost the fight.")
                        print("That's the end of the game")
                        DEAD = True
                    current_room.set_character(None)
                    fighting = False
                else:
                    print("You don't have a " + fight_with)
            else:
                print("There is no one here to fight with")
    elif command == "help":
        # Help character, check if he is friedly
        if isinstance(inhabitant, game.Friend):
            # Check if you have enough money to help him
            if wallet.money >= inhabitant.help_cost:
                wallet.spend_money(inhabitant.help_cost)
                help_character = inhabitant.help_player()
                # Recieve something as gratitude
                if help_character:
                    backpack.append(help_character)
                    print(f"You took {backpack[-1].get_name()}")
                current_room.set_character(None)
            else:
                print(f"You need {inhabitant.help_cost}, but have {wallet.money}")
    # Call taxi to UCU
    elif command == "taxi":
        length = current_room.ucu_distance
        requirements = phone.taxi_call(wallet.money, length)
        # Check if you have enough money
        if requirements:
            print("Congrats, you won and got to UCC!")
            DEAD = True
    elif command == "take":
        # Take money from ground
        if wallet.money < 50:
            wallet.get_money(50)
    else:
        print("I don't know how to " + command)
