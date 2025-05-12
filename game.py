import random

choices = ['r', 'p', 's']
while True:
    userInput = input("Rock, Paper, Scissors? (r/p/s or q to quit): ").lower()

    if userInput == 'q':
        print("Thanks for playing!")
        break
    
    if userInput not in choices:
        print("Invalid input! Please choose r, p, or s.")
        continue

    systemInput = random.choice(choices)

    print("Your choice:", userInput)
    print("System choice:", systemInput)

    # Game logic
    if userInput == systemInput:
        print("It's a tie!")
    elif (userInput == 'r' and systemInput == 's') or \
         (userInput == 'p' and systemInput == 'r') or \
         (userInput == 's' and systemInput == 'p'):
        print("🎉 You win!")
    else:
        print("💻 System wins!")
