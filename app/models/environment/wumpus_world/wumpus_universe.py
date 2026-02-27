from tkinter import NO
from ..universe import Universe

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

    
    def randomizePosition(self, character_name: str) -> None:
        """
        Randomizes the position of a character in the universe.

        :param character_name: Agent's name
        :type character_name: str
        """
        pass



