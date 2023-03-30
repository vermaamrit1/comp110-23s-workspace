"""EX06 - Choose Your Own Adventure."""

__author__ = "730451631"


points: int = 0
player: str = ""
angry: str = "\U0001F92C"
goat: str = "\U0001F410"
eyes: str = "\U0001F440"
fire: str = "\U0001F525"
party: str = "\U0001F973"
smile: str = "\U0001F603"


def main() -> None:
    """Main function that runs entire program."""
    global points
    greet()
    choice = input("Are you a UNC sports fan? ")
    if choice != "Yes" and choice != "No":
        print("No worries! \nIf you would like to play again or have a friend play, re-enter your name:")   
    while choice == "Yes":
        print(f"Good choice {goat}! But lets see if you're a true UNC superfan. ")
        truefan()
        choice = input("Congratulations, you completed the quiz. If you or a friend would like to take it again, type Yes! ")
    if choice == "No":
        print(f"Wrong answer {angry}, you're stupid... So here's a stupid game.")
        simpleminded()
    

def greet() -> None: 
    """Print welcome message where you can input character name."""
    global player
    player = input("Enter a player name: ")
    print((f"Welcome, {player}! "))
   

def truefan() -> None:
    """Prints second trivia question, calls next question if you get it right, or repeats question if you get it wrong."""
    global points
    mvp2017 = input("Who was the MVP of the 2017 NCAA National Championship Game? ")
    if mvp2017 == "Joel Berry":
        points += 1
        print(f"Correct! You have earned a point. {party} \nTotal points: {points} ")
        return worldcups()
    else:
        points -= 1
        print(f"Incorrect! You have lost a point. Get one more question wrong, and you're a fake fan. \nTotal points: {points}")
        truefan()


def worldcups() -> None:
    """Prints third trivia question, calls next question if you get it right, or repeats question if you get it wrong."""
    global points
    miahamm = input("What UNC womens soccer player won 2 world cups with the USWNT? ")
    if miahamm == "Mia Hamm":
        points += 1
        print(f"Impressive! {party} Can you keep the streak going? \nTotal points: {points}")
        return natty()
    else:
        points -= 1
        print(f"Sorry, that is incorrect. You have lost a point. Try again. \nTotal points: {points}")
        return worldcups()


def natty() -> None:
    """Prints fourth trivia question, calls next question if you get it right, or repeats question if you get it wrong."""
    global points
    natty1957 = input("What UNC basketball coach won the 1957 NCAA Basketball National Championship? ")
    if natty1957 == "Frank McGuire":
        points += 1
        print(f"Congrats! {party} You've almost proven yourself to be a UNC superfan. Let's see if you can get the final two right. \nTotal points: {points}")
        return puntreturn()
    else:
        points -= 1
        print(f"Sorry, that is incorrect. You have lost a point. Try again. \nTotal points: {points}")
        return natty()


def puntreturn() -> None:
    """Prints fifth trivia question, calls next question if you get it right, or repeats question if you get it wrong."""
    global points
    statesucks = input("What is the name of the UNC football player that scored a game winning punt return against NC State in 2012? ")
    if statesucks == "Giovanni Bernard":
        points += 1
        print(f"One more to go {eyes} \nTotal points: {points}")
        points += uncfan(points)
    else:
        points -= 1
        print(f"Sorry, that is incorrect. You have lost a point. Try again. \nTotal points: {points}")
        return puntreturn()


def uncfan(totalpoints: int) -> int: 
    """Prints first trivia question, calls next question if you get it right, or repeats question if you get it wrong."""
    import random
    points = totalpoints
    bballplayer = random.randint(10, 15)
    playerguess = input(f"What famous UNC basketball player wore the number {bballplayer}? ")
    players: dict[int, str] = {10: "Lennie Rosenbluth", 11: "Brice Johnson", 12: "Phil Ford", 13: "Cam Johnson", 14: "Danny Green", 15: "Vince Carter"}
    correct = players[bballplayer]
    if playerguess == correct:
        totalpoints += 1
        print(f"{fire}{fire}{fire} LETS GOOOOOO!!! YOU'RE A UNC SUPERFAN! {goat} \nYou scored a total of {points + totalpoints}/5 points")
    if playerguess != correct:
        totalpoints -= 1
        print(f"Sorry, that is incorrect. Unfortunately, you are not a real fan. \nTotal points: {points} ")
    totalpoints -= points
    return totalpoints


def simpleminded() -> None:
    """Initiates coinflip game."""
    import random
    global points
    coinflip = input("Heads or Tails? ")
    while coinflip == "Heads" or coinflip == "Tails":
        coin = random.randint(1, 2)
        if coinflip == "Heads" and coin == 1 or coinflip == "Tails" and coin == 2:
            points += 1
            print(f"Correct! You have earned a point. \nTotal points: {points} ")
            coinflip = input("Heads or Tails? ")
        else: 
            points -= 1
            print(f"Incorrect. Must be because you aren't a UNC fan. \n1 point has been deducted. Try again. \nTotal points: {points}")    
            coinflip = input("Heads or Tails? ")
    if coinflip != "Heads" or coinflip != "Tails":
        print("Its a pretty simple question... ")
        simpleminded()


if __name__ == "__main__":
    main()