class CharacterMenu:
    def __init__(self, app):
        self.app = app

    def run(self):
        while True:
            print("\n--- Character Management ---")
            for i, c in enumerate(self.app.characters):
                print(f"{i+1}. {c.name}, {c.char_class}, {c.level}")
            print("a. Add Character | d. Delete | e. Edit | b. Back")
            
            choice = input(">> ").lower()
            if choice == 'b': break
            elif choice == 'a': self.add_character()
            elif choice == 'd': self.delete_character()
            elif choice == 'e': self.edit_character()

    def add_character(self):
        name = input("Enter new character name: ")
        char_class = input("Enter new character class: ")
        level = int(input("Enter new character level: "))
        if name:
            from models.character import Character
            new_character = Character(name, char_class, level)
            self.app.characters.append(new_character)
            print(f"Character '{name}' created!")

    def delete_character(self):
        idx_str = input("Enter the number of the character to delete: ")
        if idx_str.isdigit():
            idx = int(idx_str) - 1
            if 0 <= idx < len(self.app.character):
                removed = self.app.character.pop(idx)
                print(f"Deleted '{removed.name}'.")
            else:
                print("Invalid index.")

    def edit_character(self):
        idx_str = input("Enter the number of the character to edit: ")
        if idx_str.isdigit():
            idx = int(idx_str) - 1
            if 0 <= idx < len(self.app.characters):
                new_name = input("Enter new name: ")
                new_class = input("Enter new class: ")
                new_level = input("Enter new level: ")
                self.app.characters[idx].name = new_name
                self.app.characters[idx].char_class = new_class
                self.app.characters[idx].level = new_level
                print("Character updated.")