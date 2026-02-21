from views.menu_view import MenuView

class RealmMenu(MenuView):
    def __init__(self, app):
        self.app = app

    def display_header(self):
        print("\n--- Realm Management ---")

    def display_items(self):
        for i, r in enumerate(self.app.realms):
            print(f"{i+1}. {r.name}, {r.description}")

    def display_options(self):
        print("a. Add Realm | d. Delete | e. Edit | b. Back")

    def handle_choice(self, choice: str) -> bool:
        if choice == 'a':
            self.add_realm()
            return True
        elif choice == 'd':
            self.delete_realm()
            return True
        elif choice == 'e':
            self.edit_realm()
            return True
        return False

    def add_realm(self):
        id = input("Enter new realm id: ")
        name = input("Enter new realm name: ")
        desc = input("Enter new realm description: ")
        if name:
            from models.realm import Realm
            new_realm = Realm(id, name, desc)
            self.app.realms.append(new_realm)
            print(f"Realm '{name}' created!")

    def delete_realm(self):
        idx_str = input("Enter the number of the Realm to delete: ")
        if idx_str.isdigit():
            idx = int(idx_str) - 1
            if 0 <= idx < len(self.app.realms):
                removed = self.app.realms.pop(idx)
                print(f"Deleted '{removed.name}'.")
            else:
                print("Invalid index.")

    def edit_realm(self):
        idx_str = input("Enter the number of the Realm to edit: ")
        if idx_str.isdigit():
            idx = int(idx_str) - 1
            if 0 <= idx < len(self.app.realms):
                new_id = input("Enter new realm id: ")
                new_name = input("Enter new realm name: ")
                new_desc = input("Enter new realm description: ")
                self.app.realms[idx].realm_id = new_id
                self.app.realms[idx].name = new_name
                self.app.realms[idx].description = new_desc
                print("Realm updated.")