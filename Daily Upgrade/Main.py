import Player, Save_Manager

# We need to move this to its own Main method at some point.
if __name__ == '__main__':
    Save_Manager.check_save_exists()

    name, goal1, goal2, goal3, xp1, xp2, xp3 = Save_Manager.load_file()
    data = [name, goal1, goal2, goal3, xp1, xp2, xp3]
    print(data)
    player_1 = Player.Player(name, goal1, goal2, goal3, float(xp1), float(xp2), float(xp3))

    # Test Loop
    print('\n' + Player.Player.checkxp(player_1))
    Player.testloop(player_1, 14)
    print('\n' + Player.Player.checkxp(player_1))
    Save_Manager.save_file(player_1)