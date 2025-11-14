<div style="max-width:820px; margin:0 auto; padding:10px;">

# MemoryGame - Python Projekt
**Rebecca Lundberg** *- Programmering i Python - Jensen YH Malmö - 14 november 2025*

## Innehåll

- [Installation](#installation)
- [Om programmet](#om-programmet)
    - [Projektstruktur](#projektstruktur)
    - [Så kör du programmet](#så-kör-du-programmet)
    - [Tester för programmet](#tester-för-programmet)
- [Min process](#min-process)
    - [Avslutning](#avslutning)



## Installation
1. Öppna terminalen och navigera till projeketets rot-mapp .../MemoryGame/, skapa ett virtuell miljö: ```python -m venv .venv```
2. Aktivera den virtuella miljön: 
    - Windows - ```.venv\Scripts\activate```,  macOS/Linux - ```source .venv/bin/activate```
3. Installera nödvändiga paket: 
    - Windows - ```pip install -r requirements.txt```, macOS/Linux - ```pip3 install -r requirements.txt```


## Om programmet
Programmet är ett memoryspel som spelas i terminalen. Du kan välja att spela 1-4 spelare på spelbräden som innehåller 3, 6, 10 eller 15 par. Väljer man att avsluta ett pågående spel finns möjligheten att spara sitt spel, endast senaste sparade spelet finns tillgängligt att fortsätta. För spel med en spelare finns en topplista där topp 3 bästa resultaten (slutförda spel på minst antal försök) kvalificerar sig.


### Projektstruktur
```
MemoryGame/
├── data/
│   └── toplist.json            # Lagrar top 3 resultat som .JSON (skapas automatiskt)
│   └── saveGame.json           # Lagrar senaste sparade spelet som .JSON (skapas automatiskt)
├── src/
│   ├── main.py                 # Huvudapplikationen
│   ├── game/
│   │   └── card.py             # Kortklassen, hanterar ett korts egenskaper och status
│   │   └── exceptions.py       # Egna exceptions för spelet
│   │   └── gameBoard.py        # Spelbrädet, storlek och kort
│   │   └── memoryGame.py       # Spelet, kopplar ihop spelbräde och spelare
│   │   └── player.py           # Spelarklassen, hanterar spelarens egenskaper och poäng
│   ├── services/
│   │   └── file_service.py     # Läs/skriv till .json
├── data/
├── tests/
│   └── test_gameBoard.py       # Tester för klassen GameBoard
│   └── test_memoryGame.py      # Tester för klassen MemoryBoard
├── requirements.txt            # Projektets beroenden
├── README.md                   # Dokumentation
└── .gitignore                  # Ignorerade filer
```

### Så kör du programmet
1. Öppna terminalen och se till att du står i rot-mappen .../MemoryGame/. För att starta spelet kör:
    - Windows - ```python scr/main.py```,  macOS/Linux - ```python3 scr/main.py```
2. Programmet kommer starta i terminalen, klicka dig fram bland menyvalen och spela spelet!
    1. Nytt spel
        - Ange spelare
        - Storlek på bräde
        - SPELA OCH HA KUL!
    2. Ladda senaste spelet
        - Om ett spel finns sparat så kommer det plockas upp och du har möjlighet att fortsätta där man slutade.
    3. Visa topplistan
        - Visar topp 3 för varje nivå

### Tester för programmet
Programmet innehåller även testfiler skrivna med **pytest** för att kontrollera att funktionerna i klasserna fungerar som de ska. Öppna terminalen och se till att du står i projektets rot-mapp .../MemoryGame/, sen kör: ```pytest```

## Min process
1. När jag bestämt mig för att jag skapa ett memoryspel så tog jag hjälp av vår tidigare uppgift kring API:er för att klura på en mappstruktur. Jag försökte också bryta ner ett spel för att komma fram till hur uppbyggnaden kring klasser etc. skulle kunna se ut; vilka delar finns och vilkrn del ska ta hand om vilken information.

2. Eftersom klasserna inte ska hantera I/O så var jag i början av projektet lite förvirrad kring mitt val att ha en MemoryGame-klass (som skulle koppla ihop brädet med spelare). Det kändes som om att jag bara  anropade på en funktion som i sin tur anropade på en funktion i nästa klass. Efter att ha konsulterat med em programmerare och AI så bestämde jag mig för att fortsätta ha upplägget som jag tänkte från början, och efter hand blev känslan att MemoryGame inte längre var en onödig mellanhand.

3. Ett problem som uppstod var att terminalhistoriken syntes vilket gjorde det väldigt enkelt att klara ett spel, man bara kunde scrolla upp. Frågade Marcus som kom med tipset att testa importera 'os' och köra os.system('clear') i koden. Detta fungerade inte för mig på Windows då man har olika kommandon för att rensa. Googlade och hittade en lösning som ska kunna funka på alla.

4. När det gäller file_service tog jag hjälp av koden i API-uppgiften och denna del tyckte jag var den svåraste i projektet. Dels att lösa en dictionary med all nödvändig information kring det pågående spelet, där jag försökte lösa så det packas ihop i respektive. Men även hur man öppnadefilen och vart och hur man uppdaterar till det pågående spelet. 

5. Jag har försökt skriva Docstrings till mina funktioner i efterhand för att göra det enklare för någon annan att läsa koden, här har jag dock tagit hjälp av AI för att rätta grammatiken då jag inte är van vid att skriva på engelska.

### Avslutning
Projektet har varit kul! Hade en inledande plan att också bygga ett ui med **Streamlit** men eftersom allt oftast tar längre tid än vad man tänkt så har jag inte hunnit detta. När jag kände att spelet fungerade så har jag istället lagt extra tid på att gå igenom min kod och försöka hitta ställen att förbättra på. Bland annat flyttade jag metoden update_latest_game() i MemoryGame till modulnivå istället för i klassen vilket ledde till att jag kunde säkerhetsställa att man inte kunde skapa ett objekt av klassen utan att ha en lista av players. Även förbättringar i läsbarhet och hur och vad funktionerna returnerar etc.

</div>