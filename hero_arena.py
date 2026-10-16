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
    
#------main routine-------------------------
