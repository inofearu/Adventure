# Modules
import random
import time
from colorama import Fore
from colorama import Style
from colorama import Back
def sleep():
    t = random.randint(0, 5)
    time.sleep(t)

# functions and lists

# Difficultys

# very easy
def very_easy():
  #modifiers
  global enemy_health_modifier
  enemy_health_modifier = 0.5
  global loot_quality 
  loot_quality = 1
  global loot_amount
  loot_amount = 1
  global drop_chance
  drop_chance = 1
  global player_health_modifier
  player_health_modifier = 1.5
  global gold_loot_amount
  gold_loot_amount = 2
  global story_cake_end
  story_cake_end = 1
  global encounter_rate_modifier
  encounter_rate_modifier = 0.8
  global stat_points
  stat_points = 50

# easy
def easy():
  #modifiers
  global enemy_health_modifier
  enemy_health_modifier = 1
  global loot_quality 
  loot_quality = 1
  global loot_amount
  loot_amount = 1
  global drop_chance
  drop_chance = 1
  global player_health_modifier
  player_health_modifier = 1
  global gold_loot_amount
  gold_loot_amount = 1
  global story_cake_end
  story_cake_end = 0
  global encounter_rate_modifier
  encounter_rate_modifier = 0.9
  global stat_points
  stat_points = 40
  
# normal
def normal():
  #modifiers
  global enemy_health_modifier
  enemy_health_modifier = 1
  global enemy_damage
  enemy_damage = 1
  global loot_quality 
  loot_quality = 1
  global loot_amount
  loot_amount = 1
  global drop_chance
  drop_chance = 1
  global player_health_modifier
  player_health_modifier = 1
  global gold_loot_amount
  gold_loot_amount = 1
  global story_cake_end
  story_cake_end = 0
  global encounter_rate_modifier
  encounter_rate_modifier = 1
  global stat_points
  stat_points = 30
  
# hard
def hard():
  #modifiers
  global enemy_health_modifier
  enemy_health_modifier = 1.2
  global loot_quality 
  loot_quality = 1.1
  global loot_amount
  loot_amount = 0.75
  global drop_chance
  drop_chance = 1
  global player_health_modifier
  player_health_modifier = 0.8
  global gold_loot_amount
  gold_loot_amount = 0.75
  global story_cake_end
  story_cake_end = 0
  global encounter_rate_modifier
  encounter_rate_modifier = 1.1
  global stat_points
  stat_points = 20

# soul-crushing
def soul_crushing():
  
  #modifiers
  global enemy_health_modifier
  enemy_health_modifier = 1
  global loot_quality  
  loot_quality = 1.15
  global loot_amount
  loot_amount = 1
  global drop_chance
  drop_chance = 1
  global player_health_modifier
  player_health_modifier = 1
  global gold_loot_amount
  gold_loot_amount = 1
  global story_cake_end
  story_cake_end = 0
  global encounter_rate_modifier
  encounter_rate_modifier = 10
  global stat_points
  stat_points = 10

# secret
def secret():
   global enemy_health_modifier
   enemy_health_modifier = 100
   global loot_quality 
   loot_quality = 0.00001
   global loot_amount
   loot_amount = 0.000001
   global drop_chance
   drop_chance = 0.0000001
   global player_health_modifier
   player_health_modifier = 0.001
   global gold_loot_amount
   gold_loot_amount = 0
   global story_cake_end
   story_cake_end = 0
   global encounter_rate_modifier
   encounter_rate_modifier = 10000
   global stat_points
   stat_points = 0



# Yes List
Yes = ["Yes", "yes", "Y", "y", "Sure", "sure", "Ye", "ye"]

# Starting Defines
gold = 100
health = 100
stamina = 100
stat_points = 30
# Program Start
name = input("What is your name? \n> ")
if name in ["god","God"]:
  gold = 99999
  phealth = 99999
  pstamina = 99999
  stat_points = 99999
else: 
  if name in ["demigod","Demigod"]:
    Gold = 99999
    stat_points = 99999
print()
print("What difficulty would you like? \n 1 for very easy \n 2 for easy \n 3 for normal \n 4 for hard", Fore.RED,"\n 5 for soul-crushing \n")
print(Style.RESET_ALL)
def difficulty_setting():
 global diffnum
 diffnum = str(input())
 if diffnum in ["1", "2", "3", "4", "5", "6"]: 
   diffnum = int(diffnum)
   if diffnum == 1:
     very_easy()
   if diffnum == 2:
     easy() 
   if diffnum == 3:
     normal()
   if diffnum == 4:
     hard()
   if diffnum == 5:
     soul_crushing()
   if diffnum == 6:
     secret()
     print(Fore.RED)
     print(Back.BLACK)
     print('What have you done')
     print(Style.RESET_ALL)
 else: 
   print("This has to be between 1 and 5, please put a new number in")
   difficulty_setting()
difficulty_setting()
def stat_point_assign():
  global stat_points
  print ('Allocate your stat points!')
  print('You have', stat_points)
  stat_points = int(stat_points)
  strength = int(input('How many points do you want in strength? \n'))
  if strength in range(0,10):
    print('Please pick a number between 0 and 10')
    stat_point_assign()
  stat_points = stat_points - strength
  print('You have',stat_points, 'left')
  perception = int(input('How many points do you want in perception? \n'))
  if perception in range(0,10):
    print('Please pick a number between 0 and 10')
    stat_point_assign()
  stat_points = stat_points - perception
  print('You have',stat_points, 'left')
  endurance = int(input('How many points do you want in endurance? \n'))
  if endurance in range(0,10):
    print('Please pick a number between 0 and 10')
    stat_point_assign()
  stat_points = stat_points - endurance
  print('You have',stat_points, 'left')
  charisma = int(input('How many points do you want in charisma? \n'))
  if charisma in range(0,10):
    print('Please pick a number between 0 and 10')
    stat_point_assign()
  stat_points = stat_points - charisma
  print('You have',stat_points, 'left')
  intelligence = int(input('How many points do you want in intelligence? \n'))
  if intelligence > 10:
    print('Please pick a number between 0 and 10')
    stat_point_assign()
  stat_points = stat_points - intelligence
  print('You have',stat_points, 'left')
  agility = int(input('How many points do you want in agility? \n'))
  if agility > 10:
    print('Please pick a number between 0 and 10')
    stat_point_assign()
  stat_points = stat_points - agility
  print('You have',stat_points, 'left')
  luck = int(input('How many points do you want in luck? \n'))
  if luck > 10:
    print('Please pick a number between 0 and 10')
    stat_point_assign()
  stat_points = stat_points - luck
  if stat_points < 0:
    print('Error, negative stat points. Please redo.')
    stat_points = stat_points + strength + perception + endurance + charisma + intelligence + agility + luck
    stat_point_assign()
stat_point_assign()