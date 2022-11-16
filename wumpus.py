

from pathlib import Path

MATRIX_SIZE = 4

ARROW_COUNT = 0

MAX_MOVES_ALLOWED = 100

PIT_LOCATIONS = []

WUMPUS_LOCATION = []

GOLD_LOCATION = []

AGENT_ALIVE = True

AGENT_DIRECTION = 0 
# RIGHT = 0
# UP = 1
# LEFT = 2
# DOWN = 3

AGENT_ARROW = 0

AGENT_GOLD = False


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


AGENT_LOCATION = Position(1, 1)

path = Path(__file__).parent


def main():
    readEnvSettings()
    proceedMovement()


def readEnvSettings():
    # Read from file.
    lines = open(path / "env1.txt", "r")
    matrixSizeFound = False
    arrowNumberFound = False

    for line in lines:
        if (not matrixSizeFound):
            MATRIX_SIZE = int(line)
            matrixSizeFound = True
            continue
        if (not arrowNumberFound):
            ARROW_COUNT = int(line)
            arrowNumberFound = True
            continue
        if (line.startswith("p ")):
            lineParts = line.split(" ")
            if (len(lineParts) == 3):
                x = lineParts[1].strip()
                y = lineParts[2].strip()
                PIT_LOCATIONS.append(Position(x, y))
        if (line.startswith("w ")):
            lineParts = line.split(" ")
            if (len(lineParts) == 3):
                x = lineParts[1].strip()
                y = lineParts[2].strip()
                WUMPUS_LOCATION.append(Position(x, y))
        if (line.startswith("g ")):
            lineParts = line.split(" ")
            if (len(lineParts) == 3):
                x = lineParts[1].strip()
                y = lineParts[2].strip()
                GOLD_LOCATION.append(Position(x, y))

        # print(PIT_LOCATIONS)
        # print(WUMPUS_LOCATION)
        # print(GOLD_LOCATION)


def proceedMovement():
    num_moves = 0
    while (not AGENT_ALIVE) and (num_moves < MAX_MOVES_ALLOWED):
        #display_in_grid()
        percept = wumpus_world.get_percept()  # get the percepts for the current location
        action = Agent.process(percept)  # and pass the percepts to the imported agent, expecting an action

        print("Action = {}".format(action_to_string(action)))
        print()

        wumpus_world.execute_action(action)  # execute the action in the wumpus world
        num_moves += 1


# def display_in_grid(self):

#         out = "+"
#         for x in range(1, MATRIX_SIZE + 1):
#             out += "---+"
#         print(out)

#         for y in range(MATRIX_SIZE, 0, -1):  # print starting from the 'bottom' up

#             # print out the first row, containing pits + gold + wumpus
#             out = "|"

#             for x in range(1, MATRIX_SIZE + 1):
#                 character = " "
#                 for item in WUMPUS_LOCATION:
#                     if item == Position(x, y):
#                        character= "W"

#                 for item in PIT_LOCATIONS:
#                     if item == Position(x, y):
#                        character= "P"
                    
#                 for item in GOLD_LOCATION:
#                     if item == Position(x, y):
#                        character= "G"
                
#                 out += character
                       
#                 out += "|"

#             print(out)

#             # print out the second row, containing the agent
#             out = "|"

#             for x in range(1, WORLD_SIZE + 1):
#                 if self.current_state.agent_alive and self.current_state.agent_location == Position(x, y):
#                     if self.current_state.agent_orientation == RIGHT:
#                         out += " A>|"
#                     elif self.current_state.agent_orientation == UP:
#                         out += " A^|"
#                     elif self.current_state.agent_orientation == LEFT:
#                         out += " A<|"
#                     else:
#                         out += " Av|"
#                 else:
#                     out += "   |"

#             print(out)
#             out = "+"

#             # print out the final horizontal line
#             for x in range(1, WORLD_SIZE + 1):
#                 out += "---+"

#             print(out)

#         # print the current percepts for the agent's location
#         print("Current percept = [stench={},breeze={},glitter={},bump={},scream={}]".format(
#             self.current_percept.stench,
#             self.current_percept.breeze,
#             self.current_percept.glitter,
#             self.current_percept.bump,
#             self.current_percept.scream))

#         print("Agent has gold = {}, agent has arrow = {}".format(
#             self.current_state.agent_has_gold,
#             self.current_state.agent_has_arrow))

#         print("Current score = {}".format(self.get_score()))
#         print()


if __name__ == "__main__":
    main()
