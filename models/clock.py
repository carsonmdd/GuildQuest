class WorldClock:
    def __init__(self, initial_minutes=0):
        # The internal integer representation (Requirement 1)
        self.total_minutes = initial_minutes

    def advance(self, minutes):
        """Adds time to the world clock."""
        if minutes > 0:
            self.total_minutes += minutes

    def get_time_parts(self, absolute_minutes=None):
        """
        Converts total minutes into a (day, hour, minute) tuple.
        Uses internal time if no absolute_minutes is provided.
        """
        time = absolute_minutes if absolute_minutes is not None else self.total_minutes
        
        days = time // (24 * 60)
        remaining_minutes = time % (24 * 60)
        hours = remaining_minutes // 60
        minutes = remaining_minutes % 60
        
        return days, hours, minutes

    def format_time(self, absolute_minutes=None):
        """Returns a readable string: 'Day 2, 14:30'"""
        d, h, m = self.get_time_parts(absolute_minutes)
        return f"Day {d}, {h:02d}:{m:02d}"

    def __repr__(self):
        return f"WorldClock(total_minutes={self.total_minutes})"
    
if __name__ == '__main__':
    clock = WorldClock(3780)
    print(clock.format_time())