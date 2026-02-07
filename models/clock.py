class WorldClock:
    def __init__(self, initial_minutes=0):
        # The internal integer representation (Requirement 1)
        self.total_minutes = initial_minutes
        self.day = 0
        self.hour = 0
        self.minute = 0
        self.update_time_parts()

    def advance(self, minutes):
        """Adds time to the world clock."""
        if minutes > 0:
            self.total_minutes += minutes
            self.update_time_parts()

    def update_time_parts(self, absolute_minutes=None):
        """
        Converts total minutes into a (day, hour, minute) tuple.
        Uses internal time if no absolute_minutes is provided.
        """
        time = absolute_minutes if absolute_minutes is not None else self.total_minutes
        
        self.day = time // (24 * 60)
        remaining_minutes = time % (24 * 60)
        self.hour = remaining_minutes // 60
        self.minute = remaining_minutes % 60

    def format_time(self):
        """Returns a readable string: 'Day 2, 14:30'"""
        return f"Day {self.day}, {self.hour:02d}:{self.minute:02d}"
    
    
if __name__ == '__main__':
    clock = WorldClock(3780)
    print(clock.format_time())