from app.models.environment.universe import Universe

class LifeUniverse(Universe):
    """
    Represents a universe for Conway's Game of Life.
    """
    def __init__(self, size = 3):
        """
        Constructor
        
        :param size: Size of the grid (number of rows and columns)
        """
        super().__init__(size)
        self.Smin: int = 2
        self.Smax: int = 3
        self.Nmin: int = 3
        self.Nmax: int = 3
        




