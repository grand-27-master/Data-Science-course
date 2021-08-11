import random


class bcolors:
    HEADER= '\033[95m'
    OKBLUE= '\033[94m'             #initialising colors
    OKGREEN= '\033[92m'
    WARNING= '\033[93m'
    FAIL= '\033[91m'
    ENDC= '\033[0m'
    BOLD= '\033[1m'
    UNDERLINE= '\033[4m'



class person:
    def __init__(self,hp,mp,atk,df,magic):
        self.maxhp=hp
        self.hp=hp
        self.maxmp=mp
        self.mp=mp
        self.atkl=atk-10                      #initialising values
        self.atkh=atk+10
        self.df=df
        self.magic=magic
        self.action=["Attack","Magic"]        #the default action statement


    def generate_damage(self):
        return  random.randrange(self.atkl, self.atkh)


        
