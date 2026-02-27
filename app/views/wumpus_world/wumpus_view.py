import logging
import pygame

from testWumpus import cart_to_iso

logger = logging.getLogger(__name__) 

class WumpusView:
    """
    View class for Wumpus World
    """

    def __init__(self, size: int):
        """
        Constructor
        """
        # Configuration
        self.GRID_SIZE = size
        self.TILE_WIDTH = 128
        self.TILE_HEIGHT = 64
        self.WIDTH = 900
        self.HEIGHT = 700

        # Colors
        self.WHITE = (255, 255, 255)
        self.GRAY = (200, 200, 200)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 200, 0)
        self.RED = (200, 0, 0)
        
        # Assets
        self.agent_img_path = "assets/knight_2.png"
        self.wumpus_img_path = "assets/monster_2.png"
        self.gold_img_path = "assets/gold.png"

        # Center map
        self.offset_x = self.WIDTH // 2
        self.offset_y = 100

    def cart_to_iso(self, x: int, y: int) -> tuple[int, int]:
        """
        Convert from cartesian to isometric coordinates
        
        :param x: x coordinate in cartesian system
        :param y: y coordinate in cartesian system
        """
        iso_x = (x - y) * (self.TILE_WIDTH // 2)
        iso_y = (x + y) * (self.TILE_HEIGHT // 2)
        return iso_x +  self.offset_x, iso_y + self.offset_y

    def draw_tile(self, screen, x: int, y: int) -> None:
        iso_x, iso_y = self.cart_to_iso(x, y)

        points = [
            (iso_x, iso_y),
            (iso_x + self.TILE_WIDTH // 2, iso_y + self.TILE_HEIGHT // 2),
            (iso_x, iso_y + self.TILE_HEIGHT),
            (iso_x - self.TILE_WIDTH // 2, iso_y + self.TILE_HEIGHT // 2),
        ]

        pygame.draw.polygon(screen, self.GRAY, points)
        pygame.draw.polygon(screen, self.BLACK, points, 2)

    def draw_character(self, screen, img, x: int, y: int) -> None:
        iso_x, iso_y = self.cart_to_iso(x, y)

        sprite_width = img.get_width()
        sprite_height = img.get_height()

        screen.blit(
            img,
            (
                iso_x - sprite_width // 2,
                iso_y + self.TILE_HEIGHT // 2 - sprite_height
            )
        )