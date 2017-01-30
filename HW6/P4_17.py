import random

player = eval(input("scissor (0), rock (1), paper (2): "))
computer = random.randint(0, 2)

if player > 2:
    print("Invaild Input!")
else:
    if player == 0:
        if computer == 0:
            print("The computer is scissor. You are scissor too. It is a draw.")
        elif computer == 1:
            print("The computer is rock. You are scissor. You lost.")
        else:
            print("The computer is paper. You are scissor. You won.")
    if player == 1:
        if computer == 0:
            print("The computer is scissor. You are rock. You won.")
        elif computer == 1:
            print("The computer is rock. You are rock too. It is a draw.")
        else:
            print("The computer is paper. You are rock. You lost.")
    if player == 2:
        if computer == 0:
            print("The computer is scissor. You are paper. You lost.")
        elif computer == 1:
            print("The computer is rock. You are paper. You won.")
        else:
            print("The computer is paper. You are paper too. It is a draw.")
