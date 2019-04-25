class Generator:
    def __init__(self):
        self.t = 0

    def get_percent(self, period):
        if period == 0:
            period = 1
        percent = (self.t - int(self.t / period) * period) / period
        self.t = self.t + 1
        return percent

    def run(self, t_rate):
        pass
