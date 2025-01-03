import time
from random import choice as c 
from random import randint as r

def When_Toss_Won_batting():
    team_user_batting_list = 0

    while True:
        user_batting_score = int(input("BAT!!(0 to 6): "))
        system_bowling_score = r(0,6)
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        if (user_batting_score != system_bowling_score):
            print(f"BAT = {user_batting_score}")
            print(f"BALL = {system_bowling_score}")
            team_user_batting_list += user_batting_score

        elif (user_batting_score == system_bowling_score):
            print(f"BAT = {user_batting_score}")
            print(f"BALL = {system_bowling_score}")
            print("You are OUT")
            break
    
    print(f"Your Score Was {team_user_batting_list}")

    print(f"So, the target is {team_user_batting_list + 1}")
    print("Now The Opponent Will Bat")

    team_system_batting_list = 0

    while True:
        if(team_system_batting_list < (team_user_batting_list+1)):
            user_bowling_score = int(input("BALL!! (0 to 6): "))
            system_batting_score = r(0,6)
            time.sleep(1)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            if (user_bowling_score != system_batting_score):
                print(f"BALL = {user_bowling_score}")
                print(f"BAT = {system_batting_score}")
                team_system_batting_list += system_batting_score

            elif (user_bowling_score == system_batting_score):
                print(f"BALL = {user_bowling_score}")
                print(f"BAT = {system_batting_score}")
                print("OUT!!")
                break

        elif (team_system_batting_list >= (team_user_batting_list + 1)):
            print(f"{team_system} has chased down the target!!")
            print(f"{team_user} has lost the match")
            break

    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)

    print("Match Summary")

    print(f"{team_system} score was {team_system_batting_list}")
    print(f"{team_user} score was {team_user_batting_list}")
    time.sleep(2)
    if((team_user_batting_list + 1) > team_system_batting_list):
        print(f"Hurray!! {team_user} won the match by {team_user_batting_list - team_system_batting_list} runs")
    elif((team_user_batting_list + 1) < team_system_batting_list):
        print(f"OHH {team_user} Lost!!")
    elif(team_user_batting_list == team_system_batting_list):
        print("TIE!!")

def When_Toss_Won_bowling():
    team_system_batting_list = 0

    while True:
        user_bowling_score = int(input("BALL!!(0 to 6): "))
        system_batting_score = r(0,6)
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        if (user_bowling_score != system_batting_score):
            print(f"BALL = {user_bowling_score}")
            print(f"BAT = {system_batting_score}")
            team_system_batting_list += system_batting_score

        elif (user_bowling_score == system_batting_score):
            print(f"BALL = {user_bowling_score}")
            print(f"BAT = {system_batting_score}")
            print(f"{team_system} is OUT")
            break

    print(f"{team_system} Score is {team_system_batting_list}")

    print(f"So, the target is {team_system_batting_list + 1}")
    print("Now you Will Bat")

    team_user_batting_list = 0

    while True:
        if(team_user_batting_list < (team_system_batting_list+1)):
            user_batting_score = int(input("BAT!! (0 to 6): "))
            system_bowling_score = r(0,6)
            time.sleep(1)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            if (user_batting_score != system_bowling_score):
                print(f"BAT = {user_batting_score}")
                print(f"Ball = {system_bowling_score}")
                team_user_batting_list += user_batting_score

            elif (user_batting_score == system_bowling_score):
                print(f"BAT = {user_batting_score}")
                print(f"Ball = {system_bowling_score}")
                print("OUT!!")
                break

        elif (team_user_batting_list >= (team_system_batting_list + 1)):
            print(f"{team_user} has chased down the target!!")
            print(f"{team_system} has lost the match")
            break

    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)

    print("Match Summary")

    print(f"{team_user} score was {team_user_batting_list}")
    print(f"{team_system} score was {team_system_batting_list}")
    time.sleep(2)
    if((team_system_batting_list + 1) > team_user_batting_list):
        print(f"OHH!! {team_system} won the match by {team_system_batting_list - team_user_batting_list} runs\nYou Lost")
    elif((team_system_batting_list + 1) < team_user_batting_list):
        print(f"HURRAY!! {team_user} won the match!!")
    elif(team_user_batting_list == team_system_batting_list):
        print("TIE!!")

def When_Toss_Lost_Batting():
    team_system_batting_list = 0

    while True:
        user_bowling_score = int(input("BAT!!(0 to 6): "))
        system_batting_score = r(0,6)
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        if (user_bowling_score != system_batting_score):
            print(f"BALL = {user_bowling_score}")
            print(f"BAT = {system_batting_score}")
            team_system_batting_list += system_batting_score

        elif (user_bowling_score == system_batting_score):
            print(f"BALL = {user_bowling_score}")
            print(f"BAT = {system_batting_score}")
            print(f"{team_system} is OUT")
            break
    
    print(f"{team_system} Score is {team_system_batting_list}")

    print(f"So, the target is {team_system_batting_list + 1}")
    print("Now You Will Bat")

    team_user_batting_list = 0

    while True:
        if(team_user_batting_list < (team_system_batting_list+1)):
            user_batting_score = int(input("BAT!! (0 to 6): "))
            system_bowling_score = r(0,6)
            time.sleep(1)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            if (user_batting_score != system_bowling_score):
                print(f"BAT = {user_batting_score}")
                print(f"Ball = {system_bowling_score}")
                team_user_batting_list += user_batting_score

            elif (user_batting_score == system_bowling_score):
                print(f"BAT = {user_batting_score}")
                print(f"Ball = {system_bowling_score}")
                print("OUT!!")
                break

        elif (team_user_batting_list >= (team_system_batting_list + 1)):
            print(f"{team_user} has chased down the target!!")
            print(f"{team_system} has lost the match")
            break

    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)

    print("Match Summary")

    print(f"{team_user} score was {team_user_batting_list}")
    print(f"{team_system} score was {team_system_batting_list}")
    time.sleep(2)
    if((team_system_batting_list + 1) > team_user_batting_list):
        print(f"OHH!! {team_system} won the match by {team_system_batting_list - team_user_batting_list} runs\nYou Lost")
    elif((team_system_batting_list + 1) < team_user_batting_list):
        print(f"HURRAY!! {team_user} won the match!!")
    elif(team_user_batting_list == team_system_batting_list):
        print("TIE!!")

def When_Toss_Lost_Bowling():
    team_user_batting_list = 0

    while True:
        user_batting_score = int(input("BAT!!(0 to 6): "))
        system_bowling_score = r(0,6)
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        if (user_batting_score != system_bowling_score):
            print(f"BAT = {user_batting_score}")
            print(f"BALL = {system_bowling_score}")
            team_user_batting_list += user_batting_score

        elif (user_batting_score == system_bowling_score):
            print(f"BAT = {user_batting_score}")
            print(f"BALL = {system_bowling_score}")
            print("You are OUT")
            break
    
    print(f"Your Score Was {team_user_batting_list}")

    print(f"So, the target is {team_user_batting_list + 1}")
    print("Now The Opponent Will Bat")

    team_system_batting_list = 0

    while True:
        if(team_system_batting_list < (team_user_batting_list+1)):
            user_bowling_score = int(input("BALL!! (0 to 6): "))
            system_batting_score = r(0,6)
            time.sleep(1)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            if (user_bowling_score != system_batting_score):
                print(f"BALL = {user_bowling_score}")
                print(f"BAT = {system_batting_score}")
                team_system_batting_list += system_batting_score

            elif (user_bowling_score == system_batting_score):
                print(f"BALL = {user_bowling_score}")
                print(f"BAT = {system_batting_score}")
                print("OUT!!")
                break

        elif (team_system_batting_list >= (team_user_batting_list + 1)):
            print(f"{team_system} has chased down the target!!")
            print(f"{team_user} has lost the match")
            break

    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)

    print("Match Summary")

    print(f"{team_system} score was {team_system_batting_list}")
    print(f"{team_user} score was {team_user_batting_list}")
    time.sleep(2)
    if((team_user_batting_list + 1) > team_system_batting_list):
        print(f"Hurray!! {team_user} won the match by {team_user_batting_list - team_system_batting_list} runs")
    elif((team_user_batting_list + 1) < team_system_batting_list):
        print(f"OHH {team_user} Lost!!")
    elif(team_user_batting_list == team_system_batting_list):
        print("TIE!!")

# TEAM NAME'S
team_user = input("Enter Name of your team: ")
team_system = input("Enter the Name of your opponent(system): ")

#TOSS
print("TOSS TIME!!")
toss = input("HEAD'S OR TAIL'S: ")

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")

toss_list = ["head","tail"]
toss_result = c(toss_list)
print(toss_result)

#TOSSING MECHANISM
if (toss_result == toss):
    print("HURRAY!!!\nYou Won The Toss")
    time.sleep(2)
    toss_selection = input("As you won the toss select Batting or Bowling: ")
    if(toss_selection == 'batting'):
        When_Toss_Won_batting()
    elif(toss_selection == 'bowling'):
        When_Toss_Won_bowling()

elif(toss_result != toss):
    print("You Lost The Toss")
    system_toss_box = ["batting", "bowling"]
    system_choice = c(system_toss_box)
    time.sleep(2)
    print("As you lost the toss the opponent will select Batting or Bowling")

    time.sleep(1)
    print(5)
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)

    print(f"The Opponent choosed {system_choice}")
    if(system_choice == 'batting'):
        When_Toss_Lost_Batting()
    elif(system_choice == 'bowling'):
        When_Toss_Lost_Bowling()