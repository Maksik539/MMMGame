# Mage Quest

A procedurally generated dungeon crawler game built with Pygame.

## Description

Mage Quest is a top-down action game where you play as a mage fighting through procedurally generated dungeons filled with enemies. The game features:

- **Dynamic Combat**: Cast projectiles to defeat various enemy types
- **Procedural Generation**: Each playthrough offers unique dungeon layouts
- **Multiple Enemy Types**: 
  - Skeletons (melee enemies that chase the player)
  - Fire Spheres (ranged enemies that maintain distance and shoot fireballs)
  - Tornados (fast-moving enemies with erratic movement patterns)
- **Level Editor**: Create and edit custom levels with an intuitive visual editor

## Project Structure

```
MMMGame/
├── main.py                 # Game entry point
├── config.py               # Game configuration and settings
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── src/                   # Source code
│   ├── __init__.py
│   ├── core/              # Core game logic
│   │   ├── __init__.py
│   │   ├── game.py        # Main game loop
│   │   ├── player.py      # Player character and controls
│   │   ├── enemies.py     # Enemy classes and AI
│   │   └── projectiles.py # Projectile system
│   ├── graphics/          # Graphics and rendering
│   │   ├── __init__.py
│   │   ├── animation.py   # Animation system
│   │   ├── procedural_sprites.py  # Procedural sprite generation
│   │   └── asset_coordinator.py   # Asset management
│   ├── world/             # World and level systems
│   │   ├── __init__.py
│   │   └── tilemap.py     # Tilemap and level building
│   ├── ui/                # User interface
│   │   ├── __init__.py
│   │   └── menu.py        # Main menu
│   └── editor/            # Level editor
│       ├── __init__.py
│       ├── launcher.py              # Editor launcher
│       ├── level_editor.py          # Main editor
│       ├── room_editor.py           # Room editing
│       ├── texture_loader.py        # Texture loading
│       ├── texture_panel.py         # Texture selection panel
│       ├── animation_loader.py      # Animation loading
│       ├── animation_panel.py       # Animation selection panel
│       ├── animation_creator.py     # Animation creation utility
│       ├── properties_panel.py      # Object properties panel
│       ├── tabs_panel.py            # Tab management
│       ├── minimap_panel.py         # Level minimap
│       ├── connections_panel.py     # Room connections
│       ├── passages_panel.py        # Level transitions
│       ├── level_utils.py           # Level utilities
│       ├── undo_redo.py             # Undo/redo system
│       └── resizable_panel.py       # Base panel class
├── assets/                # Game assets
│   ├── sprites/           # Sprite images
│   │   └── .gitkeep
│   └── tilesets/          # Tileset images
│       └── .gitkeep
└── levels/                # Level files
    └── .gitkeep
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Maksik539/MMMGame.git
   cd MMMGame
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Required packages:
   - pygame-ce 2.5.1
   - numpy 2.1.0

## How to Play

### Running the Game

```bash
python main.py
```

### Controls

- **Movement**: WASD or Arrow Keys
- **Shoot**: Left Mouse Button (shoots towards cursor)
- **Pause/Quit**: ESC

### Objective

Survive as long as possible by defeating waves of enemies. Your health is displayed in the top-left corner. Avoid enemy contact and their projectiles while eliminating them with your own magic projectiles.

## Level Editor

### Launching the Editor

From the main menu, select "Level Editor", or run it directly:

```bash
python -m src.editor.launcher
```

### Editor Controls

- **Ctrl+S**: Save level
- **Ctrl+O**: Load level
- **Ctrl+Z**: Undo
- **Ctrl+Y**: Redo
- **ESC**: Exit editor

### Editor Features

1. **Texture Panel**: Select tiles to paint in the level
2. **Animation Panel**: Manage entity animations
3. **Properties Panel**: Edit object properties
4. **Minimap**: Overview of the entire level
5. **Connections Panel**: Link rooms together
6. **Passages Panel**: Create transitions between levels

### Creating a Level

1. Select a texture from the Texture Panel
2. Click and drag in the editor area to paint tiles
3. Use the various panels to add entities, connections, and properties
4. Save your level with Ctrl+S

## Development

### Adding New Enemies

1. Create a new enemy class in `src/core/enemies.py` inheriting from `Enemy`
2. Implement the `update()` method with custom AI behavior
3. Add the enemy type to `EnemyManager.enemy_types`
4. Create a sprite in `src/graphics/procedural_sprites.py`

### Adding New Tiles

1. Add tile generation in `ProceduralSpriteGenerator.generate_tile_sprite()`
2. Update the texture list in `TexturePanel`
3. Add tile handling in `TileMap`

### Customizing Game Settings

Edit `config.py` to modify:
- Screen resolution
- Player stats (health, speed, damage)
- Enemy stats and behavior
- Spawn rates
- Colors and visual settings

## Asset System

The game uses a hybrid asset system:

1. **Procedural Generation**: Default sprites and tiles are generated algorithmically
2. **File Loading**: Custom assets can be placed in `assets/sprites/` and `assets/tilesets/`
3. **AssetCoordinator**: Automatically falls back to procedural generation if files are missing

This allows the game to run without any external assets while supporting custom graphics.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available for educational and personal use.

## Credits

Developed using:
- Pygame Community Edition (pygame-ce)
- NumPy

---

Enjoy playing and creating levels in Mage Quest!