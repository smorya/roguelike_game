import classes

red_square = classes.Location("Red Square")
red_square.set_description("A main place where you can meet russians. Attention! Many cops.")

mauzoleum = classes.Location("Lenin's  mauzoleum")
mauzoleum.set_description("Here lies oppressor and the guy who started the jail of folks.")

church = classes.Location("Moscow patriarchate church")
church.set_description("Beware, these people aren't holy. They support war. ")

kremle = classes.Location("Kremle")
kremle.set_description("Here sits putin, your main enemy.")

weapon = classes.Location("Weapon storage ")
weapon.set_description("Here they store their weapon.")

red_square.link_room(mauzoleum, "west")
red_square.link_room(weapon, "north")
red_square.link_room(church, "south")

bandera = classes.Ally("Stepan Bandera", "Your coach that explains.")
bandera.set_conversation("""
Slava Ukraini!
Visit all locations, collect all items and kill enemies.
Remember:
holy water kills pope
uranium kills soldier
history book kills propagandist-professor
javeline kills lenin

If you kill at least 2/3 you can kill putin with 
Ukrainian anthem.
Good luck!
""")
red_square.set_character(bandera)

anthem = classes.Item("anthem")
anthem.set_description("Ukrainian national anthem")
red_square.set_item(anthem)

mauzoleum.link_room(kremle, "west")
mauzoleum.link_room(red_square, "east")

lenin = classes.Enemy("lenin", "Socialist zombie-tyrant")
lenin.set_conversation("I created Ukraine buaaaa unite proletaries!")
lenin.set_weakness("javeline")
mauzoleum.set_character(lenin)

water = classes.Item("holy water")
water.set_description("Holy water from Halychyna")
mauzoleum.set_item(water)



church.link_room(red_square, "north")

pope = classes.Enemy("Moscow pope", "Lies, cruelty and hypocrisy.")
pope.set_conversation("Military operation is a God's will! We save Ukraine.")
pope.set_weakness("holy water")
church.set_character(pope)

uranium = classes.Item("uranium")
uranium.set_description("Radioactive present from Chornobyl")
church.set_item(uranium)



weapon.link_room(red_square, "south")

soldier = classes.Enemy("Soldier", "Killer, rapist, monster")
soldier.set_conversation("I want to steal your washing mashine")
soldier.set_weakness("uranium")
weapon.set_character(soldier)

javeline = classes.Item("javeline")
javeline.set_description("Bang bang bang")
weapon.set_item(javeline)



kremle.link_room(mauzoleum, "east")

putin = classes.Enemy("putin", "Tyrant without brains")
putin.set_conversation("special military operation and peace")
putin.set_weakness("anthem")
kremle.set_character(putin)





current_loc = red_square
backpack = []

dead = False

print("""
__________________
Greatings, dear fellow!
Today you will kill putin and bad russians
Find Stepan Bandera and listen to his instructions to win.
___________________""")
while dead == False:

    current_loc.get_details()
    inhabitant = current_loc.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_loc.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_loc = current_loc.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            if inhabitant == putin and inhabitant.get_defeated() < 2:
                print("You haven't killed two to start.")
            else:
                
                # Fight with the inhabitant, if there is one
                print("What will you fight with?")
                fight_with = input().lower()

                # Do I have this item?
                if fight_with in backpack:

                    if inhabitant.fight(fight_with) == True:
                        # What happens if you win?
                        print("Hooray, you won the fight!")
                        current_loc.character = None

                        if inhabitant.get_defeated() >= 2 and kremle.character == None :
                            print("Congratulations, you have vanquished the enemy horde!")
                            dead = True
                    else:
                        # What happens if you lose?
                        print("Oh dear, you lost the fight.")
                        print("That's the end of the game")
                        dead = True
                else:
                    print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_loc.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)