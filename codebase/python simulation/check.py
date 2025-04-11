import Direction as DIR
import Robot


def can_move(robot: Robot.robot, direction: DIR.direction) -> bool:
    di, dj = DIR.PIXEL_SPACE_DIRECTION_MAP[direction]
    ni, nj = robot.i + di, robot.j + dj
    if not (0 <= ni < robot.maze.height and 0 <= nj < robot.maze.width):
        return False
    if robot.maze.get_cell(robot.i, robot.j).walls[direction]:
        return False
    if robot.maze.get_cell(ni, nj).visited:
        return False
    return True