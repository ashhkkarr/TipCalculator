import random
rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
'''
paper = '''

           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'  
          '''
scissors = '''
  ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
  '''
game_images = [rock, paper, scissors]
UserChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print('user choice')
print(game_images[UserChoice])
ComputerChoice = random.randint(0,2)
print('computer choice')
print(game_images[ComputerChoice])



if UserChoice == ComputerChoice:
  print('its a draw')
elif UserChoice == 0 and ComputerChoice == 1:
  print('you lose')
elif UserChoice == 0 and ComputerChoice == 2:
  print('you win')
elif UserChoice == 1 and ComputerChoice == 0:
  print('you win')
elif UserChoice == 1 and ComputerChoice == 2:
  print('you lose')
elif UserChoice == 2 and ComputerChoice == 0:
  print('you lose')
elif UserChoice == 2 and ComputerChoice == 1:
  print('you win')