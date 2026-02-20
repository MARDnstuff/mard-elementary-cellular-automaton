from app.controllers.game_of_life.life_controller import LifeController



def main():
    startLife()

def startLife():
    life = LifeController(200, 0.5)
    life.startLife()

if __name__ == "__main__":
    main()