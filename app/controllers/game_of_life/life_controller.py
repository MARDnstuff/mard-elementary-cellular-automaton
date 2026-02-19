from app.models.environment.game_of_life.life_universe import LifeUniverse
from app.views.game_of_life.life_view import LifeView
from app.controllers.utils.utils import positive
import pygame
import sys
import os

class LifeController:
    def __init__(self, size, percentage):
        self.my_universe = LifeUniverse(size)
        self.my_universe.randomPopulateSpace(percentage)
    
    def showGrid(self) -> None:
        print(self.my_universe)
    
    def advanceSimulation(self) -> list[list]:
        output_matrix = []
        for i, row in enumerate(self.my_universe.matrix):
            new_row = []
            for j, col in enumerate(row):
                num_neighbors = 0
                
                if self.my_universe.matrix[positive(i - 1, self.my_universe.size)%self.my_universe.size][j] == 1: num_neighbors += 1
                if self.my_universe.matrix[positive(i - 1, self.my_universe.size)%self.my_universe.size][(j + 1)%self.my_universe.size] == 1: num_neighbors += 1
                if self.my_universe.matrix[i][(j + 1)%self.my_universe.size] == 1: num_neighbors += 1
                if self.my_universe.matrix[(i + 1)%self.my_universe.size][(j + 1)%self.my_universe.size] == 1: num_neighbors += 1
                if self.my_universe.matrix[(i + 1)%self.my_universe.size][j] == 1: num_neighbors += 1
                if self.my_universe.matrix[(i + 1)%self.my_universe.size][positive(j - 1, self.my_universe.size)%self.my_universe.size] == 1: num_neighbors += 1
                if self.my_universe.matrix[i][positive(j - 1, self.my_universe.size)%self.my_universe.size] == 1: num_neighbors += 1
                if self.my_universe.matrix[positive(i - 1, self.my_universe.size)%self.my_universe.size][positive(j - 1, self.my_universe.size)%self.my_universe.size] == 1: num_neighbors += 1

                if self.my_universe.matrix[i][j] == 0 and (num_neighbors >= self.my_universe.Nmin and num_neighbors <= self.my_universe.Nmax):
                    new_row.append(1)
                elif self.my_universe.matrix[i][j] == 1 and (num_neighbors >= self.my_universe.Smin and num_neighbors <= self.my_universe.Smax):
                    new_row.append(1)
                else:
                    new_row.append(0)
            output_matrix.append(new_row)
        self.my_universe.matrix = output_matrix

    def startLife(self) -> None:

        # Configuración
        WIDTH, HEIGHT = 800, 600
        ROWS, COLS = 30, 40
        CELL_SIZE = WIDTH // COLS

        # Colores
        BG_COLOR = (30, 30, 30)
        GRID_COLOR = (60, 60, 60)

        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Grid con Pygame")

        clock = pygame.time.Clock()

        def draw_grid():
            for row in range(ROWS):
                for col in range(COLS):
                    rect = pygame.Rect(
                        col * CELL_SIZE,
                        row * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE
                    )
                    pygame.draw.rect(screen, GRID_COLOR, rect, 1)  # 1 = solo borde
        
        def update_grid(screen, grid: list[list[int]], cell_size: int) -> None:
            rows = len(grid)
            cols = len(grid[0])

            for r in range(rows):
                for c in range(cols):
                    
                    if grid[r][c] == 1:
                        color = (255, 255, 255)  # blanco = viva
                    else:
                        color = (0, 0, 0)  # negro = muerta
                    
                    pygame.draw.rect(
                        screen,
                        color,
                        (c * cell_size, r * cell_size, cell_size, cell_size)
                    )

        # Loop principal
        running = True
        
        while running:
            clock.tick(5)
            screen.fill(BG_COLOR)
            os.system("cls" if os.name == "nt" else "clear")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            draw_grid()
            self.advanceSimulation()
            update_grid(screen, self.my_universe.matrix, self.my_universe.size)
            
            pygame.display.flip()


        pygame.quit()
        sys.exit()





