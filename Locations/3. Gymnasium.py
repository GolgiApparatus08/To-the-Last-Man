class gymnasium(location):
    def __init__(self, rank):
        self.rank = rank
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        
    def visit(player):
        
        #Check Rank
        location = gymnasium
        locationRank = 2
        Access = rankCheck(player)
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.gymnasiumVisits = player.gymnasiumVisits + 1
        player.message += str("At " + time + ", you workout for a good hour in the gym. ")