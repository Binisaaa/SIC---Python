print("let's play some gamesssss")
print("which game do u wanna play?")
print(" 1.fibonacci generator \n 2. fizzbuzz \n 3. rock paper scissors \n 4. number guessing game ")
choice = int(input("enter the number corresponding to the game you wanna play: "))
if choice == 4:
        import random
        answer = random.randint(1, 100)
        i = 0
        while True:
            guess = int(input("Guess: "))
            i = i+1
        if guess > answer:
            print("Too high")
        elif guess < answer:
            print("Too low")
        else:
            print("Congratulations. total try = ",i)
elif choice == 3:
    import random
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
    else:
        computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
elif choice == 2:
    print("this is fizzbuzz game where computer prints fizz for number divisible by 3 and prints buzz for numbers divisible by 5 and prints fizzbuzz for numbers divisible by both 3 and 5")
    for i in range(1,101):
        if i % 3 ==0 and i % 5 ==0:
            print("fizbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
elif choice == 1:
    n = int(input("enter how many fibonacci numbers you want: "))
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b