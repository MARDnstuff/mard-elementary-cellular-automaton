from ..universe import Universe

class WumpusUniverse(Universe):
    """
    Represents a universe for Wumpus World
    """
    def __init__(self, size = 4, width = 900, height = 700):
        """
        Constructor
        
        :param size: Size of the grid (number of rows and columns)
        """
        super().__init__(size)
        self.agent_pos = [0, 0]
        self.wumpus_pos = [2, 2]
        self.gold_pos = [size - 1, size - 1]

        # Centrar mapa
        self.offset_x = width // 2
        self.offset_y = 100

    
    def randomizePosition(self, character_name: str) -> None:
        """
        Randomizes the position of a character in the universe.

        :param character_name: Agent's name
        :type character_name: str
        """
        pass



