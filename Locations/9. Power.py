class power(location):
    def __init__(self, rank):
        self.rank = rank
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        
    def visit(player):
        
        #Check Rank
        location = power
        locationRank = 5
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.power = player.power + 1
        player.message += str("At " + time + ", you spend an hour fueling and watching over the generator, an activiy that will excuse you of some of your responsiblities tomorrow night. ")