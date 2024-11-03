class Cell:
    def __init__(self, type="normal"):
        if type not in ["normal", "blocke", "target"]:
            raise ValueError("Invalid cell type")
        self.type = type
        self.empty = True  
        self.stone = None  

    def place(self, stone):
        
        if self.type == "blocke":
            print("Cannot place a stone in a blocked cell.")
        elif not self.empty and self.type != "target":
            print("Cell is already occupied.")
        else:
            self.stone = stone
            self.empty = False

    def remove(self):
        self.stone = None  
        self.empty = True  

    def __repr__(self):
        if self.empty:
            return f"{self.type}, T, \"  \""  
        elif self.stone is not None:
            return f"{self.type}, F, {self.stone.type}"  
        else:
            return f"{self.type}, T, \"  \""  
