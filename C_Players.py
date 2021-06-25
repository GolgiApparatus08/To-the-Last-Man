class Player:
    def __init__(self, name, rank, strength, intellect, nerves, weapon, shift):
        self.name = name
        self.rank = rank
        self.strength = strength
        self.intellect = intellect
        self.nerves = nerves
        self.weapon = weapon
        self.shift = shift
        self.location = barraks
        self.honor = 1
        self.alive = True
        self.defending = False
        self.message = ""
        self.gymnasiumVisits = 0
        self.libraryVisits = 0
        self.bathhouseVisits = 0
        self.power = 0
        self.sleep = 0
        self.currentWeapon = weapon
        self.marks = []
        self.owner = ""

    def KILL(self, target):

        #Check for location access
        Access = selfRankCheck()
        if Access is false:
            return

        #Change location
        self.location = target.location

        #Make sure the target is actually alive :P
        if target.alive is False:
            self.message += str("While looking to kill them, you find " + target.name + "'s body on the floor in " + self.location + ". ")
            selfIdentify()
            return

        self.message += str("You find " + target.name " in " + target.location + ". ")

        #Deal with defending
        if target.defending is true:
            self.message += str("Unfortunatly, they're alert at the moment, and you're too intimidated to attack head on. ")
            selfIdentify()
            return

        #FIGHT!

        #Blunt
        if self.currentWeapon.weaponType is blunt:
            self.marks.append(bruises)
            target.marks.append(bruises)

            #Wins
            if self.strength > fightStrength:
                target.alive = false
                moderatorMessage += str(target.name + " has been killed by " + self.name + " in " + target.location + " at " + time + " with " + self.weapon + ". His rank was " + target.rank + ", his strength was " + target.strength + ", his intellect was " + target.intellect + ", his nerves was " + target.nerves + ", his weapon was " + target.weapon + ", and his shift was " + target.shift + ". ")
                self.honor = self.honor - target.honor
                if self.honor is 0:
                    self.honor = -1
                target.message += str(self.name + " catches you off guard and bashes your skull in with " + self.currentWeapon + ". Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details.")
                witnesses = []
                selvesInLocation(witnesses)
                for i in range(len(witnesses))
                    if witnesses[i] is alive and witnesses[i] is not self:
                        witnesses[i].message += str("You witness " + self.name + " bash " + target.name + "'s head in with " + self.currentWeapon.weaponType + ". ")
                clear(witnesses)
                return

            #Loses
            else:
                target.message += str(self.name + " comes at you with " + self.weapon + " in an attempt to bash your head in. Stronger than him, you survive the scuffle that follows, albeit with a few bruises.")
                self.message += str("You attempt to bash " + target.name + "'s head in with your " + self.currentWeapon ", but he's too strong and survives the scuffle that follows with only a few bruises.")
                return

        #Medical
        else if self.currentWeapon.weaponType is medical:

            #Wins
            if self.intellect > fightIntellect:
                target.alive = false
                moderatorMessage += str(target.name + " has been killed by " + self.name + " in " + target.location + " at " + time + " with " + self.weapon + ". His rank was " + target.rank + ", his strength was " + target.strength + ", his intellect was " + target.intellect + ", his nerves was " + target.nerves + ", his weapon was " + target.weapon + ", and his shift was " + target.shift + ". ")
                self.honor = self.honor - target.honor
                if self.honor is 0:
                    self.honor = -1
                target.message += str(self.name + " catches you off guard and manages to outwit you with " + self.currentWeapon + ". Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details.")
                witnesses = []
                selvesInLocation(witnesses)
                for i in range(len(witnesses))
                    if witnesses[i] is alive and witnesses[i] is not self:
                        witnesses[i].message += str("You witness " + self.name + " outwit " + target.name + " with" + self.currentWeapon.weaponType + ". ")
                clear(witnesses)
                return

            #Loses
            else:
                target.message += str(self.name + " tries to kill you with " + self.weapon + ", but you outwit him and survive.")
                self.message += str("You try to kill " + target.name + " with your " + self.currentWeapon ", but he's too smart and catches you, surviving the attempt.")
                return

        #Sharp
        else if self.currentWeapon.weaponType is sharp:
            self.marks.append(cuts)
            target.marks.append(cuts)

            #Wins
            if self.nerves > fightnerves:
                target.alive = false
                moderatorMessage += str(target.name + " has been killed by " + self.name + " in " + target.location + " at " + time + " with " + self.weapon + ". His rank was " + target.rank + ", his strength was " + target.strength + ", his intellect was " + target.intellect + ", his nerves was " + target.nerves + ", his weapon was " + target.weapon + ", and his shift was " + target.shift + ". ")
                self.honor = self.honor - target.honor
                if self.honor is 0:
                    self.honor = -1
                target.message += str(self.name + " catches you off guard and stabs you with " + self.currentWeapon + ". Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details.")
                witnesses = []
                selvesInLocation(witnesses)
                for i in range(len(witnesses))
                    if witnesses[i] is alive and witnesses[i] is not self:
                        witnesses[i].message += str("You witness " + self.name + " stab " + target.name + " with" + self.currentWeapon.weaponType + ". ")
                clear(witnesses)
                return

            #Loses
            else:
                target.message += str(self.name + " tries to stab you with " + self.weapon + ", but your reaction time is quicker than theirs and you survive.")
                self.message += str("You try to stab " + target.name + " with your " + self.currentWeapon ", but he's too quick, survives the attempt.")
                return

    def ASSIST(self, target):

        #Check for location access
        Access = selfRankCheck()
        if Access is false:
            return

        #Change location
        self.location = target.location

        #Make sure target is alive
        if target.alive is False:
            self.message += str("While looking to help them, you find " + target.name + "'s body on the floor in " + self.location + ". ")
            selfIdentify()
            return

#Function and list for adding players
players = []

numberWords = {
    1 : 'First', 
    2 : 'Second', 
    3 : 'Third', 
    4 : 'Fourth', 
    5 : 'Fifth', 
    6 : 'Sixth', 
    7 : 'Seventh', 
    8 : 'Eighth', 
    9 : 'Ninth', 
    10 : 'Tenth', 
    11 : 'Eleventh', 
    12 : 'Twelfth'
}

def addPlayer(playerList):    
    
    playerNumberWords = numberWords[len(playerList) + 1]

    playerList.append(
        Player(
            input(playerNumberWords + " soldier's name: \n"),
            input(playerNumberWords + " soldier's rank: \n"),
            input(playerNumberWords + " soldier's strength: \n"),
            input(playerNumberWords + " soldier's intellect: \n"),       
            input(playerNumberWords + " soldier's nerves: \n"),
            input(playerNumberWords + " soldier's weapon: \n"),
            input(playerNumberWords + " soldier's shift: \n")
        )
    )

    print(playerList[-1].name + " logged!\n")