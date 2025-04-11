import pygame 
import Constant as const
import Grid 
import Direction as DIR
import Robot

def index_to_pixel(origin, i, j):
    x0, y0 = origin
    return (x0 + j * const.CELL_SIZE, y0 + i * const.CELL_SIZE)

def calculate_origin(screen, grid_width, grid_height=None):
    if grid_height is None:
        grid_height = grid_width
    return(
        (screen.get_width() - grid_width * const.CELL_SIZE) // 2,
        (screen.get_height() - grid_height * const.CELL_SIZE) // 2
    )


class GraphicEngine:
    def __init__(self,screen,origin):
        self.screen=screen
        self.origin=origin
        self.font=pygame.font.SysFont('Arial',16)

    def draw_cell(self,corner_pos,cell:Grid.MazeCell):
        cell_color=const.VISITED_CELL_COLOR if cell.visited else const.UNVISITED_CELL_COLOR
        if cell.on_path:
            cell_color=const.PATH_COLOR
        pygame.draw.rect(self.screen,cell_color,(*corner_pos,const.CELL_SIZE,const.CELL_SIZE))
        pygame.draw.rect(self.screen,const.WEAK_BORDER,(*corner_pos,const.CELL_SIZE,const.CELL_SIZE),const.BORDER_THICKNESS)
        
    def draw_walls(self,corner_pos,cell:Grid.MazeCell):
        x,y=corner_pos
        if cell.walls[DIR.direction.NORTH]:
            #(window,color,starting point of line,ending point of line,thickness)
            pygame.draw.line(self.screen, const.THICK_BORDER, (x, y), (x + const.CELL_SIZE, y), const.WALL_THICKNESS)
        if cell.walls[DIR.direction.SOUTH]:
            pygame.draw.line(self.screen, const.THICK_BORDER, (x, y + const.CELL_SIZE), (x + const.CELL_SIZE, y + const.CELL_SIZE), const.WALL_THICKNESS)
        if cell.walls[DIR.direction.EAST]:
            pygame.draw.line(self.screen, const.THICK_BORDER, (x + const.CELL_SIZE, y), (x + const.CELL_SIZE, y + const.CELL_SIZE), const.WALL_THICKNESS)
        if cell.walls[DIR.direction.WEST]:
            pygame.draw.line(self.screen, const.THICK_BORDER, (x, y), (x, y + const.CELL_SIZE), const.WALL_THICKNESS)


    def draw_grid(self,grid:Grid.MazeGrid):
        for i in range(grid.height):
            for j in range(grid.width):
                pos=index_to_pixel(self.origin,i,j)
                cell=grid.get_cell(i,j)
                self.draw_cell(pos,cell)
                self.draw_walls(pos,cell)

    def draw_robot(self,robot:Robot.robot):
        pos=index_to_pixel(self.origin,robot.i,robot.j)
        center=(pos[0]+const.CELL_SIZE//2,pos[1]+const.CELL_SIZE//3)
        pygame.draw.circle(self.screen,const.ROBOT_COLOR,center,const.CELL_SIZE//3)
        di,dj=DIR.PIXEL_SPACE_DIRECTION_MAP[robot.orientation]
        end=(center[0]+dj*const.CELL_SIZE//2,center[1]+di*const.CELL_SIZE//2)
        pygame.draw.line(self.screen,(0,0,0),center,end,2)

    def draw_final_path(self,robot:Robot.robot):
        for x,y in robot.path:
            pos=index_to_pixel(self.origin,x,y)
            center=(pos[0]+const.CELL_SIZE//2,pos[1]+const.CELL_SIZE//3)
            pygame.draw.circle(self.screen,const.FINAL_PATH_COLOUR,center,const.CELL_SIZE//5)






