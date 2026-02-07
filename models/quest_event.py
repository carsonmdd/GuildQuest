from .clock import WorldClock
from .realm import Realm

class QuestEvent:
    def __init__(self, name: str, start_time: WorldClock, realm: Realm, end_time: WorldClock = None):
        self.event_name
        self.start_time = start_time
        self.end_time = self.end_time
        self.realm = realm
