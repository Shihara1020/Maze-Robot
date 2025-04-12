import pygame
import Robot
import Generate_random_maze as GR
import Graphic
import Algorithm
import Constant as const
import show_instruction as SI


def main():
    #initial setup
    pygame.init()
    width,height=15,15
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Maze robot simulator")
    
    #show instruction
    SI.show_instructions(screen)


    #Generate the random maze
    maze=GR.genearte_simple_maze(width,height)
    robot=Robot.robot(maze)
    origin=Graphic.calculate_origin(screen,width,height)
    graphics=Graphic.GraphicEngine(screen,origin)

    #solve the maze
    solution=Algorithm.Solve(maze,robot,screen)
    solution_path=solution.maze_solve()
    print("solution path: ",solution_path)

    #display the final solution
    screen.fill(const.BACKGROUND_COLOR)
    graphics.draw_grid(maze)
    graphics.draw_robot(robot)
    graphics.draw_final_path(robot)
    

    #add some information text
    font = pygame.font.SysFont('Arial', 16)
    text = font.render(f"Path length: {len(solution_path)} steps", True, const.TEXT_COLOR)
    screen.blit(text, (10, 10))
    text = font.render("Press ESC to quit", True, const.TEXT_COLOR)
    screen.blit(text, (10, 30))
    
    pygame.display.flip()

    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
    pygame.quit()
if __name__=="__main__":
    main()