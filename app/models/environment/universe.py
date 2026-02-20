from random import randint

class Universe:
    def __init__(self, size: int = 3):
        """
        Constructor
        
        :param size: Size of the grid
        :type size: int
        """
        self.size = size
        self.matrix = []
    
    def randomPopulateSpace(self, percentage: float) -> None:
        """
        Populate the matrix randomly
        
        :param percentage: Amount of alive cells
        :type percentage: float
        """
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