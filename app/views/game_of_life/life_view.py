import pygame
import sys

class LifeView:
    def __init__(self, size: int):
        """
        Docstring for __init__
        
        :param self: Description
        :param size: Description
        :type size: int
        """
        # Confguration
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

    def draw_grid(self, screen) -> None:
        """
        Docstring for draw_grid
        
        :param self: Description
        :param screen: Description
        """
        for row in range(self.ROWS):
            for col in range(self.COLS):
                rect = pygame.Rect(
                    col * self.CELL_SIZE,
                    row * self.CELL_SIZE,
                    self.CELL_SIZE,
                    self.CELL_SIZE
                )
                pygame.draw.rect(screen, self.GRID_COLOR, rect, 1)  # 1 = solo borde

    def update_grid(self, screen, grid: list[list[int]], cell_size: int) -> None:
        """
        Docstring for update_grid
        
        :param self: Description
        :param screen: Description
        :param grid: Description
        :type grid: list[list[int]]
        :param cell_size: Description
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


                

