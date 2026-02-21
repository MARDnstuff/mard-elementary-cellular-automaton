from random import randint
import logging

logger = logging.getLogger(__name__)

class Universe:
    """
    Base class for all universes in the cellular automaton simulation.
    """
    def __init__(self, size: int = 3):
        """
        Constructor
        
        :param size: Size of the grid
        :type size: int
        """
        if not (size >= 3 and size <= 501):
            logger.error("Size is out of bounds")
            raise ValueError("Size must be an integer between 1 and 500")
        self.size = size
        self.matrix = []
    
    def randomPopulateSpace(self, percentage: float) -> None:
        """
        Populate the matrix randomly
        
        :param percentage: Amount of alive cells
        :type percentage: float
        """
        if not (percentage > 0 and percentage <= 1):
            logger.error("Percentage is out of bounds")
            raise ValueError("Percentage must be between 0 and 1 (e.g., 0.5 for 50%)")
        for i in range(self.size):
            row = []
            for j in range(self.size):
                probability = randint(0,100)*0.01
                if probability < percentage :
                    row.append(1)
                else:
                    row.append(0)
            self.matrix.append(row)
        
    def __str__(self) -> str:
        """
        String format

        :return: String format of matrix
        :rtype: str
        """
        output = ""
        for row in self.matrix:
            output += str(row) + "\n"
        return output