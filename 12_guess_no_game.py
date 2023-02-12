secret = 7
idx = 0
limit = 3
while idx < limit:
    guess = int(input('Guess: '))
    idx += 1
    if guess == secret:
        print("Congo! You won!")
        break
else:
    print("Oops! chances over!")