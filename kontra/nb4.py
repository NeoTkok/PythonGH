class Clock:
    def __init__(self):
        self.minutes = 0
        self.hours = 0
        
    def tick(self, minutes):
        if minutes < 0:
            raise RuntimeError
        else:
            self.minutes += minutes
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60
            self.hours = self.hours % 24

    def get_time(self):
        return (self.hours, self.minutes)