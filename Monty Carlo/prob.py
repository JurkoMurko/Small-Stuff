import random as r

def pill_problem(loops):
    you_ded_count = 0
    for i in range(loops):
        l = [r.randint(0,1) for i in range(4)]

        if l[0] == r.choice(l[1:]):
            you_ded_count += 1

    percent_ded = you_ded_count / loops
    print(f"{percent_ded * 100}%")

def door_game_show_problem(count):
    win_count = 0

    for i in range(count):
        # set up the doors
        doors = [False for i in range(3)]
        prize_door_index = r.randint(0,2)
        doors[prize_door_index] = True

        # pick a door
        pick = r.randint(0,2)

        #give em a door that doesn't have a prize
        while True:
            janai_door_index = r.randint(0,2)
            if janai_door_index != prize_door_index and janai_door_index != pick:
                break

        #switch
        pick = (3 - janai_door_index) - pick

        #answer
        if pick == prize_door_index:
            win_count += 1
    
    print(f"{(win_count / count) * 100}%")

door_game_show_problem(1000)
pill_problem(1000)

