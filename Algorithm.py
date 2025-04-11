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

    def maze_solve(self):
        stack : list[tuple[int,int]] =list()
        #start position
        x,y=self.maze.start

        #Add the stack
        stack.append((x,y))

        #end position
        endX,endY=self.maze.end

        #form the BFS algorithm
        while stack:
            #get tha last node in stack
            x,y= stack[-1]

            #IF break the function the reach the destination
            if endX==x and endY==y:
                break
        
            #mark the cell has visited
            self.maze.get_cell(x,y).visited=True
            backtrac=True

            for dir in list(DIR.direction):
                dx,dy=DIR.PIXEL_SPACE_DIRECTION_MAP[dir]
                nx,ny=x+dx,y+dy

                if check.can_move(self.robot,dir):
                    self.robot.orientation=dir
                    self.robot.move_forward()
                    stack.append((self.robot.i,self.robot.j))
                    backtrac=False
                    break
            if backtrac is True:
                #Remove blocking cell in the stack
                stack.pop()
                if stack:
                    self.robot.i,self.robot.j=stack[-1]

            self.screen.fill(const.BACKGROUND_COLOR)
            ge = Graphic.GraphicEngine(self.screen, Graphic.calculate_origin(self.screen, self.maze.width, self.maze.height))
            ge.draw_grid(self.maze)
            ge.draw_robot(self.robot)
            pygame.display.flip()
            pygame.time.delay(50)
        
        self.robot.path=stack

        return self.get_path()
    
    def get_path(self):
        #self.remove_ghost_path()

        return self.robot.path
    
    def remove_ghost_path(self):
        remove:list=list()
        
        for i in range(1,len(self.robot.path)):
            x=self.robot.path[i][0]
            y=self.robot.path[i][1]

            count:int =0
            neighbor: list[str]=DIR.direction

            for dir in neighbor:
                dx,dy=DIR.PIXEL_SPACE_DIRECTION_MAP[dir]
                x+=dx
                y+=dy
                if (x,y) not in self.robot.path:
                    count+1

            
            if self.maze.grid[x][y].connectedCell-count:
                remove.append(i)

        for i in remove[::-1]:
            remove.pop(i)

        endX: int=self.maze.end[0]
        endY: int=self.maze.end[1]
        if(endX,endY) not in self.robot.path:
            self.robot.path.append((endX,endY))