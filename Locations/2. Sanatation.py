class sanitation(location):
    def __init__(self, rank):
        self.rank = rank
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        
    def visit(player):
        
        #Check Rank
        location = sanitation
        locationRank = 1
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        if player.weapon is player.currentWeapon:
            player.message += str("Around " + time + ", you sneak into sanitation and slip your " + player.weapon + " into the trash. It will never be used again. ")
            player.weapon = nothing
            player.currentWeapon = nothing
        else:
            player.message += str("Around " + time + ", you sneak into sanitation and slip " + player.owner.name + "'s " + player.currentWeapon + " into the trash. It will never be used again. ")
            player.owner.weapon = nothing
            player.currentWeapon = nothing
            moderatorMessage += str("Tell " + player.owner.name + " that someone trashed their weapon last night. ")