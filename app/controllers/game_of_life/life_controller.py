from app.models.environment.game_of_life.life_universe import LifeUniverse
from app.views.game_of_life.life_view import LifeView
from app.controllers.utils.utils import positive
from app.controllers.simulation import Simulation
import logging
import pygame
import sys


logger = logging.getLogger(__name__)

class LifeController(Simulation):
    """
    Controller class for Conway's Game of Life
    """

    def __init__(self, size: int, percentage: float) -> None:
        """
        Constructur
        
        :param size: Size of the grid
        :param percentage: amount of alive cells
        """        
        self.my_universe = LifeUniverse(size)
        self.my_universe.randomPopulateSpace(percentage)
        self.time_velocity = 5
        self.age = 0

    def advanceSimulation(self) -> list[list]:
        """
        Run the simulation, Advance the simulation on iteration
        
        :return: matrix
        :rtype: list[list]
        """
        if not self.my_universe.matrix:
            logger.error("Universe is empty")
            raise Exception("Universe is not initialized properly")

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
        self.age += 1
        logger.debug("Simulation advanced by one iteration -> Age: %d", self.age)

    

    def startSimulation(self) -> None:
        """
        Starts simulation
        """
        try:
            logger.info("Starting Life simulation")
            self.view = LifeView(self.my_universe.size)
            
            pygame.init()
            self.screen = pygame.display.set_mode((self.view.WIDTH, self.view.HEIGHT))
            logger.debug("Pygame initialized and screen created")
            pygame.display.set_caption("Grid con Pygame")

            clock = pygame.time.Clock()
            
            # Main loop
            running = True
            
            while running:
                clock.tick(self.time_velocity)
                self.screen.fill(self.view.BG_COLOR)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        logger.info("Ending Life simulation")
                        running = False
                # Main logic
                self.view.draw_grid(self.screen)
                self.advanceSimulation()
                self.view.update_grid(self.screen, self.my_universe.matrix, self.my_universe.size)
                
                pygame.display.flip()

            pygame.quit()
            sys.exit()
        except Exception as e:
            logger.error("Error in Life simulation: %s", e)
            sys.exit()





