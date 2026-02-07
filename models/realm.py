class Realm:
    def __init__(self, name, offset=0):
        self.name = name
        self.offset = offset          # Fixed minute shift (e.g., -120 for 2 hours behind)

    def to_local_time(self, world_minutes):
        """
        Requirement 6: Converts World Clock time to Realm-local time.
        Formula: (WorldTime * Multiplier) + Offset
        """
        return int((world_minutes * self.multiplier) + self.offset)

    def display_event_time(self, world_minutes, clock_ref):
        """
        Helper to format the time using the WorldClock's formatting logic 
        but with the Realm's local calculation.
        """
        local_total = self.to_local_time(world_minutes)
        return clock_ref.format_time(local_total)