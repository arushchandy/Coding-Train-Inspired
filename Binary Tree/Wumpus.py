from pathlib import Path
from enum import Enum
path = Path(__file__).parent

class Direction(Enum):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3

class Action(Enum):
    GOFORWARD = 0
    TURNLEFT = 1
    TURNRIGHT = 2
    SHOOT = 3

class Position(object):
    """ Position: Position object that holds an x, y coordinate."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @staticmethod
    def isAdjacent(location1, location2):
        """ isAdjacent: Returns if two locations are adjacent. """

        x1 = location1.x
        x2 = location2.x
        y1 = location1.y
        y2 = location2.y

        if (x1 == x2) and (y1 == (y2 - 1)) or (x1 == x2) and (y1 == (y2 + 1)) or (x1 == (x2 - 1)) and (y1 == y2) or (x1 == (x2 + 1)) and (y1 == y2):
            return True

        return False

class Agent():
    def __init__(self):
        self.MATRIX_SIZE = 4
        self.ARROW_COUNT = 0
        self.MAX_MOVES_ALLOWED = 100
        self.PIT_LOCATIONS = []
        self.WUMPUS_LOCATION = []
        self.GOLD_LOCATION = []
        self.AGENT_ALIVE = True
        self.AGENT_DIRECTION = Direction.RIGHT
        self.AGENT_ACTION = Action.GOFORWARD
        self.AGENT_ARROW = 0
        self.AGENT_GOLD = False
        self.STENCH_FOUND = False
        self.BREEZE_FOUND = False
        self.BUMP_FOUND = False
        self.SCREAM_FOUND = False
        self.WUMPUS_KILLEd = False
        self.AGENT_LOCATION = Position(1, 1)


def main():
    newAgent = Agent()
    readEnvSettings(newAgent)
    proceedMovement(newAgent)


def readEnvSettings(newAgent):
    # Read from file.
    lines = open(path / "env1.txt", "r")
    matrixSizeFound = False
    arrowNumberFound = False

    for line in lines:
        if (not matrixSizeFound):
            newAgent.MATRIX_SIZE = int(line)
            matrixSizeFound = True
            continue
        if (not arrowNumberFound):
            newAgent.ARROW_COUNT = int(line)
            arrowNumberFound = True
            continue
        if (line.startswith("p ")):
            lineParts = line.split(" ")
            if (len(lineParts) == 3):
                x =  int(lineParts[1].strip())
                y =  int(lineParts[2].strip())
                newAgent.PIT_LOCATIONS.append(Position(x, y))
        if (line.startswith("w ")):
            lineParts = line.split(" ")
            if (len(lineParts) == 3):
                x =  int(lineParts[1].strip())
                y =  int(lineParts[2].strip())
                newAgent.WUMPUS_LOCATION.append(Position(x, y))
        if (line.startswith("g ")):
            lineParts = line.split(" ")
            if (len(lineParts) == 3):
                x =  int(lineParts[1].strip())
                y =  int(lineParts[2].strip())
                newAgent.GOLD_LOCATION.append(Position(x, y))

        # print(PIT_LOCATIONS)
        # print(WUMPUS_LOCATION)
        # print(GOLD_LOCATION)


def proceedMovement(newAgent):
    num_moves = 0
    while (newAgent.AGENT_ALIVE) and (num_moves < newAgent.MAX_MOVES_ALLOWED):
        action = setState(newAgent)

        print("Action = {}".format(nextAction(action)))
        print()

        changeAction(action,newAgent)
        num_moves += 1
    
    if(not newAgent.AGENT_ALIVE):
        print(" Agent is not alive.")

    if(num_moves == newAgent.MAX_MOVES_ALLOWED or num_moves > newAgent.MAX_MOVES_ALLOWED):
        print("Agent ran out of moves")

def nextAction(action):
    if action == Action.GOFORWARD:
        return "GOFORWARD"
    if action == Action.TURNRIGHT:
        return "TURNRIGHT"
    if action == Action.TURNLEFT:
        return "TURNLEFT"
    if action == Action.SHOOT:
        return "SHOOT"
    return "UNKNOWN ACTION"

def setState(newAgent):

    if(newAgent.WUMPUS_KILLEd):
        print("Wumpus killed.")

    percept_str = ""
    if newAgent.STENCH_FOUND:
        percept_str += "Stench=True,"
    else:
        percept_str += "Stench=False,"
    if newAgent.BREEZE_FOUND:
        percept_str += "Breeze=True,"
    else:
        percept_str += "Breeze=False,"
    if newAgent.BUMP_FOUND:
        percept_str += "Bump=True,"
    else:
        percept_str += "Bump=False,"
    if newAgent.SCREAM_FOUND:
        percept_str += "Scream=True"
    else:
        percept_str += "Scream=False"
    
    print(" State :: " + percept_str)

    return Action.GOFORWARD

def changeAction(action,newAgent):
        newAgent.STENCH_FOUND = False
        newAgent.BREEZE_FOUND = False
        newAgent.BUMP_FOUND = False
        newAgent.SCREAM_FOUND = False
        newAgent.WUMPUS_KILLEd= False

        if action == Action.GOFORWARD:
            if newAgent.AGENT_DIRECTION == Direction.RIGHT:
                if newAgent.AGENT_LOCATION.x < newAgent.MATRIX_SIZE:
                    newAgent.AGENT_LOCATION.x += 1
                else:
                    newAgent.BUMP_FOUND = True
            elif newAgent.AGENT_DIRECTION == Direction.UP:
                if newAgent.AGENT_LOCATION.y < newAgent.MATRIX_SIZE:
                    newAgent.AGENT_LOCATION.y += 1
                else:
                    newAgent.BUMP_FOUND = True
            elif newAgent.AGENT_DIRECTION == Direction.LEFT:
                if newAgent.AGENT_LOCATION.x > 1:
                    newAgent.AGENT_LOCATION.x -= 1
                else:
                    newAgent.BUMP_FOUND = True
            elif newAgent.AGENT_DIRECTION == Direction.DOWN:
                if newAgent.AGENT_LOCATION.y > 1:
                    newAgent.AGENT_LOCATION.y -= 1
                else:
                    newAgent.BUMP_FOUND = True

            # Update stench percept
            newAgent.STENCH_FOUND = False

            for location in newAgent.WUMPUS_LOCATION:
                if Position.isAdjacent(newAgent.AGENT_LOCATION, location) or \
                    (newAgent.AGENT_LOCATION == location):
                    newAgent.STENCH_FOUND = True

            # Update breeze percept
            BREEZE_FOUND = False
            
            for pit in newAgent.PIT_LOCATIONS:
                if Position.isAdjacent(newAgent.AGENT_LOCATION, pit):
                    newAgent.BREEZE_FOUND = True
                elif newAgent.AGENT_LOCATION == pit:
                    newAgent.AGENT_ALIVE = False

        if action == Action.TURNLEFT:
            if newAgent.AGENT_DIRECTION == Direction.RIGHT:
                newAgent.AGENT_DIRECTION = Direction.UP
            elif newAgent.AGENT_DIRECTION == Direction.UP:
                newAgent.AGENT_DIRECTION = Direction.LEFT
            elif newAgent.AGENT_DIRECTION == Direction.LEFT:
                newAgent.AGENT_DIRECTION = Direction.DOWN
            elif newAgent.AGENT_DIRECTION == Direction.DOWN:
                newAgent.AGENT_DIRECTION = Direction.RIGHT

        if action == Action.TURNRIGHT:
            if newAgent.AGENT_DIRECTION == Direction.RIGHT:
                newAgent.AGENT_DIRECTION = Direction.DOWN
            elif newAgent.AGENT_DIRECTION == Direction.UP:
                newAgent.AGENT_DIRECTION = Direction.RIGHT
            elif newAgent.AGENT_DIRECTION == Direction.LEFT:
                newAgent.AGENT_DIRECTION = Direction.UP
            elif newAgent.AGENT_DIRECTION == Direction.DOWN:
                newAgent.AGENT_DIRECTION = Direction.LEFT

        if action == Action.SHOOT:
            if newAgent.AGENT_ARROW > 0:
                newWumpus = []
                for location in newAgent.WUMPUS_LOCATION:
                    if (((newAgent.AGENT_DIRECTION == Direction.RIGHT) and
                         (newAgent.AGENT_LOCATION.x < location.x) and
                         (newAgent.AGENT_LOCATION.y == location.y)) or
                        ((newAgent.AGENT_DIRECTION == Direction.UP) and
                         (newAgent.AGENT_LOCATION.x == location.x) and
                         (newAgent.AGENT_LOCATION.y < location.y)) or
                        ((newAgent.AGENT_DIRECTION == Direction.LEFT) and
                         (newAgent.AGENT_LOCATION.x > location.x) and
                         (newAgent.AGENT_LOCATION.y == location.y)) or
                        ((newAgent.AGENT_DIRECTION == Direction.DOWN) and
                         (newAgent.AGENT_LOCATION.x == location.x) and
                         (newAgent.AGENT_LOCATION.y > location.y))):
                        newAgent.WUMPUS_KILLEd = True
                        newAgent.SCREAM_FOUND = True
                        # self.current_percept.scream = True
                    else:
                        newWumpus.append(location)
                newAgent.WUMPUS_LOCATION = newWumpus

if __name__ == "__main__":
    main()