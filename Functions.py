import sys
import random
import math

lowerNumberWords = ["first", "second", "third", "fourth", "fifth", "sixth", 'seventh', "eighth", "ninth", "tenth", "eleventh", "twelfth"]

#Takes the string for "shift" input by the player and matches it with a location
def findShifts(players, locations):
    for p in range(len(players)):
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
            if weapons[i].name is players[p].weapon:
                players[p].weapon = weapons[i]
                weapons[i].present = True
                weapons[i].owner = players[p]
                x = 1
        if x == 0:
            print("Error: Weapon not found for " + players[p].name + ". ")

#Asks how many players there will be and returns the value as amount
def howMany():
    amount = int(input("Number of soldiers (2-12): \n"))
    if amount <= 0:
        input("You don't have a base without soldiers. Come back with some players!\n")
        sys.exit()
    elif amount == 1:
        input("There's already a last man, silly!")
        sys.exit()
    else:
        return amount

#Is called each night to read what players will be doing for each action
def readCommands(players):
    input("Press ENTER when commands are ready to be read. \n")
    contents = open('playerDataCommands.txt').readlines()
    for p in range(len(players)):
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
            players[p].commands[c].split(' ')
        print("The commands of " + players[p].name + " have been read! ")

#Attempts to send a player to a room. Is called anytime a players location might require updating. Checks if they can access the room, sends them to a location accordingly and tells them about it.
def checkAccess(player, room, WORK, hour, locations):
    if (player.location.rank >= room.rank) or (player.rank >= room.rank) or ((player.shift == room) and (WORK == True) and (locations[11].functionality == True)):
        if player.location == room:
            player.message += str("At " + hour + " you stay in " + room.name + ". ")
        else:
            player.location = room
            player.message += str("Around " + hour + " you make your way to " + room.name + ". ")
    else:
        player.message += str("Around " + hour + " you fail to access " + room.name + ", and return to " + player.location.name + ". ")

#If the locate function gets caught in a loop, this fixes it and then abandons the function so it can try again
def resolveLoop(inALoop, time, locations):
    for r in range(6):
        for l in range(len(inALoop)):
            if inALoop[l].location.rank == r + 1:
                inALoop[l].located = True
                checkAccess(inALoop[l], inALoop[l].location, False, time, locations)
                return

#Finds the player in questions target and sees if they have been located. If they are, it sends the player there, if not it trys to locate them.
def locate(players, player, time, inALoop, locations):
    player.visited = True
    inALoop.append(player)
    for p in range(len(players)):
        if players[p].name == player.commands[time][1]:
            if players[p].visited == True:
                resolveLoop(inALoop, time, locations)
                return "loop"
            else:
                if players[p].located == True:
                    player.located = True
                    checkAccess(player, players[p].location, False, time, locations)
                    return "located"
                else:
                    outcome = locate(players, players[p], time, inALoop, locations)
                    if outcome == "located":
                        player.located = True
                        checkAccess(player, players[p].location, False, time, locations)
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
def doTheyDeduce(seen, deducer, body, weapons):
    if deducer.weapon == weapons[16]:
        return
    x = 0
    if deducer.weapon == weapons[6]:
        x = -1
    while x <= 0:
        rollOutcomes = [1, 2, 3, 4, 5, 6, 7, 8]
        roll = random.choice(rollOutcomes)
        if deducer.intellect >= roll:
            tense = "is"
            if body == True:
                tense = "was"
            thingsToLearn = [
                "In the encounter, you notice that " + seen.name + "'s strength " + tense + " " + seen.strength + ". ",
                "In the encounter, you notice that " + seen.name + "'s intellect " + tense + " " + seen.intellect + ". ",
                "In the encounter, you notice that " + seen.name + "'s nerves " + tense + " " + seen.nerves + ". ",
                "In the encounter, you notice that " + seen.name + "'s weapon " + tense + " " + seen.currentWeapon + ". ",
                "In the encounter, you notice that " + seen.name + "'s shift " + tense + " " + seen.shift + ". ",
                "In the encounter, you notice that " + seen.name + "'s rank " + tense + " " + seen.rank + ". "
                ]
            learned = random.choice(thingsToLearn)
            deducer.message += learned
        x = x + 1

#Finds who is in the room with a player and gives them whatever message they need to see
def whoHere(seen, target, tell, body, locations, players, weapons):
    if locations[9].functionality == False:
        return
    whoHere = []
    for p in range(len(players)):
        if players[p].location == seen.location and players[p] != seen and players[p] != target:
            whoHere.append(players[p])
    for w in range(len(whoHere)):
        whoHere[w].message += tell
        doTheyDeduce(seen, whoHere[w], body, weapons)

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
        player.endMessage += str("Your " + attributeString + " is now " + playerAttribute + ". ")

#Decides how much time a player needs to spend working tommorrow night
def requiredWork(actor):
    actor.requiredWork = 2 - actor.power
    actor.message += str("You will have to spend " + actor.requiredWork + " actions tomorrow (plus sabotages) to complete your shift. ")

def requiredSleep(actor, locations):
    if locations[0].functionality == True:
        actor.requiredSleep = 4 - actor.sleep
    else:
        actor.requiredSleep = 5 - actor.sleep
    actor.message += str("You will have to spend " + actor.requiredSleep + " actions sleeping tomorrow. ")

#Determines what I reveal about dead bodies
def weSeeDeadPeople(actor, locations, report):
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
        list.pop(actor)

def askShifts(players):
    for p in range(len(players)):
        actor = players[p]
        if actor.alive == True:
            actor.enteredShift = input("What is " + actor.name + "'s new shift? \n")

def theTribunal(players, locations, weapons):
    tribunalists = []
    for p in range(len(players)):
        answer = input("Is " + players[p].name + "showing up to the tribunal? ")
        if answer == "Yes":
            tribunalists.append(players[p])

    if weapons[1].present == True:      #MAJOR AWARD
        answer = input("Would " + weapons[1].owner.name + " like to demote a player? ")
        if answer == "Yes":
            demoted = input("Which player?")
            for p in range(len(players)):
                if players[p].name == demoted:
                    players[p].rank = players[p].rank - 1
    
    for t in range(len(tribunalists)):
        x = 0
        while x == 0:
            answer = input("Is " + tribunalists[t].name + " voting for anyone not already input? ")
            if answer == "Yes":
                accusation = input("Who?")
                for p in range(len(players)):
                    if players[p].name == accusation:
                        if players[p].honor > 0 or players[p].alive == False:
                            tribunalists[t].honor = tribunalists[t].honor - 1
                        elif players[p].honor < 0:
                            tribunalists[t].honor = tribunalists[t].honor + 1
                        players[p].accusers.append(tribunalists[t])
            else:
                x = 1
    for p in range(len(players)):
        if len(players[p].accusers) >= len(tribunalists)/2 and players[p].alive == True:
            print(players[p].name + " has been killed by the tribunal. Soldiers who voted to kill them: \n")
            print(players[p].accusers + "\n")
            weSeeDeadPeople(players[p], locations, report)
            print(report + "\n")
            report = ""
        else:
            players[p].accusers = []
    for t in range(len(tribunalists)):
        for t2 in range(len(tribunalists)):
            doTheyDeduce(t2, t, False, weapons)
        print(tribunalists[t].message + "\n")
        tribunalists[t].message = ""

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
    if locations[9].functionality == False:
        for p in range(len(players)):
            chosenWeapon = input("Which weapon would you like to use? \n")
            for w in range(len(weapons)):
                if weapons[w].name == chosenWeapon:
                    players[p].currentWeapon = weapons[w]