import random
player_score = 0
computer_score = 0


print("Welcome to Rock Paper Scissors Terminal-Game")
print("You will battle against the notorious computer")
print("The first one to win 5 battles is Victorious.")


while player_score < 5 and computer_score < 5:
    decider = random.randint(1,3)
    computer_go = None
    if decider == 1:
        computer_go = 'rock'
    elif decider == 2:
        computer_go = 'paper'
    elif decider == 3:
        computer_go = 'scissors'
    while True:
        player_go = input("Pick your weapon! \nRock \nPaper \nScissors")
        player_go.lower()
        if player_go == 'rock' or player_go == 'paper' or player_go == 'scissors':
            break
        else:
            print('pick an option')

    print("Rock! Paper! Scissors! Shoot!")
    print("You picked {}".format(player_go))
    print("The computer picked {}".format(computer_go))



    if player_go == "rock" and computer_go == "scissors":
        player_score += 1 
        print("You get a point! :)" )
    elif player_go == "scissors" and computer_go == "paper":
        player_score += 1 
        print("You get a point! :)")
    elif player_go == "paper" and computer_go == "rock":
        player_score += 1 
        print("You get a point! :)")

    if player_go == "rock" and computer_go == "rock":
        print("Its a draw! Nobody gets a point")
    elif player_go == "scissors" and computer_go == "scissors":
        print("Its a draw! Nobody gets a point")
    elif player_go == "paper" and computer_go == "paper":
        print("Its a draw! Nobody gets a point")


    if player_go == "rock" and computer_go == "paper":
        computer_score += 1 
        print("Computer gains a point! :(")
    elif player_go == "scissors" and computer_go == "rock":
        computer_score += 1 
        print("Computer gains a point! :(")
    elif player_go == "paper" and computer_go == "scissors":
        computer_score += 1 
        print("Computer gains a point! :(")
print(player_score)
print(computer_score)
