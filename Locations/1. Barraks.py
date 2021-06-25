

class barraks(Location):
    def __init__(self, rank):
        self.rank = rank
        self.sabotages = 0
        self.workload = 0
        self.functionality = True

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
        identify()