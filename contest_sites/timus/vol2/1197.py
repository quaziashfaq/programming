#!/usr/bin/env python3

def get_knight_attack_vector(chrank, chfile):
    knight_attack_vector = []

    next_rank_position = chrank + 2
    next_file_position = chfile + 1
    knight_attack_vector.append([next_rank_position, next_file_position])

    next_rank_position = chrank + 2
    next_file_position = chfile - 1
    knight_attack_vector.append([next_rank_position, next_file_position])

    next_rank_position = chrank - 2
    next_file_position = chfile + 1
    knight_attack_vector.append([next_rank_position, next_file_position])

    next_rank_position = chrank - 2
    next_file_position = chfile - 1
    knight_attack_vector.append([next_rank_position, next_file_position])

    next_file_position = chfile - 2
    next_rank_position = chrank + 1
    knight_attack_vector.append([next_rank_position, next_file_position])

    next_file_position = chfile - 2
    next_rank_position = chrank - 1
    knight_attack_vector.append([next_rank_position, next_file_position])

    next_file_position = chfile + 2
    next_rank_position = chrank + 1
    knight_attack_vector.append([next_rank_position, next_file_position])

    next_file_position = chfile + 2
    next_rank_position = chrank - 1
    knight_attack_vector.append([next_rank_position, next_file_position])

    return(knight_attack_vector)


def validate(knight_attack_vector):
    validated_attack = [1 for i in range(8)]
    for i in range(8):
        for j in knight_attack_vector[i]:
            if j < 0 or j > 7:
                validated_attack[i] = 0
                break
    return validated_attack

def main():
    test_case = int(input())
    for i in range(test_case):
        line = input()
        line = list(line)
        #print(line)
        chrank = ord(line[0]) - ord('a')
        chfile = ord(line[1]) - ord('1')

        knight_attack_vector = get_knight_attack_vector(chrank, chfile)
        validated_attack = validate(knight_attack_vector)
        print(sum(validated_attack))


main()
