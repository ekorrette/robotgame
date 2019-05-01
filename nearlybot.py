import rg

def get_team(robot, game):
    return {loc for loc in game.robots if game.robots[loc].player_id == robot.player_id}

def get_enemies(robot, game):
    return set(game.robots) - get_team(robot, game)

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
    return robot.hp <=5

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


class Robot:
    def act(self, game):

        if wants_to_guard(self, game):
            return['guard']

        if wants_to_suicide(self, game):
            return ['suicide']
        
        if have_enemies_around(self, game):
            return ['attack', get_bot_to_attack(self, game)]

        return ['move', rg.toward(self.location, get_destination(self, game))]

               
