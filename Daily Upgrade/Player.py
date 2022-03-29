# Player Object
# I want to keep the experience gains SLOW and somewhat hidden. Progress is slow in real life, and this program will replicate that.
# Consistency > Immediate results.

class Player:
    
    # If we use preset difficult XP, we could create class variables.
    raise_xp_min = 1.005
    raise_xp_small = 1.011
    raise_xp_med = 1.01489
    raise_xp_large = 1.0189
    raise_xp_max = 1.023333

    def __init__(self, name, goal1, goal2, goal3):
        # Player name
        self.name = name
        # Player goal 1 name
        self.goal1 = goal1
        # Player goal 2 name
        self.goal2 = goal2
        # Player goal 3 name
        self.goal3 = goal3
        # Start goal 1, 2, 3 experience at 0.
        self.xp1 = 0.504
        self.xp2 = 0.504
        self.xp3 = 0.504
    
    # Returns current stats in regards to total level and experience.
    def checkxp(self):
        return 'Goals & Experience\n{}: {} \n{}: {} \n{}: {}'.format(self.goal1, format(self.xp1, '.2f'), self.goal2, format(self.xp2, '.2f'), self.goal3, format(self.xp3, '.2f'))

    def addxp(self, goal, amount):
        # Create new line
        print()
        if goal == 1:
            if (self.xp1 > 200):
                self.xp1 += amount
            else:
                self.xp1 *= amount
            # Bonus XP when under level 1.
            if (self.xp1 < 1):
                self.xp1 += 0.008
            # Slight Nerf XP after level 5 to slow down.
            if (self.xp1 > 5):
                self.xp1 -= 0.001
            # Big Nerf to XP after level 10 to slow down. (This is in addition to level 5 nerf.)
            if (self.xp1 > 10):
                self.xp1 -= 0.0015
            return print('{}: Gained ~{}% Experience!'.format(self.goal1, format(amount, '.2f').rstrip('0').rstrip('.')).upper())
        if goal == 2:
            if (self.xp2 > 200):
                self.xp2 += amount
            else:
                self.xp2 *= amount
            # Bonus XP when under level 1.
            if (self.xp2 < 1):
                self.xp2 += 0.008
            # Slight Nerf XP after level 5 to slow down.
            if (self.xp2 > 5):
                self.xp2 -= 0.001
            # Big Nerf to XP after level 10 to slow down. (This is in addition to level 5 nerf.)
            if (self.xp2 > 10):
                self.xp2 -= 0.0015
            return print('{}: Gained ~{}% Experience!'.format(self.goal2, format(amount, '.2f').rstrip('0').rstrip('.')).upper())
        if goal == 3:
            if (self.xp3 > 200):
                self.xp3 += amount
            else:
                self.xp3 *= amount
            # Bonus XP when under level 1.
            if (self.xp3 < 1):
                self.xp3 += 0.008
            # Nerf XP after level 5 to slow down.
            if (self.xp3 > 5):
                self.xp3 -= 0.001
            # Big Nerf to XP after level 10 to slow down. (This is in addition to level 5 nerf.)
            if (self.xp1 > 10):
                self.xp1 -= 0.0015
            return print('{}: Gained ~{}% Experience!'.format(self.goal3, format(amount, '.2f').rstrip('0').rstrip('.')).upper())


# This will be replaced by input, but is currently used as a placeholder.
player_1 = Player('Jason', 'Programming', 'Running', 'Content Creation')

def testloop(x=365, i=0):
        for i in range (i, x):
            player_1.addxp(2, Player.raise_xp_med)
        

# We need to move this to its own Main method at some point.
if __name__ == '__main__':
    print('\n' + player_1.checkxp())
    testloop(14)
    print('\n' + player_1.checkxp())


