import random
decider = random.randint(1,3)
computer_go = None
if decider == 1:
    computer_go = 'rock'
elif decider == 2:
    computer_go = 'paper'
elif decider == 3:
    computer_go = 'scissors'



while True:
    player_go = input("Pick 'rock', paper' or 'scissors'")
    if player_go == 'rock' or player_go == 'paper' or player_go == 'scissors':
        break
    else:
        print('pick an option')
print("The computer picked {}".format(computer_go))
print("You picked {}".format(player_go))


