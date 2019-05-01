import rg

class Robot:
    def act(self, game):

        if self.location == rg.CENTER_POINT:
            return['guard']

        for loc, bot in game.robots.items():
            if bot.player_id != self.player_id:
                if rg.wdist(loc, self.location) == 1:
                    return ['attack', loc]

        return ['move', rg.toward(self.location, rg.CENTER_POINT)]

               
