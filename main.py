import random

print("1.Start game     2.Quit")
print()
start = int(input("Enter your choice : "))
print()
cp_1 = 0
cp_2 = 0

if start == 1:
    player_1 = input("Enter player 1 name : ")
    print()
    player_2 = input("Enter player 2 name : ")
    print()
    print("Welcome to the game", player_1, "and", player_2)
    print()

    # Randomly select starting player
    if random.randint(0, 1) == 0:
        current_player = player_1
    else:
        current_player = player_2

    while True:
        if current_player == player_1:
            print(player_1, "1.Roll the dice  2.Quit")
            print()
            roll_dice = int(input("Enter your choice : "))
            print()
            if roll_dice == 1:
                dice = random.randint(1, 6)
                print("You got : ", dice)
                print()
                cp_1 = cp_1 + dice

                # Ladder logic for Player 1
                if cp_1 == 9:
                    cp_1 = 15
                    print("Congrats!", player_1, "got a ladder and reached on : ", cp_1)
                    print()
                elif cp_1 == 18:
                    cp_1 = 23
                    print("Congrats!", player_1, "got a ladder and reached on : ", cp_1)
                    print()
                elif cp_1 == 36:
                    cp_1 = 41
                    print("Congrats!", player_1, "got a ladder and reached on : ", cp_1)
                    print()
                elif cp_1 == 27:
                    cp_1 = 54
                    print("Congrats!", player_1, "got a ladder and reached on : ", cp_1)
                    print()
                elif cp_1 == 58:
                    cp_1 = 65
                    print("Congrats!", player_1, "got a ladder and reached on : ", cp_1)
                    print()

                # Snake logic for Player 1
                elif cp_1 == 5:
                    cp_1 = 1
                    print("Sorry", player_1, "was bitten by a snake and reached on : ", cp_1)
                    print()
                elif cp_1 == 24:
                    cp_1 = 10
                    print("Sorry", player_1, "was bitten by a snake and reached on : ", cp_1)
                    print()
                elif cp_1 == 40:
                    cp_1 = 1
                    print("Sorry", player_1, "was bitten by a snake and reached on : ", cp_1)
                    print()
                elif cp_1 == 33:
                    cp_1 = 23
                    print("Sorry", player_1, "was bitten by a snake and reached on : ", cp_1)
                    print()
                elif cp_1 == 92:
                    cp_1 = 8  
                    print("Sorry", player_1, "was bitten by a snake and reached on : ", cp_1)
                    print()

                print(player_1, "Your current position is : ", cp_1)
                print()

                # Check win condition after all movements
                if cp_1 >= 100:
                    print(player_1, "You won")
                    break

                # Switch turn only after player's action is fully complete
                current_player = player_2

            else:
                print("You got quit")
                break

        else:
            # Player 2 Logic
            print(player_2, "1.Roll the dice  2.Quit")
            print()
            roll_dice = int(input("Enter your choice : "))
            print()
            if roll_dice == 1:
                dice = random.randint(1, 6)
                print("You got : ", dice)
                print()
                cp_2 = cp_2 + dice

                # Ladder logic for Player 2
                if cp_2 == 9:
                    cp_2 = 15
                    print("Congrats!", player_2, "got a ladder and reached on : ", cp_2)
                    print()
                elif cp_2 == 18:
                    cp_2 = 23
                    print("Congrats!", player_2, "got a ladder and reached on : ", cp_2)
                    print()
                elif cp_2 == 36:
                    cp_2 = 41
                    print("Congrats!", player_2, "got a ladder and reached on : ", cp_2)
                    print()
                elif cp_2 == 27:
                    cp_2 = 54
                    print("Congrats!", player_2, "got a ladder and reached on : ", cp_2)
                    print()
                elif cp_2 == 58:
                    cp_2 = 65
                    print("Congrats!", player_2, "got a ladder and reached on : ", cp_2)
                    print()

                # Snake logic for Player 2
                elif cp_2 == 5:
                    cp_2 = 1
                    print("Sorry", player_2, "was bitten by a snake and reached on : ", cp_2)
                    print()
                elif cp_2 == 24:
                    cp_2 = 10
                    print("Sorry", player_2, "was bitten by a snake and reached on : ", cp_2)
                    print()
                elif cp_2 == 40:
                    cp_2 = 1
                    print("Sorry", player_2, "was bitten by a snake and reached on : ", cp_2)
                    print()
                elif cp_2 == 33:
                    cp_2 = 23
                    print("Sorry", player_2, "was bitten by a snake and reached on : ", cp_2)
                    print()
                elif cp_2 == 92:
                    cp_2 = 8
                    print("Sorry", player_2, "was bitten by a snake and reached on : ", cp_2)
                    print()

                print(player_2, "Your current position is : ", cp_2)
                print()

                # Check win condition after all movements
                if cp_2 >= 100:
                    print(player_2, "You won")
                    break

                # Switch turn back to Player 1
                current_player = player_1

            else:
                print("You got quit")
                break

else:
    print("You got quit")
