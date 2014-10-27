class GameDefine:

    FPS = 60
    DOT_DIMENSION = 32

    # Window dimensions (in Dots)
    WINDOW_WIDTH = 31
    WINDOW_HEIGHT = 20

    # Command definitions
    COMMAND_EXIT = -3
    COMMAND_SIGNAL_LOST = -2
    COMMAND_SIGNAL_FOUND = -1
    COMMAND_NONE = 0
    COMMAND_LEFT = 1
    COMMAND_RIGHT = 2
    COMMAND_BOOST = 3
    COMMAND_UNBOOST = 4

    # Color definitions
    COLOR_TRAIL = (208, 208, 208)
    COLOR_DIVIDER = (32, 32, 32)
    COLOR_CONSOLE = (128, 128, 128)
    COLOR_FONT_TITLE = (255, 255, 255)
    COLOR_FONT_CONSOLE = (0, 0, 0)

    # General Purpose settings
    GAME_TITLE = "Steering Key"

    SPEED_COLORS = [
        (113, 186, 53),
        (135, 240, 49),
        (232, 240, 49),
        (247, 254, 34),
        (254, 34, 36)
    ]

    SCORE_DECIMAL = 100


def dotget(count, scale = 1.0):
    return int(count * GameDefine.DOT_DIMENSION * scale)
