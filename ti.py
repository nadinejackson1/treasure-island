print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island. Your sole mission bestowed upon you is to find the hidden treasure.\n")

first_choice = input("It is time for you to make an important decision. Which way does thou choose to travel? Left or Right \n").lower()

if first_choice == "left":
  print("You have made a wise choice. Now it is time to decide your next route.\n")
else:
  print("The bottomless pit of earth worms has consumed you. Game Over.\n")

second_choice = input("You have come to a lake. There is a boat but it is in the middle of the lake. Would you like to swim or wait? \n").lower()

if second_choice == "wait":
  print("Another wise choice! Your grandmother must be so proud.\n")
else:
  print("Once there was a fish, a wild one at that. A big fish with lots of colors, big teeth and a spiny back. Turns out this colorful fish wasn't a friend, but a foe. It took a giant bite out of your pretty little toe. Game Over.\n")

third_choice = input("You have arrived at an ancient portal. You must make a decision which could change your life forever. Which door do you choose? Red, Blue or Yellow? \n").lower()

if third_choice == "red":
  print("FLAMES EVERYWHERE!!!! Save yourself! ... Game Over.\n")

elif third_choice == "blue":
  print("Looks like it's dinner time. Except, you are on the menu and the beasts have a fine meal planned of you. Game Over.\n")

elif third_choice == "yellow":
  print("*Cue music* Weeee are the champions, my friend! You Win!\n")

else:
  print("Nothing exciting to see here. Game Over.\n")
