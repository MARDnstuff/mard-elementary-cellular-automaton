from random import randint

class Universe:
    def __init__(self, size: int = 3):
        """
        Constructor

        Args:
            size (int): Size of the space
        Return:
            Universe instance
        """
        self.size = size
        self.matrix = []
    
    def helloWorld(self) -> str:
        print("Universe: " + str(self.size))
        pass

    def randomPopulateSpace(self, percentage: float) -> None:
        """
        Popoulates the matrix randomly
        
        Args:
            percentage (float): amount of CA alive
        Return:
            None
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
        self.matrix = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,1,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0,0],
            [0,0,1,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
        ]

    def __str__(self) -> str:
        output = ""
        for row in self.matrix:
            for elem in row:
                if elem == 1:
                    output += " * "
                else:
                    output += "   "
            output += "\n"
        return output