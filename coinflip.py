import random

class Coin:
    def __init__(self):
        self.side = None

    def flip(self):
        sides = ('heads', 'tails')
        self.side = random.choice(sides)
        return self.side

coins = [Coin(), Coin(), Coin(), Coin(), Coin()]

count_heads = 0
count_tails = 0
for coin in coins:
    if coin.flip() == 'heads':
        count_heads += 1
    else:
        count_tails += 1
print(f"{count_heads / len(coins) * 100}% heads and {count_tails / len(coins) * 100}% tails.")