import logging
import pygame


logger = logging.getLogger(__name__) 

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
        self.HEIGHT: int = 500
        self.ROWS: int = 1
        self.COLS: int = size
        self.CELL_SIZE: int = self.WIDTH // self.COLS

        # Colors
        self.BG_COLOR: tuple[int, int,int] = (30, 30, 30)
        self.GRID_COLOR: tuple[int, int,int] = (60, 60, 60)
        self.ALIVE_COLOR: tuple[int, int,int] = (255, 255, 255)
        self.DEAD_COLOR: tuple[int, int, int] = self.BG_COLOR
        


    def draw_grid(self, screen) -> None:
        """
        Draws the grid on the screen
        
        :param screen: The pygame screen surface to draw on
        """
        for row in range(self.ROWS):
            for col in range(self.COLS):
                rect = pygame.Rect(
                    col * self.CELL_SIZE,
                    row * self.CELL_SIZE,
                    self.CELL_SIZE,
                    self.CELL_SIZE
                )
                pygame.draw.rect(screen, self.GRID_COLOR, rect, 1)
        logger.debug("Grid drawn on screen")
        

    
    def update_grid(self, screen, grid: list[list[int]], cell_size: int) -> None:
        """
        Updastes the current grid
        
        :param screen: The pygame screen surface to draw on
        :param grid: The 2D list representing the current state of the grid
        :type grid: list[list[int]]
        :param cell_size: Size of each cell in pixels
        :type cell_size: int
        """
        for row in range(self.ROWS):
            for col in range(self.COLS):
                rect = pygame.Rect(
                    col * self.CELL_SIZE,
                    row * self.CELL_SIZE,
                    self.CELL_SIZE,
                    self.CELL_SIZE
                )
                
                if grid[row][col] == 1:
                    pygame.draw.rect(screen,self.ALIVE_COLOR,rect)
                else:
                    pygame.draw.rect(screen,self.DEAD_COLOR,rect)

                pygame.draw.rect(screen,self.GRID_COLOR,rect, 1)
        logger.debug("Grid updated on screen")