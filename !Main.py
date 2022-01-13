from Players import randomPlayers, readPlayerData, spawnEnemy
import random
import sys
import glob
from Functions import activityString, answer, checkAccess, clearLoop, demotion, enemyPlans, freeRest, freeWeapons, honorLog, howMany, listToString, load, locate, printHonor, randomCommands, randomize, readCommands, remind, requiredSleep, requiredWork, roomPoints, save, scratches, seen, shifts, stringList, theTribunal, updateNotes, weSeeDeadPeople, enemyPlans
from Traits import Trait
from Weapons import antiqueSword, exoticPoison, humanSkull, liftingWeight, encryptedLaptop, heavyBriefcase, majorAward, officersKnife, sacredBlade, strongBourbon, thePrince, aggressiveStimulants, petSnake, sleepingPills, neurotoxicGas, forgedKeycard, throwingShurikens, improvisedShiv
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
weapons.append(exoticPoison())
weapons.append(sleepingPills())
weapons.append(neurotoxicGas())
weapons.append(officersKnife())
weapons.append(antiqueSword())
weapons.append(forgedKeycard())
weapons.append(sacredBlade())
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

roleRestrictions = [
    "Imperial Heir",
    "Inquisitor",
    "Flesh Weaver",
    "Blood Shade",
    "Hearthfire",
    "Confessor"
]

traits = []
traits.append(Trait("Occult", "", 0, []))
traits.append(Trait("Arrogant", "", 1, []))
traits.append(Trait("Hulking", "", 1, []))
traits.append(Trait("Eccentric", "", 1, []))
traits.append(Trait("Confident", "", 1, []))
traits.append(Trait("Hoarding", "", 1, []))
traits.append(Trait("Lazy", "", 1, []))
traits.append(Trait("Fickle", "", 1, []))
traits.append(Trait("Technician", "a ", 1, []))
traits.append(Trait("Detective", "a ", 1, []))
traits.append(Trait("Bodyguard", "a ", 1, []))
traits.append(Trait("Drunk", "a ", 1, []))
traits.append(Trait("Depressive", "", 1, []))
traits.append(Trait("Vindictive", "", 1, []))
traits.append(Trait("Drama Queen", "a ", 1, []))
traits.append(Trait("Prying", "", 1, []))
traits.append(Trait("Rowdy", "", 1, []))
traits.append(Trait("Patriotic", "", 1, []))
traits.append(Trait("Philosophical", "", 1, []))
traits.append(Trait("Mysterious", "", 1, []))
traits.append(Trait("Untrusting", "", 1, []))
traits.append(Trait("Charming", "", 2, []))
traits.append(Trait("Highborn", "", 2, []))
traits.append(Trait("Heroic", "", 2, []))
traits.append(Trait("Productive", "", 2, []))
traits.append(Trait("Hacker", "a ", 2, []))
traits.append(Trait("Sociable", "", 2, []))
traits.append(Trait("Cunning", "", 2, []))
traits.append(Trait("Doctor", "a ", 2, []))
traits.append(Trait("Bodybuilder", "a ", 2, []))
traits.append(Trait("Bookworm", "a ", 2, []))
traits.append(Trait("Relaxed", "", 2, []))
traits.append(Trait("Curious", "", 3, []))
traits.append(Trait("Ruthless", "", 3, []))
traits.append(Trait("Martial Artist", "a ", 3, []))
traits.append(Trait("Deep Sleeper", "a ", 3, []))
traits.append(Trait("Mercenary", "a ", 3, []))
traits.append(Trait("Ambitious", "", 3, []))
traits.append(Trait("Imperial Heir", "the ", 0, roleRestrictions))
traits.append(Trait("Inquisitor", "an ", 0, roleRestrictions))
traits.append(Trait("Flesh Weaver", "a ", 0, roleRestrictions))
traits.append(Trait("Blood Shade", "a ", 0, roleRestrictions))
traits.append(Trait("Hearthfire", "the ", 0, roleRestrictions))
traits.append(Trait("Confessor", "the ", 0, roleRestrictions))

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
    banks = len(players)-1
    if traits[17] in players[p].traits:
        banks = banks + 1
    for o in range(banks):
        if players[o] == players[p]:
            players[p].otherRanks.append([players[p].rank])
            players[p].otherStrengths.append([players[p].strength])
            players[p].otherIntellects.append([players[p].intellect])
            players[p].otherNerves.append([players[p].nerves])
            players[p].otherWeapons.append([players[p].weapons[0].name])
            players[p].otherTraits.append([players[p].traits[0].name, players[p].traits[1].name, players[p].traits[2].name])
            players[p].otherHonors.append([" "])
        else:
            players[p].otherRanks.append([" "])
            players[p].otherStrengths.append([" "])
            players[p].otherIntellects.append([" "])
            players[p].otherNerves.append([" "])
            players[p].otherWeapons.append([" "])
            players[p].otherTraits.append([" "])
            players[p].otherHonors.append([" "])
        seen(players[o], players[p], True, players, traits, weapons)
        players[p].message = ""
updateNotes(players, traits, weapons)

#Initial weapon cards
freeWeapons(locations, weapons, players)
print("")
print("WEAPON CHANGES: ")
print(players[0].weaponChanges)
players[0].weaponChanges = ""

#Display Room Weapons
print("FREE WEAPONS: ")
for l in range(len(locations)):
    if locations[l].weapons != []:
        for w in range(len(locations[l].weapons)):
            print(str(locations[l].weapons[w].name + " in " + locations[l].name))
for p in range(len(players)):
    if traits[36] in players[p].traits:
        print(str("***Tell " + players[p].trueName))

#################################################################### Day-Night Loop ####################################################################

report = ""
time = ["11 PM", "12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM"]
numberWords = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", 'Seventh', "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]
days = int(amount/2+1)

players[0].blood = 1
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

    #Kill the Blood Shade if they cannot feed
    for p in range(len(players)):
        if traits[41] in players[p].traits:
            if players[0].blood == 0 and players[p].alive == True:
                players[p].alive = False
                players[p].causeOfDeath = "mystical"
                print("***The BLOOD SHADE dies of starvation. ")
                report = weSeeDeadPeople(players[p], locations, report, False, players, traits)
                print(report)
                report = ""
            elif players[0].blood > 0 and players[p].alive == True:
                print("***The BLOOD SHADE feeds successfully. ")
    players[0].blood = 0

    dayNumberWord = numberWords[nights]
    remind(players, traits, weapons)
    input("Press ENTER to begin the " + dayNumberWord + " night.")
    honorLog(str("NIGHT " + str(nights + 1)), players)

    if ran == False:
        readCommands(players)
    else:
        randomCommands(players, locations, weapons, traits)
    enemyPlans(players, locations, traits, nights, weapons)

    for p in range(len(players)):
        if traits[0] in players[p].traits:
            traits[0].rituals = []
            selection = answer("Ritual of battle? ", ["Yes", "No", ""])
            if selection == "Yes":
                traits[0].rituals.append("intimidate")
            selection = answer("Ritual of wisdom? ", ["Yes", "No", ""])
            if selection == "Yes":
                traits[0].rituals.append("deduce")
            selection = answer("Ritual of fortune? ", ["Yes", "No", ""])
            if selection == "Yes":
                traits[0].rituals.append("steal")
    for p in range(len(players) -1):
        players[p].endMessage += "NIGHT END: "
    report += str("COMMS: \n")

    #Hour Cycle
    for h in range(0, 8):
        players[0].hour = h
        hour = time[h]
        if players[0].debug == True:
            print("\nIt is now " + hour + ". ")

        for p in range(len(players)):
            players[p].located = False
            players[p].previousLocation = players[p].location

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
                        checkAccess(actor, locations[r], actor.commands[h][0], hour, locations, traits, weapons)
                
                if actor.commands[h][0] == "SABOTAGE" and traits[25] in actor.traits:
                    actor.located = True
                    actor.message += str("\n")
                    actor.message += str("At " + hour + " you stay in " + actor.location.name + ". ")
                elif actor.commands[h][0] == "WORK" or actor.commands[h][0] == "SABOTAGE":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.located = True
                            checkAccess(actor, locations[r], actor.commands[h][0], hour, locations, traits, weapons)
                if actor.commands[h][0] == "AMBUSH" and traits[27] in actor.traits:
                    actor.located = True
                    actor.message += str("\n")
                    actor.message += str("At " + hour + " you stay in " + actor.location.name + ". ")
                elif actor.commands[h][0] == "LOITER" or actor.commands[h][0] == "AMBUSH" or actor.commands[h][0] == "ENEMY" or actor.commands[h][0] == "WIELD" or actor.commands[h][0] == "DROP":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.located = True
                            checkAccess(actor, locations[r], actor.commands[h][0], hour, locations, traits, weapons)

        #We go through and move around the tricky buggers that reference other players locations (KILL, WATCH, STEAL, WEAVE)
        for p in range(len(players)):
            for i in range(len(players)):
                players[i].visited = False
            inALoop = []
            if players[p].located == False:
                outcome = locate(players, players[p], h, inALoop, locations, hour, traits, weapons)
                if outcome == "loop":
                    clearLoop(players, inALoop)
                    if players[p].located == False:
                        locate(players, players[p], h, inALoop, locations, hour, traits, weapons)

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
                                if players[p].trueName == actor.commands[h][1]:
                                    target1 = players[p]
                                if players[p].trueName == actor.commands[h][2]:
                                    target2 = players[p]
                            report = locations[r].visit(actor, target1, target2, locations, players, report, weapons, traits)
                        elif locations[r] == locations[2] or locations[r] == locations[4] or locations[r] == locations[6]:
                            if actor.commands[h][1] == "learn":
                                locations[r].learn(actor, locations, players, weapons, traits)
                            elif actor.commands[h][1] == "use":
                                locations[r].use(actor, locations, players, weapons, traits)
                        elif locations[r] == locations[1]:
                            locations[r].visit(actor, actor.commands[h][1], locations, players, weapons, traits)
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
                if actor.commands[h][0] == "WIELD":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.WIELD(locations[r], players, locations, weapons, traits)
                if actor.commands[h][0] == "DROP":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            weaponIndex = actor.commands[h][2] 
                            actor.DROP(weaponIndex, locations[r], players, locations, weapons, traits)
                if actor.commands[h][0] == "AMBUSH":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            for p in range(len(players)):
                                if players[p].trueName == actor.commands[h][2]:
                                    actor.AMBUSH(locations[r], players[p], locations, players, hour, weapons, traits)
                if actor.commands[h][0] == "ENEMY":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.ENEMY(actor.commands[h][2], locations[r], locations, players, weapons, traits)

                if actor.commands[h][0] == "KILL":
                    for p in range(len(players)):
                        if players[p].trueName == actor.commands[h][1]:
                            actor.KILL(players[p], actor.commands[h][2], locations, players, weapons, traits)
                if actor.commands[h][0] == "STEAL":
                    for p in range(len(players)):
                        if players[p].trueName == actor.commands[h][1]:
                            actor.STEAL(players[p], locations, players, weapons, traits)
                if actor.commands[h][0] == "WATCH":
                    for p in range(len(players)):
                        if players[p].trueName == actor.commands[h][1]:
                            target = players[p]
                    actor.WATCH(locations, players, weapons, target, traits)
                if actor.commands[h][0] == "WEAVE":
                    for p in range(len(players)):
                        if players[p].trueName == actor.commands[h][1]:
                            target = players[p]
                    actor.WEAVE(target, actor.commands[h][2], locations, players, weapons, traits)
                if actor.commands[h][0] == "INQUIRE":
                    for p in range(len(players)):
                        if players[p].trueName == actor.commands[h][1]:
                            target = players[p]
                    actor.INQUIRE(target, locations, players, weapons, traits)

        #Create Hourly Messages
        def behaviorLine(actor, activityInput, activityOutput, players, traits, nightPhase):
            involved = activityString(actor, activityInput, traits, nightPhase, weapons)
            included = stringList(involved, actor, traits)
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
                for i in range(len(involved)):
                    for p in range(len(players)):
                        if involved[i] == players[p]:
                            seen(players[p], actor, False, players, traits, weapons)
            return involved

        def baseInfo(attribute):
            stats = []
            for p in range(len(players)):
                if traits[19] not in players[p].traits:
                    if attribute == "strength":
                        stats.append(players[p].strength)
                    elif attribute == "intellect":
                        stats.append(players[p].intellect)
                    elif attribute == "rank":
                        stats.append(players[p].rank)
                    elif attribute == "nerves":
                        stats.append(players[p].nerves)
            random.shuffle(stats)
            string = listToString(stats, True)
            return string

        for p in range (len(players)):
            if players[p].alive == True:
                actor = players[p]

                #Room Actions
                behaviorLine(actor, "barraks", "the hour sleeping", players, traits, h)
                behaviorLine(actor, "sanitation", "the hour discarding a weapon", players, traits, h)
                behaviorLine(actor, "gymnasium_use", "the hour working out", players, traits, h)
                involved = behaviorLine(actor, "gymnasium_learn", "the hour searching the gym records", players, traits, h)
                if actor in involved:
                    strengths = baseInfo("strength")
                    actor.message += str("You discover the soldiers' strengths are: " + strengths + ". ")
                behaviorLine(actor, "library_use", "the hour reading books", players, traits, h)
                involved = behaviorLine(actor, "library_learn", "the hour searching the library records", players, traits, h)
                if actor in involved:
                    intellects = baseInfo("intellect")
                    actor.message += str("You discover the soldiers' intellects are: " + intellects + ". ")
                involved = behaviorLine(actor, "information", "the hour searching information's records", players, traits, h)
                if actor in involved:
                    ranks = baseInfo("rank")
                    actor.message += str("You discover the soldiers' ranks are: " + ranks + ". ")
                behaviorLine(actor, "bathhouse_use", "the hour relaxing in the sauna", players, traits, h)
                involved = behaviorLine(actor, "bathhouse_learn", "the hour searching the bathhouse records", players, traits, h)
                if actor in involved:
                    nerves = baseInfo("nerves")
                    actor.message += str("You discover the soldiers' nerves are: " + nerves + ". ")
                behaviorLine(actor, "communications", "the hour auditing comms", players, traits, h)
                behaviorLine(actor, "power", "the hour generating power", players, traits, h)
                involved = behaviorLine(actor, "armaments", "the hour searching armaments records", players, traits, h)
                if actor in involved:
                    weaponChosen = False
                    while weaponChosen == False:
                        selectedPlayer = random.choice(players)
                        if selectedPlayer.weapons != []:
                            selectedWeapon = random.choice(selectedPlayer.weapons)
                            weaponChosen = True
                            actor.message += str("You discover that " + selectedPlayer.name + " has " + selectedWeapon.name + ". ")
                involved = behaviorLine(actor, "security", "the hour investigating the security systems", players, traits, h)
                if actor in involved:
                    for l in range(len(locations)):
                        locations[l].blips = 0
                    for p in range(len(players)):
                        for l in range(len(locations)):
                            if players[p].location == locations[l]:
                                locations[l].blips = locations[l].blips + 1
                    actor.message += "You discover that there are: "
                    locationsWithBlips = []
                    for l in range(len(locations)):
                        if locations[l].blips > 0:
                            locationsWithBlips.append(locations[l])
                    for l in range(len(locationsWithBlips)-1):
                        actor.message += str(str(locationsWithBlips[l].blips) + " bodies in " + locationsWithBlips[l].name + ", ")
                    actor.message += str("and " + str(locationsWithBlips[-1].blips) + " bodies in " + locationsWithBlips[-1].name + ". ")
                involved = behaviorLine(actor, "command", "the hour searching command records", players, traits, h)
                if actor in involved:
                    withoutEnemy = players.copy()
                    withoutEnemy.pop(-1)
                    chosenPlayer = random.choice(withoutEnemy)
                    actor.message += str("You discover that " + chosenPlayer.name + " has the " + str(chosenPlayer.input) + " shift. ")

                #Generic Actions
                behaviorLine(actor, "work", "the hour working", players, traits, h)
                behaviorLine(actor, "sabotage", "the hour sabotaging", players, traits, h)
                behaviorLine(actor, "rest", "the hour resting", players, traits, h)
                behaviorLine(actor, "loiter", "the hour doing nothing", players, traits, h)
                behaviorLine(actor, "dead", "dead on the floor", players, traits, h)

                actor.events = []


    #Now for the bits that have to happen at the end of the night

        #Stuff that happened to weapons
    for p in range(len(players)-1):
        if players[p].weaponsStolen != []:
            weaponsNoArticles = []
            for w in range(len(players[p].weaponsStolen)):
                weaponsNoArticles.append(players[p].weaponsStolen[w].withoutArticle)
            stolen = listToString(weaponsNoArticles, True)
            verb = "have"
            if len(players[p].weaponsStolen) == 1 and players[p].weaponsStolen != weapons[16]:
                verb = "has"
            players[p].endMessage += str("Your " + stolen.capitalize() + " " + verb + " been stolen from you in the night. ")
        if players[p].weapons == []:
            players[p].endMessage += str("You have no weapons. ") 
        else:
            weaponNames = []
            for w in range(len(players[p].weapons)):
                weaponNames.append(players[p].weapons[w].name)
            weaponsOwned = listToString(weaponNames, True)
            verb = "s are"
            if len(weaponNames) == 1:
                verb = " is"     
            players[p].endMessage += str("Your current weapon" + verb + " " + weaponsOwned + ". ")     

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
        requiredSleep(players[p], locations, traits)

        #DEAD PEOPLE
    report += "\n"
    report += "REPORTED BODIES: \n"
    for p in range(len(players)):
        report = weSeeDeadPeople(players[p], locations, report, False, players, traits)

        #New Weapon Cards
    freeWeapons(locations, weapons, players)
    report += "\n"
    report += "WEAPON CHANGES: \n"
    report += players[0].weaponChanges
    players[0].weaponChanges = ""

        #Report All Room Weapons
    report += "\n"
    report += "FREE WEAPONS: \n"
    for l in range(len(locations)):
        if locations[l].weapons != []:
            for w in range(len(locations[l].weapons)):
                report += locations[l].weapons[w].name + " in " + locations[l].name + "\n"
    for p in range(len(players)):
        if traits[36] in players[p].traits:
            report += "***Tell " + players[p].trueName + "\n"

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
        elif players[p].reported == True:
            report += str(players[p].trueName + " is ")
            report += str("reported. \n")

        #And finally, print the messages.
    print("\n")
    for p in range(len(players)):
        if players[p].alive == True:
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

    updateNotes(players, traits, weapons)

        #Check for game ends
    livingPlayers = []
    for p in range(len(players) - 1):    
        if players[p].alive == True:
            livingPlayers.append(players[p])
    if len(livingPlayers) == 1:     #Only one player left
        print(livingPlayers[0].trueName + " is the last player left alive. They have won the game. ")
        printHonor(players)
        sys.exit()
    if len(livingPlayers) == 0:     #No players left (can this happen?)
        print("Everyone died. Nobody wins. ")
        printHonor(players)
        sys.exit()

        #Do the tribunal
    scratches(players, weapons)
    demotion(players, traits)
    theTribunal(players, locations, weapons, report, traits)
    updateNotes(players, traits, weapons)

        #Check for game ends
    livingPlayers = []
    for p in range(len(players) - 1):    
        if players[p].alive == True:
            livingPlayers.append(players[p])
    if len(livingPlayers) == 1:     #Only one player left
        print(livingPlayers[0].trueName + " is the last player left alive. They have won the game. ")
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
if traits[38] not in players[0].traits:
    mostHonor = [players[0]]
else:
    mostHonor = [players[1]]
for p in range(len(players)):
    if mostHonor[0].honor < players[p].honor and traits[38] not in players[p].traits:
        mostHonor = [players[p]]
    elif mostHonor[0].honor == players[p].honor and players[p] not in mostHonor and traits[38] not in players[p].traits:
        mostHonor.append(players[p])
if mostHonor[0].honor > 0:
    print("The game is over. Players that have the most honor and therefore win: ")
    for m in range(len(mostHonor)):
        print(mostHonor[m].trueName + " has " + str(mostHonor[m].honor))
    printHonor(players)
    sys.exit()
else:
    print("The game is over. No players have any honor. Everyone loses. ")
    printHonor(players)
    sys.exit
