from Functions import allInstances, event, whoHere
import random

class Location:
    def __init__(self):
        self.name = "none"

    def __str__(self):
        return self.name

#Checks to see if: player alive, player in room, room functional
def roomCheck(self, player, players, locations, weapons, traits):
    if player.alive == False:
        player.DEAD(locations, players)
        return False
    if player.location != self:
        player.LOITER(player.location, locations, players, weapons, False, traits)
        return False
    if self.functionality == False:
        witnesses = whoHere(player, "none", players, locations)
        event(witnesses, player, "none", "dysfunctional")
        player.LOITER(player.location, locations, players, weapons, False, traits)
        return False
    return True

class Barraks(Location):
    def __init__(self):
        self.name = "the barraks"
        self.rank = 1
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "BARRAKS"
        self.blips = 0
        self.weapons = []

    def visit(self, player, locations, players, weapons, traits):
        outcome = roomCheck(self, player, players, locations, weapons, traits)
        if outcome == False:
            return

        player.sleep = player.sleep + 1
        if players[0].debug == True:
            print(player.trueName + " is sleeping in the barracks. ")
        witnesses = whoHere(player, "none", players, locations)
        event(witnesses, player, "none", "barraks")
        return

class Sanitation(Location):
    def __init__(self):
        self.name = "sanitation"
        self.rank = 1
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "SANITATION"
        self.blips = 0
        self.weapons = []
        
    def visit(self, player, weapon, locations, players, weapons, traits):
        outcome = roomCheck(self, player, players, locations, weapons, traits)
        if outcome == False:
            return
        if weapons[int(weapon)] not in player.weapons:
            witnesses = whoHere(player, "none", players, locations)
            event(witnesses, player, "none", "sanitation_dontHave")
            player.LOITER(player.location, locations, players, weapons, False, traits)
            return

        if players[0].debug == True:
            print(player.trueName + " throws " + weapons[int(weapon)].name + " into the incinerator in sanitation. ")
        players[0].weaponChanges += str("-Destroy " + player.name + "'s " + weapons[int(weapon)].withoutArticle + "\n")
        witnesses = whoHere(player, "none", players, locations)
        event(witnesses, player, "none", "sanitation")
        return

class Gymnasium(Location):
    def __init__(self):
        self.name = "the gymnasium"
        self.rank = 2
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "GYMNASIUM"
        self.blips = 0
        self.weapons = []
        
    def use(self, player, locations, players, weapons, traits):
        outcome = roomCheck(self, player, players, locations, weapons, traits)
        if outcome == False:
            return

        player.gymnasiumVisits = player.gymnasiumVisits + 1
        if players[0].debug == True:
            print(player.trueName + " works out in the gymnasium. ")
        witnesses = whoHere(player, "none", players, locations)
        event(witnesses, player, "none", "gymnasium_use")
        return

    def learn(self, player, locations, players, weapons, traits):
        outcome = roomCheck(self, player, players, locations, weapons, traits)
        if outcome == False:
            return

        if players[0].debug == True:
            print(player.trueName + " searches for information in the gymnasium. ")
        witnesses = whoHere(player, "none", players, locations)
        event(witnesses, player, "none", "gymnasium_learn")
        return

class Medical(Location):
    def __init__(self):
        self.name = "medical"
        self.rank = 2
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "MEDICAL"
        self.blips = 0
        self.weapons = []
        
    def visit(self, player, locations, players, weapons, traits):
        outcome = roomCheck(self, player, players, locations, weapons, traits)
        if outcome == False:
            return
        if player.marks == []:
            player.LOITER(player.location, locations, players, weapons, False, traits)
            return

        if players[0].debug == True:
            print(player.trueName + " heals wounds in medical. ")
        if "bruises" in player.marks:
            allInstances(player.marks, "bruises")
            witnesses = whoHere(player, "none", players, locations)
            event(witnesses, player, "none", "medical_bruises")
        if "tired" in player.marks:
            allInstances(player.marks, "tired")
            witnesses = whoHere(player, "none", players, locations)
            event(witnesses, player, "none", "medical_tired")
        if "cuts" in player.marks:
            allInstances(player.marks, "cuts")
            witnesses = whoHere(player, "none", players, locations)
            event(witnesses, player, "none", "medical_cuts")

class Library(Location):
    def __init__(self):
        self.name = "the library"
        self.rank = 3
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "LIBRARY"
        self.blips = 0
        self.weapons = []

    def use(self, player, locations, players, weapons, traits):
        outcome = roomCheck(self, player, players, locations, weapons, traits)
        if outcome == False:
            return

        player.libraryVisits = player.libraryVisits + 1
        if players[0].debug == True:
            print(player.trueName + " reads books in the library. ")
        witnesses = whoHere(player, "none", players, locations)
        event(witnesses, player, "none", "library_use")

    def learn(self, player, locations, players, weapons, traits):
        outcome = roomCheck(self, player, players, locations, weapons, traits)
        if outcome == False:
            return

        if players[0].debug == True:
            print(player.trueName + " searches for information in the library. ")
        witnesses = whoHere(player, "none", players, locations)
        event(witnesses, player, "none", "library_learn")

class Information(Location):
    def __init__(self):
        self.name = "information"
        self.rank = 3
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "INFORMATION"
        self.blips = 0
        self.weapons = []
        
    def visit(self, player, locations, players, weapons, traits):
        outcome = roomCheck(self, player, players, locations, weapons, traits)
        if outcome == False:
            return

        if players[0].debug == True:
            print(player.trueName + " searches for information in information. ")
        witnesses = whoHere(player, "none", players, locations)
        event(witnesses, player, "none", "information")
        
class Bathhouse(Location):
    def __init__(self):
        self.name = "the bathhouse"
        self.rank = 4
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "BATHHOUSE"
        self.blips = 0
        self.weapons = []
        
    def use(self, player, locations, players, weapons, traits):
        outcome = roomCheck(self, player, players, locations, weapons, traits)
        if outcome == False:
            return

        player.bathhouseVisits = player.bathhouseVisits + 1
        if players[0].debug == True:
            print(player.trueName + " relaxes in the bathhouse. ")
        witnesses = whoHere(player, "none", players, locations)
        event(witnesses, player, "none", "bathhouse_use")

    def learn(self, player, locations, players, weapons, traits):
        outcome = roomCheck(self, player, players, locations, weapons, traits)
        if outcome == False:
            return

        if players[0].debug == True:
            print(player.trueName + " searches for information in the bathhouse. ")
        witnesses = whoHere(player, "none", players, locations)
        event(witnesses, player, "none", "bathhouse_learn")

class Communications(Location):
    def __init__(self):
        self.name = "communications"
        self.rank = 4
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "COMMUNICATIONS"
        self.blips = 0
        self.weapons = []
        
    def visit(self, player, target1, target2, locations, players, report, weapons, traits):
        outcome = roomCheck(self, player, players, locations, weapons, traits)
        if outcome == False:
            return report
        
        report += str("Audit the comms between " + str(target1.name) + " and " + str(target2.name) + " for " + player.name + ". \n")
        if players[0].debug == True:
            print(player.trueName + " searches for information in communications. ")
        witnesses = whoHere(player, "none", players, locations)
        event(witnesses, player, "none", str("communications_" + target1.name + "_" + target2.name))
        return report

class Power(Location):
    def __init__(self):
        self.name = "power"
        self.rank = 5
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "POWER"
        self.blips = 0
        self.weapons = []
        
    def visit(self, player, locations, players, weapons, traits):
        outcome = roomCheck(self, player, players, locations, weapons, traits)
        if outcome == False:
            return
        
        player.power = player.power + 1
        if players[0].debug == True:
            print(player.trueName + " works in power. ")
        witnesses = whoHere(player, "none", players, locations)
        event(witnesses, player, "none", "power")

class Armaments(Location):
    def __init__(self):
        self.name = "armaments"
        self.rank = 5
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "ARMAMENTS"
        self.blips = 0
        self.weapons = []
        
    def visit(self, player, locations, players, weapons, traits):
        outcome = roomCheck(self, player, players, locations, weapons, traits)
        if outcome == False:
            return

        if players[0].debug == True:
            print(player.trueName + " searches for information in armaments. ")
        player.allWeapons = []
        for p in range(len(players)):
            for w in range(len(players[p].weapons)):
                player.allWeapons.append(players[p].weapons[w])
        witnesses = whoHere(player, "none", players, locations)
        event(witnesses, player, "none", "armaments")

class Security(Location):
    def __init__(self):
        self.name = "security"
        self.rank = 6
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "SECURITY"
        self.blips = 0
        self.weapons = []
        
    def visit(self, player, locations, players, weapons, traits):
        outcome = roomCheck(self, player, players, locations, weapons, traits)
        if outcome == False:
            return

        if players[0].debug == True:
            print(player.trueName + " searches for information in security. ")
        witnesses = whoHere(player, "none", players, locations)
        event(witnesses, player, "none", "security")


        '''
        for l in range(len(locations)):
            locations[l].blips = 0
        for p in range(len(players)):
            for l in range(len(locations)):
                if players[p].location == locations[l]:
                    locations[l].blips = locations[l].blips + 1
        player.message += "You check the security systems and discover that there are: "
        locationsWithBlips = []
        for l in range(len(locations)):
            if locations[l].blips > 0:
                locationsWithBlips.append(locations[l])
        for l in range(len(locationsWithBlips)-1):
            player.message += str(str(locationsWithBlips[l].blips) + " bodies (alive or dead) in " + locationsWithBlips[l].name + ", ")
        player.message += str("and " + str(locationsWithBlips[len(locationsWithBlips)-1].blips) + " bodies (alive or dead) in " + locationsWithBlips[len(locationsWithBlips)-1].name + ". ")
        whoHere(player, "none", str(player.name + " is checking the security systems to see which rooms are occupied. "), str(player.trueName + " is checking the security systems to see which rooms are occupied. "), False, locations, players, weapons, traits)
        '''

class Command(Location):
    def __init__(self):
        self.name = "command"
        self.rank = 6
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "COMMAND"
        self.blips = 0
        self.weapons = []
        
    def visit(self, player, locations, players, weapons, traits):
        outcome = roomCheck(self, player, players, locations, weapons, traits)
        if outcome == False:
            return

        if players[0].debug == True:
            print(player.trueName + " searches for information in command. ")
        witnesses = whoHere(player, "none", players, locations)
        event(witnesses, player, "none", "command")