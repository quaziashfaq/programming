#!/usr/bin/python3

# Coin change problem

coins = [1, 2, 5]
max_value = 20

def find_number_of_ways(coins, max_value):
    number_of_ways = [0 for i in range(max_value+1)]

    # We can make 0 in 1 number of ways by selecting no coins
    number_of_ways[0] = 1

    for coin in coins:
        for i in range(max_value + 1 - coin):
            number_of_ways[i+coin] += number_of_ways[i]

    return number_of_ways

a = find_number_of_ways(coins, max_value)
print(a)


def find_min_number_coins_needed(coins, max_value):
    min_number_of_coins = [0 for i in range(max_value+1)]

    for coin in coins:
        for i in range(max_value + 1 - coin):
            coins_needed = min_number_of_coins[i] + 1
            found_combinations_to_make_this_sum = min_number_of_coins[i + coin] != 0
            if found_combinations_to_make_this_sum:
                min_number_of_coins[i + coin] = min(min_number_of_coins[i + coin], coins_needed)
            else:
                min_number_of_coins[i + coin] = coins_needed

    return min_number_of_coins

a = find_min_number_coins_needed(coins, max_value)
print(a)
