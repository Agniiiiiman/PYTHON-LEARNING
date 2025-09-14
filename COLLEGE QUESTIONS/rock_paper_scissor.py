for _ in range(3):
    a = input("Player 1 (rock/paper/scissors): ")
    b = input("Player 2 (rock/paper/scissors): ")
    if a == b: print("Draw")
    elif (a == 'rock' and b == 'scissors') or (a == 'paper' and b == 'rock') or (a == 'scissors' and b == 'paper'):
        print("Player 1 wins")
    else:
        print("Player 2 wins")
