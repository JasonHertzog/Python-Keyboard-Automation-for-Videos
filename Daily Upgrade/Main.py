import Player, Save_Manager

# We need to move this to its own Main method at some point.
if __name__ == '__main__':
    Save_Manager.check_save_exists()

    name, goal1, goal2, goal3, xp1, xp2, xp3 = Save_Manager.load_file()
    data = [name, goal1, goal2, goal3, xp1, xp2, xp3]
    player_1 = Player.Player(name, goal1, goal2, goal3, float(xp1), float(xp2), float(xp3))

    print('\n' + Player.Player.checkxp(player_1))
    print('\nWhat would you like to increase XP in?')
    print('1 = ' + goal1 + '\n2= ' + goal2 + '\n3= ' + goal3)
    temp = input()
    if (temp == '1'):
        print('On a scale from 1-5, how much effort did you put in?')
        temp = input()
        if temp == '1':
            Player.Player.addxp(player_1, 1, Player.Player.raise_xp_min)
        if temp == '2':
            Player.Player.addxp(player_1, 1, Player.Player.raise_xp_small)
        if temp == '3':
            Player.Player.addxp(player_1, 1, Player.Player.raise_xp_med)
        if temp == '4':
            Player.Player.addxp(player_1, 1, Player.Player.raise_xp_large)
        if temp == '5':
            Player.Player.addxp(player_1, 1, Player.Player.raise_xp_max)
    elif (temp == '2'):
        print('On a scale from 1-5, how much effort did you put in?')
        temp = input()
        if temp == '1':
            Player.Player.addxp(player_1, 2, Player.Player.raise_xp_min)
        if temp == '2':
            Player.Player.addxp(player_1, 2, Player.Player.raise_xp_small)
        if temp == '3':
            Player.Player.addxp(player_1, 2, Player.Player.raise_xp_med)
        if temp == '4':
            Player.Player.addxp(player_1, 2, Player.Player.raise_xp_large)
        if temp == '5':
            Player.Player.addxp(player_1, 2, Player.Player.raise_xp_max)
    elif (temp == '3'):
        print('On a scale from 1-5, how much effort did you put in?')
        temp = input()
        if temp == '1':
            Player.Player.addxp(player_1, 3, Player.Player.raise_xp_min)
        if temp == '2':
            Player.Player.addxp(player_1, 3, Player.Player.raise_xp_small)
        if temp == '3':
            Player.Player.addxp(player_1, 3, Player.Player.raise_xp_med)
        if temp == '4':
            Player.Player.addxp(player_1, 3, Player.Player.raise_xp_large)
        if temp == '5':
            Player.Player.addxp(player_1, 3, Player.Player.raise_xp_max)
    else: 
        print('\n' + Player.Player.checkxp(player_1))
        print('Invalid input. Restart program if you want to add experience')
    
    print('\n' + Player.Player.checkxp(player_1))




    
    # Test Loop
    # print('\n' + Player.Player.checkxp(player_1))
    # Player.testloop(player_1, 14)
    # print('\n' + Player.Player.checkxp(player_1))

    # Always save at end.
    Save_Manager.save_file(player_1)