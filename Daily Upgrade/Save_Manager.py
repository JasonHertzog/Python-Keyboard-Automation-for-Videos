import Player
from os.path import exists
# Set this to desired directory.
file_path = "C:\\Users\\Skilled Apple\\Documents\\GitHub"

def check_save_exists():
    # Check if file exists. If not, create it.
    if exists(file_path + 'daily_upgrade_save.txt'):
        pass
        # with open(file_path + 'daily_upgrade_save.txt', 'r') as f:
        #    data = f.readlines()
        #    Player.load_player(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
    else:
        Player.create_player()

def load_file():
    with open(file_path + 'daily_upgrade_save.txt', 'r') as f:
        data = f.readlines()
        print(data)
        return(data[0], data[1], data[2], data[3], data[4], data[5], data[6])

def save_file(self):
    with open(file_path + 'daily_upgrade_save.txt', 'w') as f:
        f.write(self.name)
        f.write(self.goal1) 
        f.write(self.goal2)
        f.write(self.goal3)
        f.write(str(self.xp1) + '\n') 
        f.write(str(self.xp2) + '\n') 
        f.write(str(self.xp3) + '\n')
        print('Saved!')