I = 44  # correct number
print("You cannot guess more than 5 times\n")
i = 1
while (i <= 5):
    X = int(input("\nEnter your guess\n"))
    if X > 44:
        print("\nYour no. is greater, choose a lesser no")
    elif X < 44:
        print("\nYour no. is less, choose a greater no")
    else:
        print("You choose the correct ans")
        print("Number of guesses took to finish", i)
        break
    print("Guess left", 5 - i)
    i = i + 1  # this line will increment the i by 1 until <=5 to the 3 line
    if i > 5:
        print("Game Over")


