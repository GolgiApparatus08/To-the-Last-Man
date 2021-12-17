import sys
import random
import math

from Weapons import aBluntWeapon, aMedicalWeapon, aSharpWeapon

#Calculates attacker's new honor after a killing
def newHonor(attacker, victum, players, traits):
    if victum.honor < 0 or traits[0] not in attacker.traits:
        attacker.changedHonor = attacker.honor - victum.honor
        honorCorrection(attacker, victum)
        honorLog(str(attacker.trueName + " kills " + victum.trueName + ": " + str(attacker.honor) + " -> " + str(attacker.changedHonor)), players)
        attacker.honor = attacker.changedHonor
    else:
        honorLog(str(attacker.trueName + " kills " + victum.trueName + ": " + str(attacker.honor) + " -> " + str(attacker.changedHonor) + " (INNOCENT)"), players)

#Corrects honor to never be 0
def honorCorrection(actor, target):
    if actor.changedHonor == 0:
        if target.honor > 0:
            actor.changedHonor = -1
        if target.honor < 0:
            actor.changedHonor = 1

#Honor Log
def honorLog(input, players):
    players[0].honorMessage += str(input)
    players[0].honorMessage += str("\n")

#Print Honor Log at the end
def printHonor(players):
    log = open("honorLog.txt", "w")
    log.write(players[0].honorMessage)
    log.write("\n")
    log.write("FINAL HONORS")
    sortedPlayers = []
    amount = len(players)
    while len(sortedPlayers) < amount:
        leastHonor = players[0]
        leastIndex = 0
        for p in range(len(players)):
            if players[p].honor < leastHonor.honor:
                leastHonor = players[p]
                leastIndex = p
        sortedPlayers.append(leastHonor)
        players.pop(leastIndex)
    for sp in range(len(sortedPlayers)):
        log.write("\n")
        log.write(sortedPlayers[sp].trueName + ": " + str(sortedPlayers[sp].honor))
    log.close()

#Checks if an input is allowed
def answer(question, rightAnswers):
    while True:
        answer = input(question)
        if answer in rightAnswers:
            return answer
        else:
            print("That was not an acceptable answer! ")

#Saves the current state of the game
def save(nights, saveThings, players, locations, weapons):
    save = open(str("Night" + str(nights) + ".txt"), "w")

    for s in range(len(saveThings)):
        saveThings[s] = ""

    for p in range(len(players)):
        saveThings[0] += str(players[p].name + " ")
        saveThings[1] += str(str(players[p].rank) + " ")
        saveThings[2] += str(str(players[p].strength) + " ")
        saveThings[3] += str(str(players[p].intellect) + " ")
        saveThings[4] += str(str(players[p].nerves) + " ")
        weaponIndex = "none"
        infWeaponIndex = "none"
        for w in range(len(weapons)):
            if players[p].weapon == weapons[w]:
                weaponIndex = w
            if players[p].infWeapon == weapons[w]:
                infWeaponIndex = w
        saveThings[5] += str(str(weaponIndex) + " ")
        infShiftIndex = "none"
        for l in range(len(locations)):
            if players[p].location == locations[l]:
                locationIndex = l
            if players[p].shift == locations[l]:
                shiftIndex = l
            if players[p].infShift == locations[l]:
                infShiftIndex = l
        saveThings[6] += str(str(locationIndex) + " ")
        saveThings[7] += str(str(shiftIndex) + " ")
        saveThings[8] += str(str(players[p].honor) + " ")
        saveThings[9] += str(str(players[p].alive) + " ")
        saveThings[10] += str(str(players[p].gymnasiumVisits) + " ")
        saveThings[11] += str(str(players[p].libraryVisits) + " ")
        saveThings[12] += str(str(players[p].bathhouseVisits) + " ")
        mark = ""
        if "bruises" in players[p].marks:
            mark += str(1) 
        if "tired" in players[p].marks:
            mark += str(2) 
        if "cuts" in players[p].marks:
            mark += str(3)
        if mark == "":
            mark += str(0)
        saveThings[13] += str(mark + " ")
        if players[p].causeOfDeath == "none":
            death = "0"
        elif players[p].causeOfDeath == "a blunt weapon":
            death = "1"
        elif players[p].causeOfDeath == "a medical weapon":   
            death = "2"
        elif players[p].causeOfDeath == "a sharp weapon":
            death = "3"
        elif players[p].causeOfDeath == "an ambush":
            death = "4"
        elif players[p].causeOfDeath == "the tribunal":
            death = "5"
        saveThings[14] += str(death + " ")
        saveThings[15] += str(str(players[p].reported) + " ")
        saveThings[16] += str(str(players[p].infRank) + " ")
        saveThings[17] += str(str(players[p].infStrength) + " ")
        saveThings[18] += str(str(players[p].infIntellect) + " ")
        saveThings[19] += str(str(players[p].infNerves) + " ")
        saveThings[20] += str(str(infWeaponIndex) + " ")
        saveThings[21] += str(str(infShiftIndex) + " ")
        saveThings[22] += str(str(players[p].requiredWork) + " ")
        saveThings[23] += str(str(players[p].requiredSleep) + " ")
    for l in range(len(locations)):
        saveThings[24] += str(str(locations[l].sabotages) + " ")
        saveThings[25] += str(str(locations[l].workload) + " ")
        saveThings[26] += str(str(locations[l].functionality) + " ")
        saveThings[27] += str(str(locations[l].blips) + " ")

    save.write(str(nights))
    save.write("\n")
    for s in range(len(saveThings)):
        save.write(saveThings[s])
        save.write("\n")

    save.close()

#Turns lists to something I can print
def listToString(list):
        string = ""
        for l in range(len(list)):
            if l == len(list) - 1:
                string += str(list[l])
            else:
                string += str(list[l]) + ", "
        return string

#Asks how many players there will be and returns the value as amount
def howMany(numbers):
    amount = int(answer("Number of soldiers (2-11): \n", numbers))
    if amount <= 0:
        input("You don't have a base without soldiers. Come back with some players!\n")
        sys.exit()
    elif amount == 1:
        input("There's already a last man, silly!")
        sys.exit()
    elif amount > 11:
        input("There's not enough weapons to play with this many people. Sorry! ")
        sys.exit()
    else:
        return amount

#Loads the game to an earlier night
def load(file, saveThings, players, weapons, locations):
    contents = open(str(file)).readlines()
    nights = int(contents[0])
    print(contents[0])
    print(nights)
    for s in range(len(saveThings)):
        saveThings[s] = contents[1 + s].split(" ")
        print(str(saveThings[s]))

    for p in range(len(players)):
        players[p].name = saveThings[0][p]
        players[p].rank = int(saveThings[1][p])
        players[p].strength = int(saveThings[2][p])
        players[p].intellect = int(saveThings[3][p])
        players[p].nerves = int(saveThings[4][p])
        weaponIndex = saveThings[5][p]
        if weaponIndex == "none":
            players[p].weapon = "none"
        else:
            players[p].weapon = weapons[int(weaponIndex)]
        players[p].location = locations[int(saveThings[6][p])]
        players[p].shift = locations[int(saveThings[7][p])]
        players[p].honor = int(saveThings[8][p])
        if saveThings[9][p] == "True":
            players[p].alive = True
        elif saveThings[9][p] == "False":
            players[p].alive = False
        players[p].gymnasiumVisits = int(saveThings[10][p])
        players[p].libraryVisits = int(saveThings[11][p])
        players[p].bathhouseVisits = int(saveThings[12][p])
        players[p].marks = []
        marks = ["bruises", "tired", "cuts"]
        for m in range(len(marks)):
            if saveThings[13][p].find(str(m + 1)):
                players[p].marks.append(marks[m])
        deaths = ["none", "a blunt weapon", "a medical weapon", "a sharp weapon", "an ambush", "the tribunal"]
        for d in range(len(deaths)):
            if int(saveThings[14][p]) == d:
                players[p].causeOfDeath = deaths[d]
        if saveThings[15][p] == "True":
            players[p].reported = True
        elif saveThings[15][p] == "False":
            players[p].reported = False
        if saveThings[16][p] == "none":
            players[p].infRank = str(saveThings[16][p])
        else:
            players[p].infRank = int(saveThings[16][p])
        if saveThings[17][p] == "none":
            players[p].infStrength = str(saveThings[17][p])
        else:
            players[p].infStrength = int(saveThings[17][p])
        if saveThings[18][p] == "none":
            players[p].infIntellect = str(saveThings[18][p])
        else:
            players[p].infIntellect = int(saveThings[18][p])
        if saveThings[19][p] == "none":
            players[p].infNerves = str(saveThings[19][p])
        else:
            players[p].infNerves = int(saveThings[19][p])
        if saveThings[20][p] == "none":
            players[p].infWeapon = "none"
        else:
            players[p].infWeapon = weapons[int(saveThings[20][p])]
        if saveThings[21][p] == "none":
            players[p].infShift = "none"
        else:    
            players[p].infShift = locations[int(saveThings[21][p])]
        players[p].requiredWork = int(saveThings[22][p])
        players[p].requiredSleep = int(saveThings[23][p])

        players[p].currentWeapon = players[p].weapon

    for l in range(len(locations)):
        locations[l].sabotages = int(saveThings[24][p])
        locations[l].workload = int(saveThings[25][p])
        if saveThings[26][p] == "True":
            locations[l].functionality = True
        elif saveThings[26][p] == "False":
            locations[l].functionality = False
        locations[l].blips = int(saveThings[27][p])
    return nights

#Splits things :P
def mySplit(ob):
    ob.split()
    words = []
    newWord = True
    for x in range(len(ob)):
        if newWord == True:
            words.append(ob[x])
            newWord = False
        else:
            if ob[x] != " ":
                words[-1] += str(ob[x])
                newWord = False
            else:
                newWord = True
    return words

#Is called each night to read what players will be doing for each action
def readCommands(players):
    correct = False
    while correct == False:
        contents = open('playerData.txt').readlines()
        for p in range(len(players) - 1):
            players[p].commands = []
            if contents[(p * 16) + 6] != "":
                input("WARNING: " + players[p].name + "'s commands are not lined up! ")
                continue
            players[p].commands.append(contents[(p * 16) + 7].strip())
            players[p].commands.append(contents[(p * 16) + 8].strip())
            players[p].commands.append(contents[(p * 16) + 9].strip())
            players[p].commands.append(contents[(p * 16) + 10].strip())
            players[p].commands.append(contents[(p * 16) + 11].strip())
            players[p].commands.append(contents[(p * 16) + 12].strip())
            players[p].commands.append(contents[(p * 16) + 13].strip())
            players[p].commands.append(contents[(p * 16) + 14].strip())
            if contents[(p * 16) + 15] != "":
                input("WARNING: " + players[p].name + "'s commands are not lined up! ")
                continue
            for c in range(len(players[p].commands)):
                if players[0].debug == True:
                    print("COMMAND " + str(c + 1) + ": " + players[p].commands[c])
            for c in range(len(players[p].commands)):
                players[p].commands[c] = mySplit(players[p].commands[c])
            if players[0].debug == True:
                print(players[p].trueName + " command's have been read! \n")
        correct = True

#Generates random commands for random player set in testing
def randomCommands(players, locations, weapons):
    for p in range(len(players)-1):
        if players[p].alive == False:
            players[p].commands = ["DEAD", "DEAD", "DEAD", "DEAD", "DEAD", "DEAD", "DEAD", "DEAD"]
        else:
            players[p].commands = ["none", "none", "none", "none", "none", "none", "none", "none"]

            commandHours = [0, 1, 2, 3, 4, 5, 6, 7]
            #Pick Rest Hours randomly
            hoursToRest = players[p].requiredSleep
            for i in range(hoursToRest):
                roll = random.randint(0,len(commandHours) - 1)
                restHour = commandHours[roll]
                players[p].commands[restHour] = "REST"
                commandHours.pop(roll)
            #Sometimes Work Randomly
            outcomes = [0, 1]
            roll = random.choice(outcomes)
            if roll == 1:
                hoursToWork = players[p].shift.workload
                if players[p].weapon == weapons[7]:
                    hoursToWork = 1
                if len(commandHours) >= hoursToWork:    
                    for i in range(hoursToWork):
                        roll = random.randint(0,len(commandHours) - 1)
                        workHour = commandHours[roll]
                        players[p].commands[workHour] = str("WORK " + players[p].shift.input)
                        commandHours.pop(roll)
            #Randomly pick actions for remaining hours
            actions = [
                "SABOTAGE",
                "LOITER",
                "AMBUSH",
                "KILL",
                "KILL",
                "KILL",
                "WATCH",
                "STEAL",
                "BARRAKS",
                "SANITATION",
                "GYMNASIUM",
                "MEDICAL",
                "LIBRARY",
                "INFORMATION",
                "BATHHOUSE",
                "COMMUNICATIONS",
                "POWER",
                "ARMAMENTS",
                "SECURITY",
                "COMMAND"
            ]
            playersToTarget = []
            for i in range(len(players)-1):
                if players[i].reported == False and players[i] != players[p]:
                    playersToTarget.append(players[i])
            for c in range(len(players[p].commands)):
                if players[p].commands[c] == "none":
                    command = random.choice(actions)
                    if command == "SABOTAGE" or command == "LOITER":
                        room = random.choice(locations)
                        players[p].commands[c] = str(command + " " + room.input)
                    if command == "AMBUSH":
                        room = random.choice(locations)
                        target = random.choice(playersToTarget)
                        players[p].commands[c] = str(command + " " + room.input + " " + target.name)
                    if command == "KILL" or command == "WATCH" or command == "STEAL":
                        target = random.choice(playersToTarget)
                        players[p].commands[c] = str(command + " " + target.name)
                    for l in range(len(locations)):
                        if locations[l].input == command and (l == 2 or l == 4 or l == 6):
                            players[p].commands[c] = str(command + " use")
                        elif locations[l].input == command and l == 7:
                            equal = True
                            while equal == True:
                                target1 = random.choice(playersToTarget)
                                target2 = random.choice(playersToTarget)
                                if target1 != target2:
                                    equal = False
                            players[p].commands[c] = str(command + " " + target1.name + " " + target2.name)
                        elif locations[l].input == command:
                            players[p].commands[c] = str(command)
        if players[p].alive == True:
            for c in range(len(players[p].commands)):
                if players[0].debug == True:
                    print("COMMAND " + str(c+1) + ": " + players[p].commands[c])
                players[p].commands[c] = mySplit(players[p].commands[c])
            if players[0].debug == True:
                print(players[p].trueName + " command's have been read! \n")

#Gives Living Players Shifts
def shifts(players, locations, traits):
    shiftsToChoose = locations.copy()
    playersToAssign = []
    for p in range(len(players)-1):
        if players[p].reported == False:
            playersToAssign.append(players[p])

    aShiftWasChosen = False
    player = "none"
    for pa in range(len(playersToAssign)):
        if traits[21] in playersToAssign[pa].traits:
            player = playersToAssign[pa]
            playerIndex = pa
            aShiftWasChosen = True

    if player != "none":
        if players[0].ran == True:
            chosenShift = random.choice(locations)
        else:
            locationInputs = []
            for i in range(len(locations)):
                locationInputs.append(locations[i].input)
            chosenShift = answer("Which shift would " + player.name + " like for the next night? ", locationInputs)
            print(" ")
        for l in range(len(locations)):
            if locations[l].input == chosenShift or locations[l] == chosenShift:
                player.shift = locations[l]
                print("SHIFTS: ")
                print(player.trueName + "'s shift is now " + str(player.shift) + "! ")
                shiftsToChoose.pop(l)
                playersToAssign.pop(playerIndex)

    if aShiftWasChosen == False:
        print("SHIFTS: ")
    for pa in range(len(playersToAssign)):
        roll = random.randint(0, len(shiftsToChoose)-1)
        playerShift = shiftsToChoose[roll]
        shiftsToChoose.pop(roll)
        playersToAssign[pa].shift = playerShift
        playersToAssign[pa].shift.workload = playersToAssign[pa].shift.workload + playersToAssign[pa].requiredWork
        print(playersToAssign[pa].trueName + "'s shift is now " + str(playersToAssign[pa].shift) + "! ")

#To randomize a list
def randomize(original):
    randomized = []
    x = 0
    while len(randomized) < len(original):
        choice = random.choice(original)
        if choice not in randomized:
            randomized.append(choice)
        x = x + 1
    return randomized

#Attempts to send a player to a room. Is called anytime a players location might require updating. Checks if they can access the room, sends them to a location accordingly and tells them about it.
def checkAccess(player, room, WORK, hour, locations):
    if player.alive == False:
        return
    if player.location == room:
        player.message += str("\n")
        player.message += str("At " + hour + " you stay in " + room.name + ". ")
        if player.debug == True:
            print("MOVE: " + player.trueName + " has remained in " + room.name + ". ")
    else:
        canAccess = False
        if player.location.rank >= room.rank:
            canAccess = True
        elif player.rank >= room.rank:
            canAccess = True
        elif player.shift == room and WORK == True:
            canAccess = True
        elif locations[11].functionality == False:
            canAccess = True
        if canAccess == True:
            player.location = room
            player.message += str("\n")
            player.message += str("Around " + hour + " you make your way to " + room.name + ". ")
            if player.debug == True:
                print("MOVE: " + player.trueName + " has been moved to " + room.name + ". ")
        else:
            player.message += str("\n")
            player.message += str("Around " + hour + " you fail to access " + room.name + ", and return to " + player.location.name + ". ")
            if player.debug == True:
                print("MOVE: " + player.trueName + " failed to access " + room.name + " and returned to " + player.location.name + ". ")

#If the locate function gets caught in a loop, this fixes it and then abandons the function so it can try again
def resolveLoop(inALoop, hour, locations):
    for r in range(6):
        for l in range(len(inALoop)):
            if inALoop[l].location.rank == r + 1:
                inALoop[l].located = True
                checkAccess(inALoop[l], inALoop[l].location, False, hour, locations)
                return

#Finds the player in questions target and sees if they have been located. If they are, it sends the player there, if not it trys to locate them.
def locate(players, player, time, inALoop, locations, hour):
    player.visited = True
    inALoop.append(player)
    for p in range(len(players)):
        if players[p].trueName == player.commands[time][1]:
            if players[p].visited == True:
                resolveLoop(inALoop, hour, locations)
                return "loop"
            else:
                if players[p].located == True:
                    player.located = True
                    checkAccess(player, players[p].location, False, hour, locations)
                    return "located"
                else:
                    outcome = locate(players, players[p], time, inALoop, locations, hour)
                    if outcome == "located":
                        player.located = True
                        checkAccess(player, players[p].location, False, hour, locations)
                        return "located"
                    else:
                        return "loop"

#Resets the loop list and visited attribute at the end of a locate attempt
def clearLoop(players, inALoop):
    for p in range(len(players)):
        players[p].visited = False
        inALoop = []
        return inALoop

#Removes ALL of a particular item from a list
def allInstances(list, item):
    done = False
    while done == False:
        index = "none"
        for l in range(len(list)):
            if list[l] == item:
                index = l
        if index == "none":
            done = True
        else:
            list.pop(index)

def activityString(self, activity, traits):
    involved = []
    for e in range(len(self.events)):
        if activity == "work" and self.events[e].action == "sabotage" and traits[8] not in self.traits and self.events[e].actor != self:
            involved.append(self.events[e].actor)
        elif self.events[e].action == activity and activity != "sabotage":
            involved.append(self.events[e].actor)
        elif self.events[e].action == activity and activity == "sabotage":
            if traits[8] in self.traits or self.events[e].actor == self:
                involved.append(self.events[e].actor)
    string = stringList(involved, self)
    return string

def stringList(players, self):
    txt = ""
    names = []
    for p in range(len(players)):
        if players[p] != self:
            names.append(players[p].name)
    if self in players:
        names.append("you")
    if len(names) == 1:
        names[0] = names[0].capitalize()
    for n in range(len(names)):
        if n != (len(names) - 1) and n != (len(names) - 2):
            txt += str(names[n] + ", ")
        if n == (len(names) - 2) and len(names) > 2:
            txt += str(names[n] + ", and ")
        if n == (len(names) - 2) and len(names) < 3:
            txt += str(names[n] + " and ")
        if n == (len(names) - 1):
            txt += str(names[n])
    return txt

class Event:
    def __init__(self, actor, target, action, actorWeapon, targetWeapon, actorHonor, targetHonor):
        self.actor = actor 
        self.target = target
        self.action = action
        self.actorWeapon = actorWeapon
        self.targetWeapon = targetWeapon
        self.actorHonor = actorHonor
        self.targetHonor = targetHonor

#Produce wounds
def getHurt(actor1, actor2, mark, traits):
    if traits[28] not in actor1.traits:
        actor1.marks.append(mark)
    if traits[28] not in actor2.traits:
        actor2.marks.append(mark)

#Makes an "event" package which is given to every witness of the event, as well as the actor and target
def event(witnesses, actor, target, action):
    actorWeapon = actor.currentWeapon
    targetWeapon = "bite me"
    targetHonor = "bite me"
    if target != "none":
        targetWeapon = target.currentWeapon
        targetHonor = target.honor
    actorHonor = actor.honor
    
    currentEvent = Event(
        actor,
        target,
        action,
        actorWeapon,
        targetWeapon,
        actorHonor,
        targetHonor,
    )
    for w in range(len(witnesses)):
        witnesses[w].events.append(currentEvent)
    actor.events.append(currentEvent)
    if target != "none":
        target.events.append(currentEvent)

#Finds who is in the room with a player during an action
def whoHere(seen, target, players, locations):
    if locations[8].functionality == False:
        return []
    whoHere = []
    for p in range(len(players)):
        if players[p].location == seen.location and players[p] != seen and players[p] != target and players[p].alive == True:
            whoHere.append(players[p])
    return whoHere

#Someone has been seen, this will show their wounds and any deductions
def seen(seen, witness, players, traits):

    for p in range(len(players)):
        if players[p] == seen:
            playerIndex = p

    #Do they deduce and how much
    howMuch = 0
    chances = 1
    if traits[32] in witness.traits:
        chances = 2
    while chances > 0:
        rollOutcomes = [1, 2, 3, 4, 5, 6, 7, 8]
        roll = random.choice(rollOutcomes)
        if witness.intellect >= roll:
            howMuch = howMuch + 1
        chances = chances - 1
    
    #Minor string changes
    name = seen.name
    tense = "is"
    secondTense = "have"
    end = ". "
    if seen.alive == False:
        name = str(seen.name + "'s body")
        tense = "was"
        secondTense = "had"
    if traits[17] in witness.traits:
        name = seen.trueName
    if howMuch > 0:
        end = "; and "

    wounds = False
    if "bruises" in seen.marks and "cuts" not in seen.marks and "tired" not in seen.marks:
        witness.message += str(name + " looks covered in bruises" + end)
        wounds = True
    elif "cuts" in seen.marks and "bruises" not in seen.marks and "tired" not in seen.marks:
        witness.message += str(name + " looks covered in cuts" + end)
        wounds = True
    elif "tired" in seen.marks and "bruises" not in seen.marks and "cuts" not in seen.marks:
        witness.message += str(name + " looks mentally exhausted" + end)
        wounds = True
    elif "bruises" in seen.marks and "cuts" in seen.marks and "tired" not in seen.marks:
        witness.message += str(name + " looks covered in bruises and cuts" + end)
        wounds = True
    elif "bruises" in seen.marks and "tired" in seen.marks and "cuts" not in seen.marks:
        witness.message += str(name + " looks covered in bruises and mentally exhausted" + end)
        wounds = True
    elif "bruises" not in seen.marks and "cuts" in seen.marks and "tired" in seen.marks:
        witness.message += str(name + " looks covered in cuts and mentally exhausted" + end)
        wounds = True
    elif "bruises" in seen.marks and "cuts" in seen.marks and "tired" in seen.marks:
        witness.message += str(name + " looks covered in bruises, covered in cuts, and mentally exhausted" + end)
        wounds = True

    #Deductions
    if howMuch > 0:
        thingsToLearn = []
        if traits[1] not in seen.traits:
            thingsToLearn.append("rank")
        if traits[2] not in seen.traits:
            thingsToLearn.append("strength")
        if traits[3] not in seen.traits:
            thingsToLearn.append("intellect")
        if traits[4] not in seen.traits:
            thingsToLearn.append("nerves")
        if traits[5] not in seen.traits:
            thingsToLearn.append("weapon")
        if traits[6] not in seen.traits:
            thingsToLearn.append("shift")
        if traits[18] in witness.traits and witness != players[-1]:
            thingsToLearn.append("honor")
        if traits[7] not in seen.traits:
            thingsToLearn.append("traits")
        deduced = []
        while howMuch > 0:
            choice = random.randint(0, len(thingsToLearn)-1)
            deduced.append(thingsToLearn[choice])
            thingsToLearn.pop(choice)
            howMuch = howMuch - 1

        if wounds == True:
            witness.message += "you deduce that "
        else:
            witness.message += str("You deduce that ")
        for d in range(len(deduced)):
            end = ". "
            beginning = str(name + "'s")
            if len(deduced) > 1 and d == 0:
                end = " and "
            if wounds == True or d > 0:
                beginning = "their"
            if deduced[d] == "rank":
                witness.message += str(beginning + " rank " + tense + " " + str(seen.rank) + end)
                witness.otherRanks[playerIndex].append(seen.rank)
            if deduced[d] == "strength":
                witness.message += str(beginning + " strength " + tense + " " + str(seen.strength) + end)
                witness.otherStrengths[playerIndex].append(seen.strength)
            if deduced[d] == "intellect":
                witness.message += str(beginning + " intellect " + tense + " " + str(seen.intellect) + end)
                witness.otherIntellects[playerIndex].append(seen.intellect)
            if deduced[d] == "nerves":
                witness.message += str(beginning + " nerves " + tense + " " + str(seen.nerves) + end)
                witness.otherNerves[playerIndex].append(seen.nerves)
            if deduced[d] == "weapon":
                if seen.currentWeapon != "none":
                    witness.message += str(beginning + " weapon " + tense + " " + str(seen.currentWeapon) + end)
                    witness.otherWeapons[playerIndex].append(seen.currentWeapon)
                else:
                    beginning = name
                    if secondTense == "have":
                        secondTense = "has"
                    witness.message += str(beginning + " " + secondTense + " no weapon" + end)
                    witness.otherWeapons[playerIndex].append("none")
            if deduced[d] == "shift":
                if seen.shift != "shift":
                    witness.message += str(beginning + " shift " + tense + " " + str(seen.shift) + end)
                else:
                    beginning = name 
                    if secondTense == "have":
                        secondTense = "has"
                    witness.message += str(beginning + " " + secondTense + " no shift" + end)
            if deduced[d] == "honor":
                witness.message += str(beginning + " honor " + tense + " " + str(seen.honor) + end)
                witness.otherHonors[playerIndex].append(seen.honor)
            if deduced[d] == "traits":
                traitToLearn = random.choice(seen.traits)
                witness.message += str("one of " + beginning + " traits " + tense + " " + traitToLearn.name.upper() + end)
                witness.otherTraits[playerIndex].append(traitToLearn.name)

#Roll that decides if a player defends when they are attacked
def doTheyDefend(attacker, target):
    rollOutcomes = [1, 2, 3, 4, 5, 6, 7, 8]
    difference = target.strength - attacker.strength
    roll = random.choice(rollOutcomes)
    if difference >= roll:
        return "pass"
    else:
        return "fail"

#Updates player attributes based on room visits
def roomPoints(player, playerRoomVisits, attributeString, playerAttribute):
    if playerRoomVisits > 1:
        points = math.floor(playerRoomVisits / 2)
        playerAttribute = playerAttribute + points
        loss = points * 2
        playerRoomVisits = playerRoomVisits - loss
        player.endMessage += str("Your " + attributeString + " is now " + str(playerAttribute) + ". ")

#Decides how much time a player needs to spend working tommorrow night
def requiredWork(actor, locations):
    if locations[1].functionality == True:
        actor.requiredWork = 2 - actor.power
    else:
        actor.requiredWork = 3 - actor.power
    actor.power = 0
    if actor.requiredWork < 0:
        actor.requiredWork = 0
    actor.endMessage += str("You will have to spend " + str(actor.requiredWork) + " actions (plus sabotages) to complete your shift, ")

def requiredSleep(actor, locations):
    if locations[0].functionality == True:
        actor.requiredSleep = 4 - actor.sleep
    else:
        actor.requiredSleep = 5 - actor.sleep
    actor.sleep = 0
    if int(actor.requiredSleep) < 0:
        actor.requiredSleep = 0
    actor.endMessage += str("and " + str(actor.requiredSleep) + " actions resting tomorrow night. ")

#Determines what I reveal about dead bodies
def weSeeDeadPeople(actor, locations, report, tribunal):
    if actor.alive == False and actor.reported == False and actor.location.functionality == True:
        if tribunal == True:
            report += str("Their last location was " + actor.location.name + ". ")
        else:
            report += str(actor.name + "'s body has been found in " + str(actor.location) + ": ")
        if locations[5].functionality == True:
            report += str("Their rank was " + str(actor.rank) + ". ")
        if locations[2].functionality == True:
            report += str("Their strength was " + str(actor.strength) + ". ")
        if locations[4].functionality == True:
            report += str("Their intellect was " + str(actor.intellect) + ". ")
        if locations[6].functionality == True:
            report += str("Their nerves was " + str(actor.nerves) + ". ")
        if locations[9].functionality == True:
            report += str("Their weapon was " + str(actor.weapon) + ". ")
        if locations[11].functionality == True:
            report += str("Their shift was " + str(actor.shift) + ". ")
        report += str("They were " + actor.traits[0].name + ", " + actor.traits[1].name + ", and " + actor.traits[2].name + ". ")
        if locations[3].functionality == True:
            report += str("They were killed by " + actor.causeOfDeath + ". ")
        report += "\n"
        actor.reported = True
        return report
    return report

#Highborn
def demotion(players, traits):
    for p in range(len(players)):
        if players[p].alive == True and traits[22] in players[p].traits:
            if players[0].ran == False:
                response = answer("Would " + players[p].name + " like to demote a player? ", ["Yes", "No"])
            else:
                roll = random.randint(0, 1)
                if roll == 1:
                    response = "Yes"
                else:
                    response = "No"
            if response == "Yes":
                if players[0].ran == False:
                    playerNames = []
                    for p in range(len(players)-1):
                        playerNames.append(players[p].name)
                    demoted = answer("Which player?", playerNames)
                else:
                    toDemote = []
                    for i in range(len(players)-1):
                        if players[i] != players[p] and players[i].location != "none":
                            toDemote.append(players[i])
                    demoted = random.choice(toDemote)
                for i in range(len(players) - 1):
                    if players[i].name == demoted:
                        players[i].rank = players[i].rank - 1

#Court is in Session
def theTribunal(players, locations, weapons, report, traits):
    extantPlayers = []
    for p in range(len(players)-1):
        if players[p].reported == False:
            extantPlayers.append(players[p])
    if len(extantPlayers) < 3:
        input("There are not enough soldiers left to conduct a tribunal. ")
        return
    tribunalists = []
    print("")
    if players[0].ran == True:
        input("Press ENTER to randomize tribunal attendance! ")
    for p in range(len(players) - 1):
        if players[p].alive == True:
            if players[0].ran == True:
                roll = random.randint(0, 5)
                if roll > 0:
                    tribunalists.append(players[p])
            else:
                response = answer("Is " + players[p].name + " showing up to the tribunal? ", ["Yes", "No"])
                if response == "Yes":
                    tribunalists.append(players[p])

#"Is " + players[p].name + " showing up to the tribunal? "

    print("")
    for t in range(len(tribunalists)):
        print(tribunalists[t].trueName)
        print(" ")
        for i in range(len(tribunalists)):
            if tribunalists[t] != tribunalists[i]:
                tribunalists[t].message += str(tribunalists[i].name + " has showed up to the tribunal. ")
                if locations[8].functionality == True:
                    seen(tribunalists[i], tribunalists[t], players, traits)
        if locations[8].functionality == False:
            tribunalists[t].message += str("Because the power is out, you can only bearly make them out by candle light, and cannot deduce anything about them or notice any wounds. ")
        if tribunalists[t].message == "":
            tribunalists[t].message = "No one else showed up to the tribunal. "
        print(tribunalists[t].message)
        tribunalists[t].message = ""
        print(" ")
    for t in range(len(tribunalists)):
        tribunalists[t].marks = []

    input("Press ENTER to begin voting! ")
    print(" ")
    honorLog(str("\nTHE TRIBUNAL"), players)
    for t in range(len(tribunalists)):
        if players[0].ran == True:
            response = []
            for p in range(len(players) -1):
                if players[p] != tribunalists[t]:
                    roll = random.randint(0, 1)
                    if roll == 1 and players[p].reported == False:
                        response.append(players[p].name)
        else:
            response = input("Who is " + tribunalists[t].name + " voting for? ")
            response.split()
        for r in range(len(response)):
            for p in range(len(players) - 1):
                if response[r] == players[p].name and players[p].reported == False:
                    oldHonor = tribunalists[t].changedHonor
                    if players[p].honor > 0 and traits[0] not in tribunalists[t].traits:
                        tribunalists[t].changedHonor = tribunalists[t].changedHonor - 1
                        honorCorrection(tribunalists[t], players[p])
                        honorLog(str(tribunalists[t].name + " voted " + players[p].name + ": " + str(oldHonor) + " -> " + str(tribunalists[t].changedHonor)), players)
                    elif players[p].honor > 0:
                        honorLog(str(tribunalists[t].name + " voted " + players[p].name + ": " + str(oldHonor) + " -> " + str(tribunalists[t].changedHonor) + " (INNOCENT)"), players)
                    elif players[p].honor < 0:
                        tribunalists[t].changedHonor = tribunalists[t].changedHonor + 1
                        honorCorrection(tribunalists[t], players[p])
                        honorLog(str(tribunalists[t].name + " voted " + players[p].name + ": " + str(oldHonor) + " -> " + str(tribunalists[t].changedHonor)), players)
                    players[p].accusers.append(tribunalists[t])
    for p in range(len(players)):
        players[p].honor = players[p].changedHonor
    for e in range(len(extantPlayers)):
        print("Votes to Kill " + extantPlayers[e].name + ": ")
        for a in range(len(extantPlayers[e].accusers)):
                print(extantPlayers[e].accusers[a].name)
        if len(extantPlayers[e].accusers) >= len(extantPlayers)/2 and extantPlayers[e].alive == True:
            print(extantPlayers[e].name + " has been executed by the tribunal. ")
            extantPlayers[e].alive = False
            extantPlayers[e].causeOfDeath = "the tribunal"
            report = weSeeDeadPeople(extantPlayers[e], locations, report, True)
            print(report + "\n")
            report = ""
        elif len(extantPlayers[e].accusers) >= len(extantPlayers)/2:
            print("The tribunal attempts to execute " + extantPlayers[e].name + ", but finds them already dead. ")
            report = weSeeDeadPeople(extantPlayers[e], locations, report, True)
            print(report + "\n")
            report = ""
        else:
            print(extantPlayers[e].name + " has survived the tribunal. ")
            print("\n")
            extantPlayers[e].accusers = []

#Gives someone with sleeping pills a sleep for resting
def freeRest(actor, traits):
    if traits[35] in actor.traits:
        actor.sleep = actor.sleep + 1
        actor.message += str("Because you're a deep sleeper, it was extra refreshing. ")

#calculates the work done to a location
def workload(actor, room, traits):
    if traits[24] in actor.traits:
        room.workload = 0
    else:
        room.workload = room.workload - 1

#Asks players what weapon they would like to use if Armaments is down.
def chooseYourWeapon(players, locations):
    for p in range(len(players) - 1):
        if locations[9].functionality == False:
            if players[0].ran == True:
                weaponsToChoose = [aBluntWeapon(), aMedicalWeapon(), aSharpWeapon()]
                chosenWeapon = random.choice(weaponsToChoose)
            else:
                chosenWeapon = answer("Which type of weapon would " + players[p].name + " like to use for the night (blunt, medical, or sharp)? \n", ["blunt", "medical", "sharp"])
            if chosenWeapon == "blunt":
                players[p].currentWeapon = aBluntWeapon()
            elif chosenWeapon == "medical":
                players[p].currentWeapon = aMedicalWeapon()
            elif chosenWeapon == "sharp":
                players[p].currentWeapon = aSharpWeapon()

#Finds out if anyone attacks in response to a murder or witnessing of a murder
def bloodFeud(attacker, target, present, players, weapons, time, locations, traits):
    if present != []:
        playersRandomized = randomize(players)
        presentRandomized = randomize(present)
        for p in range(len(playersRandomized)):
            for i in range(len(presentRandomized)):
                if traits[33] in attacker.traits and playersRandomized[p] == presentRandomized[i] and playersRandomized[p].alive == True and attacker.alive == True and playersRandomized[p] != playersRandomized[-1]:
                    attacker.message += str("You decide that it is better to be feared than loved and attack " + playersRandomized[p].name + " in order to silence a witness. ")
                    attacker.KILL(playersRandomized[p], time, locations, playersRandomized, weapons, traits)
                if playersRandomized[p] == presentRandomized[i] and traits[23] in playersRandomized[p].traits and playersRandomized[p].alive == True and attacker.alive == True and attacker != playersRandomized[-1]:
                    playersRandomized[p].message += str("In righteous fury, you decide to avenge " + target.name + " by attacking " + attacker.name + ". ")
                    playersRandomized[p].KILL(attacker, time, locations, playersRandomized, weapons, traits)

#The Enemy's Brain
def enemyPlans(players, locations, weapons, nights):
    players[-1].commands = ["none", "none", "none", "none", "none", "none", "none", "none"]

    #Pick Rest Hours randomly
    hoursToRest = 4
    if players[-1].weapon == weapons[10] and nights != 0:
        hoursToRest = 2
    commandHours = [0, 1, 2, 3, 4, 5, 6, 7]
    for i in range(hoursToRest):
        roll = random.randint(0,len(commandHours) - 1)
        restHour = commandHours[roll]
        players[-1].commands[restHour] = "REST"
        commandHours.pop(roll)

    #Loiter in highest ranking room at first opportunity
    x = 0
    for c in range(len(players[-1].commands)):
        if players[-1].commands[c] == "none" and x == 0:
            rank = players[-1].rank
            highestLocations = []
            for l in range(len(locations)):
                if locations[l].rank == rank:
                    highestLocations.append(locations[l])
            loiterChoice = random.choice(highestLocations)
            players[-1].commands[c] = str("SABOTAGE " + loiterChoice.input) #Might as well sabotage it while hes there
            x = x + 1

    #Should we try to kill someone?
    attack = False
    vulnerable = [players[0]]
    for p in range(len(players)-1):
        if players[-1].weapon.type == "blunt":
            if players[p].infStrength != "none" and vulnerable[0].infStrength == "none":
                vulnerable = [players[p]]
            elif players[p].infStrength != "none" and players[p].infStrength < vulnerable[0].infStrength and players[p] != players[0]:
                vulnerable = [players[p]]
            elif players[p].infStrength != "none" and players[p].infStrength == vulnerable[0].infStrength and players[p] != players[0]:
                vulnerable.append(players[p])
            if players[p].infStrength != "none" and players[p].infStrength < players[-1].strength:
                attack = True
        if players[-1].weapon.type == "medical":
            if players[p].infIntellect != "none" and vulnerable[0].infIntellect == "none":
                vulnerable = [players[p]]
            elif players[p].infIntellect != "none" and players[p].infIntellect < vulnerable[0].infIntellect and players[p] != players[0]:
                vulnerable = [players[p]]
            elif players[p].infIntellect != "none" and players[p].infIntellect == vulnerable[0].infIntellect and players[p] != players[0]:
                vulnerable.append(players[p])
            if players[p].infIntellect != "none" and players[p].infIntellect < players[-1].intellect:
                attack = True
        if players[-1].weapon.type == "sharp":
            if players[p].infNerves != "none" and vulnerable[0].infNerves == "none":
                vulnerable = [players[p]]
            if players[p].infNerves != "none" and players[p].infNerves < vulnerable[0].infNerves and players[p] != players[0]:
                vulnerable = [players[p]]
            elif players[p].infNerves != "none" and players[p].infNerves == vulnerable[0].infNerves and players[p] != players[0]:
                vulnerable.append(players[p])
            if players[p].infNerves != "none" and players[p].infNerves < players[-1].nerves:
                attack = True
    if attack == True:
        randomVulnerable = randomize(vulnerable)
        mostVulnerable = randomVulnerable[0]
        for v in range(len(randomVulnerable)):
            if randomVulnerable[v].infStrength < mostVulnerable.infStrength:
                mostVulnerable = randomVulnerable[v]
            
        #Attack the most vulnerable
        x = 0
        for c in range(len(players[-1].commands)):
            if players[-1].commands[c][0] == "none" and x == 0:
                players[-1].commands[c] = str("KILL " + mostVulnerable.name)
                x = x + 1
                roll = [1, 2]
                rollChoice = random.choice(roll)
                if rollChoice == 1:
                    players[-1].commands[c+1] = str("MEDICAL")

    #Spend the remaining hours training or spying
    outcomes = ["SABOTAGE"]
    if locations[2].functionality == True:
        outcomes.append("GYMNASIUM use")
    if locations[4].functionality == True:
        outcomes.append("LIBRARY use")
    if locations[6].functionality == True:
        outcomes.append("BATHHOUSE use")
    for c in range(len(players[-1].commands)):
        if players[-1].commands[c] == "none":
            decision = random.choice(outcomes)
            if decision == "SABOTAGE":
                accessRooms = []
                for l in range(len(locations)):
                    if locations[l].rank <= players[-1].rank:
                        accessRooms.append(locations[l])
                roomToSabotage = random.choice(accessRooms)
                players[-1].commands[c] = str("SABOTAGE " + roomToSabotage.input)
            else:
                players[-1].commands[c] = decision

    for c in range(len(players[-1].commands)):
        if players[-1].debug == True:
                print("COMMAND " + str(c+1) + ": " + players[-1].commands[c])
        players[-1].commands[c] = mySplit(players[-1].commands[c])

    #Enemy takes a name
    namesToCopy = []
    for p in range(len(players) - 1):
        if players[p].reported == False:
            namesToCopy.append(players[p])
    chosenName = random.choice(namesToCopy)
    players[-1].name = chosenName.name
    if players[0].debug == True:
        print("The Enemy will be called " + players[-1].name + " for the night. ")
        print(" ")