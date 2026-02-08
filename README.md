⚔️ GuildQuest: Text-Based Game Engine
GuildQuest is a Python-based RPG management engine that allows you to track campaigns, quest events, and characters across multiple realms with unique time-dilation rules.

🛠 Prerequisites
Language: Python 3.10 or higher

Libraries: None (Uses standard Python libraries only)

🚀 How to Run
To start the game, navigate to the root directory (the folder containing main.py) and run the following command in your terminal:

Bash
python main.py
🎮 How to Provide Input
The game uses a Command Line Interface (CLI). Follow these rules for the best experience:

Menu Navigation: Use the keys indicated in the brackets (e.g., 1, 2, a, b) and press Enter.

Time Entry: When prompted for "World Clock" time, enter the value in total minutes (e.g., 1500 for Day 1, 01:00).

Character Lists: When adding characters to an event, type their names separated by a single space.

Example: Aragorn Legolas Gimli

Case Sensitivity: Realm names and Character names are case-sensitive. Ensure they match exactly how they were created.

📂 Project Structure
main.py: The entry point and main game loop.

engine/: Logic for the World Clock and core mechanics.

models/: Data definitions for Campaigns, Realms, and Characters.

views/: The terminal UI and menu logic.

💡 A Note on the "World Clock"
The internal engine tracks time as a single integer (Total Minutes).

1 Day = 1440 minutes.

1 Hour = 60 minutes.
