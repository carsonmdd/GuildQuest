from views.menu_view import MenuView

class CampaignMenu(MenuView):
    def __init__(self, facade):
        self.facade = facade

    def display_header(self):
        print("\n--- Campaign Management ---")

    def display_items(self):
        campaigns = self.facade.get_campaigns()
        for i, c in enumerate(campaigns):
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
            campaigns = self.facade.get_campaigns()
            if 0 <= idx < len(campaigns):
                self.manage_single_campaign(idx)
                return True
        return False

    def add_campaign(self):
        name = input("Enter new campaign name: ")
        if self.facade.add_campaign(name):
            print(f"Campaign '{name}' created!")

    def delete_campaign(self):
        idx_str = input("Enter the number of the campaign to delete: ")
        if not idx_str.isdigit():
            print("Invalid input.")
            return

        idx = int(idx_str) - 1
        removed = self.facade.delete_campaign(idx)
        if removed:
            print(f"Archived '{removed.name}'.")
        else:
            print("Invalid index.")

    def edit_campaign(self):
        idx_str = input("Enter the number of the campaign to rename: ")
        if not idx_str.isdigit():
            print("Invalid input.")
            return

        idx = int(idx_str) - 1
        new_name = input("Enter new name: ")
        if self.facade.rename_campaign(idx, new_name):
            print("Campaign updated.")
        else:
            print("Update failed. Check index and name.")

    def manage_single_campaign(self, campaign_index: int):
        while True:
            campaign = self.facade.get_campaigns()[campaign_index]
            print(f"\n--- {campaign.name} ---")
            for i, ev in enumerate(campaign.events):
                world_t = self.facade.clock.format_time(ev.start_time)
                local_t = ev.realm.display_event_time(ev.start_time)
                print(f"  {i+1}. {ev.event_name} [{ev.realm.name}]")
                print(f"     Time: {world_t} (Local: {local_t})")

            print("\na. Add Event | r. Remove | e. Edit | b. Back")
            choice = input(">> ").lower()
            if choice == 'b': break
            elif choice == 'a': self.add_event(campaign_index)
            elif choice == 'r': self.remove_event(campaign_index)
            elif choice == 'e': self.edit_event(campaign_index)

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

    def add_event(self, campaign_index: int):
        data = self._prompt_for_event_data()
        if not data: return
        
        success, message = self.facade.add_event_to_campaign(campaign_index, *data)
        print(message)

    def remove_event(self, campaign_index: int):
        idx_str = input("Enter the number of the event to delete: ")
        if not idx_str.isdigit():
            print("Invalid input.")
            return

        idx = int(idx_str) - 1
        removed = self.facade.remove_event_from_campaign(campaign_index, idx)
        if removed:
            print(f"Deleted '{removed.event_name}'.")
        else:
            print("Invalid index.")

    def edit_event(self, campaign_index: int):
        idx_str = input("Enter the number of the event to edit: ")
        if not idx_str.isdigit():
            print("Invalid input.")
            return

        idx = int(idx_str) - 1
        data = self._prompt_for_event_data()
        if not data: return

        title, realm_name, start, end, chars = data
        campaign = self.facade.get_campaigns()[campaign_index]
        if 0 <= idx < len(campaign.events):
            campaign.update_quest_event(idx, title, start, end, realm_name, chars)
            print("Event updated.")
        else:
            print("Invalid index.")