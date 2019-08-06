def num_coins(cents):
    coins = [50,20,10,5]
    count = 0
    for coin in coins:
        while cents >= coin:
            cents = cents - coin
            count = count + 1

    return count

print(num_coins(135))