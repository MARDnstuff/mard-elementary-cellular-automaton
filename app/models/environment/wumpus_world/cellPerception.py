class cellPerception:
    """
    Constant enviroment (cell) perception
    """
    def __init__(self):
        # Pos - Type
        # 0 -> stench
        # 1 -> breeze
        # 2 -> glitter
        self.perception: list[int] = [0, 0, 0]

        # Type could be:
        # P = PIT
        # W = WUMPUS
        # A = AGENT
        # G = GOLD
        self.type = None

    

    def __str__(self):
        return  f"[ type: {str(self.type)} , env: {str(self.perception)} ]"
        