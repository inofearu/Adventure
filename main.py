# Modules
import random
import time
from colorama import Fore
from colorama import Style
from colorama import Back
def sleep():
    t = random.randint(0, 5)
    time.sleep(t)
#developer switch
switch = 0
# functions and lists

#player level stuff
player_level = 1
player_xp = 0

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

def dcontinueq():
  global continueq
  global stat_points
  print('\nYou still have', stat_points, 'stat points left, if you continue now you will lose them\n Continue? Y/N\n')
  continueq = input('> ')
  continueq = continueq.lower()
  if continueq in ["y","n"]:
    if continueq in ['y']:
      print('\nOk, Voiding stat points...\n')
      stat_points = 0
    if continueq in ['n']:
      redo = input('\nRedo stat point allocation? Y/N\n> ')
      redo = redo.lower()
      if redo in ['y','n']:
        if redo in ['y']:
          print('redoing...\n')
          stat_point_assign()
        else:
          dcontinueq()
      else:
        print('Answer has to be Y or N\n')
        dcontinueq()
  else:
    print('Answer has to be Y or N\n')
    dcontinueq()

def redocontinuem():
  redocontinue = input('\nRedo or Continue? R/C\n> ')
  redocontinue = redocontinue.lower()
  if redocontinue in ['r','c']:
    if redocontinue in ['r']:
      stat_point_assign()
    else:
      print('\nContinuing...\n')
  else:
    print('Answer has to be R or C\n')
    redocontinuem()
# Yes List
Yes = ["Yes", "yes", "Y", "y", "Sure", "sure", "Ye", "ye"]

# Starting Defines
gold = 100
health = 100
stamina = 100
stat_points = 30
# Program Start
def name_selection():
  global name
  name = input("What is your name? \n> ")
name_selection()
# difficulty select
def difficulty_select():
 print()
 print("What difficulty would you like? \n 1 for very easy \n 2 for easy \n 3 for normal \n 4 for hard", Fore.RED,"\n 5 for soul-crushing \n")
 print(Style.RESET_ALL)
difficulty_select()
# difficulty conversion
def difficulty_setting():
 global difficulty_number
 difficulty_number = str(input("> "))
 if difficulty_number in ["1", "2", "3", "4", "5", "6"]: 
   difficulty_number = int(difficulty_number)
   if difficulty_number == 1:
     very_easy()
   if difficulty_number == 2:
     easy() 
   if difficulty_number == 3:
     normal()
   if difficulty_number == 4:
     hard()
   if difficulty_number == 5:
     soul_crushing()
   if difficulty_number == 6:
     secret()
     print(Fore.RED)
     print(Back.BLACK)
     print('What have you done')
     print(Style.RESET_ALL)
 else: 
   print("This has to be between 1 and 5, please put a new number in")
   difficulty_setting()
difficulty_setting()
global base_points
base_points = stat_points
# dev mode
if name in ["god","God"]:
  gold = 99999
  phealth = 99999
  pstamina = 99999
  base_points = 99999
else: 
  if name in ["demigod","Demigod"]:
    Gold = 99999
    base_points = 99999
zeroten = ["0","1","2","3","4","5","6","7","8","9","10"]
# initial stat assignment
def stat_point_assign():
  global strength
  global perception
  global endurance
  global charisma
  global intelligence
  global agility
  global luck
  global stat_points
  if stat_points < base_points:
    stat_points = base_points
  if stat_points > base_points:
    stat_points = base_points
  print ('Allocate your stat points!')
  print('You have', stat_points, 'stat points\n')
  stat_points = int(stat_points)
  # strength
  strength = str(input('How many points do you want in strength? \n'))
  if strength in zeroten:
    strength = int(strength)
    stat_points = stat_points - strength
    print('You have',stat_points, 'stat points left') 
  else:
    print('Please pick a number between 0 and 10\n')
    stat_points = base_points
    stat_point_assign()
  # perception
  perception = str(input('How many points do you want in perception? \n'))
  if perception in zeroten:
    perception = int(perception)
    stat_points = stat_points - perception
    print('You have',stat_points, 'stat points left') 
  else:
    print('Please pick a number between 0 and 10\n')
    stat_points = base_points
    stat_point_assign()
  # endurance
  endurance = str(input('How many points do you want in endurance? \n'))
  if endurance in zeroten:
    endurance = int(endurance)
    stat_points = stat_points - endurance
    print('You have',stat_points, 'stat points left') 
  else:
    print('Please pick a number between 0 and 10\n')
    stat_points = base_points
    stat_point_assign()
  # charisma
  charisma = str(input('How many points do you want in charisma? \n'))
  if charisma in zeroten:
    charisma = int(charisma)
    stat_points = stat_points - charisma
    print('You have',stat_points, 'stat points left') 
  else:
    print('Please pick a number between 0 and 10\n')
    stat_points = base_points
    stat_point_assign()
  # intelligence
  intelligence = str(input('How many points do you want in intelligence? \n'))
  if intelligence in zeroten:
    intelligence = int(intelligence)
    stat_points = stat_points - intelligence
    print('You have',stat_points, 'stat points left') 
  else:
    print('Please pick a number between 0 and 10\n')
    stat_points = base_points
    stat_point_assign()
  # agility
  agility = str(input('How many points do you want in agility? \n'))
  if agility in zeroten:
    agility = int(agility)
    stat_points = stat_points - agility
    print('You have',stat_points, 'stat points left') 
  else:
    print('Please pick a number between 0 and 10\n')
    stat_points = base_points
    stat_point_assign()
  # luck
  luck = str(input('How many points do you want in luck? \n'))
  if luck in zeroten:
    luck = int(luck)
    stat_points = stat_points - luck 
  else:
    print('Please pick a number between 0 and 10\n')
    stat_points = base_points
    stat_point_assign()
  # stat points below 0 error
  if stat_points < 0:
    print('Error, negative stat points. Please redo.')
    stat_point_assign()
  print(stat_points, 'stat points left')
  print('Strength -', strength)
  print('Perception -', perception)
  print('Endurance -', endurance)
  print('Intelligence -', intelligence)
  print('Agility -', agility)
  print('Luck -', luck)
  if stat_points > 0:
    dcontinueq()
  redocontinuem()
  if switch == 1:
    print('\nMESSAGE- Due to you being in dev mode, you can choose to set all your stats to whatever you wish now but be careful not to input any letters!\n Change stats? Y/N\n')
    devmodestats = str(input('> '))
    devmodestats = devmodestats.lower()
    if devmodestats in ['y','n']:
      if devmodestats in ['y']:
        strength = int(input('Strength > '))
        perception = int(input('Perception > '))
        endurance = int(input('Endurance > '))
        intelligence = int(input('Intelligence > '))
        agility = int(input('Agility > '))
        luck = int(input('Luck > '))
stat_point_assign()