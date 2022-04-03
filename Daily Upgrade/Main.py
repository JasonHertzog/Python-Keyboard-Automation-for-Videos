import Player, Save_Manager

# Main Method Below


if __name__ == '__main__':
    Save_Manager.check_save_exists()

    # Load and initialize player object with data from save file.
    name, goal1, goal2, goal3, xp1, xp2, xp3 = Save_Manager.load_file()
    data = [name, goal1, goal2, goal3, xp1, xp2, xp3]
    player_1 = Player.Player(name, goal1, goal2, goal3, float(xp1), float(xp2), float(xp3))
    
    # Always show current XP when starting up.
    print('\n' + Player.Player.checkxp(player_1))
    
    # Eventually replace this with menu prompt options.
    # For now, just go right to increase_xp_prompt.
    Player.increase_xp_prompt(player_1)

    # Always save at end.
    Save_Manager.save_file(player_1)
