from ..universe import Universe

class ElementaryUniverse(Universe):
    """
    Represents a universe for Elementary Cellular Automaton
    """
    def __init__(self, size: int = 3, rule: int = 0) -> None:
        """
        Constructor
        
        :param size: Size of the grid (number of rows and columns)
        """
        if size%2 == 0:
            size += 1
        super().__init__(size)
        self.rule = self.convert_rule(rule)

    def convert_rule(self, rule: int) -> int:
        """
        Converts the rule number to a binary representation (0-255)
        """
        if not (0 <= rule <= 255):
            raise ValueError("Rule should be between 0 and 255")
        
        # "10101010"
        binary = f"{rule:08b}"
        # [1, 0, 1, 0, 1, 0, 1, 0]
        bit_array = [int(bit) for bit in binary]
        bit_array.reverse()
        return bit_array


    def populateSpace(self) -> None:
        """
        Populates the universe with an initial pattern (single cell in the center)
        """
        self.matrix = [[0] * self.size]
        mid = self.size // 2 
        self.matrix[0][mid] = 1
        

