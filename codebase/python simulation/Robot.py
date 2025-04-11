import Direction as DIR

class robot:
    def __init__(self,maze):
        self.maze=maze
        self.i,self.j=maze.start
        self.orientation=DIR.direction.EAST  #mark the front of the robot
        self.path=[]
        self.maze.get_cell(self.i,self.j).visited=True
        self.previoscellX,self.previouscellY=maze.start
   
    def move_forward(self):
        di,dj=DIR.PIXEL_SPACE_DIRECTION_MAP[self.orientation]
        newi,newj=self.i+di,self.j+dj
        self.i,self.j=newi,newj

    def turn_left(self):
        self.orientation = {
            DIR.direction.NORTH: DIR.direction.WEST,
            DIR.direction.WEST: DIR.direction.SOUTH,
            DIR.direction.SOUTH: DIR.direction.EAST,
            DIR.direction.EAST: DIR.direction.NORTH
        }[self.orientation]

    def turn_right(self):
        self.orientation = {
            DIR.direction.NORTH: DIR.direction.WEST,
            DIR.direction.WEST: DIR.direction.SOUTH,
            DIR.direction.SOUTH: DIR.direction.EAST,
            DIR.direction.EAST: DIR.direction.NORTH
        }[self.orientation]

    def move_back(self):
        if self.previoscellX==1 and self.previouscellY==0:
            self.orientation=DIR.direction.WEST
        elif self.previoscellX==-1 and self.previouscellY==0:
            self.orientation=DIR.direction.EAST
        elif self.previoscellX==0 and self.previouscellY==1:
            self.orientation=DIR.direction.NORTH
        elif self.previoscellX==0 and self.previouscellY==-1:
            self.orientation=DIR.direction.SOUTH
        self.move_forward()

    
