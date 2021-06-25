class communications(location):
    def __init__(self, rank):
        self.rank = rank
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        
    def visit(player, target1, target2):
        
        #Check Rank
        location = communications
        locationRank = 4
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.message += str("Around " + time + ", you visit communications to audit the comms shared between " + target1.name + " and " + target2.name + " this morning and afternoon. The computer returns that it has noted your attempt and will, if accepted, send you the result of the audit by morning. ")
        moderatorMessage += str("Send " + player.name + " any comms shared between " + target1.name + " and " + target2.name " yesterday. ")