from Players import randomPlayers, readPlayerData, spawnEnemy
import random
import sys
from Functions import askShifts, checkAccess, chooseYourWeapon, clearLoop, enemyPlans, findShifts, findWeapons, howMany, locate, newRandomShifts, randomCommands, randomize, readCommands, requiredSleep, requiredWork, roomPoints, theTribunal, weSeeDeadPeople, enemyPlans
from Weapons import antiqueSword, captainsKnife, humanSkull, liftingWeight, encryptedLaptop, heavyBriefcase, majorAward, strongBourbon, thePrince, aggressiveStimulants, petSnake, firstAid, sleepingPills, neurotoxicGas, forgedKeycard, sacredDagger, throwingShurikens, improvisedShiv
from Locations import Barraks, Sanitation, Gymnasium, Medical, Library, Information, Bathhouse, Communications, Power, Armaments, Security, Command

ran = True

weapons = []
weapons.append(liftingWeight())
weapons.append(majorAward())
weapons.append(encryptedLaptop())
weapons.append(heavyBriefcase())
weapons.append(thePrince())
weapons.append(humanSkull())
weapons.append(strongBourbon())
weapons.append(aggressiveStimulants())
weapons.append(petSnake())
weapons.append(firstAid())
weapons.append(sleepingPills())
weapons.append(neurotoxicGas())
weapons.append(captainsKnife())
weapons.append(antiqueSword())
weapons.append(forgedKeycard())
weapons.append(sacredDagger())
weapons.append(throwingShurikens())
weapons.append(improvisedShiv())

locations = []
locations.append(Barraks())
locations.append(Sanitation())
locations.append(Gymnasium())
locations.append(Medical())
locations.append(Library())
locations.append(Information())
locations.append(Bathhouse())
locations.append(Communications())
locations.append(Power())
locations.append(Armaments())
locations.append(Security())
locations.append(Command())

seed = random.randint(0, sys.maxsize)
random.seed(4573953984)
print(random.seed)

players = []
amount = howMany()
if ran == False:
    readPlayerData(players, amount, locations[0])
    print(" ")
    findShifts(players, locations)
    findWeapons(players, weapons)
else:
    randomPlayers(players, amount, locations, weapons, locations[0])
    for p in range(len(players)):
        players[p].shift.workload = players[p].shift.workload + players[p].requiredWork
    print(" ")
spawnEnemy(players, weapons, locations[0])
players[-1].trueName = "The Enemy"

#################################################################### Day-Night Loop ####################################################################

report = ""
time = ["11 PM", "12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM"]
numberWords = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", 'Seventh', "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]
days = int(amount/2+1)

for nights in range(days):
    dayNumberWord = numberWords[nights]
    print(" ")
    input("Press ENTER to begin the " + dayNumberWord + " night.")

    if ran == False:
        readCommands(players)
    else:
        randomCommands(players, locations)
    enemyPlans(players, locations, weapons, nights)
    chooseYourWeapon(players, locations, weapons)

    #Enemy takes a name
    namesToCopy = []
    for p in range(len(players) - 1):
        namesToCopy.append(players[p])
    chosenName = random.choice(namesToCopy)
    players[-1].name = chosenName.name
    if players[0].debug == True:
        print("The Enemy will be called " + players[-1].name + " for the night. ")
        print("The Enemy rank is: " + str(players[-1].rank))
    
    #Hour Cycle
    for h in range(0, 8):
        hour = time[h]
        if players[0].debug == True:
            print("\nIt is now " + hour + ". ")

        for p in range(len(players)):
            players[p].located = False

        #We go through and move people around based on their commands
        for p in range(len(players)):
            actor = players[p]
            if actor.alive == False:
                actor.located = True
            else:
                if actor.commands[h][0] == "REST":
                    actor.located = True
                    actor.message += str("\n")
                    actor.message += str("At " + hour + " you stay in " + actor.location.name + ". ")
                    if actor.debug == True:
                        print("MOVE: " + actor.trueName + " has remained in " + actor.location.name + ". ")
            
                for r in range(len(locations)):
                    if locations[r].input == actor.commands[h][0]:
                        actor.located = True
                        checkAccess(actor, locations[r], False, hour, locations)
                
                if actor.commands[h][0] == "SABOTAGE" and actor.weapon == weapons[2]:
                    actor.located = True
                    actor.message += str("\n")
                    actor.message += str("At " + hour + " you stay in " + actor.location.name + ". ")
                elif actor.commands[h][0] == "WORK" or actor.commands[h][0] == "SABOTAGE":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.located = True
                            checkAccess(actor, locations[r], True, hour, locations)
                if actor.commands[h][0] == "AMBUSH" and actor.weapon == weapons[11]:
                    actor.located = True
                    actor.message += str("\n")
                    actor.message += str("At " + hour + " you stay in " + actor.location.name + ". ")
                elif actor.commands[h][0] == ("LOITER" or "AMBUSH" or "ENEMY"):
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.located = True
                            checkAccess(actor, locations[r], False, hour, locations)

        #We go through and move around the tricky buggers that reference other players locations (KILL, WATCH, STEAL)
        for p in range(len(players)):
            for i in range(len(players)):
                players[i].visited = False
            inALoop = []
            if players[p].located == False:
                outcome = locate(players, players[p], h, inALoop, locations, hour)
                if outcome == "loop":
                    clearLoop(players, inALoop)
                    if players[p].located == False:
                        locate(players, players[p], h, inALoop, locations, hour)

        #Ok, now for the actions themselves
        playersRandomized = randomize(players)
        for pr in range(len(playersRandomized)):
            actor = playersRandomized[pr]
            if actor.alive == False:
                actor.DEAD(locations, players, weapons)
            else:
                if actor.commands[h][0] == "REST":
                    actor.REST(locations, players, weapons)
            
                for r in range(len(locations)):
                    if locations[r].input == actor.commands[h][0]:
                        if locations[r] == locations[7]:
                            locations[r].visit(actor, actor.commands[h][1], actor.commands[h][2], locations, players, report, weapons)
                        elif locations[r] == locations[2] or locations[r] == locations[4] or locations[r] == locations[6]:
                            if actor.commands[h][1] == "learn":
                                locations[r].learn(actor, locations, players, weapons)
                            elif actor.commands[h][1] == "use":
                                locations[r].use(actor, locations, players, weapons)
                        else:
                            locations[r].visit(actor, locations, players, weapons)

                if actor.commands[h][0] == "WORK":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.WORK(locations[r], locations, players, weapons)
                if actor.commands[h][0] == "SABOTAGE":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.SABOTAGE(locations[r], locations, players, weapons)
                if actor.commands[h][0] == "LOITER":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.LOITER(locations[r], locations, players, weapons)
                if actor.commands[h][0] == "AMBUSH":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            for p in range(len(players)):
                                if players[p].name == actor.commands[h][2]:
                                    actor.AMBUSH(locations[r], players[p], locations, players, hour, report, weapons)
                if actor.commands[h][0] == "ENEMY":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.ENEMY(locations[r], locations, players, weapons, time, report)

                if actor.commands[h][0] == "KILL":
                    for p in range(len(players)):
                        if players[p].trueName == actor.commands[h][1]:
                            actor.KILL(players[p], report, hour, locations, players, weapons)
                if actor.commands[h][0] == "STEAL":
                    for p in range(len(players)):
                        if players[p].trueName == actor.commands[h][1]:
                            actor.STEAL(players[p], locations, players, weapons)
                if actor.commands[h][0] == "WATCH":
                    actor.WATCH(locations, players, weapons)

        if weapons[8].present == True:
            spotter = weapons[8].owner
            playersWithoutYou = players.copy()
            playersWithoutYou.pop(spotter)
            spotted = random.choice(playersWithoutYou)
            spotter.message += str("You learn through your trained pet snake that " + spotted.name + " was in " + spotted.location.name + " during this hour. ")
                
    #Now for the bits that have to happen at the end of the night
        #End Messages
    for p in range(len(players)):
        players[p].message += str("\n")
        players[p].message += str("\n")
        players[p].message += str("NIGHT END: ")

        #Stuff that happened to weapons
    for p in range(len(players)):
        if players[p].weaponDestroyed == True:
            players[p].message += str("You weapon is nowhere to be found, and must have been destroyed last night. ")
            players[p].weaponDestroyed = False
        elif players[p].weapon == "none":
            players[p].message += str("You remain without a weapon. ")
        elif players[p].weapon.used == True:
            players[p].message += str("Your weapon was used by someone else to attack last night. ")
            players[p].weapon.used = False

        #New attributes
    for p in range(len(players)):
        actor = players[p]
        roomPoints(actor, actor.gymnasiumVisits, "strength", actor.strength)
        roomPoints(actor, actor.libraryVisits, "intellect", actor.intellect)
        roomPoints(actor, actor.bathhouseVisits, "nerves", actor.nerves)

        #Room functionality
    for l in range(len(locations)):
        room = locations[l]
        room.functionality = True
        if room.workload > 0:
            room.functionality = False
            report += str(room.name + " is disfunctional. ")
            for p in range(len(players)):
                if players[p].shift == room and players[p].rank != 1:
                    players[p].rank = players[p].rank - 1
                    players[p].message += str("Because you failed to complete your shift, you've been demoted to rank " + str(players[p].rank) + ". ")
        else:
            for p in range(len(players)):
                if players[p].shift == room and players[p].rank != 6:
                    players[p].rank = players[p].rank + 1
                    players[p].message += str("Because you completed your shift, you've been promoted to rank " + str(players[p].rank) + ". ")
        if room.sabotages > 0:
            room.workload = room.workload + room.sabotages
            report += str(room.name + " has " + str(room.sabotages) + " sabotages. ")
            room.sabotages = 0

        #Personal rules for tomorrow night
    for p in range(len(players) - 1):
        requiredWork(players[p], locations)
        requiredSleep(players[p], locations)

        #DEAD PEOPLE
    if locations[10].functionality == True:
        for p in range(len(players)):
            weSeeDeadPeople(players[p], locations, players, report)

        #And finally, print the messages.
    print("\n")
    for p in range(len(players)):
        actor = players[p]
        print(actor.trueName)
        print(actor.message)
        actor.message = ""
        print("\n")
    print(report)
    report = ""
    print(" ")

        #Get people there new random shifts
    if ran == False:
        askShifts(players)
        findShifts(players, locations)
    else:
        newRandomShifts(players, locations)

        #Do the tribunal
    theTribunal(players, locations, weapons, report)

        #Check for game ends
    livingPlayers = []
    for p in range(len(players) - 1):    
        if players[p].alive == True:
            livingPlayers.append(players[p])
    if len(livingPlayers) == 1:     #Only one player left
        print(livingPlayers[0] + " is the last player left alive. They have won the game. ")
        sys.exit()
    if len(livingPlayers) == 0:     #No players left (can this happen?)
        print("Everyone died. Nobody wins. ")
        sys.exit()
    if nights == days - 1:          #Game time is up
        honor = False
        for l in range(len(livingPlayers)):
            if livingPlayers[l].honor > 0:
                honor = True
        if honor == False:
            print("Nobody left alive has any honor. Everyone loses. ")
            sys.exit()
        mostHonor = [livingPlayers[0]]
        for l in range(len(livingPlayers)):
            if mostHonor[0].honor < livingPlayers[l].honor:
                mostHonor = [livingPlayers[l]]
            if mostHonor[0].honor == livingPlayers[l].honor:
                mostHonor.append(livingPlayers[l])
        print("The game is over. Players that have the most honor and therefore win: \n")
        print(mostHonor)
        sys.exit()
