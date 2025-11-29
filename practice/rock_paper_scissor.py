for _ in range (3):
    a=input("PLAYER 1(ROCK/PAPER/SCISSOR):")
    b=input("PLAYER 2(ROCK/PAPER/SCISSOR):")
    if a==b:
        print ("DRAW")
    elif(a=="ROCK" and b=="SCISSOR")    or   (a=="PAPER" and b=="ROCK")  or (a=="SCISSOR" and b=="PAPER"):
        print("PLAYER 1 WINS")
    else:
        print("PLAYER 2 WINS")