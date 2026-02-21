from models.user import User
from models.clock import WorldClock
from models.realm import Realm
from models.campaign import Campaign
from models.character import Character

class GameFacade:
    """
    Facade providing a simplified interface to the GuildQuest subsystem.
    Handles coordination between User, Campaigns, Realms, and Clock.
    """
    def __init__(self, user_id: int):
        self.user = User(user_id)
        self.clock = WorldClock()
        self.realms = []
        self._seed_initial_data()

    def _seed_initial_data(self):
        # Initial data setup moved from main.py to Facade
        tutorial_realm = Realm(realm_id='R1', name="Sky Haven", local_time_offset=1440)
        self.realms.append(tutorial_realm)
        
        starter_campaign = Campaign(name="The First Journey")
        self.user.campaigns.append(starter_campaign)

        starting_character = Character('Harold', 'Archer', 15)
        self.user.characters.append(starting_character)

    # --- Time Management ---
    def get_world_time_str(self):
        return self.clock.format_time()

    def advance_time(self, minutes: int):
        self.clock.advance(minutes)

    # --- Campaign Management ---
    def get_campaigns(self):
        return self.user.campaigns

    def add_campaign(self, name: str):
        if name:
            self.user.add_campaign(name)
            return True
        return False

    def delete_campaign(self, index: int):
        if 0 <= index < len(self.user.campaigns):
            return self.user.remove_campaign(index)
        return None

    def rename_campaign(self, index: int, new_name: str):
        if 0 <= index < len(self.user.campaigns) and new_name:
            self.user.update_campaign(index, new_name)
            return True
        return False

    # --- Event Management ---
    def add_event_to_campaign(self, campaign_index, title, realm_name, start, end, char_names):
        if not (0 <= campaign_index < len(self.user.campaigns)):
            return False, "Invalid campaign index."

        realm = self.get_realm_by_name(realm_name)
        if not realm:
            return False, f"Realm '{realm_name}' not found."

        if not self.validate_characters(char_names):
            return False, "One or more characters do not exist."

        campaign = self.user.campaigns[campaign_index]
        campaign.add_quest_event(title, realm, start, end, char_names)
        return True, "Event added successfully."

    def remove_event_from_campaign(self, campaign_index, event_index):
        if 0 <= campaign_index < len(self.user.campaigns):
            campaign = self.user.campaigns[campaign_index]
            if 0 <= event_index < len(campaign.events):
                return campaign.remove_quest_event(event_index)
        return None

    # --- Realm & Character Lookups ---
    def get_realms(self):
        return self.realms

    def get_realm_by_name(self, name: str):
        return next((r for r in self.realms if r.name == name), None)

    def get_characters(self):
        return self.user.characters

    def validate_characters(self, char_names: list):
        existing_names = {char.name for char in self.user.characters}
        return all(name in existing_names for name in char_names)

    def add_realm(self, realm_id, name, desc):
        new_realm = Realm(realm_id, name, desc)
        self.realms.append(new_realm)
        return new_realm

    def add_character(self, name, char_class, level):
        new_char = Character(name, char_class, level)
        self.user.characters.append(new_char)
        return new_char
