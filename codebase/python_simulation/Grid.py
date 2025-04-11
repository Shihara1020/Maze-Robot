import Direction as DIR

#for each cell contain the four wall south,east,north and west
#creat the variable to track the robot is visted or not
class MazeCell:
    def __init__(self):
        self.walls={d:True for d in DIR.direction}
        self.visited=False
        self.connectedCell=0
        self.on_path=False


#Maze 
class MazeGrid:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.grid=[[MazeCell() for _ in range(width)] for _ in range(height)]
        self.start=(0,0)
        self.end=(height-1,width-1)
    
    #remove the wall from (i1,j1) cell to (i2,j2) cell
    def remove_wall(self,i1,j1,i2,j2):
        self.grid[i1][j1].connectedCell+=1
        self.grid[i2][j2].connectedCell+=1

        if i1==i2:
            if j1+1==j2:
                self.grid[i1][j1].walls[DIR.direction.EAST]=False
                self.grid[i2][j2].walls[DIR.direction.WEST]=False
            elif j1-1==j2:
                self.grid[i1][j1].walls[DIR.direction.WEST]=False
                self.grid[i2][j2].walls[DIR.direction.EAST]=False
        elif j1==j2:
            if i1+1==i2:
                self.grid[i1][j1].walls[DIR.direction.SOUTH]=False
                self.grid[i2][j2].walls[DIR.direction.NORTH]=False
            elif i1-1==i2:
                self.grid[i1][j1].walls[DIR.direction.NORTH]=False
                self.grid[i2][j2].walls[DIR.direction.SOUTH]=False        
    
    def get_cell(self,i,j):
        return self.grid[i][j]