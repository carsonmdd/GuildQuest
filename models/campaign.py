from clock import WorldClock
from quest_event import QuestEvent

class Campaign:
    def __init__(self, name: str):
        self.name = name
        self.archived = False

    def add_quest_event():
        return
    
    def update_quest_event():
        return
    
    def remove_quest_event():
        return
    
    def get_day_view(date: WorldClock) -> list[QuestEvent]:
        return
    
    def get_week_view(start_date: WorldClock) -> list[QuestEvent]:
        return
    
    def get_month_view(month: int, year: int) -> list[QuestEvent]:
        return
    
    def getYearView(year: int) -> list[QuestEvent]:
        return