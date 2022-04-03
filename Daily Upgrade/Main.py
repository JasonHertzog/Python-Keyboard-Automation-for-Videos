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
        if input() == '1':
            Player.addxp(player_1, 1, 1)
        if input() == '2':
            Player.addxp(player_1, 1, 2)
        if input() == '3':
            Player.addxp(player_1, 1, 3)
        if input() == '4':
            Player.addxp(player_1, 1, 4)
        if input() == '5':
            Player.addxp(player_1, 1, 5)
    elif (temp == '2'):
        print('On a scale from 1-5, how much effort did you put in?')
        if input() == '1':
            Player.addxp(player_1, 2, 1)
        if input() == '2':
            Player.addxp(player_1, 2, 2)
        if input() == '3':
            Player.addxp(player_1, 2, 3)
        if input() == '4':
            Player.addxp(player_1, 2, 4)
        if input() == '5':
            Player.addxp(player_1, 2, 5)
    elif (temp == '3'):
        print('On a scale from 1-5, how much effort did you put in?')
        if input() == '1':
            Player.addxp(player_1, 3, 1)
        if input() == '2':
            Player.addxp(player_1, 3, 2)
        if input() == '3':
            Player.addxp(player_1, 3, 3)
        if input() == '4':
            Player.addxp(player_1, 3, 4)
        if input() == '5':
            Player.addxp(player_1, 3, 5)
    else: 
        print('\n' + Player.Player.checkxp(player_1))
        print('Invalid input. Restart program if you want to add experience')




    
    # Test Loop
    # print('\n' + Player.Player.checkxp(player_1))
    # Player.testloop(player_1, 14)
    # print('\n' + Player.Player.checkxp(player_1))

    # Always save at end.
    Save_Manager.save_file(player_1)