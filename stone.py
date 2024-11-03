class Stone:
    def __init__(self, type):
        if type not in ["iron", "blue", "redd"]:
            raise ValueError("Invalid stone type")
        self.type = type

    def __repr__(self):
        return f"{self.type}"
