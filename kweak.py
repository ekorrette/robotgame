import rg
import heapq

k = 5

def get_team(robot, game):
    return {loc for loc in game.robots if game.robots[loc].player_id == robot.player_id}

def get_enemies(robot, game):
    return set(game.robots) - get_team(robot, game)

'''
def get_robots_around(robot, game):
    bots = []
    location = robot.location
    for loc in game.robots.keys():
        if loc in rg.locs_around(location):
            bots.append(game.robots[loc])
    return bots

def get_enemies_around(robot, game):
    robots_around = get_robots_around(robot, game)
    enemies = []
    for bot in robots_around:
        if bot.player_id != robot.player_id:
            enemies.append(bot)
    return enemies

def have_enemies_around(robot, game):
    return bool(len(get_enemies_around(robot, game)))

def have_little_hp(robot):
    return robot.hp <= rg.settings.collision_damage

def wants_to_suicide(robot, game):
    if have_little_hp(robot):
        if have_enemies_around(robot, game):
            return True
    return False


def get_destination(robot, game):
    return rg.CENTER_POINT

def is_in_destination(robot, game):
    return get_destination(robot, game) == robot.location

def wants_to_guard(robot, game):
    return is_in_destination(robot, game)


def get_bot_to_attack(robot, game):
    enemies = get_enemies_around(robot, game)
    return min(enemies, key=lambda x: x.hp).location


enemies_to_attack = []
attacking_bots = {}
'''

def get_k_weakest_enemies(robot, game):
    enemies = get_enemies(robot, game)
    n = min(k, len(enemies))
    return heapq.nsmallest(n, enemies, key=lambda x: game.robots[x].hp)

def get_nearest_weak(robot, game):
    weak = get_k_weakest_enemies(robot, game)
    if len(weak):
    	nearest = min(weak, \
                key=lambda x: rg.wdist(robot.location, game.robots[x].location))
    	return nearest
    else:
    	return None    

class Robot:
    def act(self, game):
        target = get_nearest_weak(self, game)
        if target is None:
        	return ['guard']

        toward = rg.toward(self.location, target)

        if toward in game.robots:
            return ['attack', toward]
        else:
            return ['move', toward]

'''
        if wants_to_guard(self, game):
            return['guard']

        if wants_to_suicide(self, game):
            return ['suicide']
        
        if have_enemies_around(self, game):
            return ['attack', get_bot_to_attack(self, game)]

        return ['move', rg.toward(self.location, get_destination(self, game))]
'''
               
