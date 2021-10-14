import sys
import random
import math

lowerNumberWords = ["first", "second", "third", "fourth", "fifth", "sixth", 'seventh', "eighth", "ninth", "tenth", "eleventh", "twelfth"]

#Takes the string for "shift" input by the player and matches it with a location
def findShifts(players, locations):
    for p in range(len(players)):
        if players[p].enteredShift == "none":
            return
        for l in range(len(locations)):
            if locations[l].name == players[p].enteredShift:
                players[p].shift = locations[l]
                locations[l].workload = locations[l].workload + players[p].requiredWork
                if locations[1].functionality == False:
                    locations[l].workload = locations[l].workload + 1

#Takes the string for "weapon" input by the player and matches it with a real weapon
def findWeapons(players, weapons):
    for p in range(len(players)):
        x = 0
        for i in range(len(weapons)):
            if weapons[i].name == players[p].weapon:
                players[p].weapon = weapons[i]
                weapons[i].present = True
                weapons[i].owner = players[p]
                print(weapons[i].name + " has been successfully assignged too " + players[p].name + "! ")
                x = 1
        if x == 0:
            print("Error: Weapon not found for " + players[p].name + ". ")
            sys.exit

#Asks how many players there will be and returns the value as amount
def howMany():
    amount = int(input("Number of soldiers (2-15): \n"))
    if amount <= 0:
        input("You don't have a base without soldiers. Come back with some players!\n")
        sys.exit()
    elif amount == 1:
        input("There's already a last man, silly!")
        sys.exit()
    elif amount > 15:
        input("There's not enough weapons to play with this many people. Sorry! ")
        sys.exit()
    else:
        return amount

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
    contents = open('playerData.txt').readlines()
    for p in range(len(players) - 1):
        players[p].commands = []
        players[p].commands.append(contents[(p * 17) + 8].strip())
        players[p].commands.append(contents[(p * 17) + 9].strip())
        players[p].commands.append(contents[(p * 17) + 10].strip())
        players[p].commands.append(contents[(p * 17) + 11].strip())
        players[p].commands.append(contents[(p * 17) + 12].strip())
        players[p].commands.append(contents[(p * 17) + 13].strip())
        players[p].commands.append(contents[(p * 17) + 14].strip())
        players[p].commands.append(contents[(p * 17) + 15].strip())
        for c in range(len(players[p].commands)):
            if players[0].debug == True:
                print("COMMAND " + str(c + 1) + ": " + players[p].commands[c])
        for c in range(len(players[p].commands)):
            players[p].commands[c] = mySplit(players[p].commands[c])
        if players[0].debug == True:
            print(players[p].trueName + " command's have been read! \n")
    return

#Generates random commands for random player set in testing
def randomCommands(players, locations):
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
                for i in range(hoursToWork):
                    if len(commandHours) > hoursToWork:
                        roll = random.randint(0,len(commandHours) - 1)
                        workHour = commandHours[roll]
                        print(players[p].commands[workHour])
                        commandHours.pop(roll)
            #Randomly pick actions for remaining hours
            actions = [
                "SABOTAGE",
                "LOITER",
                "AMBUSH",
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
                        randomPlayer = random.randint(0, len(players)-1)
                        target = players[randomPlayer]
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
        for c in range(len(players[p].commands)):
            if players[0].debug == True:
                print("COMMAND " + str(c+1) + ": " + players[p].commands[c])
            players[p].commands[c] = mySplit(players[p].commands[c])
        if players[0].debug == True:
            print(players[p].trueName + " command's have been read! \n")

def newRandomShifts(players, locations):
    for p in range(len(players)-1):
        playerShift = random.choice(locations)
        players[p].shift = playerShift
        players[p].shift.workload = players[p].shift.workload + players[p].requiredWork
        if players[0].debug == True:
            print(players[p].trueName + "'s shift is now " + str(players[p].shift) + "! ")

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
    if player.location == room:
        player.message += str("\n")
        player.message += str("At " + hour + " you stay in " + room.name + ". ")
        if player.debug == True:
            print("MOVE: " + player.trueName + " has remained in " + room.name + ". ")
    else: 
        if (player.location.rank >= room.rank) or (player.rank >= room.rank) or ((player.shift == room) and (WORK == True) and (locations[11].functionality == True)):
            player.location = room
            player.message += str("\n")
            player.message += str("Around " + hour + " you make your way to " + room.name + ". ")
            if player.debug == True:
                print("MOVE: " + player.trueName + " has been moved to " + room.name + ". ")
        else:
            player.message += str("\n")
            player.message += str("Around " + hour + " you fail to access " + room.name + ", and return to " + player.location.name + ". ")
            if player.debug == True:
                print("MOVE: " + player.trueName + " failed to access " + room.name + ". ")

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

#Roll that decides if a player learns something about another player
def doTheyDeduce(seen, deducer, body, weapons, players):
    if seen.weapon == weapons[16]:
        return
    if deducer.weapon == weapons[12]:
        name = seen.trueName
    else:
        name = seen.name
    x = 0
    if deducer.weapon == weapons[6]:
        x = -1
    while x <= 0:
        rollOutcomes = [1, 2, 3, 4, 5, 6, 7, 8]
        roll = random.choice(rollOutcomes)
        if deducer.intellect >= roll:
            tense = "is"
            secondTense = "has"
            if body == True:
                tense = "was"
                secondTense = "had"
            thingsToLearn = [
                "You deduce that " + name + "'s strength " + tense + " " + str(seen.strength) + ". ",
                "You deduce that " + name + "'s intellect " + tense + " " + str(seen.intellect) + ". ",
                "You deduce that " + name + "'s nerves " + tense + " " + str(seen.nerves) + ". ",
                "You deduce that " + name + "'s weapon " + tense + " " + str(seen.currentWeapon) + ". ",
                "You deduce that " + name + "'s shift " + tense + " " + str(seen.shift) + ". ",
                "You deduce that " + name + "'s rank " + tense + " " + str(seen.rank) + ". "
                ]
            if seen.shift == "shift":
                thingsToLearn[4] = "You deduce that " + name + " " + secondTense + " no shift. "
            if deducer.weapon == weapons[5] and deducer != players[-1]:
                thingsToLearn.append("You deduce that " + name + "'s honor " + tense + " " + str(seen.honor) + ". ")
            learned = random.choice(thingsToLearn)
            deducer.message += learned
            if deducer == players[-1]:
                if learned == thingsToLearn[0]:
                    seen.infStrength = seen.strength
                elif learned == thingsToLearn[1]:
                    seen.infIntellect = seen.intellect
                elif learned == thingsToLearn[2]:
                    seen.infNerves = seen.nerves
        x = x + 1

#Finds who is in the room with a player and gives them whatever message they need to see
def whoHere(seen, target, tell, tellTrue, body, locations, players, weapons):
    if locations[8].functionality == False:
        return
    whoHere = []
    for p in range(len(players)):
        if players[p].location == seen.location and players[p] != seen and players[p] != target:
            whoHere.append(players[p])
    for w in range(len(whoHere)):
        if whoHere[w].weapon == weapons[12]:
            whoHere[w].message += tellTrue
        else:
            whoHere[w].message += tell
        wounds(seen, whoHere[w], body)
        doTheyDeduce(seen, whoHere[w], body, weapons, players)
    return whoHere

#Talk about wounds
def wounds(seen, witness, body):
    starter = "They"
    if body == True:
        starter = "The body"
    if "bruises" in seen.marks and "cuts" not in seen.marks and "tired" not in seen.marks:
        witness.message += str(starter + " looked covered in bruises. ")
    elif "cuts" in seen.marks and "bruises" not in seen.marks and "tired" not in seen.marks:
        witness.message += str(starter + " looked covered in cuts. ")
    elif "tired" in seen.marks and "bruises" not in seen.marks and "cuts" not in seen.marks:
        witness.message += str(starter + " looked mentally exhausted. ")
    elif "bruises" in seen.marks and "cuts" in seen.marks and "tired" not in seen.marks:
        witness.message += str(starter + " looked covered in bruises and cuts. ")
    elif "bruises" in seen.marks and "tired" in seen.marks and "cuts" not in seen.marks:
        witness.message += str(starter + " looked covered in bruises and mentally exhausted. ")
    elif "bruises" not in seen.marks and "cuts" in seen.marks and "tired" in seen.marks:
        witness.message += str(starter + " looked covered in cuts and mentally exhausted. ")
    elif "bruises" in seen.marks and "cuts" in seen.marks and "tired" in seen.marks:
        witness.message += str(starter + " looked covered in bruises, covered in cuts, and mentally exhausted. ")

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
        player.message += str("Your " + attributeString + " is now " + str(playerAttribute) + ". ")

#Decides how much time a player needs to spend working tommorrow night
def requiredWork(actor, locations):
    if locations[1].functionality == True:
        actor.requiredWork = 2 - actor.power
    else:
        actor.requiredWork = 3 - actor.power
    if actor.requiredWork < 0:
        actor.requiredWork = 0
    actor.message += str("You will have to spend " + str(actor.requiredWork) + " actions (plus sabotages) to complete your shift, ")

def requiredSleep(actor, locations):
    if locations[0].functionality == True:
        actor.requiredSleep = 4 - actor.sleep
    else:
        actor.requiredSleep = 5 - actor.sleep
    actor.message += str("and " + str(actor.requiredSleep) + " actions resting tomorrow night. ")

#Determines what I reveal about dead bodies
def weSeeDeadPeople(actor, locations, players, report):
    if actor.alive == False:
        report += str("Alert the group that " + actor.name + " is dead along with their last location. ")
        if locations[2].functionality == True:
            report += str("Tell the group what their strength was. ")
        if locations[3].functionality == True:
            report += str("Tell the group what type of weapon they were killed with (Not applicable if they were killed by the tribunal). ")
        if locations[4].functionality == True:
            report += str("Tell the group what their intellect was. ")
        if locations[5].functionality == True:
            report += str("Tell the group what their rank was. ")
        if locations[6].functionality == True:
            report += str("Tell the group what their nerves was. ")
        if locations[9].functionality == True:
            report += str("Tell the group what their weapon was. ")
        if locations[11].functionality == True:
            report += str("Tell the group what their shift was. ")
        actor.location = "none"

#Ask for shifts
def askShifts(players):
    for p in range(len(players) - 1):
        if players[p].alive == True:
            players[p].enteredShift = input("What is " + players[p].name + "'s new shift? \n")

#Court is in Session
def theTribunal(players, locations, weapons, report):
    tribunalists = []
    print("\n")
    if players[0].ran == True:
        input("Press ENTER to randomize tribunal attendance! ")
    for p in range(len(players) - 1):
        if players[0].ran == True:
            roll = random.randint(0, 1)
            if roll == 1:
                tribunalists.append(players[p])
        else:
            answer = input("Is " + players[p].name + " showing up to the tribunal? ")
            if answer == "y":
                tribunalists.append(players[p])

    print("")
    for t in range(len(tribunalists)):
        print(tribunalists[t].trueName)
        print(" ")
        for i in range(len(tribunalists)):
            if tribunalists[t] != tribunalists[i]:
                tribunalists[t].message += str(tribunalists[i].name + " has showed up to the tribunal. ")
                if locations[8].functionality == True:
                    wounds(tribunalists[i], tribunalists[t], False)
                    doTheyDeduce(tribunalists[i], tribunalists[t], False, weapons, players)
        if locations[8].functionality == False:
            tribunalists[t].message += str("Because the power is out, you can only bearly make them out by candle light, and cannot deduce anything about them or notice any wounds. ")
        if tribunalists[t].message == "":
            tribunalists[t].message = "No one else showed up to the tribunal. "
        print(tribunalists[t].message)
        tribunalists[t].message = ""
        print(" ")

    if weapons[1].present == True:      #MAJOR AWARD
        answer = input("Would " + weapons[1].owner.name + " like to demote a player? ")
        if answer == "Yes":
            demoted = input("Which player?")
            for p in range(len(players) - 1):
                if players[p].name == demoted:
                    players[p].rank = players[p].rank - 1

    input("Press ENTER to begin voting! ")
    print(" ")
    for t in range(len(tribunalists)):
        if players[0].ran == True:
            answer = []
            for p in range(len(players) -1):
                roll = random.randint(0, 1)
                if roll == 1:
                    answer.append(players[p].name)
        else:
            answer = input("Who is " + tribunalists[t].name + " voting for? ")
            answer.split()
        for a in range(len(answer)):
            for p in range(len(players) - 1):
                if answer[a] == players[p].name:
                    if players[p].honor > 0 or players[p].alive == False:
                        tribunalists[t].honor = tribunalists[t].honor - 1
                    elif players[p].honor < 0:
                        tribunalists[t].honor = tribunalists[t].honor + 1
                    players[p].accusers.append(tribunalists[t])
    for p in range(len(players) - 1):
        if len(players[p].accusers) >= len(tribunalists)/2 and players[p].alive == True:
            print(players[p].name + " has been killed by the tribunal. Soldiers who voted to kill them:")
            players[p].alive == False
            for a in range(len(players[p].accusers)):
                print(players[p].accusers[a].name)
            report += str(players[p].name + " has been killed by the tribunal. Their rank was " + str(players[p].rank) + ", their strength was " + str(players[p].strength) + ", their intellect was " + str(players[p].intellect) + ", their nerves was " + str(players[p].nerves) + ", their weapon was " + players[p].weapon.name + ", and their shift was " + players[p].shift.name + ". ")
            weSeeDeadPeople(players[p], locations, players, report)
            print(report + "\n")
            report = ""
        else:
            players[p].accusers = []

#Gives someone with sleeping pills a sleep for resting
def freeRest(actor, weapons):
    if actor.weapon == weapons[10]:
        actor.sleep = actor.sleep + 1
        actor.message += str("The rest was extra refreshing due to the sleeping pills, and you won't have to sleep as much tomorrow.")

#calculates the work done to a location
def workload(actor, room, weapons):
    if actor.weapon == weapons[7]:
        room.workload = 0
    else:
        room.workload = room.workload - 1

#Asks players what weapon they would like to use if Armaments is down.
def chooseYourWeapon(players, locations, weapons):
    for p in range(len(players) - 1):
        if players[p].weapon == weapons[3] or locations[9].functionality == False:
            chosenWeapon = input("Which weapon would " + players[p].name + " like to use? \n")
            for w in range(len(weapons)):
                if weapons[w].name == chosenWeapon:
                    players[p].currentWeapon = weapons[w]

#Finds out if anyone attacks in response to a murder or witnessing of a murder
def bloodFeud(attacker, target, present, players, weapons, report, time, locations):
    playersRandomized = randomize(players)
    presentRandomized = randomize(present)
    for p in range(len(playersRandomized)):
        for i in range(len(presentRandomized)):
            if attacker.weapon == weapons[4] and playersRandomized[p] == presentRandomized[i] and playersRandomized[p].alive == True and attacker.alive == True and playersRandomized[p] != playersRandomized[-1]:
                attacker.message += str("You decide that it is better to be feared than loved and attack " + playersRandomized[p].name + " in order to silence a witness. ")
                attacker.KILL(playersRandomized[p], report, time, locations, playersRandomized, weapons)
            if playersRandomized[p] == presentRandomized[i] and playersRandomized[p].weapon == weapons[16] and playersRandomized[p].alive == True and attacker.alive == True and attacker != playersRandomized[-1]:
                playersRandomized[p].message += str("In righteous fury, you decide to avenge " + target.name + " by attacking " + attacker.name + ". ")
                playersRandomized[p].KILL(attacker, report, time, locations, playersRandomized, weapons)

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