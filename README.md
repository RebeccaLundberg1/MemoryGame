1. Skapa ett virtual envirment 
2. pip install requiremnts 


## 📁 Projektstruktur

```
MemoryGame/
├── src/
│   ├── main.py                 # Huvudapplikationen
│   ├── game/
│   │   └── card.py             #
│   │   └── memory_game.py
│   │   └── player.py
│   │   └── game_board.py
│   ├── ui/
│   │   └── .py                 # 
│   ├── services/
│   │   └── file_service.py     # Läs/skriv till .json
│   └── data/
│       └── db.json             # Databasfil (skapas automatiskt)
├── tests/
│   └── .py                     # Tester
├── requirements.txt            # Projektets beroenden
├── README.md                   # Dokumentation
└── .gitignore                  # Ignorerade filer

```



Card
    id
    image
    is_flipped
    is_matched

Game_board 
    size 
    cards 

Player
    id
    topscore {2x3, 3x4, 4x4, 4x5}

Memory_game
    player
    game_board
    number_of_flips