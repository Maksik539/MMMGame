import os

# ===== ЭКРАН И ИГРА =====
# Виртуальные размеры (базовые)
VIRTUAL_WIDTH = 1024
VIRTUAL_HEIGHT = 768
SCALE = 1  # Масштаб (1x = 1024×768, 2x = 2048×1536)

FULLSCREEN = True
SCREEN_WIDTH = VIRTUAL_WIDTH * SCALE
SCREEN_HEIGHT = VIRTUAL_HEIGHT * SCALE

# ===== РЕДАКТОР УРОВНЕЙ =====
EDITOR_WIDTH = 1680
EDITOR_HEIGHT = 900
EDITOR_FULLSCREEN = False
EDITOR_FONT_SIZE = 12

# ===== РАЗМЕРЫ СПРАЙТОВ И ТАЙЛОВ =====
SPRITE_SIZE = 16
TILE_SIZE = 16
FPS = 60

# ===== РАЗМЕРЫ КОМНАТ =====
MAX_ROOM_WIDTH = 64      # тайлы
MAX_ROOM_HEIGHT = 48     # тайлы
MIN_ROOM_WIDTH = 16      # тайлы
MIN_ROOM_HEIGHT = 12     # тайлы
MAX_ROOMS = 7            # максимум комнат в уровне

# ===== РАЗМЕРЫ КНОПОК МЕНЮ =====
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_MARGIN = 20

# ===== ЦВЕТА =====
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (40, 40, 40)
LIGHT_GRAY = (200, 200, 200)
DARK_BLUE = (20, 30, 60)

# ===== ПУТИ К АССЕТАМ =====
BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
SPRITES_DIR = os.path.join(ASSETS_DIR, 'sprites')
PLAYER_SPRITES_DIR = os.path.join(SPRITES_DIR, 'player')
ENEMIES_SPRITES_DIR = os.path.join(SPRITES_DIR, 'enemies')
TILES_DIR = os.path.join(ASSETS_DIR, 'tiles')
# Tilesets находятся в src/tilesets
TILESETS_DIR = os.path.join(BASE_DIR, 'src', 'tilesets')
LEVELS_DIR = os.path.join(BASE_DIR, 'levels')

# Создаём директории если их нет
for directory in [ASSETS_DIR, SPRITES_DIR, TILES_DIR, LEVELS_DIR]:
    os.makedirs(directory, exist_ok=True)

# ===== ДИНАМИЧЕСКАЯ РЕГИСТРАЦИЯ ТЕКСТУР =====
TILESET_CATEGORIES = {
    "terrain": "Terrain",
    "objects": "Objects",
    "enemies": "Enemies",
    "decorations": "Decorations",
    "rooms": "Rooms",
    "other": "Other"
}

# Известные текстуры (для обратной совместимости)
KNOWN_TILESETS = {
    "tileset": {"category": "terrain", "description": "Main tileset"},
    "objects": {"category": "objects", "description": "Interactive objects"},
    "walls": {"category": "terrain", "description": "Wall tiles"},
    "floors": {"category": "terrain", "description": "Floor variants"},
    "enemies_objects": {"category": "enemies", "description": "Enemies and objects"},
    "patterns": {"category": "decorations", "description": "Patterns and textures"},
    "rooms": {"category": "rooms", "description": "Ready-made rooms"},
    "rooms_tileset": {"category": "rooms", "description": "Room main tileset"}
}

# ===== ОБЪЕКТЫ И ВРАГИ =====
OBJECT_TYPES = {
    "static": "Static (no interaction)",
    "interactive": "Interactive (can use)",
    "trap": "Trap (damage)"
}

INTERACTIVE_SUBTYPES = {
    "chest": "Chest",
    "door": "Door",
    "box": "Box",
    "lever": "Lever"
}

TRAP_SUBTYPES = {
    "spikes": "Spikes",
    "fire": "Fire",
    "ice": "Ice",
    "water": "Water"
}

ENEMY_TYPES = ["skeleton", "fire_sphere", "tornado"]

# ===== РЕДАКТОР ПАРАМЕТРЫ =====
EDITOR_GRID_COLOR = (100, 100, 100)
EDITOR_GRID_ALPHA = 50
EDITOR_SELECTION_COLOR = (0, 255, 0)
EDITOR_MINIMAP_CELL_SIZE = 30

# ===== ИСТОРИЯ (UNDO/REDO) =====
MAX_HISTORY_STEPS = 100

# Спавн игрока
PLAYER_SPAWN_COLOR = (0, 255, 0)
PLAYER_SPAWN_RADIUS = 8

# ============================================================
# LEVEL PASSAGES (Проходы между уровнями)
# ============================================================

PASSAGE_TYPES = {
    "door": {
        "name": "Дверь",
        "color": (200, 100, 50),
        "symbol": "🚪"
    },
    "stairs": {
        "name": "Лестница",
        "color": (150, 150, 150),
        "symbol": "🪜"
    },
    "portal": {
        "name": "Портал",
        "color": (200, 50, 200),
        "symbol": "🌀"
    },
    "edge": {
        "name": "Край карты",
        "color": (100, 100, 200),
        "symbol": "→"
    }
}

PASSAGE_DIRECTIONS = ["up", "down", "left", "right"]