import random

choices = ["Bear", "Hunter", "Ninja"]
Ultron = random.choice(choices)
Shinchan = False
Ultron_score = 0
Shinchan_score = 0

while True:
    Shinchan = input("Bear--Hunter--Ninja : ").capitalize()
    if Shinchan == Ultron:
        print("Tie!")
    elif Shinchan == "Bear":
        if Ultron == "Hunter":
            print("You lose!", Ultron, "Shoots the", Shinchan)
            Ultron_score+=1
        else:
            print("You win!", Shinchan, "Eats the", Ultron)
            Shinchan_score+=1
    elif Shinchan == "Hunter":
        if Ultron == "Ninja":
            print("You lose!", Ultron, "Kills the", Shinchan)
            Ultron_score+=1
        else:
            print("You win!", Shinchan, "Shoots the", Ultron)
            Shinchan_score+=1
    elif Shinchan == "Ninja":
        if Ultron == "Bear":
            print("You lose...", Ultron, "Eats the", Shinchan)
            Ultron_score+=1
        else:
            print("You win!", Shinchan, "Kills the", Ultron)
            Shinchan_score+=1
    elif Shinchan=='End':
        print("Final Scores:")
        print(f"Ultron:{Ultron_score}")
        print(f"Shinchan:{Shinchan_score}")
        break
