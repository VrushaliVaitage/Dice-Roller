import random


dice_pic = {
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│  ●      │",
       "│         │",
       "│      ●  │",
       "└─────────┘"),
    3:("┌─────────┐",
       "│  ●      │",
       "│    ●    │",
       "│      ●  │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│  ●   ●  │",
       "│         │",
       "│  ●   ●  │",
       "└─────────┘"), 
    5:("┌─────────┐",
       "│  ●   ●  │",
       "│    ●    │",
       "│  ●   ●  │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│  ●   ●  │",
       "│  ●   ●  │",
       "│  ●   ●  │",
       "└─────────┘"),   

}

dice_list = []
total=0
no_of_dice=int(input("How many dice you want? "))


for i in range(no_of_dice):
   dice_list.append(random.randint(1,6))

# vertical representation
# for i in range(no_of_dice):
#    for line in dice_pic.get(dice_list[i]):
#       print(line)

# Horizontal representation 
for line in range(5):
   for die in dice_list:
      print(dice_pic.get(die)[line], end="")
   print()
   
for i in dice_list:
   total=total+i
print(f'total: {total}')







# print("\u25CF \u250C \u2500  \u2510  \u2502 \u2514 \u2518")
#  ● ┌ ─  ┐  │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"