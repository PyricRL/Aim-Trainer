Aim Trainer/
├── main.py         # Entry Point
├── gui.py          # Display all graphics
├── tracker.py      # Game Logic
├── stats.py        # Accuracy Calculations
├── targets.py      # Target Spawning
└── style.qss       # Custom Theme

main.py
    handle open and closing of window

gui.py
    display all gui elements
    allow for switching between screens/gamemodes

tracker.py
    handles logic:
        targets clicked
        time ticking
        compare scores/leaderboard

stats.py
    calculates stats
        time for whole game

target.py
    basic target class

gamemodes/
    grid.py
        spawn within a center grid
    random.py
        spawn randomly all throughout the screen

style.qss
    styling for everything