class bathhouse(location):
    def __init__(self, rank):
        self.rank = rank
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        
    def visit(player):

        #Check Rank
        location = ba
        locationRank = 4
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.bathhouseVisits = player.bathhouseVisits + 1
        player.message += str("At " + time + ", you spend an hour plugged into simulated combat in bathhouse. Your reflexes honed, you feel more precise than ever. ")