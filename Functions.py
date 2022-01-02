import sys
import random
import math

#Returns which weapons types are available
def available(owned, locations):
    availableTypes = []
    for o in range(len(owned)):
        availableTypes.append(str(owned[o].type))
    if locations[9].functionality == False:
        availableTypes = ["blunt", "medical", "sharp"]
    return availableTypes

#Reminds the moderator of all unique player command rules
def remind(players, traits, weapons):
    print("")
    print("COMMAND RULES: ")
    for p in range(len(players)-1):
        if players[p].alive == True:
            players[p].message += str("must rest " + str(players[p].requiredSleep) + " hours, ")
            if traits[11] in players[p].traits:
                players[p].message += str("cannot work, ")
            if weapons[0] in players[p].weapons:
                players[p].message += str("must rest +1 for every kill they plan, ")
            if weapons[7] in players[p].weapons:
                players[p].message += str("must work as many hours as they are able toward completing their shift, ")
            if weapons[13] in players[p].weapons:
                players[p].message += str("must attempt to kill at least one player, ")
            if traits[39] in players[p].traits:
                players[p].message += str("cannot wield or steal, ")
            players[p].message = players[p].message[:-1]
            players[p].message = players[p].message[:-1]
            print(players[p].name + ": " + players[p].message)
            players[p].message = ""
    print(" ")

#Calculates attacker's new honor after a killing
def newHonor(attacker, victum, players, traits, weapons):
    if weapons[11] in victum.weapons:
        honorLog(str(attacker.trueName + " kills " + victum.trueName + ": " + str(attacker.honor) + " -> " + str(attacker.honor) + " (NEUROTOXIC GAS)"), players)
        return
    if victum.honor < 0 or traits[43] not in attacker.traits:
        attacker.changedHonor = attacker.honor - victum.honor
        honorCorrection(attacker, victum)
        honorLog(str(attacker.trueName + " kills " + victum.trueName + ": " + str(attacker.honor) + " -> " + str(attacker.changedHonor)), players)
        attacker.honor = attacker.changedHonor
    else:
        honorLog(str(attacker.trueName + " kills " + victum.trueName + ": " + str(attacker.honor) + " -> " + str(attacker.changedHonor) + " (CONFESSOR)"), players)

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
    save = open(str("Saves/Night" + str(nights) + ".txt"), "w")

    for s in range(len(saveThings)):
        saveThings[s] = ""

    for p in range(len(players)):
        saveThings[0] += str(players[p].name + " ")
        saveThings[1] += str(str(players[p].rank) + " ")
        saveThings[2] += str(str(players[p].strength) + " ")
        saveThings[3] += str(str(players[p].intellect) + " ")
        saveThings[4] += str(str(players[p].nerves) + " ")
        weaponIndexes = ""
        for w in range(len(weapons)):
            for pw in range(len(players[p].weapons)):
                if players[p].weapons[pw] == weapons[w]:
                    weaponIndexes += weapons[w].index
        if weaponIndexes == "":
            weaponIndexes = "none"
        saveThings[5] += str(str(weaponIndexes) + " ")
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
        saveThings[20] += str(str(infShiftIndex) + " ")
        saveThings[21] += str(str(players[p].requiredWork) + " ")
        saveThings[22] += str(str(players[p].requiredSleep) + " ")
    for l in range(len(locations)):
        saveThings[23] += str(str(locations[l].sabotages) + " ")
        saveThings[24] += str(str(locations[l].workload) + " ")
        saveThings[25] += str(str(locations[l].functionality) + " ")
        saveThings[26] += str(str(locations[l].blips) + " ")

    save.write(str(nights))
    save.write("\n")
    for s in range(len(saveThings)):
        save.write(saveThings[s])
        save.write("\n")

    save.close()

#Turns lists to something I can print
def listToString(list, grammer):
        string = ""
        for l in range(len(list)):
            if l == len(list) - 1:
                string += str(list[l])
            elif l == 0 and len(list) == 2 and grammer == True:
                string += str(list[l]) + " and "
            elif l == len(list) - 2 and len(list) > 2 and grammer == True:
                string += str(list[l]) + ", and "
            else:
                string += str(list[l]) + ", "
        return string

#Asks how many players there will be and returns the value as amount
def howMany(numbers):
    amount = int(answer("Number of soldiers (2-12): \n", numbers))
    if amount <= 0:
        input("You don't have a base without soldiers. Come back with some players!\n")
        sys.exit()
    elif amount == 1:
        input("There's already a last man, silly!")
        sys.exit()
    elif amount > 12:
        input("There's not enough shifts to play with this many people. Sorry! ")
        sys.exit()
    else:
        return amount

#Loads the game to an earlier night
def load(file, saveThings, players, weapons, locations):
    contents = open("Saves/" + str(file)).readlines()
    nights = int(contents[0])
    for s in range(len(saveThings)):
        saveThings[s] = contents[1 + s].split(" ")
        print(str(saveThings[s]))

    for p in range(len(players)):
        players[p].name = saveThings[0][p]
        players[p].rank = int(saveThings[1][p])
        players[p].strength = int(saveThings[2][p])
        players[p].intellect = int(saveThings[3][p])
        players[p].nerves = int(saveThings[4][p])
        weaponIndexes = saveThings[5][p]
        players[p].weapons = []
        if weaponIndexes != "none":
            weaponAmount = len(weaponIndexes)/2
            for a in range(weaponAmount):
                weaponIndex = weaponIndexes[a*2:a*2+2]
                for w in range(len(weapons)):
                    if weapons[w].index == str(weaponIndex):
                        players[p].weapons.append(weapons[w])
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
            players[p].infShift = "none"
        else:    
            players[p].infShift = locations[int(saveThings[20][p])]
        players[p].requiredWork = int(saveThings[21][p])
        players[p].requiredSleep = int(saveThings[22][p])

    for l in range(len(locations)):
        locations[l].sabotages = int(saveThings[23][p])
        locations[l].workload = int(saveThings[24][p])
        if saveThings[25][p] == "True":
            locations[l].functionality = True
        elif saveThings[25][p] == "False":
            locations[l].functionality = False
        locations[l].blips = int(saveThings[26][p])
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
def randomCommands(players, locations, weapons, traits):
    for p in range(len(players)-1):
        if players[p].alive == False:
            players[p].commands = ["DEAD", "DEAD", "DEAD", "DEAD", "DEAD", "DEAD", "DEAD", "DEAD"]
        else:
            players[p].commands = ["none", "none", "none", "none", "none", "none", "none", "none"]

            commandHours = [0, 1, 2, 3, 4, 5, 6, 7]
            #Pick Rest Hours randomly
            if players[p].weapons != []:
                outcomes = [0, 1]
                attackAttempts = random.choice(outcomes)
            hoursToRest = players[p].requiredSleep
            if weapons[0] in players[p].weapons:
                hoursToRest = hoursToRest + attackAttempts
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
                if len(commandHours) >= hoursToWork:    
                    for i in range(hoursToWork):
                        roll = random.randint(0,len(commandHours) - 1)
                        workHour = commandHours[roll]
                        players[p].commands[workHour] = str("WORK " + players[p].shift.input)
                        commandHours.pop(roll)
            #Sometimes attack
            playersToTarget = []
            for i in range(len(players)-1):
                if players[i].reported == False and players[i] != players[p]:
                    playersToTarget.append(players[i])
            while attackAttempts > 0:
                if len(commandHours) > 0:
                    roll = random.randint(0,len(commandHours) - 1)
                    target = random.choice(playersToTarget)
                    bestType = highestStat(players[p], locations)
                    attackHour = commandHours[roll]
                    players[p].commands[attackHour] = str("KILL" + " " + target.name + " " + bestType)
                    commandHours.pop(roll)
                attackAttempts = attackAttempts - 1
            #Sometimes go for free weapons
            room = wieldForDummies(players[p], locations)
            if room != "none" and traits[39] not in players[p].traits:
                if len(commandHours) > 0:
                    roll = random.randint(0,len(commandHours) - 1)
                    wieldHour = commandHours[roll]
                    players[p].commands[wieldHour] = str("WIELD " + room.input)
                    commandHours.pop(roll)
            #Randomly pick actions for remaining hours
            actions = [
                "SABOTAGE",
                "LOITER",
                "AMBUSH",
                "WATCH",
            ]
            if players[p].weapons != []:
                if locations[1].functionality == True or traits[12] in players[p].traits:
                    actions.append("SANITATION")
                else:
                    actions.append("DROP")
            if traits[39] not in players[p].traits:
                actions.append("STEAL")
            for l in range(len(locations)):
                if locations[l] != locations[1]:
                    if locations[l].functionality == True or traits[12] in players[p].traits:
                        actions.append(locations[l].input)

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
                    if command == "WATCH" or command == "STEAL":
                        target = random.choice(playersToTarget)
                        players[p].commands[c] = str(command + " " + target.name)
                    if command == "DROP":
                        weaponToChuck = random.choice(players[p].weapons)
                        room = random.choice(locations)
                        for w in range(len(weapons)):
                            if weaponToChuck == weapons[w]:
                                weaponIndex = w
                        players[p].commands[c] = str(command + " " + room.input + " " + str(weaponIndex))
                    for l in range(len(locations)):
                        if locations[l].input == command and (l == 2 or l == 4 or l == 6):
                            players[p].commands[c] = str(command + " use")
                        elif locations[l].input == command and l == 1:
                            weaponToChuck = random.choice(players[p].weapons)
                            for w in range(len(weapons)):
                                if weaponToChuck == weapons[w]:
                                    weaponIndex = w
                            players[p].commands[c] = str(command + " " + str(weaponIndex))
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

#Random choice that might not be so random after all ;)
def magic(actor, target, ritual, traits):
    doOffering = False
    if ritual in traits[0].rituals:
        doOffering = True
    if actor.offerings > 0 and doOffering == True:
        actor.offerings = actor.offerings - 1
        return 1
    elif actor.offerings > 0 and doOffering == True:
        target.offerings = target.offerings - 1
        return 8
    else:
        outcomes = [1, 2, 3, 4, 5, 6, 7, 8]
        return random.choice(outcomes)

#Gives Living Players Shifts
def shifts(players, locations, traits):
    shiftsToChoose = locations.copy()
    playersToAssign = []
    for p in range(len(players)-1):
        if players[p].reported == False:
            playersToAssign.append(players[p])
    playersToAssign = randomize(playersToAssign)

    player = "none"
    for pa in range(len(playersToAssign)):
        if traits[21] in playersToAssign[pa].traits:
            player = playersToAssign[pa]
            playerIndex = pa

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
    else:
        print("SHIFTS: ")
    for pa in range(len(playersToAssign)):
        roll = random.randint(0, len(shiftsToChoose)-1)
        playersToAssign[pa].shift = shiftsToChoose[roll]
        shiftsToChoose.pop(roll)
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
def checkAccess(player, room, action, hour, locations, traits):
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
        elif player.shift == room and action == "WORK":
            canAccess = True
        elif locations[11].functionality == False:
            canAccess = True
        elif action == "WATCH" and traits[26] in player.traits:
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
def resolveLoop(inALoop, hour, locations, time, traits):
    for r in range(6):
        for l in range(len(inALoop)):
            if inALoop[l].location.rank == r + 1:
                inALoop[l].located = True
                checkAccess(inALoop[l], inALoop[l].location, inALoop[l].commands[time][0], hour, locations, traits)
                return

#Finds the player in questions target and sees if they have been located. If they are, it sends the player there, if not it trys to locate them.
def locate(players, player, time, inALoop, locations, hour, traits):
    player.visited = True
    inALoop.append(player)
    for p in range(len(players)):
        if players[p].trueName == player.commands[time][1]:
            if players[p].visited == True:
                resolveLoop(inALoop, hour, locations, time, traits)
                return "loop"
            else:
                if players[p].located == True:
                    player.located = True
                    checkAccess(player, players[p].location, players[p].commands[time][0], hour, locations, traits)
                    return "located"
                else:
                    outcome = locate(players, players[p], time, inALoop, locations, hour, traits)
                    if outcome == "located":
                        player.located = True
                        checkAccess(player, players[p].location, players[p].commands[time][0], hour, locations, traits)
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

def activityString(self, activity, traits, nightPhase, weapons):
    involved = []
    for e in range(len(self.events)):
        #WORK INCLUDES UNSEEN SABOTAGE
        if activity == "work" and self.events[e].action == "sabotage" and traits[8] not in self.traits and self.events[e].actor != self and weapons[2] not in self.events[e].actor.weapons:
            involved.append(self.events[e].actor)
        #PLAYER CAN SEE SABOTAGE
        elif activity == "sabotage" and self.events[e].action == activity:
            if traits[8] in self.traits or self.events[e].actor == self or weapons[2] in self.events[e].actor.weapons:
                involved.append(self.events[e].actor)   
        #DEATH INCLUDES LOITER FOR DRAMA QUEENS
        elif activity == "dead" and traits[14] in self.events[e].actor.traits and self.events[e].action == "loiter" and nightPhase >= 4:
            involved.append(self.events[e].actor)
        #PLAYER SEES THERE OWN LOITER
        elif activity == self.events[e].action and activity == "loiter" and self.events[e].actor == self:
            completedTask = False
            for i in range(len(self.events)):
                if self.events[i].actor == self:
                    if self.events[i].action == "stealBody_success" or self.events[i].action == "stealBody_nothing" or self.events[i].action == "steal_success" or self.events[i].action == "steal_nothing" or self.events[i].action == "kill_intimidate" or self.events[i].action == "kill_noWeapon":
                        completedTask = True
            if completedTask == False:
                involved.append(self)
        #LOITER CAN BE SEEN
        elif activity == "loiter" and self.events[e].action == activity:
            if traits[14] not in self.events[e].actor.traits or nightPhase < 4:     
                involved.append(self.events[e].actor)  
        #GENERIC
        elif activity == self.events[e].action:
            involved.append(self.events[e].actor)
    string = stringList(involved, self)
    return string

def stringList(objects, self):
    txt = ""
    names = []
    for i in range(len(objects)):
        if objects[i] != self:
            names.append(objects[i].name)
    if self in objects:
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
def getHurt(actor1, actor2, mark, traits):              #TRAIT DEBUFF: Doctor
    if traits[28] not in actor1.traits:
        actor1.marks.append(mark)
    if traits[28] not in actor2.traits:                 
        actor2.marks.append(mark)

#Makes an "event" package which is given to every witness of the event, as well as the actor and target
def event(witnesses, actor, target, action):
    actorWeapon = actor.weapons
    targetWeapon = "bite me"
    targetHonor = "bite me"
    if target != "none":
        targetWeapon = target.weapons
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

def knowBank(bank, seenName, learned, players):
    p = 0
    while p < len(players):
        if players[p].trueName == seenName:
            index = p
            p = len(players)
        p = p + 1

    if bank[index][0] == " ":
        bank[index][0] = learned
    else:
        bank[index].append(learned)

#Someone has been seen, this will show their wounds and any deductions
def seen(seen, witness, freebi, players, traits, weapons):
    if seen == witness:
        return

    #PATRIOTIC
    seenName = seen.name
    if traits[17] in witness.traits:
        seenName = seen.trueName
    
    p = 0
    while p < len(players):
        if players[p].trueName == seenName:
            index = p
            p = 100
        p = p + 1

    #Do they deduce and how much
    howMuch = 0
    chances = 1
    if traits[32] in witness.traits and freebi == False:            #TRAIT DEBUFF: Curious
        chances = 2
    if weapons[6] in witness.weapons:                               #WEAPON DEBUFF: Strong Bourbon
        chances = 0
    while chances > 0:
        if freebi == True:
            roll = 1
        else:
            roll = magic(witness, seen, "deduce", traits)
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
    if traits[17] in witness.traits:                    #TRAIT DEBUFF: Patriotic
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

    #Determine if they have already seen all the weapons to see
    weaponToFind = False
    if seen.weapons == []:
        weaponToFind = True
    else:
        for w in range(len(seen.weapons)):
            if seen.weapons[w].name not in witness.otherWeapons[index]:
                weaponToFind = True

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
        if traits[5] not in seen.traits and weaponToFind == True:
            thingsToLearn.append("weapons")
        if traits[6] not in seen.traits and freebi == False:
            thingsToLearn.append("shift")
        if traits[18] in witness.traits and witness != players[-1]:
            thingsToLearn.append("honor")
        if traits[7] not in seen.traits and len(witness.otherTraits[index]) < 3 and seen != players[-1]:
            thingsToLearn.append("traits")
        if traits[9] in witness.traits and freebi == False:
            thingsToLearn.append("location")
        deduced = []
        while howMuch > 0:
            choice = random.randint(0, len(thingsToLearn)-1)
            deduced.append(thingsToLearn[choice])
            thingsToLearn.pop(choice)
            howMuch = howMuch - 1

        incriminatingTraits = [
            traits[13],
            traits[16],
            traits[25],
            traits[27],
            traits[28],
            traits[33],
            traits[36],
            traits[38]
        ]

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
                knowBank(witness.otherRanks, seenName, seen.rank, players)
            if deduced[d] == "strength":
                witness.message += str(beginning + " strength " + tense + " " + str(seen.strength) + end)
                knowBank(witness.otherStrengths, seenName, seen.strength, players)
            if deduced[d] == "intellect":
                witness.message += str(beginning + " intellect " + tense + " " + str(seen.intellect) + end)
                knowBank(witness.otherIntellects, seenName, seen.intellect, players)
            if deduced[d] == "nerves":
                witness.message += str(beginning + " nerves " + tense + " " + str(seen.nerves) + end)
                knowBank(witness.otherNerves, seenName, seen.nerves, players)
            if deduced[d] == "weapons":
                if seen.weapons != []:
                    weaponFound = False
                    while weaponFound == False:
                        randomWeapon = random.choice(seen.weapons)
                        if randomWeapon.name not in witness.otherWeapons[index]:
                            witness.message += str("one of " + beginning + " weapons " + tense + " " + str(randomWeapon) + end)
                            knowBank(witness.otherWeapons, seenName, randomWeapon, players)
                            weaponFound = True
                else:
                    beginning = name
                    if secondTense == "have":
                        secondTense = "has"
                    witness.message += str(beginning + " " + secondTense + " no weapon" + end)
                    knowBank(witness.otherWeapons, seenName, "none", players)
            if deduced[d] == "shift":
                if seen.shift != "shift":
                    witness.message += str(beginning + " shift " + tense + " " + str(seen.shift) + end)
                else:
                    beginning = name 
                    if secondTense == "have":
                        secondTense = "has"
                    witness.message += str(beginning + " " + secondTense + " no shift" + end)
            if deduced[d] == "location":
                witness.message += str(beginning + " previous location was " + str(seen.previousLocation) + end)
            if deduced[d] == "honor":
                witness.message += str(beginning + " honor " + tense + " " + str(seen.honor) + end)
                knowBank(witness.otherHonors, seenName, seen.honor, players)
            if deduced[d] == "traits":
                traitFound = False
                while traitFound == False:
                    traitToLearn = random.choice(seen.traits)
                    if weapons[5] in seen.weapons:
                        traitToLearn = random.choice(incriminatingTraits)
                    if traitToLearn.name not in witness.otherTraits[index]:
                        witness.message += str("one of " + beginning + " traits " + tense + " " + traitToLearn.name.upper() + end)
                        knowBank(witness.otherTraits, seenName, traitToLearn.name, players)
                        traitFound = True

#Checks for and spawns weapons in rooms
def freeWeapons(locations, weapons, players):
    idealWeapons = math.ceil((len(players) - 1) / 4)
    freeWeapons = []
    for l in range(len(locations)):
        for lw in range(len(locations[l].weapons)):
            freeWeapons.append(locations[l].weapons[lw])
    if len(freeWeapons) < idealWeapons:
        weaponsToChoose = []
        for w in range(len(weapons)):
            available = True
            for p in range(len(players)):
                if players[p].weapons != []:
                    for pw in range(len(players[p].weapons)):
                        if players[p].weapons[pw] == weapons[w]:
                            available = False 
            for l in range(len(locations)):
                if locations[l].weapons != []:
                    for lw in range(len(locations[l].weapons)):
                        if weapons[w] == locations[l].weapons[lw]:
                            available = False
            if available == True:
                weaponsToChoose.append(weapons[w])
        if len(weaponsToChoose) > idealWeapons - len(freeWeapons):
            while len(freeWeapons) < idealWeapons:
                weaponPlaced = random.randint(0, len(weaponsToChoose)-1)
                roomPlaced = random.choice(locations)
                players[0].weaponChanges += str("-Spawn the " + weaponsToChoose[weaponPlaced].withoutArticle + " in " + roomPlaced.name + "\n")
                roomPlaced.weapons.append(weaponsToChoose[weaponPlaced])
                freeWeapons.append(weaponsToChoose[weaponPlaced])
                weaponsToChoose.pop(weaponPlaced)

#Roll that decides if a player defends when they are attacked
def doTheyDefend(attacker, target, traits):
    roll = magic(target, attacker, "intimidate", traits)
    if target in attacker.accusers and traits[13] in attacker.traits:
        return "fail"
    if roll > target.strength:
        return "fail"
    else:
        return "pass"

#Updates the players notes
def updateNotes(players, traits, weapons):
    for p in range(len(players)-1):
        playerDocument = open(str("Player_Notes/" + players[p].name + ".txt"), "w")

        banks = len(players)-1
        if traits[17] in players[p].traits:
            banks = banks + 1
        for o in range(banks):
            playerDocument.write(players[o].trueName.upper())
            if players[o].reported == True:
                playerDocument.write(" (known dead)")
            playerDocument.write("\n")
            string = listToString(players[p].otherRanks[o], False)
            playerDocument.write("rnk: ")
            playerDocument.write(string)
            playerDocument.write("\n")
            string = listToString(players[p].otherStrengths[o], False)
            playerDocument.write("str: ")
            playerDocument.write(string)
            playerDocument.write("\n")
            string = listToString(players[p].otherIntellects[o], False)
            playerDocument.write("int: ")
            playerDocument.write(string)
            playerDocument.write("\n")
            string = listToString(players[p].otherNerves[o], False)
            playerDocument.write("nrv: ")
            playerDocument.write(string)
            playerDocument.write("\n")
            string = listToString(players[p].otherWeapons[o], False)
            if weapons[3] in players[o].weapons:
                playerDocument.write("wpn(" + str(len(players[0].weapons)) + "): ")
            else:
                playerDocument.write("wpn: ")
            playerDocument.write(string)
            playerDocument.write("\n")
            string = listToString(players[p].otherTraits[o], False)
            playerDocument.write("trt: ")
            playerDocument.write(string)
            playerDocument.write("\n")
            if traits[18] in players[p].traits and players[p] != players[o]:
                string = listToString(players[p].otherHonors[o], False)
                playerDocument.write("hnr: ")
                playerDocument.write(string)
                playerDocument.write("\n")
            playerDocument.write("\n")

        playerDocument.close()

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

def requiredSleep(actor, locations, traits):
    if locations[0].functionality == True:
        actor.requiredSleep = 4 - actor.sleep
    else:
        actor.requiredSleep = 5 - actor.sleep
    actor.sleep = 0
    if int(actor.requiredSleep) < 0 or traits[11] in actor.traits:
        actor.requiredSleep = 0
    actor.endMessage += str("and " + str(actor.requiredSleep) + " actions resting tomorrow night. ")

def everyoneLearns(bank, learned, about, players):
    for p in range(len(players)):
        if about == players[p]:
            index = p

    def replaceOrAdd(spot, learn):
        if spot[0] == " ":
            spot[0] = learn
        else:
            spot.append(learn)

    for p in range(len(players)):
        if bank == "rank":
            replaceOrAdd(players[p].otherRanks[index], learned)
        elif bank == "strength":
            replaceOrAdd(players[p].otherStrengths[index], learned)
        elif bank == "intellect":
            replaceOrAdd(players[p].otherIntellects[index], learned)
        elif bank == "nerves":
            replaceOrAdd(players[p].otherNerves[index], learned)
        elif bank == "weapons":
            for w in range(len(about.weapons)):
                if about.weapons[w].name not in players[p].otherWeapons[index]:
                    replaceOrAdd(players[p].otherWeapons[index], about.weapons[w].name)
        elif bank == "traits":
            for t in range(3):
                if about.traits[t].name not in players[p].otherTraits[index]:
                    replaceOrAdd(players[p].otherTraits[index], about.traits[t].name)

#Determines what I reveal about dead bodies
def weSeeDeadPeople(actor, locations, report, tribunal, players):
    shouldReport = False
    if actor.alive == False and actor.reported == False and actor.location.functionality == True:
        shouldReport = True
    if tribunal == True:
        shouldReport = True
    if shouldReport == True:
        if tribunal == True:
            report += str("Their last location was " + actor.location.name + ". ")
        else:
            report += str(actor.name + "'s body has been found in " + str(actor.location) + ": ")
        if locations[5].functionality == True:
            report += str("Their rank was " + str(actor.rank) + ". ")
            everyoneLearns("rank", actor.rank, actor, players)
        if locations[2].functionality == True:
            report += str("Their strength was " + str(actor.strength) + ". ")
            everyoneLearns("strength", actor.strength, actor, players)
        if locations[4].functionality == True:
            report += str("Their intellect was " + str(actor.intellect) + ". ")
            everyoneLearns("intellect", actor.intellect, actor, players)
        if locations[6].functionality == True:
            report += str("Their nerves was " + str(actor.nerves) + ". ")
            everyoneLearns("nerves", actor.nerves, actor, players)
        if locations[9].functionality == True:
            if actor.weapons == []:
                report += "They had no weapon. "
            elif len(actor.weapons) == 1:
                report += "Their weapon was " + actor.weapons[0].name + ". "
            else:
                report += "Their weapons were "
                report += stringList(actor.weapons, "")
                report += ". "
            everyoneLearns("weapons", "", actor, players)
        if locations[11].functionality == True:
            report += str("Their shift was " + str(actor.shift) + ". ")
        report += str("Their traits were " + actor.traits[0].name + ", " + actor.traits[1].name + ", and " + actor.traits[2].name + ". ")
        everyoneLearns("traits", "", actor, players)
        if locations[3].functionality == True and actor.causeOfDeath != "the tribunal":
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
        print("")
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

    #Shows the tribunalists things about attendance
    print("")
    for t in range(len(tribunalists)):
        print(tribunalists[t].trueName)
        print(" ")
        showedUp = []
        for i in range(len(tribunalists)):
            if tribunalists[t] != tribunalists[i]:
                showedUp.append(tribunalists[i])
        if showedUp == []:
            tribunalists[t].message += "No one else showed up to the tribunal. "
        else:
            people = stringList(showedUp, tribunalists[t])
            tribunalists[t].message += str(people + " showed up to the tribunal. ")       
        if locations[8].functionality == True:
            for s in range(len(showedUp)):
                seen(showedUp[s], tribunalists[t], False, players, traits, weapons)
        elif showedUp != []:
            tribunalists[t].message += str("Because the power is out, you can only bearly make them out by candle light, and cannot deduce anything about them or notice any wounds. ")
        if traits[15] in tribunalists[t].traits:
            decidedNot = []
            for p in range(len(players)-1):
                if players[p] not in tribunalists and players[p].alive == True:
                    decidedNot.append(players[p])
            if decidedNot != []:
                people = stringList(decidedNot, tribunalists[t])
                tribunalists[t].message += str(people + " decided not to show despite being alive (Prying). ")
        print(tribunalists[t].message)
        tribunalists[t].message = ""
        print(" ")
    for t in range(len(tribunalists)):
        tribunalists[t].marks = []
    for p in range(len(players)):
        players[p].accusers = []

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
                    if players[p].honor > 0 and traits[43] not in tribunalists[t].traits and weapons[11] not in players[p].weapons:
                        tribunalists[t].changedHonor = tribunalists[t].changedHonor - 1
                        honorCorrection(tribunalists[t], players[p])
                        honorLog(str(tribunalists[t].name + " voted " + players[p].name + ": " + str(oldHonor) + " -> " + str(tribunalists[t].changedHonor)), players)
                    elif players[p].honor > 0:
                        honorLog(str(tribunalists[t].name + " voted " + players[p].name + ": " + str(oldHonor) + " -> " + str(tribunalists[t].changedHonor) + " (CONFESSOR/NEUROTOXIC GAS)"), players)
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
            report = weSeeDeadPeople(extantPlayers[e], locations, report, True, players)
            print(report)
            report = ""
        elif len(extantPlayers[e].accusers) >= len(extantPlayers)/2:
            print("The tribunal attempts to execute " + extantPlayers[e].name + ", but finds them already dead. ")
            report = weSeeDeadPeople(extantPlayers[e], locations, report, True, players)
            print(report)
            report = ""
        else:
            print(extantPlayers[e].name + " has survived the tribunal. ")
            print("")

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

#Adds cuts to whoever has the Improvised Shiv before the tribunal
def scratches(players, weapons):
    for p in range(len(players)):
        if weapons[16] in players[p].weapons:
            players[p].marks.append("cuts")

#Finds out if anyone attacks in response to a murder or witnessing of a murder
def bloodFeud(attacker, present, players, weapons, locations, traits):
    if present != []:
        attackerBestType = highestStat(attacker, locations)
        presentRandomized = randomize(present)
        for i in range(len(presentRandomized)):
            presentBestType = highestStat(presentRandomized[i], locations)
            #If the witness is Heroic, they attack the attacker
            if traits[23] in presentRandomized[i].traits and presentRandomized[i].alive == True and attacker.alive == True and attacker != players[-1] and presentBestType != "":
                presentRandomized[i].KILL(attacker, presentBestType, locations, players, weapons, traits)
            #If the attacker is Ruthless, they attack the witness
            if traits[33] in attacker.traits and presentRandomized[i].alive == True and attacker.alive == True and presentRandomized[i] != players[-1] and attackerBestType != "":
                attacker.KILL(presentRandomized[i], attackerBestType, locations, players, weapons, traits)

#Finds a player's highest stat for which they own a corresponding weapon
def highestStat(actor, locations):
    availableTypes = available(actor.weapons, locations)
    highestStat = ["", ""]
    if "blunt" in availableTypes:
        highestStat = [actor.strength, "blunt"]
    if "medical" in availableTypes:
        if actor.intellect > actor.strength or highestStat[1] == "":
            highestStat = [actor.intellect, "medical"]
    if "sharp" in availableTypes:
        if highestStat[1] == "":
            highestStat = [actor.nerves, "sharp"]
        elif highestStat[1] == "blunt" and actor.nerves > actor.strength:
            highestStat = [actor.nerves, "sharp"]
        elif highestStat[1] == "medical" and actor.nerves > actor.intellect:
            highestStat = [actor.nerves, "sharp"]
    bestType = highestStat[1]
    return bestType

#Determines who to attack given a pool and wether one must be chosen
def whoToAttack(possibilities, players, locations):
    availableTypes = available(players[-1].weapons, locations)

    vulnerability = []
    for p in range(len(possibilities)):
        if possibilities[p].infStrength != "none":
            vulnerability.append(["blunt", players[-1].strength - possibilities[p].infStrength, possibilities[p].name])
        if possibilities[p].infIntellect != "none":
            vulnerability.append(["medical", players[-1].intellect - possibilities[p].infIntellect, possibilities[p].name])    
        if possibilities[p].infNerves != "none":
            vulnerability.append(["sharp", players[-1].nerves - possibilities[p].infNerves, possibilities[p].name])

    if vulnerability != []:
        sortedVulnerability = []
        amount = len(vulnerability)
        while len(sortedVulnerability) < amount:
            mostVulnerable = vulnerability[0]
            mostIndex = 0
            for v in range(len(vulnerability)):
                if vulnerability[v][1] > mostVulnerable[1]:
                    mostVulnerable = vulnerability[v]
                    mostIndex = v
            sortedVulnerability.append(mostVulnerable)
            vulnerability.pop(mostIndex)

        search = 0
        while search < amount:
            if sortedVulnerability[search][0] in availableTypes and sortedVulnerability[search][1] > 0:
                mostVulnerable = sortedVulnerability[search]
                search = search + 100
            search = search + 1
        return mostVulnerable
    else:
        return "none"

#Decides whether an AI will WIELD and which room they will target
def wieldForDummies(actor, locations):
    availableTypes = available(actor.weapons, locations)
    possible = ["blunt", "medical", "sharp"]
    notAvailable = []
    if "blunt" not in availableTypes:
        notAvailable.append("blunt")
    if "medical" not in availableTypes:
        notAvailable.append("medical")
    if "sharp" not in availableTypes:
        notAvailable.append("sharp")
    want = []
    for l in range(len(locations)):
        if locations[l].rank <= actor.rank:
            for w in range(len(locations[l].weapons)):
                if locations[l].weapons[w].type in notAvailable:
                    want.append(locations[l])
    if want != []:
        chosen = random.choice(want)
        return chosen
    else:
        return "none"
    
#The Enemy's Brain
def enemyPlans(players, locations, traits, nights, weapons):
    players[-1].commands = ["none", "none", "none", "none", "none", "none", "none", "none"]

    #Pick Rest Hours randomly
    hoursToRest = 4
    if traits[35] in players[-1].traits and nights != 0:
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
            highestLocations = []
            for l in range(len(locations)):
                if locations[l].rank == players[-1].rank:
                    highestLocations.append(locations[l])
            loiterChoice = random.choice(highestLocations)
            players[-1].commands[c] = str("SABOTAGE " + loiterChoice.input) #Might as well sabotage it while he's there
            x = x + 1

    #Try to pick up a weapon maybe
    room = wieldForDummies(players[-1], locations)
    if room != "none" and traits[39] not in players[-1].traits:
        x = 0
        for c in range(len(players[-1].commands)):
            if players[-1].commands[c] == "none" and x == 0:
                players[-1].commands[c] = str("WIELD " + room.input)
                x = x + 1

    #Attack someone maybe
    noEnemy = players.copy()
    noEnemy.pop(-1)
    target = whoToAttack(noEnemy, players, locations)
    if target != "none":
        x = 0
        for c in range(len(players[-1].commands)):
            if players[-1].commands[c][0] == "none" and x == 0:
                players[-1].commands[c] = str("KILL " + target[2] + " " + target[0])
                x = x + 1

    #Discard an extra weapon maybe
    availableTypes = []
    repeatWeapon = []
    for w in range(len(players[-1].weapons)):
        if players[-1].weapons[w].type in availableTypes:
            repeatWeapon.append(players[-1].weapons[w])
        availableTypes.append(str(players[-1].weapons[w].type))
    if repeatWeapon != []:
        weaponToDestory = random.choice(repeatWeapon)
        for w in range(len(weapons)):
            if weapons[w] == weaponToDestory:
                index = w
        x = 0
        for c in range(len(players[-1].commands)):
            if players[-1].commands[c][0] == "none" and x == 0:
                if locations[1].functionality == True or traits[12] in players[-1].traits:
                    players[-1].commands[c] = str("SANITATION " + str(index))
                    x = x + 1
                else:
                    room = random.choice(locations)
                    players[-1].commands[c] = str("DROP " + room.input + " " + str(index))
                    x = x + 1

    #Spend the remaining hours training or sabotaging
    outcomes = ["SABOTAGE"]
    if locations[2].functionality == True or traits[12] in players[-1].traits:
        outcomes.append("GYMNASIUM use")
    if locations[4].functionality == True or traits[12] in players[-1].traits:
        outcomes.append("LIBRARY use")
    if locations[6].functionality == True or traits[12] in players[-1].traits:
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