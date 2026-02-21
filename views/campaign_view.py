from models.campaign import Campaign
from models.user import User
from models.realm import Realm
from models.clock import WorldClock
from views.menu_view import MenuView

class CampaignMenu(MenuView):
    def __init__(self, user: User, realms: Realm):
        self.user = user
        self.realms = realms
        self.clock = WorldClock()

    def display_header(self):
        print("\n--- Campaign Management ---")

    def display_items(self):
        for i, c in enumerate(self.user.campaigns):
            print(f"{i+1}. {c.name} ({len(c.events)} Events)")

    def display_options(self):
        print("a. Add Campaign | d. Delete | e. Edit | b. Back")

    def handle_choice(self, choice: str) -> bool:
        if choice == 'a':
            self.add_campaign()
            return True
        elif choice == 'd':
            self.delete_campaign()
            return True
        elif choice == 'e':
            self.edit_campaign()
            return True
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(self.user.campaigns):
                self.manage_single_campaign(idx)
                return True
        return False

    def add_campaign(self):
        name = input("Enter new campaign name: ")
        if name:
            self.user.add_campaign(name)
            print(f"Campaign '{name}' created!")

    def delete_campaign(self):
        idx_str = input("Enter the number of the campaign to delete: ")
        if idx_str.isdigit():
            idx = int(idx_str) - 1
            if 0 <= idx < len(self.user.campaigns):
                removed = self.user.remove_campaign(idx)
                print(f"Archived '{removed.name}'.")
            else:
                print("Invalid index.")

    def edit_campaign(self):
        idx_str = input("Enter the number of the campaign to rename: ")
        if idx_str.isdigit():
            idx = int(idx_str) - 1
            if 0 <= idx < len(self.user.campaigns):
                new_name = input("Enter new name: ")
                self.user.update_campaign(idx, new_name)
                print("Campaign updated.")

    def manage_single_campaign(self, index: str):
        campaign = self.user.campaigns[index]
        while True:
            print(f"\n--- {campaign.name} ---")
            for i, ev in enumerate(campaign.events):
                world_t = self.clock.format_time(ev.start_time)
                local_t = ev.realm.display_event_time(ev.start_time)
                print(f"  {i+1}. {ev.event_name} [{ev.realm.name}]")
                print(f"     Time: {world_t} (Local: {local_t})")

            print("\na. Add Event | r. Remove | e. Edit | b. Back")
            choice = input(">> ").lower()
            if choice == 'b': break
            elif choice == 'a': self.add_event(campaign)
            elif choice == 'r': self.remove_event(campaign)
            elif choice == 'e': self.edit_event(campaign)

    def add_event(self, campaign: Campaign):
        title = input("Event Title: ")
        name = input("Enter Realm Name: ") 
        start_time = int(input("Event Start Time: "))
        end_time = int(input("Event End Time: "))
        characters = input("Event Characters (space separated): ").split()
        realm = next((r for r in self.realms if r.name == name), None)

        existing_names = {char.name for char in self.user.characters}
        missing = [name for name in characters if name not in existing_names]
        if missing:
            print(f"Error: The following characters do not exist: {', '.join(missing)}")
            return
        
        if realm:
            campaign.add_quest_event(title, realm, start_time, end_time, characters)

    def remove_event(self, campaign: Campaign):
        idx_str = input("Enter the number of the event to delete: ")
        if idx_str.isdigit():
            idx = int(idx_str) - 1
            if 0 <= idx < len(self.user.campaigns):
                removed = campaign.remove_quest_event(idx)
                print(f"Deleted '{removed.event_name}'.")
            else:
                print("Invalid index.")

    def edit_event(self, campaign: Campaign):
        idx_str = input("Enter the number of the event to edit: ")
        if idx_str.isdigit():
            idx = int(idx_str) - 1
            if 0 <= idx < len(campaign.events):
                new_name = input("Enter new name: ")
                new_start_time = int(input("Enter new start time: "))
                new_end_time = int(input("Enter new end time: "))
                new_realm = input("Enter new realm: ")
                new_characters = input("Enter new characters (space separated): ").split()
                campaign.update_quest_event(new_name, new_start_time, new_end_time, new_realm, new_characters)
                print("Campaign updated.")