from os import name
import random
import sys
from Functions import available, doTheyDefend, event, getHurt, highestStat, newHonor, whoHere, whoToAttack, workload, bloodFeud

class Player:
    def __init__(self, name, rank, strength, intellect, nerves, weapon, location, traits):

        #Game Rules
        self.debug = True
        self.ran = True

        self.name = name
        self.rank = rank
        self.infRank = "none"
        self.strength = strength
        self.infStrength = "none"
        self.intellect = intellect
        self.infIntellect = "none"
        self.nerves = nerves
        self.infNerves = "none"
        self.weapons = [weapon]
        self.location = location
        self.shift = "none"
        self.infShift = "none"
        self.honor = 1
        self.alive = True
        self.message = ""
        self.gymnasiumVisits = 0
        self.libraryVisits = 0
        self.bathhouseVisits = 0
        self.power = 0
        self.sleep = 0
        self.marks = []
        self.commands = []
        self.located = False
        self.visited = False
        self.weaponsStolen = []
        self.accusers = []
        self.requiredWork = 2
        self.requiredSleep = 4
        self.trueName = name
        self.causeOfDeath = "none"
        self.endMessage = ""
        self.reported = False
        self.traits = traits
        self.honorMessage = ""
        self.changedHonor = self.honor
        self.events = []
        self.initiatedFights = 0            #For the Rowdy trait
        self.otherRanks = []
        self.otherStrengths = []
        self.otherIntellects = []
        self.otherNerves = []
        self.otherTraits = []
        self.otherWeapons = []
        self.otherHonors = []
        self.previousLocation = location
        self.allWeapons = []
        self.weaponChanges = ""

    def DEAD(self, locations, players):
        if players[0].debug == True and self.reported == False:
            print(self.trueName + " is dead in " + self.location.name + ". ")
        witnesses = whoHere(self, "none", players, locations)
        event(witnesses, self, "none", "dead")

    def REST(self, locations, players, weapons, traits):
        if self.alive == False:
            self.DEAD(locations, players)
            return
        if players[0].debug == True and self.location != locations[0]:
            print(self.trueName + " is resting in " + self.location.name + ". ")
        
        if self.location == locations[0] and locations[0].functionality == True:   #Barraks
            self.location.visit(self, locations, players, weapons, traits)
        else:                               #Anywhere else
            witnesses = whoHere(self, "none", players, locations)
            event(witnesses, self, "none", "rest")

    def WORK(self, room, locations, players, weapons, traits):
        if self.alive == False:
            self.DEAD(locations, players)
            return
        if self.location != room:
            self.LOITER(self.location, locations, players, weapons, False, traits)
            return
        if players[0].debug == True:
            print(self.trueName + " is working in " + self.location.name + ". ")

        workload(self, self.location, traits)
        witnesses = whoHere(self, "none", players, locations)
        event(witnesses, self, "none", "work")

    def SABOTAGE(self, room, locations, players, weapons, traits):
        if self.alive == False:
            self.DEAD(locations, players)
            return
        if traits[25] in self.traits:       #TRAIT: HACKER
            room.sabotages = room.sabotages + 1
            if players[0].debug == True:
                print(self.trueName + " sabotages " + room.name + " with their hacking from " + self.location.name + ". ")
            witnesses = whoHere(self, "none", players, locations)
            event(witnesses, self, "none", "sabotage_hacker")
            self.LOITER(self.location, locations, players, weapons, True, traits)
            return
        if self.location != room:
            self.LOITER(self.location, locations, players, weapons, False, traits)
            return
        if players[0].debug == True:
            print(self.trueName + " is sabotaging " + self.location.name + ". ")

        room.sabotages = room.sabotages + 1
        witnesses = whoHere(self, "none", players, locations)
        event(witnesses, self, "none", "sabotage")

    def LOITER(self, room, locations, players, weapons, taskCompleted, traits):
        if self.alive == False:
            self.DEAD(locations, players)
            return
        if room == locations[0] and self.location == locations[0] and locations[0].functionality == True:
            locations[0].visit(self, locations, players, weapons, traits)
            return
        if self.location != room:
            self.LOITER(self.location, locations, players, weapons, False, traits)
            return
        if players[0].debug == True and taskCompleted == False:
            print(self.trueName + " is loitering in " + self.location.name + ". ")

        witnesses = whoHere(self, "none", players, locations)
        event(witnesses, self, "none", "loiter")

    def AMBUSH(self, room, target, locations, players, time, weapons, traits):
        if self.alive == False:
            self.DEAD(locations, players)
            return
        if traits[27] in self.traits and target.location == room and target.alive == True:
            target.alive = False
            target.causeOfDeath = "a medical weapon"
            newHonor(self, target, players, traits, weapons)
            if players[0].debug == True:
                print(self.trueName + " kills " + target.name + " with a trap in " + room.name + " from " + self.location.name + ". ")
            witnesses = whoHere(self, target, players, locations)
            event(witnesses, self, target, "ambush_chemist")
            self.LOITER(self.location, locations, players, weapons, True, traits)
            return
        elif traits[27] in self.traits and target.location != room:
            if players[0].debug == True:
                print(self.trueName + " attempts kill " + target.trueName + " in " + room.name + " with a trap from " + self.location.name + ", but they're not there. ")
            witnesses = whoHere(self, target, players, locations)
            event(witnesses, self, target, "ambush_chemist_fail")
            self.LOITER(self.location, locations, players, weapons, False, traits)
            return
        if self.location != room:
            self.LOITER(self.location, locations, players, weapons, False, traits)
            return
        if self.location != target.location:
            witnesses = whoHere(self, target, players, locations)
            event(witnesses, self, target, "ambush_fail")
            self.LOITER(self.location, locations, players, weapons, False, traits)
            return

        target.alive = False
        target.causeOfDeath = "an ambush"
        newHonor(self, target, players, traits, weapons)
        if players[0].debug == True:
                print(self.trueName + " ambushes and kills " + target.name + " in " + room.name + ". ")
        witnesses = whoHere(self, target, players, locations)
        event(witnesses, self, target, "ambush")
        bloodFeud(self, witnesses, players, weapons, time, locations, traits)
        return

    def ENEMY(self, weaponType, room, locations, players, weapons, traits):
        if self.alive == False:
            self.DEAD(locations, players)
            return
        if self.location != room:
            self.LOITER(self.location, locations, players, weapons, False, traits)
            return
        if self.location != players[-1].location:
            witnesses = whoHere(self, players[-1], players, locations)
            event(witnesses, self, players[-1], "enemy_notPresent")
            self.LOITER(self.location, locations, players, weapons, False, traits)
            return
        
        youFailed = False
        availableTypes = available(self.weapons, locations)

        #Has no weapon
        if weaponType not in availableTypes:
            witnesses = whoHere(self, players[-1], players, locations)
            event(witnesses, self, players[-1], "enemy_dontHave")
            youFailed = True

        #Has blunt weapon
        if weaponType == "blunt" and youFailed == False:
            getHurt(self, players[-1], "blunt", traits)
            if self.strength > players[-1].strength:
                if players[0].debug == True:
                    print(self.trueName + " kills The Enemy in " + self.location.name + ". ")
                witnesses = whoHere(self, players[-1], players, locations)
                event(witnesses, self, players[-1], "enemy_bluntSuccess")
            else:
                youFailed = True
                witnesses = whoHere(self, players[-1], players, locations)
                event(witnesses, self, players[-1], "enemy_bluntFail")

        #Has medical weapon
        if weaponType == "medical" and youFailed == False:
            getHurt(self, players[-1], "tired", traits)
            if self.intellect > players[-1].intellect:
                if players[0].debug == True:
                    print(self.trueName + " kills The Enemy in " + self.location.name + ". ")
                witnesses = whoHere(self, players[-1], players, locations)
                event(witnesses, self, players[-1], "enemy_medicalSuccess")
            else:
                youFailed = True
                witnesses = whoHere(self, players[-1], players, locations)
                event(witnesses, self, players[-1], "enemy_medicalFail")

        #Has sharp weapon
        if weaponType == "sharp" and youFailed == False:
            getHurt(self, players[-1], "cuts", traits)
            if self.nerves > players[-1].nerves:
                if players[0].debug == True:
                    print(self.trueName + " kills The Enemy in " + self.location.name + ". ")
                witnesses = whoHere(self, players[-1], players, locations)
                event(witnesses, self, players[-1], "enemy_sharpSuccess")
            else:
                youFailed = True
                witnesses = whoHere(self, players[-1], players, locations)
                event(witnesses, self, players[-1], "enemy_sharpFail")

        #The Enemy's Turn
        if youFailed == True:
            bestAngle = whoToAttack(self, players, locations)
            if bestAngle == "none":
                bestType = highestStat(players[-1], locations)
            else:
                bestType = bestAngle[0]

            if bestType == "blunt":
                getHurt(self, players[-1], "bruises", traits)
                if players[-1].strength > self.strength:
                    if players[0].debug == True:
                        print(self.trueName + " is killed by The Enemy in " + self.location.name + ". ")
                    self.alive = False
                    self.causeOfDeath = "a blunt weapon"
                    witnesses = whoHere(players[-1], self, players, locations)
                    event(witnesses, players[-1], self, "enemyAttack_bluntSuccess")
                else:
                    if players[0].debug == True:
                        print(self.trueName + " failed to kill The Enemy in " + self.location.name + " and survived its counter attack. ")
                    witnesses = whoHere(players[-1], self, players, locations)
                    event(witnesses, players[-1], self, "enemyAttack_bluntFail")
            if bestType == "medical":
                getHurt(self, players[-1], "tired", traits)
                if players[-1].intellect > self.intellect:
                    if players[0].debug == True:
                        print(self.trueName + " is killed by The Enemy in " + self.location.name + ". ")
                    self.alive = False
                    self.causeOfDeath = "a medical weapon"
                    witnesses = whoHere(players[-1], self, players, locations)
                    event(witnesses, players[-1], self, "enemyAttack_medicalSuccess")
                else:
                    if players[0].debug == True:
                        print(self.trueName + " failed to kill The Enemy in " + self.location.name + " and survived its counter attack. ")
                    witnesses = whoHere(players[-1], self, players, locations)
                    event(witnesses, players[-1], self, "enemyAttack_medicalFail")
            if bestType == "sharp":
                getHurt(self, players[-1], "cuts", traits)
                if players[-1].nerves > self.nerves:
                    if players[0].debug == True:
                        print(self.trueName + " is killed by The Enemy in " + self.location.name + ". ")
                    self.alive = False
                    self.causeOfDeath = "a sharp weapon"
                    witnesses = whoHere(players[-1], self, players, locations)
                    event(witnesses, players[-1], self, "enemyAttack_sharpSuccess")
                else:
                    if players[0].debug == True:
                        print(self.trueName + " failed to kill The Enemy in " + self.location.name + " and survived its counter attack. ")
                    witnesses = whoHere(players[-1], self, players, locations)
                    event(witnesses, players[-1], self, "enemyAttack_sharpFail")
            if bestType == "":
                if players[0].debug == True:
                    print("The enemy has no weapon and thus cannot retaliate. ")
                witnesses = whoHere(players[-1], self, players, locations)
                event(witnesses, players[-1], self, "enemyAttack_noWeapon")

    def WATCH(self, locations, players, weapons, target, traits):
        if self.alive == False:
            self.DEAD(locations, players)
            return
        if self.location != target.location:
            self.LOITER(self.location, locations, players, weapons, False, traits)
            return

        if players[0].debug == True:
            print(self.trueName + " watches " + target.name + " closely. ")
        self.LOITER(self.location, locations, players, weapons, False, traits)

    def WIELD(self, room, players, locations, weapons, traits):
        if self.alive == False:
            self.DEAD(locations, players)
            return
        if self.location != room:
            self.LOITER(self.location, locations, players, weapons, False, traits)
            return
        if room.weapons == []:
            event([], self, "none", "wield_noWeapon")
            self.LOITER(self.location, locations, players, weapons, False, traits)
            return

        index = random.randint(0, len(room.weapons)-1)
        players[0].weaponChanges += str("-Add the " + room.weapons[index].withoutArticle + " from " + room.name + " to " + self.trueName + "'s hand \n")
        self.weapons.append(room.weapons[index])
        room.weapons.pop(index)
        if players[0].debug == True:
            print(self.trueName + " aquires " + self.weapons[-1].name + " in " + room.name + ". ")
        witnesses = whoHere(self, "none", players, locations)
        event(witnesses, self, "none", "wield")
        return
        
    def STEAL(self, target, locations, players, weapons, traits):
        def newOwner(thief, victum):
            weaponIndex = random.randint(0, len(victum.weapons)-1)
            weapon = victum.weapons[weaponIndex]
            thief.weapons.append(weapon)
            victum.weapons.pop(weaponIndex)
            victum.weaponsStolen.append(weapon)
            players[0].weaponChanges += str("-Move " + victum.name + "'s " + weapon.withoutArticle + " to " + thief.trueName + "'s hand \n")
            return weapon

        if self.alive == False:
            self.DEAD(locations, players)
            return
        if self.location != target.location:
            self.LOITER(self.location, locations, players, weapons, False, traits)
            return
        if traits[39] in self.traits:
            self.LOITER(self.location, locations, players, weapons, False, traits)
            return
        if target.alive == False and target.weapons != []:
            stolen = newOwner(self, target)
            if players[0].debug == True:
                print(self.trueName + " steals " + stolen.name + " off " + target.name + "'s body in " + target.location.name + ". ")
            witnesses = whoHere(self, target, players, locations)
            event(witnesses, self, target, "stealBody_success")
            self.LOITER(self.location, locations, players, weapons, True, traits)
            return
        if target.alive == False:
            if players[0].debug == True:
                print(self.trueName + " steals nothing off " + target.name + "'s body in " + target.location.name + ". ")
            witnesses = whoHere(self, target, players, locations)
            event(witnesses, self, target, "stealBody_nothing")
            self.LOITER(self.location, locations, players, weapons, True, traits)
            return

        outcomes = [1, 2, 3, 4, 5, 6, 7, 8]
        roll = random.choice(outcomes)
        if self.nerves >= roll or weapons[1] in target.weapons:
            if target.weapons != []:
                stolen = newOwner(self, target)
                if players[0].debug == True:
                    print(self.trueName + " steals " + stolen.name + " off " + target.name + " in " + target.location.name + ". ")
                witnesses = whoHere(self, target, players, locations)
                event(witnesses, self, target, "steal_success")
                self.LOITER(self.location, locations, players, weapons, True, traits)
            else:
                if players[0].debug == True:
                    print(self.trueName + " steals nothing off " + target.name + " in " + target.location.name + ". ")
                witnesses = whoHere(self, target, players, locations)
                event(witnesses, self, target, "steal_nothing")
                self.LOITER(self.location, locations, players, weapons, True, traits)
        else:
            if players[0].debug == True:
                print(self.trueName + " is caught trying to steal " + target.name + "'s weapon in " + target.location.name + ". ")
            witnesses = whoHere(self, target, players, locations)
            event(witnesses, self, target, "steal_fail")

    def KILL(self, target, weaponType, time, locations, players, weapons, traits):
        #Make sure there in the right place
        if self.location != target.location:
            self.LOITER(self.location, locations, players, weapons, False, traits)
            return
        #Make sure their target isn't already dead
        if target.alive == False:
            witnesses = whoHere(self, target, players, locations)
            event(witnesses, self, target, "kill_body")
            self.LOITER(self.location, locations, players, weapons, False, traits)
            return
        #Check for bodyguards
        for p in range(len(players)):           
            if players[p].location == self.location:
                if traits[10] in players[p].traits:
                    defend = doTheyDefend(self, players[p], traits)
                    if defend == "pass":
                        if players[0].debug == True:
                            print(self.trueName + " tries to attack " + target.name + " in " + target.location.name + ", but is scared away by " + players[p].name + ". ")
                        event([], self, players[p], "bodyguard")
                        self.LOITER(self.location, locations, players, weapons, True, traits)
                        return
        #Check if the target intimidates
        defend = doTheyDefend(self, target, traits)
        if defend == "pass":
            if players[0].debug == True:
                print(self.trueName + " tries to attack " + target.name + " in " + target.location.name + ", but is scared away. ")
            witnesses = whoHere(self, target, players, locations)
            event(witnesses, self, target, "kill_intimidate")
            self.LOITER(self.location, locations, players, weapons, True, traits)
            return
        #Make sure they have access to the weapontype they want to use
        availableTypes = available(self.weapons, locations)
        if weaponType not in availableTypes:
            if players[0].debug == True:
                print(self.trueName + " tries to attack " + target.name + " in " + target.location.name + ", but has no weapon. ")
            witnesses = whoHere(self, target, players, locations)
            event(witnesses, self, target, "kill_noWeapon")
            self.LOITER(self.location, locations, players, weapons, True, traits)
            return

        self.initiatedFights = self.initiatedFights + 1
        def fightType(weaponType):
            if weaponType == "blunt":
                attributeSelf = self.strength
                attributeTarget = target.strength
                wounds = "bruises"
                causeofDeath = "a blunt weapon"
                success = "kill_bluntSuccess"
                defense = "kill_bluntDefense"
                fail = "kill_bluntFail"
            elif weaponType == "medical":
                attributeSelf = self.intellect
                attributeTarget = target.intellect
                wounds = "tired"
                causeofDeath = "a medical weapon"
                success = "kill_medicalSuccess"
                defense = "kill_medicalDefense"
                fail = "kill_medicalFail"
            elif weaponType == "sharp":
                attributeSelf = self.nerves
                attributeTarget = target.nerves
                wounds = "cuts"
                causeofDeath = "a sharp weapon"
                success = "kill_sharpSuccess"
                defense = "kill_sharpDefense"
                fail = "kill_sharpFail"

            getHurt(self, target, wounds, traits)
            #Check for instant failure based on weapons
            weaponFailsThem = False
            weaponFailsYou = False
            if weapons[15] in self.weapons and self.honor < target.honor:
                weaponFailsYou = True
            if weapons[12] in self.weapons and self.rank < target.rank:
                weaponFailsYou = True
            if weapons[15] in target.weapons and target.honor < self.honor:
                weaponFailsThem = True
            if weapons[12] in target.weapons and target.rank < self.rank:
                weaponFailsThem = True
            if attributeSelf > attributeTarget and weaponFailsYou == False:
                outcome = "success"
            elif attributeSelf <= attributeTarget and weaponFailsThem == True and weaponFailsYou == False:
                outcome = "success"
            elif attributeSelf > attributeTarget and weaponFailsYou == True and weaponFailsThem == False:
                outcome = "failure"
            elif attributeSelf <= attributeTarget and weaponFailsThem == False:
                outcome = "failure"

            if outcome == "success":
                target.alive = False
                target.causeOfDeath = causeofDeath
                newHonor(self, target, players, traits, weapons)
                if players[0].debug == True:
                    print(self.trueName + " kills " + target.name + " in " + target.location.name + ". ")
                witnesses = whoHere(self, target, players, locations)
                event(witnesses, self, target, success)
                bloodFeud(self, witnesses, players, weapons, time, locations, traits)
                return
            else:
                if traits[34] in target.traits and self != players[-1]:
                    self.alive = False
                    self.causeOfDeath = causeofDeath
                    newHonor(self, target, players, traits, weapons)
                    newHonor(target, self, players, traits, weapons)
                    if players[0].debug == True:
                        print(self.trueName + " fails to kill " + target.name + " and is beat to death in " + target.location.name + ". ")
                    witnesses = whoHere(self, target, players, locations)
                    event(witnesses, self, target, defense)
                    return
                else:
                    if players[0].debug == True:
                        print(self.trueName + " fails to kill " + target.name + " in " + target.location.name + ". ")
                    witnesses = whoHere(self, target, players, locations)
                    event(witnesses, self, target, fail)
                    return

        #Attackers Weapon
        if weaponType == "blunt":
            fightType("blunt")
        elif weaponType == "medical":
            fightType("medical")
        elif weaponType == "sharp":
            fightType("sharp")

#Is called to insert players into the game by reading their data of of playerData.txt
def readPlayerData(players, amount, startingLocation, weapons, traits):
    print("\n")
    contents = open('playerData.txt').readlines()
    for p in range(amount):
        players.append(
            Player(
                contents[p * 8].strip(),
                int(contents[(p * 8) + 1]),
                int(contents[(p * 8) + 2]),
                int(contents[(p * 8) + 3]),
                int(contents[(p * 8) + 4]),
                contents[(p * 8) + 5].strip(),
                startingLocation,
                contents[(p * 8) + 6].split()
        ))
        for w in range(len(weapons)):
            if players[p].weapons[0] == weapons[w].name:
                players[p].weapons = [weapons[w]]
        traitValue = 0
        for t in range(len(traits)):
            for pt in range(3):
                if players[p].traits[pt] == traits[t].name:
                    players[p].traits[pt] = traits[t]
                    traitValue = traitValue + traits[t].value


        print(" ")
        print("NAME: " + players[p].name)
        print("rank: " + str(players[p].rank))
        print("str: " + str(players[p].strength))
        print("int: " + str(players[p].intellect))
        print("ner: " + str(players[p].nerves))
        print("WEAPON: " + players[p].weapons[0].name)
        print("TRAITS: " + players[p].traits[0].name + ", " + players[p].traits[1].name + ", " + players[p].traits[2].name)
        print(traitValue)


#This is for generating a player set with random stats for testing
def randomPlayers(players, amount, weapons, startingLocation, traits):
    namesToChoose = [
        "Scott",
        "Jack",
        "Ryan",
        "Sebby",
        "Paul",
        "Nathan",
        "Nate",
        "Ed",
        "Lisa",
        "Eddie",
        "Kevin",
        "Ish",
        "Skylar",
        "Christian",
        "Morgan",
        "Susu",
        "Jun",
        "Jesus",
        "Sheogoth_the_Unborn",
        "Sol_Invictus",
        "Julius_Caesar",
        "The_Buddha"
    ]
    stats = ["rank", "strength", "intellect", "nerves"]
    weaponsToChoose = weapons.copy()
    traitsToChoose = traits.copy()

    for p in range(amount):
        roll = random.randint(0,len(namesToChoose) - 1)
        playerName = namesToChoose[roll]
        namesToChoose.pop(roll)
        playerTraits = []
        points = 12
        for i in range(3):
            traitNames = []
            for pt in range(len(playerTraits)):
                traitNames.append(playerTraits[pt].name)
            availableTrait = False
            while availableTrait == False:
                roll = random.randint(0,len(traitsToChoose) -1)
                chooseAgain = False
                for c in range(len(traitsToChoose[roll].contras)):
                    if traitsToChoose[roll].contras[c] in traitNames:
                        chooseAgain = True
                if chooseAgain == False:
                    availableTrait = True
            playerTraits.append(traitsToChoose[roll])
            points = points - traitsToChoose[roll].value
            traitsToChoose.pop(roll)
        playerRank = 1
        playerStrength = 1
        playerIntellect = 1
        playerNerves = 1
        for s in range(points):
            stat = random.choice(stats)
            if stat == "rank":
                playerRank = playerRank + 1
            elif stat == "strength":
                playerStrength = playerStrength + 1
            elif stat == "intellect":
                playerIntellect = playerIntellect + 1
            elif stat == "nerves":
                playerNerves = playerNerves + 1
        roll = random.randint(0,len(weaponsToChoose) - 1)
        playerWeapon = weaponsToChoose[roll]
        weaponsToChoose.pop(roll)

        players.append(
            Player(
                playerName,
                playerRank,
                playerStrength,
                playerIntellect,
                playerNerves,
                playerWeapon,
                startingLocation,
                playerTraits
        ))
        print(" ")
        print("NAME: " + players[p].name)
        print("rank: " + str(players[p].rank))
        print("str: " + str(players[p].strength))
        print("int: " + str(players[p].intellect))
        print("ner: " + str(players[p].nerves))
        print("WEAPON: " + players[p].weapons[0].name)
        print("TRAITS: " + players[p].traits[0].name + ", " + players[p].traits[1].name + ", " + players[p].traits[2].name)
        print(12 - points)

        if traits[11] in players[p].traits:
            players[p].requiredSleep = 0

#Creates the enemy
def spawnEnemy(players, weapons, startingLocation, traits):
    stats = ["rank", "strength", "intellect", "nerves"]
    weaponsToChoose = []
    for w in range(len(weapons)):
        x = 0
        for p in range(len(players)):
            if players[p].weapons[0] == weapons[w]:
                x = x + 1
        if x == 0:
            weaponsToChoose.append(weapons[w])
    traitsToChoose = []
    for t in range(len(traits)):
        x = 0
        for p in range(len(players)):
            for pt in range(3):
                if players[p].traits[pt] == traits[t]:
                    x = x + 1
        if x == 0:
            traitsToChoose.append(traits[t])
    playerTraits = []
    points = 10
    for i in range(3):
        roll = random.randint(0,len(traitsToChoose) - 1)
        playerTraits.append(traitsToChoose[roll])
        points = points - traitsToChoose[roll].value
        traitsToChoose.pop(roll)
    playerRank = 1
    playerStrength = 1
    playerIntellect = 1
    playerNerves = 1
    for s in range(points):
        stat = random.choice(stats)
        if stat == "rank":
            playerRank = playerRank + 1
        elif stat == "strength":
            playerStrength = playerStrength + 1
        elif stat == "intellect":
            playerIntellect = playerIntellect + 1
        elif stat == "nerves":
            playerNerves = playerNerves + 1

    players.append(
        Player(
            "The Enemy",
            playerRank,
            playerStrength,
            playerIntellect,
            playerNerves,
            random.choice(weaponsToChoose),
            startingLocation,
            playerTraits
        ))

    print("NAME: The Enemy")
    print("rank: " + str(players[-1].rank))
    print("str: " + str(players[-1].strength))
    print("int: " + str(players[-1].intellect))
    print("ner: " + str(players[-1].nerves))
    print("WEAPON: " + str(players[-1].weapons[0].name))
    print("TRAITS: " + players[-1].traits[0].name + ", " + players[-1].traits[1].name + ", " + players[-1].traits[2].name)
    print(10 - points)
    print(" ")