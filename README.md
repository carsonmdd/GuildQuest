# 🛡️ GuildQuest

GuildQuest is a text-based RPG management engine for tracking world time, managing campaigns, and logging quest events.

## 🚀 Getting Started
Launch the application from your terminal:
```bash
python main.py
```

## 🕹️ Controls & Navigation
Interact with menus by typing a character and pressing **Enter**:
- **Numbers:** Select menu categories or specific list items.
- **Action Letters:**
  - `a` - **Add**: Create a new entry.
  - `d` - **Delete**: Remove an entry.
  - `e` - **Edit**: Update an existing entry.
  - `b` - **Back**: Return to the previous menu.

## 📂 Features

### 1. World Clock & Time Advancement
The World Time is always visible at the top of the main menu.
- **Advance Time:** Select option `4` to fast-forward the world clock by a specific number of minutes.

### 2. Campaigns & Quest Events
Organize your adventures into Campaigns and populate them with Quest Events.
- **Quest Events:** When creating an event, you will provide:
  - **Title:** The name of the scene or quest.
  - **Realm:** The location (must match an existing Realm name).
  - **Times:** Start and end times in total minutes.
  - **Characters:** A space-separated list of names (e.g., `Aragorn Gandalf`).

### 3. Realms
Manage the different regions of your world.
- **Local Time:** Each realm can have a time offset (in minutes), allowing for different time zones relative to the World Clock.

### 4. Characters
Maintain a roster of heroes for your quests.
- **Details:** Track Name, Class, and Level for every character in your party.
