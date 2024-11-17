from cell import Cell
from stone import Stone

class Board:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        
        self.grid = [[Cell() for _ in range(w)] for _ in range(h)]
        self.moves = []  

    def set_type(self, x, y, type):
        if 0 <= x < self.h and 0 <= y < self.w:
            self.grid[x][y] = Cell(type)
        else:
            print("Invalid cell coordinates")

    def place_stone(self, x, y, stone):
        if 0 <= x < self.h and 0 <= y < self.w:
            cell = self.grid[x][y]
            cell.place(stone)
        else:
            print("Invalid cell coordinates")

    def move_stone(self, from_x, from_y, to_x, to_y):
            if not (0 <= from_x < self.h and 0 <= from_y < self.w):
                print("Invalid source cell coordinates")
                return
            if not (0 <= to_x < self.h and 0 <= to_y < self.w):
                print("Invalid destination cell coordinates")
                return

            from_cell = self.grid[from_x][from_y]
            to_cell = self.grid[to_x][to_y]

            if from_cell.empty or from_cell.stone.type not in ["blue", "redd"]:
                print("Only blue and red magnets can be moved.")
                return

            if to_cell.type == "blocke":
                print("Cannot move to a blocked cell.")
                return
            if not to_cell.empty and to_cell.type != "target":
                print("Destination cell is either occupied or blocked.")
                return

            stone = from_cell.stone
            to_cell.place(stone)
            from_cell.remove()

            self.moves.append(((from_x, from_y), (to_x, to_y)))

            if stone.type == "blue":
                self.apply_repulsion(to_x, to_y)

            if stone.type == "redd":
                self.apply_attraction(to_x, to_y)

    def apply_repulsion(self, x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            stones_to_move = []

            while 0 <= nx < self.h and 0 <= ny < self.w:
                neighbor_cell = self.grid[nx][ny]

                if not neighbor_cell.empty and neighbor_cell.stone and neighbor_cell.stone.type in ["iron", "redd"]:
                    stones_to_move.append((nx, ny))  
                elif neighbor_cell.empty:
                    stones_to_move.append((nx, ny))  
                    break  
                else:
                    break  

                nx += dx
                ny += dy

            if len(stones_to_move) > 1:
                for i in range(len(stones_to_move) - 1, 0, -1):
                    src_x, src_y = stones_to_move[i - 1]
                    dest_x, dest_y = stones_to_move[i]

                    if self.grid[dest_x][dest_y].empty:
                        self.grid[dest_x][dest_y].place(self.grid[src_x][src_y].stone)
                        self.grid[src_x][src_y].remove()

            elif len(stones_to_move) == 1:
                src_x, src_y = stones_to_move[0]
                dest_x, dest_y = nx, ny

                if 0 <= dest_x < self.h and 0 <= dest_y < self.w and self.grid[dest_x][dest_y].empty:
                    self.grid[dest_x][dest_y].place(self.grid[src_x][src_y].stone)
                    self.grid[src_x][src_y].remove()
    
    def apply_attraction(self, x, y):  
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            stones_to_move = []
            while 0 <= nx < self.h and 0 <= ny < self.w:
                neighbor_cell = self.grid[nx][ny]
                
                if neighbor_cell.stone and neighbor_cell.stone.type in ["iron", "blue"]:
                    stones_to_move.append((nx, ny))

                elif neighbor_cell.empty:
                    stones_to_move.append((nx, ny))
                else:
                    break   
                nx += dx
                ny += dy
            for i in range(len(stones_to_move)):
                src_x, src_y = stones_to_move[i]
                dest_x = src_x - dx
                dest_y = src_y - dy
                
                if 0 <= dest_x < self.h and 0 <= dest_y < self.w and self.grid[dest_x][dest_y].empty:
                    self.grid[dest_x][dest_y].place(self.grid[src_x][src_y].stone)
                    self.grid[src_x][src_y].remove()
 
    def check_win(self):
        
        for row in self.grid:
            for cell in row:
                if cell.type == "target" and (cell.empty or cell.stone is None):
                    return False  
        return True

    def display(self):
        for row in self.grid:
            print(" | ".join(str(cell) for cell in row))
            print("-" * (self.w * 20))



