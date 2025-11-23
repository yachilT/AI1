from color_blocks_state import color_blocks_state

# you can add helper functions and params
global_goal_blocks = None

def is_match(block1, block2, goal_blocks):
    goal_pairs = list((goal_blocks[i], goal_blocks[i+1]) for i in range(len(goal_blocks)-1))
    for color1 in block1:
        for color2 in block2:
            if (color1, color2) in goal_pairs or (color2, color1) in goal_pairs:
                return 0
    return 1

def init_goal_for_heuristics(goal_blocks):
    global global_goal_blocks
    global_goal_blocks = list(map(lambda s: int(s), goal_blocks.split(",")))

def base_heuristic(_color_blocks_state):
    blocks = _color_blocks_state.blocks_states
    goal_blocks = global_goal_blocks
    
    return sum(is_match(blocks[i], blocks[i+1], goal_blocks) for i in range(len(blocks)-1))


def advanced_heuristic(_color_blocks_state):
    global global_goal_blocks
    h_base = base_heuristic(_color_blocks_state)
    
    blocks = _color_blocks_state.blocks_states
    for i in range(len(blocks)):
        if blocks[i][0] not in global_goal_blocks:
            h_base += 1  # Penalty for blocks with colors not in the goal
    return h_base
