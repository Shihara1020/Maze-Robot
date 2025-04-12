import pygame
import Constant as const
def show_instructions(screen):
    """Display instructions for the simulation"""
    font = pygame.font.SysFont('Arial', 16)
    instructions = [
        "Maze Robot Simulator",
        "",
        "Controls:",
        "SPACE - Pause/Resume",
        "UP ARROW - Speed up",
        "DOWN ARROW - Slow down",
        "ESC - Quit",
        "",
        "Press any key to continue..."
    ]
    
    screen.fill(const.BACKGROUND_COLOR)
    for i, line in enumerate(instructions):
        text = font.render(line, True, const.TEXT_COLOR)
        screen.blit(text, (50, 50 + i * 25))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False