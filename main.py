from board import Board
from stone import Stone


attempts_per_level = [5, 5, 5, 2, 2,1,1]
levels = [
    {
        'size': 4,
        'targets': [(1, 1), (1, 3)],
        'stones': [(1, 2, "iron"), (2, 0, "blue")]
    },
    {
        'size': 5,
        'targets': [(0, 2), (2, 2), (2, 0), (2, 4), (4, 2)],
        'stones': [(1, 2, "iron"), (2, 1, "iron"), (3, 2, "iron"), (2, 3, "iron"), (4, 0, "blue")]
    },
    {
        'size': 4,
        'targets': [(0, 3), (2, 3)],
        'stones': [(1, 2, "iron"), (2, 0, "blue")]
    },
    {
        'size': 5,
        'targets': [(0, 0), (0, 2), (4, 1)],
        'stones': [(1, 1, "iron"), (3, 1, "iron"), (2, 0, "blue")]
    },
    {
        'size': 4,
        'targets': [(0, 0),(1, 0),(1, 2), (0, 2), (3, 0)],
        'blockes': [(0, 1), (1, 1), (2, 1)],
        'stones': [(1, 0, "iron"), (2, 0, "iron"), (2, 2, "iron"), (1, 2, "iron"), (3, 1, "blue")]
    }
    , {
        'size': 5,
        'targets': [(0, 1),(0,2),(0, 3)],
        'blockes': [(1, 0), (1, 1), (1, 3), (1, 4)],
        'stones': [(0, 0, "iron"), (0, 4, "iron"), (1,2, "redd")]
    },
     {
        'size': 5,
        'targets': [(1, 0),(2,0),(4,0),(4,2)],
        'blockes': [(0,2), (0,3), (1,2), (1,3)],
        'stones': [(0, 0, "iron"), (1, 0, "iron"),(4,3, "iron"),(3,1, "redd")]
    }
]

def setup_level(level_index):
    level = levels[level_index]
    n = level['size']
    board = Board(n, n)

    
    for target in level['targets']:
        board.set_type(*target, "target")
        
    for target in level['blockes']:
        board.set_type(*target, "blocke")
 
    for stone in level['stones']:
        x, y, stone_type = stone
        board.place_stone(x, y, Stone(stone_type))

    return board

def play_level(level_index):
    board = setup_level(level_index)
    max_attempts = attempts_per_level[level_index]
    attempts = 0

    board.display()

    while attempts < max_attempts:
        print(f"Remaining attempts: {max_attempts - attempts}")
        print("Enter coordinates of the stone to move (x1, y1) or 'q' to quit:")
        user_input = input("Input: ")

        if user_input.lower() == 'q':
            print("Exiting the game.")
            break  

        try: 
            from_x, from_y = map(int, user_input.split(','))

            if 0 <= from_x < board.h and 0 <= from_y < board.w:
                if board.grid[from_x][from_y].empty or board.grid[from_x][from_y].stone.type not in ["blue", "iron", "redd"]:
                    print("The selected cell does not contain a blue, iron, or red magnet.")
                    continue

                print("Enter the target coordinates (x2, y2) to move the stone:")
                target_input = input("Input: ")
                target_x, target_y = map(int, target_input.split(','))

                if 0 <= target_x < board.h and 0 <= target_y < board.w:
                    board.move_stone(from_x, from_y, target_x, target_y)
                    board.display()  

                    if board.check_win():
                        print("Congratulations! You've won the game!")
                        return  

                    attempts += 1
                else:
                    print("Invalid target coordinates, they must be within the board limits.")
            else:
                print("Invalid coordinates, they must be within the board limits.")

        except ValueError:
            print("Please enter valid coordinates in the format (x, y).")

    print("You have run out of attempts. Unfortunately, you lost this level.")

while True:
    print("Choose a level (1-) or 'q' to quit:")
    for i in range(1, len(attempts_per_level) + 1):
        print(f"Level {i}: {attempts_per_level[i - 1]} attempts")
    
    level_choice = input("Your choice: ")
    if level_choice.lower() == 'q':
        print("Exiting the game.")
        break
    
    try:
        level_index = int(level_choice) - 1
        if 0 <= level_index < len(attempts_per_level):
            play_level(level_index)
        else:
            print("Invalid choice, please choose a valid number.")
    except ValueError:
        print("Please enter a valid number.")


