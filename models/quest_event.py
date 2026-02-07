from .realm import Realm

class QuestEvent:
    def __init__(self, event_name: str, start_time: int, realm: Realm, end_time: int = None, characters=None):
        self.event_name = event_name
        self.start_time = start_time
        self.end_time = end_time
        self.realm = realm
        self.characters = characters