

class ElementaryView:
    """
    View class for Elementary Cellular Automaton
    """
    
    def __init__(self, size: int):
        """
        Constructor
        
        :param size: Size of the grid (number of rows and columns)
        :type size: int
        """
        # Screen Configuration
        self.WIDTH: int = 800
        self.HEIGHT: int = 800
        self.ROWS: int = size
        self.COLS: int = size
        self.CELL_SIZE: int = self.WIDTH // self.COLS

        # Colors
        self.BG_COLOR: tuple[int, int,int] = (30, 30, 30)
        self.GRID_COLOR: tuple[int, int,int] = (60, 60, 60)
        self.ALIVE_COLOR: tuple[int, int,int] = (255, 255, 255)
        self.DEAD_COLOR: tuple[int, int, int] = self.BG_COLOR
        pass

    def helloWorld(self) -> str:
        print("ElementaryView")
        pass