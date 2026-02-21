from .campaign import Campaign

class User:
    def __init__(self, id: int):
        self.user_id = id
        self._campaigns = []
        self._characters = []

    def get_campaigns(self):
        """Returns a copy of the campaigns list."""
        return list(self._campaigns)

    def get_characters(self):
        """Returns a copy of the characters list."""
        return list(self._characters)

    def add_campaign(self, name: str):
        self._campaigns.append(Campaign(name))
    
    def remove_campaign(self, idx: int):
        if 0 <= idx < len(self._campaigns):
            return self._campaigns.pop(idx)
        return None
    
    def update_campaign(self, idx: int, name: str):
        if 0 <= idx < len(self._campaigns):
            self._campaigns[idx].name = name
    