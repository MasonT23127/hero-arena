'''
    Author: Mason Twemlow
    Date: 15/10/2026
    Version 1.0
    Description: Hero Arena simulation game where the user can create, edit and fight heroes.
'''



#----------libraries----------------------
import random
import datetime
import string
import os

#------functions-------------------------

#These are the standard heroes
#User can add additonal or remove heroes if they'd like.
# "Name/title, Health, Attack, Defence, Weapon"
heroes_list =[  "Legal Man", 70, 80, 65, 60, 
                "Window Face", 40, 100, 35, 100, 
                "Deploy", 70, 70, 70, 65,
                'Tanker', 100, 45, 100, 30,
                "Lava Palms", 65, 70, 70, 70,
                "Forceful", 60, 80, 40, 95]



#View the Hero Roster
def hero_roster():
    print("**..  Hero List:  ..**")
# "Name/title, Health, Attack, Defence, Weapon"
# Stats are 1-100. 1 being the worst possible and 100 is the best. 
# However, heroes must use all maximum points allocated. = 275 points



    for i in range(0, len(heroes_list), 5):
        print(f"Name: {heroes_list[i]}")
        print(f"Health: {heroes_list[i+1]}")
        print(f"Attack: {heroes_list[i+2]}")
        print(f"Defence: {heroes_list[i+3]}")
        print(f"Weapon: {heroes_list[i+4]}")
        print("-----------------------------")


 

 #User can add their own hero to the roster
 # However, they must use all allocated points.
def add_hero():
    print("**..  Add Your Hero:  ..**")
    name = input("Enter your hero's name/title: ")
    health = int(input("Enter your hero's health (1-100): "))
    attack = int(input("Enter your hero's attack (1-100): "))
    defence = int(input("Enter your hero's defence (1-100): "))
    weapon = int(input("Enter your hero's weapon (1-100): "))

    #calculations if the user has entered 275 points
    total_points = health + attack + defence + weapon
    if total_points != 275:
        print("Error: Total points must equal 275. Please try again.")
        return

    new_hero = [name, health, attack, defence, weapon]
    heroes_list.extend(new_hero)
    print(f"New hero added: {new_hero}")
    



# Allows the user to edit any hero they'll like
def edit_hero():
    print("**..  Edit Heroes:  ..**")
    print("Here is the current hero roster:")
    hero_roster()
    hero_name = input("Enter the name of the hero you want to edit: ")

    # Find the hero in the roster
    for i in range(0, len(heroes_list), 5):
        if heroes_list[i] == hero_name:
            print(f"Editing hero: {heroes_list[i]}")
            print(f"Current Health: {heroes_list[i+1]}")
            print(f"Current Attack: {heroes_list[i+2]}")
            print(f"Current Defence: {heroes_list[i+3]}")
            print(f"Current Weapon: {heroes_list[i+4]}")
            print("-----------------------------")

        #now asking the user's input
            health = int(input("Enter new health: "))
            attack = int(input("Enter new attack: "))
            defence = int(input("Enter new defence: "))
            weapon = int(input("Enter new weapon: "))

            #changes the stats
            heroes_list[i+1] = health
            heroes_list[i+2] = attack
            heroes_list[i+3] = defence
            heroes_list[i+4] = weapon

            print(f"{hero_name} successfully updated.")
            return



# Allows the user to remove any hero they would like from the roster
#including their own heros that they have created.
def remove_hero():
    print("**.. Remove Heroes: ..**")
    print("Here is the current Hero Roster:")
    hero_roster()

    hero_name = input("Enter the name of the hero you want to remove: ")

    #Find hero in roster
    for i in range(0, len(heroes_list), 5):
        if heroes_list[i] == hero_name:
            print(f"Removing hero: {heroes_list[i]}")

            # remove the hero and the stats
            del heroes_list[i:i+5] # had to research how to delete

            print("Hero has been removed.")
            hero_roster()
            return


#Allows the user to battle heroes
#User will choose two heroes, and then will fight, which is done by taking turns.
#winner is determined by who reaches 0 health first.

def battle():
    print("**.. Battle ..**")
    



    print("Here is your current roster:")
    hero_roster()

    # First hero choice
    hero1 = input("Enter your first hero: ")
    for i in range(0, len(heroes_list), 5):
        if heroes_list[i] == hero1:
            print(f"Your first hero: {heroes_list[i]} ")
            health1 = heroes_list[i+1]
            attack1 = heroes_list[i+2]
            defence1 = heroes_list[i+3]
            weapon1 = heroes_list[i+4]
            print(f"Your first hero's stats - Health: {health1}, Attack: {attack1}, Defence: {defence1}, Weapon: {weapon1}")

    # Second hero choice
    hero2 = input("Enter your second hero: ")
    for i in range(0, len(heroes_list), 5):
        if heroes_list[i] == hero2:
            print(f"Your Second hero: {heroes_list[i]}")
            health2 = heroes_list[i+1]
            attack2 = heroes_list[i+2]
            defence2 = heroes_list[i+3]
            weapon2 = heroes_list[i+4]
            print(f"Your second hero's stats - Health: {health2}, Attack: {attack2}, Defence: {defence2}, Weapon: {weapon2}")


    change = input("Would you like to change your heroes? (y/n)")

    if change ==("y"):
        battle()
    else:
        print("The battle will now begin!")
        print(f"{hero1} vs {hero2}")
        print("Let the battle begin!")
   
   
   # Formula for damage
    # What damage the first hero does:
    damage1 = attack1 + weapon1 - defence2
    
    # What damage the second hero does:
    damage2 = attack2 + weapon2 - defence1




    #Random number, which will decrease attack damage
    rand_num = random.randint(50, 80)
    damage1 -= rand_num
    
    rand_num2 = random.randint(50, 80)
    damage2 -= rand_num
  
   
   
    print(f"Random number for {hero1}: {rand_num}. Final damage: {damage1}")
    health2 -=damage1
    print(f"Damaged {hero2} for {damage1}, they are now on {health2} health! ")


    
    print(f"Random number for {hero2}: {rand_num2}. Final damage: {damage2}")
    health -=damage2
    print(f"Damaged {hero1} for {damage2}, they are now on {health} health! ")




#------main routine-------------------------
if(__name__=="__main__"):
    battle()


