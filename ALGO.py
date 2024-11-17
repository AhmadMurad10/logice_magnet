from collections import deque
import copy  
import heapq

class Algorithm:
   
    def BFS(initial_board):

        queue = deque([(initial_board, [])])
        visited = set()
        solved = False  

        while queue:
            if solved:
                break  

            current_board, path = queue.popleft()

            if current_board.check_win():
                if not solved:  
                    solved = True
                    print("\nYou won the level!")
                    print("Moves you made:")
                    for move in path:
                        print(f"From {move[0]} to {move[1]}")

                    print("\nSolution Path with Board States:")
                  
                    solution_board = initial_board
                    solution_board.display()  
                    print("----------------------------")

                    for move in path:
                        x, y = move[0]
                        new_x, new_y = move[1]
                        solution_board.move_stone(x, y, new_x, new_y)
                        solution_board.display()
                        print("----------------------------")
                break  

            serialized_state = tuple(
                tuple(cell.stone.type if cell.stone else None for cell in row) for row in current_board.grid
            )

            if serialized_state in visited:
                continue  

            visited.add(serialized_state)
           
            for x in range(current_board.h):
                for y in range(current_board.w):
                    cell = current_board.grid[x][y]
                    
                    if cell.stone and cell.stone.type in ["blue", "redd"]:
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            new_x, new_y = x + dx, y + dy
                            if 0 <= new_x < current_board.h and 0 <= new_y < current_board.w:
                               
                                new_board = copy.deepcopy(current_board)

                                new_board.move_stone(x, y, new_x, new_y)
 
                                new_serialized_state = tuple(
                                    tuple(cell.stone.type if cell.stone else None for cell in row) for row in new_board.grid
                                )

                                if new_serialized_state not in visited:
                                    queue.append((new_board, path + [((x, y), (new_x, new_y))]))

        if not solved:
            print("No solution found.")

    def DFS(initial_board):
        
        stack = [(initial_board, [])]
        visited = set()
        solved = False 

        while stack:
            if solved:
                break 

            current_board, path = stack.pop()
           
            if current_board.check_win():
                if not solved:  
                    solved = True
                    print("\nYou won the level!")
                    print("Moves you made:")
                    for move in path:
                        print(f"From {move[0]} to {move[1]}")

                    print("\nSolution Path with Board States:")
                    
                    solution_board = initial_board
                    solution_board.display()  
                    print("----------------------------")

                    for move in path:
                        x, y = move[0]
                        new_x, new_y = move[1]
                        solution_board.move_stone(x, y, new_x, new_y)
                        solution_board.display()
                        print("----------------------------")
                break  
  
            serialized_state = tuple(
                tuple(cell.stone.type if cell.stone else None for cell in row) for row in current_board.grid
            )

            if serialized_state in visited:
                continue  

            visited.add(serialized_state)

            for x in range(current_board.h):
                for y in range(current_board.w):
                    cell = current_board.grid[x][y]
                    
                    if cell.stone and cell.stone.type in ["blue", "redd"]:
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            new_x, new_y = x + dx, y + dy
                            if 0 <= new_x < current_board.h and 0 <= new_y < current_board.w:
                               
                                new_board = copy.deepcopy(current_board)

                                new_board.move_stone(x, y, new_x, new_y)

                                new_serialized_state = tuple(
                                    tuple(cell.stone.type if cell.stone else None for cell in row) for row in new_board.grid
                                )

                                if new_serialized_state not in visited:
                                    stack.append((new_board, path + [((x, y), (new_x, new_y))]))

        if not solved:
            print("No solution found.")

    def UCS(initial_board):
        priority_queue = []
        visited = set()
        solved = False

        def serialize_board(board):
            return tuple(
                tuple(cell.stone.type if cell.stone and cell.stone.type else "empty" for cell in row)
                for row in board.grid
            )

        initial_serialized_state = serialize_board(initial_board)
        heapq.heappush(priority_queue, (0, 0, initial_serialized_state, [], initial_board))  

        while priority_queue:
            if solved:
                break

            cost, step_count, serialized_state, path, current_board = heapq.heappop(priority_queue)

            if serialized_state in visited:
                continue
            visited.add(serialized_state)

            print("\nCurrent Path (cost: {}, steps: {}):".format(cost, step_count))
            for move in path:
                print(f"From {move[0]} to {move[1]}")
            current_board.display()
            print("----------------------------")

            if current_board.check_win():
                solved = True
                print("\nYou won the level!")
                print("Moves you made:")
                for move in path:
                    print(f"From {move[0]} to {move[1]}")

                print("\nSolution Path with Board States:")
                solution_board = initial_board
                solution_board.display()
                print("----------------------------")

                for move in path:
                    x, y = move[0]
                    new_x, new_y = move[1]
                    solution_board.move_stone(x, y, new_x, new_y)
                    solution_board.display()
                    print("----------------------------")
                break

            for x in range(current_board.h):
                for y in range(current_board.w):
                    for new_x in range(current_board.h):
                        for new_y in range(current_board.w):
                            if (x, y) == (new_x, new_y):
                                continue

                            cell = current_board.grid[x][y]
                            if cell.stone and cell.stone.type in ["blue", "redd"]:
                                new_board = copy.deepcopy(current_board)
                                new_board.move_stone(x, y, new_x, new_y)

                                new_serialized_state = serialize_board(new_board)

                                if new_serialized_state in visited:
                                    print(f"Skipping already visited state at move: {((x, y), (new_x, new_y))}")
                                    continue

                               
                                move_cost = 1  
                                new_cost = cost + move_cost

                                print(f"Trying move: From {(x, y)} to {(new_x, new_y)} (new cost: {new_cost}, steps: {step_count + 1})")
                                heapq.heappush(
                                    priority_queue, (new_cost, step_count + 1, new_serialized_state, path + [((x, y), (new_x, new_y))], new_board)
                                )


        if not solved:
            print("No solution found.")
    
    