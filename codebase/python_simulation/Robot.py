import Direction as DIR

class robot:
    def __init__(self,maze):
        self.maze=maze
        self.i,self.j=maze.start
        self.orientation=DIR.direction.EAST  #mark the front of the robot
        self.path=[]
        self.maze.get_cell(self.i,self.j).visited=True
        self.steps=0
        self.previous_positions = []  # Stack to track previous positions
        self.direction_history = []   # Stack to track movement directions
   
    def move_forward(self):
        di, dj = DIR.PIXEL_SPACE_DIRECTION_MAP[self.orientation]
        new_i, new_j = self.i + di, self.j + dj

        if 0 <= new_i < self.maze.height and 0 <= new_j < self.maze.width:
            if not self.maze.get_cell(self.i, self.j).walls[self.orientation]:
                # Save the previous position before moving
                self.previous_positions.append((self.i, self.j))
                self.direction_history.append(self.orientation)
                
                # Move to the new position
                self.i, self.j = new_i, new_j
                self.steps += 1
                self.maze.get_cell(self.i, self.j).visited = True
                return True
        return False 

    
    def backtrack(self):
        """Return to the previous position"""
        if self.previous_positions:
            # Get the previous position
            prev_i, prev_j = self.previous_positions.pop()
            prev_direction = self.direction_history.pop()
            
            # Update current position
            self.i, self.j = prev_i, prev_j
            
            # Set orientation to the opposite of the previous direction
            # This helps the robot face the right way for backtracking
            self.orientation = DIR.OPPOSITE_DIRECTION[prev_direction]
            
            return True
        return False

    
