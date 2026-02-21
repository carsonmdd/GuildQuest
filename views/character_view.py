from views.menu_view import MenuView

class CharacterMenu(MenuView):
    def __init__(self, facade):
        self.facade = facade

    def display_header(self):
        print("\n--- Character Management ---")

    def display_items(self):
        characters = self.facade.get_characters()
        for i, c in enumerate(characters):
            print(f"{i+1}. {c.name}, {c.char_class}, {c.level}")

    def display_options(self):
        print("a. Add Character | d. Delete | e. Edit | b. Back")

    def handle_choice(self, choice: str) -> bool:
        if choice == 'a':
            self.add_character()
            return True
        elif choice == 'd':
            self.delete_character()
            return True
        elif choice == 'e':
            self.edit_character()
            return True
        return False

    def add_character(self):
        name = input("Enter new character name: ")
        char_class = input("Enter new character class: ")
        
        try:
            level = int(input("Enter new character level: "))
        except ValueError:
            print("Level must be a number.")
            return

        self.facade.add_character(name, char_class, level)
        print(f"Character '{name}' created!")

    def delete_character(self):
        idx_str = input("Enter the number of the character to delete: ")
        if not idx_str.isdigit():
            print("Invalid input.")
            return

        idx = int(idx_str) - 1
        characters = self.facade.get_characters()
        if 0 <= idx < len(characters):
            removed = characters.pop(idx)
            print(f"Deleted '{removed.name}'.")
        else:
            print("Invalid index.")

    def edit_character(self):
        idx_str = input("Enter the number of the character to edit: ")
        if not idx_str.isdigit():
            print("Invalid input.")
            return

        idx = int(idx_str) - 1
        characters = self.facade.get_characters()
        if not (0 <= idx < len(characters)):
            print("Invalid index.")
            return

        new_name = input("Enter new name: ")
        new_class = input("Enter new class: ")
        new_level = input("Enter new level: ")
        
        characters[idx].name = new_name
        characters[idx].char_class = new_class
        characters[idx].level = new_level
        print("Character updated.")