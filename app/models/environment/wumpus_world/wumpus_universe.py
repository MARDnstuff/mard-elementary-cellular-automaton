from ..universe import Universe
from .cellPerception import cellPerception
from app.controllers.utils.utils import printMatrix, positive
from random import randint
import logging

logger = logging.getLogger(__name__)

class WumpusUniverse(Universe):
    """
    Represents a universe for Wumpus World
    """
    def __init__(self, size = 4):
        """
        Constructor
        
        :param size: Size of the grid (number of rows and columns)
        """
        super().__init__(size)

        # ID of each character and object
        self.PIT = "P"
        self.GOLD = "G"
        self.AGENT = "A"
        self.WUMPUS = "W"

        # Percentage Pit creation
        self.pit_percentage = 0.2

        # Empty matrix, each cell contains a perception object
        self.matrix = [
            [cellPerception() for _ in range(self.size)]
            for _ in range(self.size)
        ]
        logger.debug("Matrix has been initialized correctly")

        # Intial position of the agent
        self.agent_pos = [0, 0]
        self.wumpus_pos = None
        self.gold_pos = None

        self.randomizeInitialPosition()
        printMatrix(self.matrix)


    def placeWumpus(self, x: int, y: int) -> None:
        """
        Place Wumpus in a given position

        :param x: row in matrix
        :param y: column in matrix
        """
        self.matrix[x][y].type = "W"
        self.wumpus_pos = [x , y]
        # Pos - Type
        # 0 -> stench
        if x + 1 < self.size:
            down = [x + 1, y]
            self.matrix[down[0]][down[1]].perception[0] = 1
        
        if x - 1 >= 0:
            up = [x - 1, y]
            self.matrix[up[0]][up[1]].perception[0] = 1
        
        if y + 1 < self.size:
            right = [ x , y + 1]
            self.matrix[right[0]][right[1]].perception[0] = 1
        
        if y - 1 >= 0:
            left = [x, y - 1]
            self.matrix[left[0]][left[1]].perception[0] = 1
        
        logger.debug(f"Wumpus has been placed in {self.wumpus_pos}")
        
    def placeGold(self, x: int, y: int) -> None:
        """
        Place Gold in a given position

        :param x: row in matrix
        :param y: column in matrix
        """
        # Pos - Type
        # 2 -> glitter
        self.matrix[x][y].type = "G"
        self.matrix[x][y].perception[2] = 1
        self.gold_pos = [x, y]
        logger.debug(f"Gold has been placed in {self.gold_pos}")

    def placePit(self, x: int, y: int) -> None:
        """
        Place a PIT in a given position

        :param x: row in matrix
        :param y: column in matrix
        """
        # Pos - Type
        # 1 -> breeze

        self.matrix[x][y].type = "P"
        
        # TODO: Avoid propagating the breeze when the neighbour is a Pit
        if x + 1 < self.size:
            down = [x + 1, y]
            self.matrix[down[0]][down[1]].perception[1] = 1
        
        if x - 1 >= 0:
            up = [x - 1, y]
            self.matrix[up[0]][up[1]].perception[1] = 1
        
        if y + 1 < self.size:
            right = [ x , y + 1]
            self.matrix[right[0]][right[1]].perception[1] = 1
        
        if y - 1 >= 0:
            left = [x, y - 1]
            self.matrix[left[0]][left[1]].perception[1] = 1
        
        logger.debug(f"Pit has been placed in [{x}, {y}]")


    def randomizeInitialPosition(self) -> None:
        """
        Randomizes the position of a character / object in the universe.
        """
        self.used_pos = set()
        self.used_pos.add((self.agent_pos[0], self.agent_pos[1]))

        # Agent initial position is always [0,0]
        self.matrix[self.agent_pos[0]][self.agent_pos[1]].type = "A"

        # Wumpus random position
        placed = False
        while(not placed):
            x,y = randint(0, self.size - 1) , randint(0, self.size - 1)
            if (x,y) not in self.used_pos:
                self.placeWumpus(x, y)
                self.used_pos.add((x,y))
                placed = True

        # Gold random position
        placed = False
        while(not placed):
            x,y = randint(0, self.size - 1) , randint(0, self.size - 1)
            if (x,y) not in self.used_pos:
                self.placeGold(x,y)
                self.used_pos.add((x,y))
                placed = True
        
        # PIT Random position
        for x, row in enumerate(self.matrix):
            for y, col in enumerate(row):
                probability = randint(0,100)*0.01
                if (x,y) not in self.used_pos and probability < self.pit_percentage:
                    self.placePit(x,y)
                    self.used_pos.add((x,y))
        logger.info("All objects / characters have been randomly placed")


