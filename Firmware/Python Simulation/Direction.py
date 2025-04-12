from enum import Enum
class direction(Enum):
    WEST=0
    EAST=1
    SOUTH=2
    NORTH=3

PIXEL_SPACE_DIRECTION_MAP={
    direction.SOUTH:(1,0),
    direction.NORTH:(-1,0),
    direction.EAST:(0,1),
    direction.WEST:(0,-1),
}

# Opposite directions for backtracking
OPPOSITE_DIRECTION = {
    direction.NORTH: direction.SOUTH,
    direction.SOUTH: direction.NORTH,
    direction.EAST: direction.WEST,
    direction.WEST: direction.EAST
}
