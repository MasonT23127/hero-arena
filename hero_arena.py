'''
    Author: Mason Twemlow
    Date: 15/10/2026
    Version 1.0
    Description: Hero Arena simulation game
'''



#----------libraries----------------------
import random
import datetime

#------functions-------------------------
def hero_roster():
    print("**..  Hero List:  ..**")
# "Name/title, Health, Attack, Defence, Weapon"
# Stats are 1-100. 1 being the worst possible and 100 is the best. 
# However, heroes must use all maximum points allocated. = 275 points

    heroes_list =["Legal Man", 70, 80, 65, 60, 
                "Window Face", 40, 100, 35, 100, 
                "Deploy", 70, 70, 70, 65,
                'Tanker', 100, 45, 100, 30,
                "Lava Palms", 65, 70, 70, 70,
                "Forceful", 60, 80, 40, 95]

    for i in range(0, len(heroes_list), 5):
        print(f"Name: {heroes_list[i]}")
        print(f"Health: {heroes_list[i+1]}")
        print(f"Attack: {heroes_list[i+2]}")
        print(f"Defence: {heroes_list[i+3]}")
        print(f"Weapon: {heroes_list[i+4]}")
        print("-----------------------------")



def add_hero(): #User can add their own hero to the roster
    print("**..  Add Your Hero:  ..**")
    name = input("Enter your hero's name/title: ")
    health = int(input("Enter your hero's health (1-100): "))
    attack = int(input("Enter your hero's attack (1-100): "))
    defence = int(input("Enter your hero's defence (1-100): "))
    weapon = int(input("Enter your hero's weapon (1-100): "))

#------main routine-------------------------
