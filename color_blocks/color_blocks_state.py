
def init_goal_for_search(goal_blocks):
    color_blocks_state.global_goal_blocks = list(map(lambda s: int(s), goal_blocks.split(",")))


class color_blocks_state:
    # you can add global params
    global_goal_blocks = None
    
    
    def __init__(self, blocks_str, **kwargs):
        # you can use the init function for several purposes
        self.blocks_states = list(map(lambda s: tuple(map(int, s.split(','))), blocks_str[1:-1].split("),(")))


    def clone(self):
        return color_blocks_state(self.get_state_str())
    
    @staticmethod
    def is_goal_state(_color_blocks_state):
        return all(_color_blocks_state.block_states[i][0] == color_blocks_state.global_goal_blocks[i] for i in range(len(color_blocks_state.global_goal_blocks)))

    def flip(self, start_index):
        state = self.clone()
        state.blocks_states = state.blocks_states[:start_index] + state.blocks_states[start_index:][::-1]
        return state
    def spin(self, block_index):
        state = self.clone()
        block = state.blocks_states[block_index]
        state.blocks_states[block_index] = (block[1], block[0])
        return state
    
    def get_neighbors(self):
        neighbors = []
        blocks_count = len(self.blocks_states)
        for i in range(blocks_count):
            neighbors.append(self.spin(i))
        for i in range(blocks_count - 1):
            neighbors.append(self.flip(i))
        return neighbors
        
    # for debugging states
    def get_state_str(self):
        return ",".join(map(lambda s: f"({s[0]},{s[1]})", self.blocks_states))



    #you can add helper functions