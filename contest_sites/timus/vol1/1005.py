#!/usr/bin/python3

n = int(input())
stones_weight = [int(i) for i in input().split()]
#stones_weight.sort()
#print(stones_weight)

def find_sum_of_combination_weights(n, stones_weight):
    weights = [0 for i in range(2**n)]
#    print(len(weights))
    for i in range(n):
        j = 0
        last_sum_calculated_at = 2 ** i - 1
        #next_sum_position_gap = 2 ** i
        next_sum_position_gap = last_sum_calculated_at + 1
        while j <= last_sum_calculated_at:
            weights[j + next_sum_position_gap] = weights[j] + stones_weight[i]
            j += 1
    return weights




a = find_sum_of_combination_weights(n, stones_weight)
#a = list(set(a))
a.sort()
#print(a)
#print(type(a))
#print(a)

def find_min_weight_difference_of_2_piles(stones_weight, all_possible_stone_piles_weight_sum):
    total_weight = sum(stones_weight)
    minimum_weight_difference = total_weight
    half_weight_sum = total_weight // 2 + 1
    #print(half_weight_sum)
    i = 0
    while i < len(all_possible_stone_piles_weight_sum) and all_possible_stone_piles_weight_sum[i] <= half_weight_sum:
        d = abs(total_weight - 2 * all_possible_stone_piles_weight_sum[i])
        if d < minimum_weight_difference:
            minimum_weight_difference = d
        i += 1
    return minimum_weight_difference

result = find_min_weight_difference_of_2_piles(stones_weight, a)
print(result)
