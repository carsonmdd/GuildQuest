from views.menu_view import MenuView

class RealmMenu(MenuView):
    def __init__(self, facade):
        self.facade = facade

    def display_header(self):
        print("\n--- Realm Management ---")

    def display_items(self):
        realms = self.facade.get_realms()
        for i, r in enumerate(realms):
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
        realm_id = input("Enter new realm id: ")
        name = input("Enter new realm name: ")
        desc = input("Enter new realm description: ")
        if name:
            self.facade.add_realm(realm_id, name, desc)
            print(f"Realm '{name}' created!")

    def delete_realm(self):
        idx_str = input("Enter the number of the Realm to delete: ")
        if not idx_str.isdigit():
            print("Invalid input.")
            return

        idx = int(idx_str) - 1
        realms = self.facade.get_realms()
        if 0 <= idx < len(realms):
            removed = realms.pop(idx)
            print(f"Deleted '{removed.name}'.")
        else:
            print("Invalid index.")

    def edit_realm(self):
        idx_str = input("Enter the number of the Realm to edit: ")
        if not idx_str.isdigit():
            print("Invalid input.")
            return

        idx = int(idx_str) - 1
        realms = self.facade.get_realms()
        if not (0 <= idx < len(realms)):
            print("Invalid index.")
            return

        new_id = input("Enter new realm id: ")
        new_name = input("Enter new realm name: ")
        new_desc = input("Enter new realm description: ")
        
        realms[idx].realm_id = new_id
        realms[idx].name = new_name
        realms[idx].description = new_desc
        print("Realm updated.")