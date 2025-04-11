import Grid
import Direction as DIR
import random

def genearte_simple_maze(width,height)->Grid.MazeGrid:
    maze=Grid.MazeGrid(width,height)
    def dfs(i,j,visited):
        visited.add((i,j))
        directions=list(DIR.direction)
        random.shuffle(directions)

        for dir in directions:
            di,dj=DIR.PIXEL_SPACE_DIRECTION_MAP[dir]
            newi,newj=i+di,j+dj
            if 0<=newi<height and 0<=newj<width and (newi,newj) not in visited:
                maze.remove_wall(i,j,newi,newj)
                dfs(newi,newj,visited)        
    dfs(0,0,set())
    for i in range(height):
        for j in range(width):
            maze.get_cell(i, j).visited = False  # Start clean
    return maze