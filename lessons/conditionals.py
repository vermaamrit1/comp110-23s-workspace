"""If it's raining, tell me to pack umbrella"""

weather: str = input("what is the weather like? ")

if (weather == "rain"):
    print("Pack an umbrella!")
    print("But splash in the puddles!")
else:
    if (weather == "snow"):
        print("Pack a jacket!")
    print("You don't need an umbrellla")
print("Have a lovely day")