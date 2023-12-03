import random
decider = random.randint(1,3)
go = None
if decider == 1:
    go = 'rock'
elif decider == 2:
    go = 'paper'
elif decider == 3:
    go = 'scissors'
print(go)

