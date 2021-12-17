from Players import randomPlayers, readPlayerData, spawnEnemy
import random
import sys
import glob
from Functions import activityString, answer, checkAccess, chooseYourWeapon, clearLoop, demotion, enemyPlans, freeRest, honorLog, howMany, listToString, load, locate, printHonor, randomCommands, randomize, readCommands, requiredSleep, requiredWork, roomPoints, save, seen, shifts, theTribunal, weSeeDeadPeople, enemyPlans
from Traits import Trait
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

traits = []
traits.append(Trait("Honest", "", -1))

traits.append(Trait("Arrogant", "", 1))
traits.append(Trait("Heavyset", "", 1))
traits.append(Trait("Eccentric", "", 1))
traits.append(Trait("Stuttering", "", 1))
traits.append(Trait("Hoarder", "", 1))
traits.append(Trait("Lazy", "", 1))
traits.append(Trait("Fickle", "", 1))
traits.append(Trait("Technician", "a ", 1))
traits.append(Trait("Detective", "a ", 1))
traits.append(Trait("Bodyguard", "a ", 1))
traits.append(Trait("Drunk", "a ", 1))
traits.append(Trait("Depressive", "", 1))
traits.append(Trait("Vincidtive", "", 1))
traits.append(Trait("Drama Queen", "a ", 1))
traits.append(Trait("Prying", "", 1))
traits.append(Trait("Rowdy", "", 1))
traits.append(Trait("Patriotic", "", 1))
traits.append(Trait("Philosophical", "", 1))
traits.append(Trait("Mysterious", "", 1))
traits.append(Trait("Suspicious", "", 1))

traits.append(Trait("Charming", "", 2))
traits.append(Trait("Highborn", "", 2))
traits.append(Trait("Heroic", "", 2))
traits.append(Trait("Productive", "", 2))
traits.append(Trait("Hacker", "a ", 2))
traits.append(Trait("Sociable", "", 2))
traits.append(Trait("Cunning", "", 2))
traits.append(Trait("Doctor", "a ", 2))
traits.append(Trait("Bodybuilder", "a ", 2))
traits.append(Trait("Bookworm", "a ", 2))
traits.append(Trait("Relaxed", "", 2))

traits.append(Trait("Curious", "", 3))
traits.append(Trait("Ruthless", "", 3))
traits.append(Trait("Martial Artist", "a ", 3))
traits.append(Trait("Deep Sleeper", "a ", 3))
traits.append(Trait("Mercenary", "a ", 3))
traits.append(Trait("Ambitious", "", 3))

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]

saveThings = []
for i in range(28):
    saveThings.append("")

seed = random.randint(0, sys.maxsize)
random.seed(seed)
print(random.seed)

weLoading = answer("Load from another game?", ["Yes", "No", ""])

players = []
amount = howMany(numbers)
if ran == False and weLoading == "No":
    readPlayerData(players, amount, locations[0], weapons, traits)
    print(" ")
else:
    randomPlayers(players, amount, weapons, locations[0], traits)
    print(" ")
spawnEnemy(players, weapons, locations[0], traits)
players[-1].trueName = "The Enemy"
players[-1].honor = -100
shifts(players, locations, traits)

#Set up knowledge banks
for p in range(len(players)):
    for o in range(len(players)):
        players[p].otherRanks.append(["?"])
        players[p].otherStrengths.append(["?"])
        players[p].otherIntellects.append(["?"])
        players[p].otherNerves.append(["?"])
        players[p].otherWeapons.append(["?"])
        players[p].otherTraits.append(["?"])
        players[p].otherHonors.append(["?"])

#################################################################### Day-Night Loop ####################################################################

report = ""
time = ["11 PM", "12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM"]
numberWords = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", 'Seventh', "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]
days = int(amount/2+1)

nights = 0
while nights < days:

    #Save and Load
    save(nights, saveThings, players, locations, weapons)
    response = answer("\nWould you like to load a past night?", ["Yes", "No", ""])
    if response == "Yes":
        allFiles = glob.glob("*.txt")
        print(allFiles)
        response = input("From which file would you like to load?")
        nights = load(response, saveThings, players, weapons, locations)

    dayNumberWord = numberWords[nights]
    print(" ")
    input("Press ENTER to begin the " + dayNumberWord + " night.")
    honorLog(str("NIGHT " + str(nights + 1)), players)

    if ran == False:
        readCommands(players)
    else:
        randomCommands(players, locations, weapons)
    enemyPlans(players, locations, weapons, nights)
    chooseYourWeapon(players, locations)
    
    for p in range(len(players) -1):
        players[p].endMessage += "NIGHT END: "
    report += str("COMMS: \n")

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
                elif actor.commands[h][0] == "LOITER" or actor.commands[h][0] == "AMBUSH" or actor.commands[h][0] == "ENEMY":
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
                actor.DEAD(locations, players)
            else:
                if actor.commands[h][0] == "REST":
                    actor.REST(locations, players, weapons, traits)
            
                for r in range(len(locations)):
                    if locations[r].input == actor.commands[h][0]:
                        if locations[r] == locations[7]:
                            for p in range(len(players) -1):
                                if players[p].name == actor.commands[h][1]:
                                    target1 = players[p]
                                if players[p].name == actor.commands[h][2]:
                                    target2 = players[p]
                            report = locations[r].visit(actor, target1, target2, locations, players, report, weapons, traits)
                        elif locations[r] == locations[2] or locations[r] == locations[4] or locations[r] == locations[6]:
                            if actor.commands[h][1] == "learn":
                                locations[r].learn(actor, locations, players, weapons, traits)
                            elif actor.commands[h][1] == "use":
                                locations[r].use(actor, locations, players, weapons, traits)
                        else:
                            locations[r].visit(actor, locations, players, weapons, traits)

                if actor.commands[h][0] == "WORK":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.WORK(locations[r], locations, players, weapons, traits)
                if actor.commands[h][0] == "SABOTAGE":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.SABOTAGE(locations[r], locations, players, weapons, traits)
                if actor.commands[h][0] == "LOITER":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.LOITER(locations[r], locations, players, weapons, False, traits)
                if actor.commands[h][0] == "AMBUSH":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            for p in range(len(players)):
                                if players[p].trueName == actor.commands[h][2]:
                                    actor.AMBUSH(locations[r], players[p], locations, players, hour, weapons, traits)
                if actor.commands[h][0] == "ENEMY":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.ENEMY(locations[r], locations, players, weapons, traits)

                if actor.commands[h][0] == "KILL":
                    for p in range(len(players)):
                        if players[p].trueName == actor.commands[h][1]:
                            actor.KILL(players[p], hour, locations, players, weapons, traits)
                if actor.commands[h][0] == "STEAL":
                    for p in range(len(players)):
                        if players[p].trueName == actor.commands[h][1]:
                            actor.STEAL(players[p], locations, players, weapons, traits)
                if actor.commands[h][0] == "WATCH":
                    for p in range(len(players)):
                        if players[p].trueName == actor.commands[h][1]:
                            target = players[p]
                    actor.WATCH(locations, players, weapons, target, traits)
           
        #Create Hourly Messages
        def behaviorLine(actor, activityInput, activityOutput, players, traits):
            included = activityString(actor, activityInput, traits)
            if included != "":
                verb = "spend"
                if activityInput == "dead":
                    verb = "are"
                includedList = included.split()
                if included != "You" and len(includedList) == 1:
                    verb = "spends"
                    if activityInput == "dead":
                        verb = "is"
                actor.message += str(included + " " + verb + " " + activityOutput + ". ")
                if activityInput == "rest":
                    if "you" in includedList or "You" in includedList:
                        freeRest(actor, traits)
                for i in range(len(includedList)):
                    nameFound = includedList[i].replace(",", "")
                    for p in range(len(players)):
                        if nameFound == players[p].name:
                            seen(players[p], actor, players, traits)

        for p in range (len(players)):
            actor = players[p]
            #THINGSTODO: loiter is not always shown if its you.

            #Room Actions
            behaviorLine(actor, "barraks", "the hour sleeping", players, traits)
            behaviorLine(actor, "sanitation", "the hour discarding a weapon", players, traits)
            behaviorLine(actor, "gymnasium_use", "the hour working out", players, traits)
            behaviorLine(actor, "gymnasium_learn", "the hour searching the gym records", players, traits)
            behaviorLine(actor, "library_use", "the hour reading books", players, traits)
            behaviorLine(actor, "library_learn", "the hour searching the library records", players, traits)

            #Generic Actions
            behaviorLine(actor, "work", "the hour working", players, traits)
            behaviorLine(actor, "sabotage", "the hour sabotaging", players, traits)
            behaviorLine(actor, "rest", "the hour resting", players, traits)
            behaviorLine(actor, "loiter", "the hour doing nothing", players, traits)
            behaviorLine(actor, "dead", "dead on the floor", players, traits)

            #Medical


            actor.events = []


    #Now for the bits that have to happen at the end of the night

    for p in range(len(players)):
        playerDocument = open(str(players[p].name + ".txt"), "w")

        for o in range(len(players)):
            playerDocument.write(players[o].name)
            playerDocument.write("\n")
            string = listToString(players[p].otherRanks[p])
            playerDocument.write(string)
            playerDocument.write("\n")
            string = listToString(players[p].otherStrengths[p])
            playerDocument.write(string)
            playerDocument.write("\n")
            string = listToString(players[p].otherIntellects[p])
            playerDocument.write(string)
            playerDocument.write("\n")
            string = listToString(players[p].otherNerves[p])
            playerDocument.write(string)
            playerDocument.write("\n")
            string = listToString(players[p].otherWeapons[p])
            playerDocument.write(string)
            playerDocument.write("\n")
            string = listToString(players[p].otherTraits[p])
            playerDocument.write(string)
            playerDocument.write("\n")
            string = listToString(players[p].otherHonors[p])
            playerDocument.write(string)
            playerDocument.write("\n")
            playerDocument.write("\n")

        #Stuff that happened to weapons
    for p in range(len(players)):
        if players[p].weaponDestroyed == True:
            players[p].endMessage += str("You weapon is nowhere to be found, and must have been destroyed last night. ")
            players[p].weaponDestroyed = False
        elif players[p].weapon == "none":
            players[p].endMessage += str("You remain without a weapon. ")
        elif players[p].weapon.used == True:
            players[p].endMessage += str("Your weapon was used by someone else to attack last night. ")
            players[p].weapon.used = False

        #New attributes
    for p in range(len(players)):
        actor = players[p]
        roomPoints(actor, actor.gymnasiumVisits, "strength", actor.strength)
        roomPoints(actor, actor.libraryVisits, "intellect", actor.intellect)
        roomPoints(actor, actor.bathhouseVisits, "nerves", actor.nerves)

        #Room functionality
    report += "\n"
    report += "DYSFUNCTIONS: \n"
    for l in range(len(locations)):
        room = locations[l]
        room.functionality = True
        if room.workload > 0:
            room.workload = 0
            room.functionality = False
            if room.sabotages > 0:
                report += str(room.name + " is disfunctional ")
            else:
                report += str(room.name + " is disfunctional. \n")
            for p in range(len(players)):
                if players[p].shift == room and players[p].rank != 1 and players[p].alive == True:
                    players[p].rank = players[p].rank - 1
                    players[p].endMessage += str("Because you failed to complete your shift, you've been demoted to rank " + str(players[p].rank) + ". ")
                elif players[p].shift == room and players[p].alive == True:
                    players[p].endMessage += str("You would be demoted for failing to complete your shift, but you're already rank 1. ")
        else:
            for p in range(len(players)):
                if players[p].shift == room and players[p].rank != 6 and players[p].alive == True:
                    players[p].rank = players[p].rank + 1
                    players[p].endMessage += str("Because you completed your shift, you've been promoted to rank " + str(players[p].rank) + ". ")
                elif players[p].shift == room and players[p].alive == True:
                    players[p].endMessage += str("You would be promoted for completing your shift, but you're already rank 6. ")
        if room.sabotages > 0:
            room.workload = room.workload + room.sabotages
            if room.sabotages == 1:
                sabs = "sabotage"
            else:
                sabs = "sabotages"
            if room.functionality == False:
                report += str("and has " + str(room.sabotages) + " " + sabs + ". \n")
            else:
                report += str(room.name + " has " + str(room.sabotages) + " " + sabs + ". \n")
            room.sabotages = 0

        #Personal rules for tomorrow night
    for p in range(len(players) - 1):
        requiredWork(players[p], locations)
        requiredSleep(players[p], locations)

        #DEAD PEOPLE
    report += "\n"
    report += "REPORTED BODIES: \n"
    for p in range(len(players)):
        report = weSeeDeadPeople(players[p], locations, report, False)

        #The Alive the Dead and the Removed
    report += "\n"
    report += "PLAYER STATUSES: \n"
    for p in range(len(players)-1):
        if players[p].alive == True:
            report += str(players[p].trueName + " is ")
            report += str("alive. \n")
        elif players[p].alive == False and players[p].reported == False:
            report += str(players[p].trueName + " is ")
            report += str("dead. \n")

        #And finally, print the messages.
    print("\n")
    for p in range(len(players)):
        actor = players[p]
        if actor == players[-1]:
            print(actor.trueName + " (" + actor.name + ")")
        else:
            print(actor.trueName)
        print(actor.message)
        actor.message = ""
        if players[p].alive == True:
            print(" ")
            print(actor.endMessage)
            actor.endMessage = ""
        print("\n")
    print(report)
    report = ""

        #Check for game ends
    livingPlayers = []
    for p in range(len(players) - 1):    
        if players[p].alive == True:
            livingPlayers.append(players[p])
    if len(livingPlayers) == 1:     #Only one player left
        print(livingPlayers[0].name + " is the last player left alive. They have won the game. ")
        printHonor(players)
        sys.exit()
    if len(livingPlayers) == 0:     #No players left (can this happen?)
        print("Everyone died. Nobody wins. ")
        printHonor(players)
        sys.exit()

        #Do the tribunal
    demotion(players, traits)
    theTribunal(players, locations, weapons, report, traits)

        #Check for game ends
    livingPlayers = []
    for p in range(len(players) - 1):    
        if players[p].alive == True:
            livingPlayers.append(players[p])
    if len(livingPlayers) == 1:     #Only one player left
        print(livingPlayers[0].name + " is the last player left alive. They have won the game. ")
        printHonor(players)
        sys.exit()
    if len(livingPlayers) == 0:     #No players left (can this happen?)
        print("Everyone died. Nobody wins. ")
        printHonor(players)
        sys.exit()

        #Get people there new random shifts
    shifts(players, locations, traits)

    nights = nights + 1
    players[0].honorMessage += str("\n")

#All nights have finished, and the game is over
mostHonor = [players[0]]
for p in range(len(players)):
    if mostHonor[0].honor < players[p].honor:
        mostHonor = [players[p]]
    elif mostHonor[0].honor == players[p].honor and players[p] not in mostHonor:
        mostHonor.append(players[p])
if mostHonor[0].honor > 0:
    print("The game is over. Players that have the most honor and therefore win: ")
    for m in range(len(mostHonor)):
        print(mostHonor[m].name + " has " + str(mostHonor[m].honor))
    printHonor(players)
    sys.exit()
else:
    print("The game is over. No players have any honor. Everyone loses. ")
    printHonor(players)
    sys.exit
