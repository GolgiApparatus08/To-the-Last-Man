import sys
from enum import Enum

########################################################################### Weapons ###########################################################################

class weapon(Enum):
    alarmClock = 1
    combatAward = 2
    encryptedLaptop = 3
    heavyBriefcase = 4
    humanSkull = 5
    liquorHandle = 6
    aggressiveStimulants = 7
    exoticPoison = 8
    neurotoxicGas = 9
    petSnake = 10
    revivalDefibrillator = 11
    sleepingPills = 12
    decorativeSword = 13
    forgedKeycard = 14
    imporvisedShiv = 15
    kitchenKnife = 16
    sacredDagger = 17
    throwingShurikens = 18
    nothing = 19

class weaponType(Enum):
    blunt = 1
    medical = 2
    sharp = 3
    noType = 4

weaponType = {
    weapon.alarmClock : weaponType.blunt, 
    weapon.combatAward : weaponType.blunt, 
    weapon.encryptedLaptop : weaponType.blunt, 
    weapon.heavyBriefcase : weaponType.blunt, 
    weapon.humanSkull : weaponType.blunt, 
    weapon.liquorHandle : weaponType.blunt,
    weapon.aggressiveStimulants : weaponType.medical,
    weapon.exoticPoison : weaponType.medical,
    weapon.neurotoxicGas : weaponType.medical,
    weapon.petSnake : weaponType.medical,
    weapon.revivalDefibrillator : weaponType.medical,
    weapon.sleepingPills : weaponType.medical,
    weapon.decorativeSword : weaponType.sharp,
    weapon.forgedKeycard : weaponType.sharp,
    weapon.imporvisedShiv : weaponType.sharp,
    weapon.kitchenKnife : weaponType.sharp,
    weapon.sacredDagger : weaponType.sharp,
    weapon.throwingShurikens : weaponType.sharp,
    weapon.nothing : weaponType.noType
    }

########################################################################## Locations ##########################################################################

bookFacts = []
bookFacts.append("Fish brought from the bottom most depths of the ocean will literally melt upon reaching the surface, physically incapable of dealing with the lower pressure.")                                   
bookFacts.append("The distinction between straight and gay individuals was not made at all until the 19th century. Previous to this, only specific sexual acts--not people types--were considered abberations.")   
bookFacts.append("Under the philosophy known as 'platonism', the creator of the universe is not God, but rather an evil force known as 'the Demiurge' that has trapped humanity in a false prison of matter.")      
bookFacts.append("During the golden age of piracy, many captains were hired by governments to raid and steal from merchant ships belonging to enemy nations. These would become know as 'privateers'.")             
bookFacts.append("The ancient greeks considered direct tax equivalent to slavery, and financed their city-states entirely on fees for public services.")                                                           
bookFacts.append("The vast majority of gladitorial matches did not end in death for either party, and most gladiators fought professionally for many years.")                                                       
bookFacts.append("In traditional astrology, marriage and love are represented by two different areas of one's chart, as marriage was mostly political/economic for most of human history.")                    
bookFacts.append("Humans can guess (at above expected rates) whether another human is looking at them through a two-way mirror. The mechanism behind this is currently unknown.")                                  
bookFacts.append("Black holes are completly invisible, and so can only be distinguished by the human eye as areas absent of matter or light.")
bookFacts.append("Previous to Darwin's theory of evolution, an alternative theory was proposed in which physical changes over an organisms lifetime could be transmitted to their offspring.")
bookFacts.append("LSD was invented when a researcher spilled just the right amount of the chemical he was working with on his skin and experienced a trip. If he had spilled more, he would have died.")

#Setup location idenitifiers

def selfIdentify():
    eyes = []
    for i in range(len(players)):
        if players[i].location is target.location:
            eyes.append(player[i])
    for i in range(len(eyes)):
        if eyes[i] is alive and eyes[i] is not self:
            eyes[i].message += str(self.name + " is also present. ")
            self.message += str(eyes[i].name + " is also present. ")
        else if eyes[i] is not alive and is not self:
            self.message += str(eyes[i].name + "'s body is also laying on the floor. ")
    clear(eyes)
    return

def playerIdentify():
    eyes = []
    for i in range(len(players)):
        if players[i].location is player.location:
            eyes.append(player[i])
    for i in range(len(eyes)):
        if eyes[i] is alive and eyes[i] is not player:
            eyes[i].message += str(player.name + " is also present. ")
            player.message += str(eyes[i].name + " is also present. ")
        else if eyes[i] is not alive and is not player:
            player.message += str(eyes[i].name + "'s body is also laying on the floor. ")
    clear(eyes)
    return

#Setup rankCheck



#Setup locations

class location:
    def __init__(self, rank):
        self.rank = rank
        self.sabotages = 0
        self.works = 0
        self.functionality = True

    def rankCheck(self, player):
    if int(player.rank) < locationRank:
        player.message += str("Around " + str(time) + ", you fail to access " + Location + ". ")
        ears = []
        for i in range(len(players)):
            if players[i].location is location:
                ears.append(player[i])
        for i in range(len(ears)):
            if ears[i] is alive:
                ears[i].message += str("Around " + str(time) + ", you heard " + Location + "'s door deny access to someone. ")
        clear(ears)
        return False
    return True


class barraks(location):
    def visit(player):
        
        #Check Rank
        location = barraks
        locationRank = 1
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.sleep = player.sleep + 1
        player.message += str("At " + time + ", you manage to get a good hour of geniune sleep in. You will be able to stave off rest more effectively tomorrow, should the need arise. ")
        identify() sdfsdfsdfsdf


class sanitation(location):
    def visit(player):
        
        #Check Rank
        location = sanitation
        locationRank = 1
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        if player.weapon is player.currentWeapon:
            player.message += str("Around " + time + ", you sneak into sanitation and slip your " + player.weapon + " into the trash. It will never be used again. ")
            player.weapon = nothing
            player.currentWeapon = nothing
        else:
            player.message += str("Around " + time + ", you sneak into sanitation and slip " + player.owner.name + "'s " + player.currentWeapon + " into the trash. It will never be used again. ")
            player.owner.weapon = nothing
            player.currentWeapon = nothing
            moderatorMessage += str("Tell " + player.owner.name + " that someone trashed their weapon last night. ")
    
class gymnasium(location):
    def visit(player):
        
        #Check Rank
        location = gymnasium
        locationRank = 2
        Access = rankCheck(player)
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.gymnasiumVisits = player.gymnasiumVisits + 1
        player.message += str("At " + time + ", you workout for a good hour in the gym. ")
    
class medical(location):
    def visit(player):
        
        #Check Rank
        Access = rankCheck(player)
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        if "cuts" in player.marks and "bruises" not in player.marks:
            player.marks.clear()
            player.message += str("Around " + time + ", you use the advanced systems in medical to seal up most of your cuts from the earlier fight. Tomorrow morning, no one will be the wiser. ")
        elif "cuts" not in player.marks and "bruises" in player.marks:
            player.marks.clear()
            player.message += str("Around " + time + ", you use the advanced systems in medical to rapidly heal most of your bruises from the earlier fight. Tomorrow morning, no one will be the wiser. ")
        elif "cuts" in player.marks and "bruises" in player.marks:
            player.marks.clear()
            player.message += str("Around " + time + ", you use the advanced systems in medical to rapidly heal all of your cuts and bruises from those earlier fights. Tomorrow morning, no one will be the wiser. ")
        else:
            player.message += str("Around " + time + ", you visit medical. )
    
class library(location):
    def visit(player):
        
        #Check Rank
        location
        locationRank = 3
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.libraryVisits = player.libraryVisits + 1
        player.message += str("At " + time + ", you peruse the books in the base's library for about an hour. Deep in the shelves, you find an old book that explains: '" + random.choice(bookFacts) + "' Inspiration strikes, and you suddenly get a wonderful idea of how to deal with your current predicament. ")
    
class information(location):
    def visit(player, target):
        
        #Check Rank
        location = information
        locationRank = 3
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.message += str("Around " + time + ", you scour all the files you can find on " + target.name + " in information, and eventually discover their intellect is " + target.intellect + " and their precision is " + target.precision + ". ")
    
class wargames(location):
    def visit(player):

        #Check Rank
        location = wargames
        locationRank = 4
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.wargamesVisits = player.wargamesVisits + 1
        player.message += str("At " + time + ", you spend an hour plugged into simulated combat in wargames. Your reflexes honed, you feel more precise than ever. ")
    
class communications(location):
    def visit(player, target1, target2):
        
        #Check Rank
        location = communications
        locationRank = 4
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.message += str("Around " + time + ", you visit communications to audit the comms shared between " + target1.name + " and " + target2.name + " this morning and afternoon. The computer returns that it has noted your attempt and will, if accepted, send you the result of the audit by morning. ")
        moderatorMessage += str("Send " + player.name + " any comms shared between " + target1.name + " and " + target2.name " yesterday. ")

class power(location):
    def visit(player):
        
        #Check Rank
        location = power
        locationRank = 5
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.power = player.power + 1
        player.message += str("At " + time + ", you spend an hour fueling and watching over the generator, an activiy that will excuse you of some of your responsiblities tomorrow night. ")

class armaments(location):
    def visit(player, target):
        
        #Check Rank
        location = armaments
        locationRank = 5
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.message += str("Around " + time + ", you stop by armaments to see if you can learn anything useful about " + target.name + ". From the training logs, you discover that their strength is " + target.strength + " and that they have " + target.weapon + " (" + target.weaponType + ") on hand that that they could use to kill. ")
    
class security(location):
    def visit(player, target):
        
        #Check Rank
        location = security
        locationRank = 6
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.message += str("Around " + time + ", you visit security and search " + target.name + "'s name in the tracking database. On a projected map, you see a blip light up in " + target.location + ". ")
    
class command(location):
    def visit(player, target):
        
        #Check Rank
        location = command
        locationRank = 6
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location

        #Effect
        player.message += str("Around " + time + ", you visit command to see if the base's highest ranking records might reveal something useful about " + target.name + ". You discover that their rank is " + target.rank + " and their currently assigned to the " + shift + " shift. ")

barraks = barraks(1, "the barraks")
sanitation = sanitation(1)
gymnasium = gymnasium(2)
medical = medical(2)
library = library(3)
information = information(3)
wargames = wargames(4)
communications = communications(4)
power = power(5)
armaments = armaments(5)
security = security(6)
command = command(6)

########################################################################### Players ###########################################################################

class Player:
    def __init__(self, name, rank, strength, intellect, precision, weapon, shift):
        self.name = name
        self.rank = rank
        self.strength = strength
        self.intellect = intellect
        self.precision = precision
        self.weapon = weapon
        self.shift = shift
        self.location = barraks
        self.honor = 1
        self.alive = True
        self.defending = False
        self.message = ""
        self.gymnasiumVisits = 0
        self.libraryVisits = 0
        self.wargamesVisits = 0
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
                moderatorMessage += str(target.name + " has been killed by " + self.name + " in " + target.location + " at " + time + " with " + self.weapon + ". His rank was " + target.rank + ", his strength was " + target.strength + ", his intellect was " + target.intellect + ", his percision was " + target.percision + ", his weapon was " + target.weapon + ", and his shift was " + target.shift + ". ")
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
                moderatorMessage += str(target.name + " has been killed by " + self.name + " in " + target.location + " at " + time + " with " + self.weapon + ". His rank was " + target.rank + ", his strength was " + target.strength + ", his intellect was " + target.intellect + ", his percision was " + target.percision + ", his weapon was " + target.weapon + ", and his shift was " + target.shift + ". ")
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
            if self.precision > fightPercision:
                target.alive = false
                moderatorMessage += str(target.name + " has been killed by " + self.name + " in " + target.location + " at " + time + " with " + self.weapon + ". His rank was " + target.rank + ", his strength was " + target.strength + ", his intellect was " + target.intellect + ", his percision was " + target.percision + ", his weapon was " + target.weapon + ", and his shift was " + target.shift + ". ")
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
            input(playerNumberWords + " soldier's precision: \n"),
            input(playerNumberWords + " soldier's weapon: \n"),
            input(playerNumberWords + " soldier's shift: \n")
        )
    )

    print(playerList[-1].name + " logged!\n")

######################################################################### Add Players #########################################################################

#Ask for player amount
playerNumber = input("Number of soldiers (2-12): \n")

#Tell 0 players to fuck off
if int(playerNumber) <= 0:                                                       
    input("You don't have a base without soldiers. Come back with some players!\n")
    sys.exit()

#Tell 1 player to fuck off
if int(playerNumber) is 1:
    input("There's already a last man, silly!")
    sys.exit()

#Create players
for i in range(0,int(playerNumber)):
    addPlayer(players)

#################################################################### Day-Night Loop ####################################################################

days = int(playerNumber/2+1)

#Day Cycle
for nights in range(0, days):

    #Readiness check
    dayNumberWord = numberWords[nights + 1]
    input("Press ENTER to begin the " + dayNumberWords + "night.")

    #Moderator's Message
    moderatorMessage = ""

    #Define Time
    time = {
        0 : "11 PM",
        1 : "12 AM"
    }

    #Hour Cylce
    for hour in range(0, 7):
        time[hour]