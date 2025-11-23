
def init_goal_for_search(goal_blocks):
    color_blocks_state.global_goal_blocks = list(map(lambda s: int(s), goal_blocks.replace(" ", "").split(",")))


class color_blocks_state:
    # you can add global params
    global_goal_blocks = None
    
    
    def __init__(self, blocks_str=None, blocks_list=None, **kwargs):
        # you can use the init function for several purposes
        if blocks_str:
            self.blocks_states = list(map(lambda s: tuple(map(int, s.split(','))), blocks_str.replace(" ", "")[1:-1].split("),(")))
        
        if blocks_list:
            self.blocks_states = blocks_list


    def clone(self):
        return color_blocks_state(blocks_list=self.blocks_states.copy())
    
    @staticmethod
    def is_goal_state(_color_blocks_state):
        return all(_color_blocks_state.blocks_states[i][0] == color_blocks_state.global_goal_blocks[i] for i in range(len(color_blocks_state.global_goal_blocks)))

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
        # return list of (neighbor_state, edge_cost) pairs
        blocks_count = len(self.blocks_states)

        neighbors = [self.spin(i) for i in range(len(blocks_count))] + [self.flip(i) for i in range(blocks_count - 1)]
        return zip(neighbors, [1] * len(neighbors))
        
    # for debugging states
    def get_state_str(self):
        return ",".join(map(lambda s: f"({s[0]} ,{s[1]})", self.blocks_states))

    def __hash__(self):
        return hash(self.get_state_str())
    def __eq__(self, other):
        return all(c[0] == o[0] and c[0] == o[0] for c, o in zip(self.blocks_states, other.blocks_states))

    #you can add helper functions