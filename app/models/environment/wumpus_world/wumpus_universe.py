from ..universe import Universe

class WumpusUniverse(Universe):
    """
    Represents a universe for Wumpus World
    """
    def __init__(self, size = 3):
        """
        Constructor
        
        :param size: Size of the grid (number of rows and columns)
        """
        super().__init__(size)