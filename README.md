# 🛡️ GuildQuest

GuildQuest is a text-based RPG management engine built in Python. It allows users to track game time across multiple Realms, manage Campaigns, and log Quest Events featuring a roster of custom characters.

## 🚀 Environment & Version

- **Language:** Python 3.10+
- **Dependencies:** None (Uses standard library only)

---

## 🕹️ How to Play / Provide Input

GuildQuest uses a **Command-Line Interface (CLI)**. When you run `main.py`, you will interact with the program through the following input types:

### 1. Menu Navigation

Menus are navigated using single-character keys followed by the **Enter** key.

- **Numbers (1-5):** Select primary menu categories or specific list items.
- **Letters:** \* `a` - Add
    - `d` - Delete
    - `e` - Edit
    - `b` - Back (Returns to the previous menu)

### 2. Creating Events & Realms

When prompted for data, follow these formatting rules:

- **Names/Titles:** Can include spaces (e.g., `The Dragon's Lair`).
- **Time:** Enter as a whole number representing total minutes (e.g., `1440` for Day 1).
- **Characters:** When adding participants to an event, enter names separated by a **single space** (e.g., `Aragorn Gandalf Gimli`).

---

## 📁 Project Structure

```text
guildquest/
├── main.py              # Application entry point & main loop
├── models/              # Entity models that follow the UML diagram
│   ├── campaign.py
│   ├── realm.py
│   └── character.py
│   └── clock.py
│   └── quest_event.py
│   └── user.py
└── views/               # Different views for the text-based UI
    ├── campaign_view.py
    ├── realm_view.py
    └── character_view.py
```
