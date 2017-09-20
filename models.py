import decimal


class User:
    def __init__(self, name: str, id: int=0):
        self.id = id
        self.name = name


class Bid:
    def __init__(self, user: User, value: decimal):
        self.user = user
        self.value = value


class Auction:
    def __init__(self, description):
        self.description = description
        self.bids = []

    def register_bid(self, bid: Bid):
        self.bids.append(bid)


class Appraiser:
    def __init__(self):
        self.biggest_bid = decimal.Decimal('-Inf')
        self.smallest_bid = decimal.Decimal('Inf')

    def appraise(self, auction: Auction):
        self.biggest_bid = max(bid.value for bid in auction.bids)
        self.smallest_bid = min(bid.value for bid in auction.bids)
