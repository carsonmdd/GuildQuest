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
        if not idx_str.isdigit():
            print("Invalid input. Please enter a number.")
            return

        idx = int(idx_str) - 1
        if not (0 <= idx < len(self.user.campaigns)):
            print("Invalid index.")
            return

        removed = self.user.remove_campaign(idx)
        print(f"Archived '{removed.name}'.")

    def edit_campaign(self):
        idx_str = input("Enter the number of the campaign to rename: ")
        if not idx_str.isdigit():
            print("Invalid input. Please enter a number.")
            return

        idx = int(idx_str) - 1
        if not (0 <= idx < len(self.user.campaigns)):
            print("Invalid index.")
            return

        new_name = input("Enter new name: ")
        if not new_name:
            print("Name cannot be empty.")
            return

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

    def _get_realm_by_name(self, name: str):
        realm = next((r for r in self.realms if r.name == name), None)
        if not realm:
            print(f"Error: Realm '{name}' not found.")
        return realm

    def _validate_characters(self, char_names: list):
        existing_names = {char.name for char in self.user.characters}
        missing = [name for name in char_names if name not in existing_names]
        if missing:
            print(f"Error: The following characters do not exist: {', '.join(missing)}")
            return False
        return True

    def _prompt_for_event_data(self):
        try:
            title = input("Event Title: ")
            realm_name = input("Enter Realm Name: ")
            start_time = int(input("Event Start Time: "))
            end_time = int(input("Event End Time: "))
            characters = input("Event Characters (space separated): ").split()
            return title, realm_name, start_time, end_time, characters
        except ValueError:
            print("Invalid input format. Times must be numbers.")
            return None

    def add_event(self, campaign: Campaign):
        data = self._prompt_for_event_data()
        if not data: return
        
        title, realm_name, start, end, chars = data
        realm = self._get_realm_by_name(realm_name)
        
        if realm and self._validate_characters(chars):
            campaign.add_quest_event(title, realm, start, end, chars)
            print(f"Event '{title}' added to {campaign.name}.")

    def remove_event(self, campaign: Campaign):
        idx_str = input("Enter the number of the event to delete: ")
        if not idx_str.isdigit():
            print("Invalid input.")
            return

        idx = int(idx_str) - 1
        if not (0 <= idx < len(campaign.events)):
            print("Invalid index.")
            return

        removed = campaign.remove_quest_event(idx)
        print(f"Deleted '{removed.event_name}'.")

    def edit_event(self, campaign: Campaign):
        idx_str = input("Enter the number of the event to edit: ")
        if not idx_str.isdigit():
            print("Invalid input.")
            return

        idx = int(idx_str) - 1
        if not (0 <= idx < len(campaign.events)):
            print("Invalid index.")
            return

        data = self._prompt_for_event_data()
        if not data: return

        title, realm_name, start, end, chars = data
        campaign.update_quest_event(idx, title, start, end, realm_name, chars)
        print("Event updated.")