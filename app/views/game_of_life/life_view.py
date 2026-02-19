import pygame
import sys

class LifeView:
    def __init__(self):
        pass

    def helloWorld(self) -> str:
        print("LifeView")
        pass

    def test(self) -> None:
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

        # Loop principal
        running = True
        while running:
            clock.tick(5)
            screen.fill(BG_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            draw_grid()
            pygame.display.flip()

        pygame.quit()
        sys.exit()
