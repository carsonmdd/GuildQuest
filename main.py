from models.game_facade import GameFacade
from views.campaign_view import CampaignMenu
from views.character_view import CharacterMenu
from views.realm_view import RealmMenu

class GuildQuestApp:
    def __init__(self):
        self.facade = GameFacade(user_id=1)
        self.running = True

    def display_menu(self):
        print(f"\n--- GuildQuest | World Time: {self.facade.get_world_time_str()} ---")
        print("1. Manage Campaigns & Events")
        print("2. Manage Realms")
        print("3. Manage Characters")
        print("4. Advance Time")
        print("5. Exit")

    def run(self):
        print("Welcome to GuildQuest!")
        while self.running:
            self.display_menu()
            choice = input("\nSelect an option: ")
            self.handle_input(choice)

    def handle_input(self, choice):
        if choice == "1":
            CampaignMenu(self.facade).run()
        elif choice == "2":
            RealmMenu(self.facade).run()
        elif choice == "3":
            CharacterMenu(self.facade).run()
        elif choice == "4":
            try:
                minutes = int(input("How many minutes to advance? "))
                self.facade.advance_time(minutes)
            except ValueError:
                print("Please enter a valid number of minutes.")
        elif choice == "5":
            self.running = False
        else:
            print("Invalid command.")

if __name__ == "__main__":
    app = GuildQuestApp()
    app.run()