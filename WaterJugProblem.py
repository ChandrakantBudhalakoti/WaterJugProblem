# Water Jug Problem Solver using AI

# Define the initial and goal state of the problem
initial_state = (0, 0)
goal_state = (2, 0)

# Define the maximum capacities of the two jugs
max_jug_1 = 4
max_jug_2 = 3

# Define a function to get all possible next states from the current state
def get_next_states(state):
    next_states = set()
    jug_1, jug_2 = state
    
    # Fill jug 1
    next_states.add((max_jug_1, jug_2))
    
    # Fill jug 2
    next_states.add((jug_1, max_jug_2))
    
    # Empty jug 1
    next_states.add((0, jug_2))
    
    # Empty jug 2
    next_states.add((jug_1, 0))
    
    # Pour jug 1 into jug 2
    if jug_1 + jug_2 <= max_jug_2:
        next_states.add((0, jug_1 + jug_2))
    else:
        next_states.add((jug_1 - (max_jug_2 - jug_2), max_jug_2))
    
    # Pour jug 2 into jug 1
    if jug_1 + jug_2 <= max_jug_1:
        next_states.add((jug_1 + jug_2, 0))
    else:
        next_states.add((max_jug_1, jug_2 - (max_jug_1 - jug_1)))
    
    return next_states

# Define a function to solve the problem using a simple AI approach
def solve():
    current_state = initial_state
    visited_states = set()
    path = []
    
    while current_state != goal_state:
        visited_states.add(current_state)
        next_states = get_next_states(current_state)
        unvisited_states = next_states - visited_states
        
        if not unvisited_states:
            # Backtrack if there are no unvisited states from the current state
            path.pop()
            current_state = path[-1]
        else:
            # Choose the first unvisited state as the next state
            next_state = unvisited_states.pop()
            path.append(next_state)
            current_state = next_state
    
    return path

# Print the solution path
solution_path = solve()
for state in solution_path:
    print(state)

