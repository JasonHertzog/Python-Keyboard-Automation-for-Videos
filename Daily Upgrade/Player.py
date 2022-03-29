# Player Object

class Player:
    
    def __init__(self, name, goal1, goal2, goal3):
        self.name = name
        self.goal1 = goal1
        self.goal2 = goal2
        self.goal3 = goal3
        self.xp1 = 0
        self.xp2 = 0
        self.xp3 = 0
    
    def checkxp(self):
        return 'Goals & Experience\n{}: {} \n{}: {} \n{}: {}'.format(self.goal1, self.xp1, self.goal2, self.xp2, self.goal3, self.xp3)

player_1 = Player('Jason', 'Programming', 'Running', 'Content Creation')


# We need to move this to its own Main method at some point.
if __name__ == '__main__':
    print(player_1.checkxp())


