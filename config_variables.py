import pygame as py
py.font.init()


#=================== General constants ==================================
FPS = 30
WIN_WIDTH = 1000
WIN_HEIGHT = 520
STARTING_POS = (WIN_WIDTH/2, WIN_HEIGHT-100)
SCORE_VEL_MULTIPLIER = 0.1                     #bonus for faster cars
BAD_GENOME_TRESHOLD = 200                       #if a car is too far behind it is removed

INPUT_NEURONS = 9
OUTPUT_NEURONS = 4

#=================== Car Specs ==================================

CAR_DBG = True             # Draw sensors
FRICTION  = -0.1
MAX_VEL = 10
MAX_VEL_REDUCTION = 1              #at the start reduce maximum speed
ACC_STRENGHT = 0.2
BRAKE_STREGHT = 1
TURN_VEL = 2
SENSOR_DISTANCE = 200
ACTIVATION_TRESHOLD = 0.5

#=================== Road Specs ==================================

ROAD_DBG = False
MAX_ANGLE = 1
MAX_DEVIATION = 130
SPACING = 240
NUM_POINTS  = 15                #number of points for each segment
SAFE_SPACE = SPACING + 50       #buffer space above the screen
ROAD_WIDTH = 200

#=================== Display and Colors ==================================

NODE_RADIUS = 12
NODE_SPACING = 5
LAYER_SPACING = 40
CONNECTION_WIDTH = 1

SELECTED_NEURON = (221, 86, 0)

WHITE = (255, 255, 255)
ORANGE = (255, 152, 87)
DARK_ORANGE_PALE = (253, 107, 14)
ORANGE_PALE = (255, 152, 87)
TEXT = (0, 0, 0)
GRAY = (255, 255, 255) # backgorund window
BLACK = (0, 0, 0)
RED = (200, 0, 0)
HIDEN = (40, 40, 40)
LINE_SENSOR_COLOR = (100, 100, 100)
DARK_RED = (100, 0, 0) # Red Node border
RED_PALE = (250, 200, 200)
DARK_RED_PALE = (150, 100, 100)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 100, 0) # Green Node border
GREEN_PALE = (200, 250, 200)
DARK_GREEN_PALE = (100, 150, 100)
BLUE = (0,0,255)
BLUE_PALE = (200, 200, 255)
DARK_BLUE = (100, 100, 150)

NODE_FONT = py.font.SysFont("comicsans", 20)
STAT_FONT = py.font.SysFont("comicsans", 20)


#=================== Constants for internal use ==================================
GEN = 0

#enumerations
ACC = 0
BRAKE = 1
TURN_LEFT = 2
TURN_RIGHT = 3

INPUT = 0
MIDDLE = 1
OUTPUT = 2
