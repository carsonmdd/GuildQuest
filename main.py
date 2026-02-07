from models.clock import WorldClock
from models.campaign import Campaign
from models.realm import Realm
from views.campaign_view import CampaignMenu
from views.character_view import CharacterMenu
from views.realm_view import RealmMenu
from models.user import User
from models.character import Character

class GuildQuestApp:
    def __init__(self):
        self.clock = WorldClock()
        self.user = User(1)
        self.realms = {}
        self.running = True

    def display_menu(self):
        print(f"\n--- GuildQuest | World Time: {self.clock.format_time()} ---")
        print("1. Manage Campaigns & Events")
        print("2. Manage Realms")
        print("3. Manage Characters")
        print("4. Advance Time")
        print("5. Exit")

    def run(self):
        print("Welcome to GuildQuest!")
        self.seed_initial_data() 

        while self.running:
            self.display_menu()
            choice = input("\nSelect an option: ")
            self.handle_input(choice)

    def handle_input(self, choice):
        if choice == "1":
            CampaignMenu(self.user, self.realms, self.clock).run()
        elif choice == "2":
            RealmMenu(self.user).run()
        elif choice == "3":
            CharacterMenu(self.user).run()
        elif choice == "4":
            hours = int(input("How many hours to advance? "))
            self.clock.advance(hours * 60)
        elif choice == "5":
            self.running = False
        else:
            print("Invalid command.")

    def seed_initial_data(self):
        # Quick setup so the game isn't empty on launch
        tutorial_realm = Realm(realm_id='R1', name="Sky Haven", local_time_offset=1440)
        self.realms["R1"] = tutorial_realm
        
        starter_campaign = Campaign(name="The First Journey")
        self.user.campaigns.append(starter_campaign)

        starting_character = Character('Harold', 'Archer', 15)
        self.user.characters.append(starting_character)
        print("System Initialized: Default Realm, Campaign, and Character created.")

if __name__ == "__main__":
    app = GuildQuestApp()
    app.run()