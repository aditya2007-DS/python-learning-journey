# Simple Guess Attempts Counter

correct = 7

for attempt in range(1, 4):
    guess = int(input("Guess: "))
    if guess == correct:
        print("Correct!")
        break
    else:
        print("Try again")