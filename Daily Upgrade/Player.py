import Save_Manager
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

    def __init__(self, name, goal1, goal2, goal3, xp1=0.504, xp2=0.503, xp3=0.502):
        # Player name
        self.name = name
        # Player goal 1 name
        self.goal1 = goal1
        # Player goal 2 name
        self.goal2 = goal2
        # Player goal 3 name
        self.goal3 = goal3
        # Start goal 1, 2, 3 experience at 0.
        self.xp1 = xp1
        self.xp2 = xp2
        self.xp3 = xp3
    
    # Returns current stats in regards to total level and experience.
    def checkxp(self):
        return ('Goals & Experience\n{} {} \n{} {} \n{} {}'.format(self.goal1, format(self.xp1, '.2f'), self.goal2, format(self.xp2, '.2f'), self.goal3, format(self.xp3, '.2f')))

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



# Create your player.
# This player will be saved after completion.
def create_player():
    print('Enter your name')
    temp_name = input()
    print('Enter your primary goal')
    temp_goal1 = input()
    print('Enter your secondary goal')
    temp_goal2 = input()
    print('Enter your final goal')
    temp_goal3 = input()
    player_0 = Player(temp_name, temp_goal1, temp_goal2, temp_goal3, xp1=0.504, xp2=0.503, xp3=0.502)
    print('Hello ' + player_0.name + '! Good luck with your goals!!')

    # Initializes save file. The second arg 'x' creates the save file.
    save_file = open(Save_Manager.file_path + "daily_upgrade_save.txt", 'x')
    save_file.close()
    with open(Save_Manager.file_path + 'daily_upgrade_save.txt', 'a') as f:
        # Store the save values with initial values.
            f.write(player_0.name)
            f.write('\n')
            f.write(player_0.goal1)
            f.write('\n')
            f.write(player_0.goal2)
            f.write('\n')
            f.write(player_0.goal3)
            f.write('\n')
            f.write(str(player_0.xp1))
            f.write('\n')
            f.write(str(player_0.xp2))
            f.write('\n')
            f.write(str(player_0.xp3))
            f.write('\n')
    

# Used for testing purposes (XP gains currently)
def testloop(self, x=365, i=0):
        for i in range (i, x):
            Player.addxp(self, 2, Player.raise_xp_med)
        


def increase_xp_prompt(self):
    print('\nWhat would you like to increase XP in?')
    # Display options to user.
    print('1 = ' + self.goal1 + '2 = ' + self.goal2 + '3 = ' + self.goal3)
    # Create and store temporary variable for choice of player.
    temp = input()
    if (temp == '1'):
        # User chooses to add XP to goal 1
        print('On a scale from 1-5, how much effort did you put in?')
        temp = input()
        if temp == '1':
            Player.addxp(self, 1, Player.raise_xp_min)
        if temp == '2':
            Player.addxp(self, 1, Player.raise_xp_small)
        if temp == '3':
            Player.addxp(self, 1, Player.raise_xp_med)
        if temp == '4':
            Player.addxp(self, 1, Player.raise_xp_large)
        if temp == '5':
            Player.addxp(self, 1, Player.raise_xp_max)
    elif (temp == '2'):
        # User chooses to add XP to goal 2
        print('On a scale from 1-5, how much effort did you put in?')
        temp = input()
        if temp == '1':
            Player.addxp(self, 2, Player.raise_xp_min)
        if temp == '2':
            Player.addxp(self, 2, Player.raise_xp_small)
        if temp == '3':
            Player.addxp(self, 2, Player.raise_xp_med)
        if temp == '4':
            Player.addxp(self, 2, Player.raise_xp_large)
        if temp == '5':
            Player.addxp(self, 2, Player.raise_xp_max)
    elif (temp == '3'):
        # User chooses to add XP to goal 3
        print('On a scale from 1-5, how much effort did you put in?')
        temp = input()
        if temp == '1':
            Player.addxp(self, 3, Player.raise_xp_min)
        if temp == '2':
            Player.addxp(self, 3, Player.raise_xp_small)
        if temp == '3':
            Player.addxp(self, 3, Player.raise_xp_med)
        if temp == '4':
            Player.addxp(self, 3, Player.raise_xp_large)
        if temp == '5':
            Player.addxp(self, 3, Player.raise_xp_max)
    else: 
        # No valid response, so do nothing.
        print('\n' + Player.checkxp(self))
        print('Invalid input. Restart program if you want to add experience')
    # End by showing player XP.
    print('\n' + Player.checkxp(self))

