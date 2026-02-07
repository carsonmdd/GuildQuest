from models.campaign import Campaign
class CampaignMenu:
    def __init__(self, app):
        self.app = app

    def run(self):
        while True:
            print("\n--- Campaign Management ---")
            for i, c in enumerate(self.app.campaigns):
                print(f"{i+1}. {c.name} ({len(c.events)} Events)")
            print("a. Add Campaign | d. Delete | e. Edit | b. Back")
            
            choice = input(">> ").lower()
            if choice == 'b': break
            elif choice == 'a': self.add_campaign()
            elif choice == 'd': self.delete_campaign()
            elif choice == 'e': self.edit_campaign()
            elif choice.isdigit(): self.manage_single_campaign(int(choice)-1)

    def add_campaign(self):
        name = input("Enter new campaign name: ")
        if name:
            from models.campaign import Campaign
            new_campaign = Campaign(name)
            self.app.campaigns.append(new_campaign)
            print(f"Campaign '{name}' created!")

    def delete_campaign(self):
        idx_str = input("Enter the number of the campaign to delete: ")
        if idx_str.isdigit():
            idx = int(idx_str) - 1
            if 0 <= idx < len(self.app.campaigns):
                removed = self.app.campaigns.pop(idx)
                print(f"Archived '{removed.name}'.")
            else:
                print("Invalid index.")

    def edit_campaign(self):
        idx_str = input("Enter the number of the campaign to rename: ")
        if idx_str.isdigit():
            idx = int(idx_str) - 1
            if 0 <= idx < len(self.app.campaigns):
                new_name = input("Enter new name: ")
                self.app.campaigns[idx].name = new_name
                print("Campaign updated.")

    def manage_single_campaign(self, index: str):
        campaign = self.app.campaigns[index]
        while True:
            print(f"\n--- {campaign.name} ---")
            for i, ev in enumerate(campaign.events):
                # Requirement 6: Display World vs Local Time
                world_t = self.app.clock.format_time(ev.start_time)
                local_t = ev.realm.display_event_time(ev.start_time, self.app.clock)
                print(f"  {i+1}. {ev.title} [{ev.realm.name}]")
                print(f"     Time: {world_t} (Local: {local_t})")

            print("\na. Add Event | r. Remove Event | b. Back")
            choice = input(">> ").lower()
            if choice == 'b': break
            elif choice == 'a': self.add_event(campaign)

    def add_event(self, campaign: Campaign):
        title = input("Event Title: ")
        realm_id = input("Enter Realm Name: ") 
        realm = next((r for r in self.app.realms.values() if r.name == realm_id), None)
        if realm:
            campaign.add_quest_event(title, self.app.clock.total_minutes, realm)