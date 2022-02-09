# Resources and constants

# Screen Constraints
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Strings
TITLE = 'Shooting Jet Game'

# Config
JET_CENTER = (SCREEN_WIDTH // 2, int(0.85 * SCREEN_HEIGHT))
JET_SCALE = (80, 80)
SHOT_SCALE = (20, 20)
ENEMY_SCALE = (80, 80)

# Colors
DARK = (20, 20, 20)
LIGHT = (200, 200, 200)

# Images
JET_IMG = 'jet.png'
SHOT_IMG = 'shot.png'
ENEMY_IMG = 'enemy.png'

# Constraints
DX_JET = 5
DY_JET = 5
DY_SHOT = 3
DY_ENEMY = 2
ALLOWED_JET_ENEMY_OVERLAP = 30
MIN_GEN_ENEMIES = 0
MIN_ENSURE_ENEMIES = 2
MAX_GEN_ENEMIES = 5