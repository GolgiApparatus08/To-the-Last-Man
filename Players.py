from Locations import Barraks
import sys
import string

moderatorMessage = ""
locations = []

class Player:
    def __init__(self, name, rank, strength, intellect, nerves, weapon, enteredShift, location):
        self.name = name
        self.rank = rank
        self.strength = strength
        self.intellect = intellect
        self.nerves = nerves
        self.weapon = weapon
        self.enteredShift = enteredShift
        self.location = location
        self.shift = "shift"
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
        self.commands = []

    def KILL(self, target):

        global moderatorMessage

        #Check for location access
        Access = selfRankCheck()
        if Access is False:
            return

        #Change location
        self.location = target.location

        #Make sure the target is actually alive :P
        if target.alive is False:
            self.message += str("While looking to kill them, you find " + target.name + "'s body on the floor in " + self.location + ". ")
            return

        self.message += str("You find " + target.name + " in " + target.location + ". ")

        #Deal with defending
        if target.defending is true:
            self.message += str("Unfortunatly, they're alert at the moment, and you're too intimidated to attack head on. ")
            return

        #FIGHT!

        #Blunt
        if self.currentWeapon.type is "blunt":
            self.marks.append("bruises")
            target.marks.append("bruises")

            #Wins
            if self.strength > fightStrength:
                target.alive = false
                moderatorMessage += str(target.name + " has been killed by " + self.name + " in " + target.location + " at " + time + " with " + self.weapon + ". His rank was " + target.rank + ", his strength was " + target.strength + ", his intellect was " + target.intellect + ", his nerves was " + target.nerves + ", his weapon was " + target.weapon + ", and his shift was " + target.shift + ". ")
                self.honor = self.honor - target.honor
                if self.honor is 0:
                    self.honor = -1
                target.message += str(self.name + " catches you off guard and bashes your skull in with " + self.currentWeapon + ". Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details.")
                return

            #Loses
            else:
                target.message += str(self.name + " comes at you with " + self.weapon + " in an attempt to bash your head in. Stronger than him, you survive the scuffle that follows, albeit with a few bruises.")
                self.message += str("You attempt to bash " + target.name + "'s head in with your " + self.currentWeapon + ", but he's too strong and survives the scuffle that follows with only a few bruises.")
                return

        #Medical
        elif self.currentWeapon.weaponType is medical:

            #Wins
            if self.intellect > fightIntellect:
                target.alive = false
                moderatorMessage += str(target.name + " has been killed by " + self.name + " in " + target.location + " at " + time + " with " + self.weapon + ". His rank was " + target.rank + ", his strength was " + target.strength + ", his intellect was " + target.intellect + ", his nerves was " + target.nerves + ", his weapon was " + target.weapon + ", and his shift was " + target.shift + ". ")
                self.honor = self.honor - target.honor
                if self.honor is 0:
                    self.honor = -1
                target.message += str(self.name + " catches you off guard and manages to outwit you with " + self.currentWeapon + ". Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details.")
                witnesses = []
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
                return

            #Loses
            else:
                target.message += str(self.name + " tries to stab you with " + self.weapon + ", but your reaction time is quicker than theirs and you survive.")
                self.message += str("You try to stab " + target.name + " with your " + self.currentWeapon ", but he's too quick, survives the attempt.")
                return









numberWords = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", 'Seventh', "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]
lowerNumberWords = ["first", "second", "third", "fourth", "fifth", "sixth", 'seventh', "eighth", "ninth", "tenth", "eleventh", "twelfth"]

def howMany():
    amount = input("Number of soldiers (2-12): \n")
    if amount <= 0:
        input("You don't have a base without soldiers. Come back with some players!\n")
        sys.exit()
    elif amount is 1:
        input("There's already a last man, silly!")
        sys.exit()
    else:
        return amount

def addPlayers(players, amount, startingLocation):    

    for p in range(amount):
        players.append(
            Player(
                input(numberWords[p] + " soldier's name: \n"),
                input(numberWords[p] + " soldier's rank: \n"),
                input(numberWords[p] + " soldier's strength: \n"),
                input(numberWords[p] + " soldier's intellect: \n"),       
                input(numberWords[p] + " soldier's nerves: \n"),
                input(numberWords[p] + " soldier's weapon: \n"),
                input(numberWords[p] + " soldier's shift: \n"),
                startingLocation
            )
        )

        print(players[p].name + " logged! \n")

def askCommands(players):
    for p in range(len(players)):
        players[p].commands.append(
            input("What is " + players[p].name + "'s first command? \n"),
            input("What is " + players[p].name + "'s second command? \n"),
            input("What is " + players[p].name + "'s third command? \n"),
            input("What is " + players[p].name + "'s fourth command? \n"),
            input("What is " + players[p].name + "'s fifth command? \n"),
            input("What is " + players[p].name + "'s sixth command? \n"),
            input("What is " + players[p].name + "'s seventh command? \n"),
            input("What is " + players[p].name + "'s eighth command? \n")
        )
        for c in range(len(players[p].commands)):
            players[p].commands[c] = string.split(players[p].commands)