import Player

# We need to move this to its own Main method at some point.
if __name__ == '__main__':
    print('\n' + Player.player_1.checkxp())
    Player.testloop(14)
    print('\n' + Player.player_1.checkxp())