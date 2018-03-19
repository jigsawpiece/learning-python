#Coin Flip Simulator

import random

def coin_flip(n):
    n = int(n)
    heads = 0
    tails = 0
    options = ('heads', 'tails')
    
    for x in range(0, n):
        if random.choice(options) == 'heads':
            heads += 1
        else: tails += 1

    total = heads + tails

    return {'heads': heads, 'tails': tails, 'total': total}

print(coin_flip(input("How many times do you want to flip a coin?")))

            
