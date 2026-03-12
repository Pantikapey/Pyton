class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Mailing(to={self.to_address}, from={self.from_address}, "
                f"cost={self.cost}, track='{self.track}')")

    def __repr__(self):
        return (f"Mailing(to_address={self.to_address!r}, "
                f"from_address={self.from_address!r}, cost={self.cost!r}, track={self.track!r})")track
