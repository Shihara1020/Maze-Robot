import pygame
import Robot
import Generate_random_maze as GR
import Graphic
import Algorithm
import Constant as const



def main():
    #initial setup
    pygame.init()
    width,height=10,10
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Maze robot simulator")

    #Generate the random maze
    maze=GR.genearte_simple_maze(width,height)
    robot=Robot.robot(maze)
    origin=Graphic.calculate_origin(screen,width,height)
    graphics=Graphic.GraphicEngine(screen,origin)


    solution=Algorithm.Solve(maze,robot,screen)
    solution_path=solution.maze_solve()
    print("solution path: ",solution_path)


    screen.fill(const.BACKGROUND_COLOR)
    graphics.draw_grid(maze)
    graphics.draw_robot(robot)
    graphics.draw_final_path(robot)
    pygame.display.flip()
    
    running=True


    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
if __name__=="__main__":
    main()