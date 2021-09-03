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



# Yes List
Yes = ["Yes", "yes", "Y", "y", "Sure", "sure", "Ye", "ye"]

# Starting Defines
Gold = 100
Health = 100
Stamina = 100
Stat_Points = 30
# Program Start
name = input("What is your name? \n")
if name in ["god","God"]:
  Gold = 99999
  Health = 99999
  Stamina = 99999
  Stat_Points = 99999
else: 
  if name in ["demigod","Demigod"]:
    Gold = 99999
    Stat_Points = 99999
print()
DiffNum = input("What difficulty would you like? \n 1 for very easy \n 2 for easy \n 3 for normal \n 4 for hard \n 5 for soul-crushing \n")





