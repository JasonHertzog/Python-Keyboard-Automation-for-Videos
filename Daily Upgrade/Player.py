# Player Object

class Player:
    
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
        self.xp1 = 0
        self.xp2 = 0
        self.xp3 = 0
    
    # Returns current stats in regards to total level and experience.
    def checkxp(self):
        return 'Goals & Experience\n{}: {} \n{}: {} \n{}: {}'.format(self.goal1, self.xp1, self.goal2, self.xp2, self.goal3, self.xp3)

    def addxp(self, goal, amount=1):
        # Create new line
        print()
        if goal == 1:
            self.xp1 += amount
            return print('{}: Gained {} Experience!'.format(self.goal1, amount).upper())
        if goal == 2:
            self.xp2 += amount
            return print('{}: Gained {} Experience!'.format(self.goal2, amount).upper())
        if goal == 3:
            self.xp3 += amount
            return print('{}: Gained {} Experience!'.format(self.goal3, amount).upper())


# This will be replaced by input, but is currently used as a placeholder.
player_1 = Player('Jason', 'Programming', 'Running', 'Content Creation')


# We need to move this to its own Main method at some point.
if __name__ == '__main__':
    print('\n' + player_1.checkxp())
    player_1.addxp(1, 5)
    player_1.addxp(2)
    print('\n' + player_1.checkxp())


