from models import User, Auction, Bid, Appraiser


def test_one():
    joao = User(name='Joao')
    jose = User(name='Jose')
    maria = User(name='Maria')

    auction = Auction("Playstation 3 Novo")

    auction.register_bid(Bid(joao, 300.0))
    auction.register_bid(Bid(jose, 400.0))
    auction.register_bid(Bid(maria, 250.0))

    appraiser = Appraiser()
    appraiser.appraise(auction)

    expected_biggest = 400.0
    expected_smallest = 250.0

    assert expected_biggest == appraiser.biggest_bid
    assert expected_smallest == expected_smallest
