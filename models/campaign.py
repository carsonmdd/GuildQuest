from .clock import WorldClock
from .quest_event import QuestEvent

class Campaign:
    def __init__(self, name: str):
        self.name = name
        self.archived = False
        self.events = []

    def add_quest_event(self, title, realm, start_time, end_time, characters):
        self.events.append(QuestEvent(title, start_time, realm, end_time, characters))
    
    def update_quest_event(self, idx: int, name: int, start_time: int, end_time: int, realm: str):
        self.events[idx].event_name = name
        self.events[idx].start_time = start_time
        self.events[idx].name = end_time
        self.events[idx].name = realm

    def remove_quest_event(self, idx: int):
        return self.events.pop(idx)