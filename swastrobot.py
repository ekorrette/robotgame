import rg

myrobots = {}
myswast = {}
swasts = [(9,9), (9,8), (9,10), (8,9), (10,9), (7,9), (7,11), (9,7), (9,11), (7,8), (8,11), (11,10), (10,7), (7,7), (7,11), (11,11), (11,7)]

def chooseswast(botloc):
        unused = [swast for swast in swasts if swast not in myswast]
        return min(unused, key = lambda x: rg.dist(x, botloc))


class Robot:

        def act(self, game):
            if len(myrobots) == len(swasts):
                return ['suicide']

            if self.robot_id not in myrobots:
                myrobots[self.robot_id] = chooseswast(self.location)
                myswast[myrobots[self.robot_id]] = self.robot_id
                print self.robot_id, myrobots[self.robot_id]
    
            destination = myrobots[self.robot_id]

            if self.location == destination:
                return ['guard']

            move = rg.toward(self.location, destination)

            return ['move', move]



            
