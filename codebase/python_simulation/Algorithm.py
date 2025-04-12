import Direction as DIR
import check
import Constant as const
import Graphic
import pygame

class Solve:
    def __init__(self,maze,robot,screen):
        self.maze=maze
        self.robot=robot
        self.screen=screen
        self.delay_speed = const.DELAY_SPEED
        self.paused = False
    def update_display(self):
        """Update the display with current maze and robot state"""
        self.screen.fill(const.BACKGROUND_COLOR)
        ge = Graphic.GraphicEngine(self.screen, Graphic.calculate_origin(self.screen, self.maze.width, self.maze.height))
        ge.draw_grid(self.maze)
        ge.draw_robot(self.robot)
        
        # Display information
        font = pygame.font.SysFont('Arial', 16)
        steps_text = font.render(f"Steps: {self.robot.steps}", True, const.TEXT_COLOR)
        self.screen.blit(steps_text, (10, 10))
        
        pygame.display.flip()
        
        # Handle events during solving
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_UP:
                    self.delay_speed = max(1, self.delay_speed // 2)
                elif event.key == pygame.K_DOWN:
                    self.delay_speed = min(500, self.delay_speed * 2)
        
        # If paused, wait for space to be pressed again
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.paused = False
            pygame.time.delay(100)
        
        pygame.time.delay(self.delay_speed)


    def maze_solve(self):
        stack : list[tuple[int,int]] =list()
        #start position
        x,y=self.maze.start

        endX,endY=self.maze.end

        #Add the stack
        stack.append((x,y))

        self.robot.path = [(x, y)]  # Start with the initial position

        

        #form the BFS algorithm
        while stack:
            #get tha last node in stack
            x,y= stack[-1]

            # Mark current cell as on path
            self.maze.get_cell(x, y).on_path = True

            #IF break the function the reach the destination
            if endX==x and endY==y:
                break
        
            #mark the cell has visited
            self.maze.get_cell(x,y).visited=True
            

            # Try to move in a direction
            moved = False

            for dir in list(DIR.direction):
                # Check if movement is possible in this direction
                if check.can_move(self.robot, dir):
                    # Set orientation before moving
                    self.robot.orientation = dir
                    # Move the robot
                    if self.robot.move_forward():
                        stack.append((self.robot.i, self.robot.j))
                        self.robot.path.append((self.robot.i, self.robot.j))
                        moved = True
                        break
            
            # If no move is possible, backtrack
            if not moved:
                #Remove blocking cell in the stack
                stack.pop()
                if stack:
                    # Using our improved backtracking method
                    self.robot.backtrack()
                    # Mark last position as not on path anymore
                    last_pos = self.robot.path.pop()
                    self.maze.get_cell(last_pos[0], last_pos[1]).on_path = False

            self.update_display()
        
        # Ensure the end is included in the path
        if (endX, endY) not in self.robot.path:
            self.robot.path.append((endX, endY))
        
        # Optimize path
        self.optimize_path()
        
        return self.robot.path
    
    def optimize_path(self):
        """Remove unnecessary steps from the path (dead ends)"""
        # Mark the final path
        for i, j in self.robot.path:
            self.maze.get_cell(i, j).on_path = True
        
        # Update the display one more time to show the complete path
        self.update_display()
        return self.robot.path