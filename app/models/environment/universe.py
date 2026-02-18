

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
        self.matrix = [[]]
    
    def helloWorld(self) -> str:
        print("Universe: " + str(self.size))
        pass