from .clock import WorldClock
from .quest_event import QuestEvent

class Campaign:
    def __init__(self, name: str):
        self.name = name
        self.archived = False
        self._events = []

    def get_events(self):
        """Returns a copy of the events list to prevent direct modification."""
        return list(self._events)

    def add_quest_event(self, title, realm, start_time, end_time, characters):
        self._events.append(QuestEvent(title, start_time, realm, end_time, characters))
    
    def update_quest_event(self, idx: int, name: str, start_time: int, end_time: int, realm_name: str, characters: list):
        if 0 <= idx < len(self._events):
            self._events[idx].event_name = name
            self._events[idx].start_time = start_time
            # Note: existing code had some bugs here (setting .name instead of .end_time)
            # and was trying to set realm_name to an attribute that might not exist or be correct.
            # Keeping it simple for the refactoring but fixing the obvious attribute errors.
            self._events[idx].end_time = end_time
            self._events[idx].characters = characters

    def remove_quest_event(self, idx: int):
        if 0 <= idx < len(self._events):
            return self._events.pop(idx)
        return None