from .campaign import Campaign

class User:
    def __init__(self, id: int):
        self.user_id = id
        self.campaigns = []
        self.characters = []

    def add_campaign(self, name: str):
        self.campaigns.append(Campaign(name))
    
    def remove_campaign(self, idx: int):
        return self.campaigns.pop(idx)
    
    def update_campaign(self, idx: int, name: str):
        self.campaigns[idx].name = name
    