#!/usr/bin/python3

# uva - 253

first_three_faces = [
    [1, 2, 3],
    [2, 6, 3],
    [3, 2, 6],
    [4, 2, 1],
    [5, 1, 3],
    [6, 5, 3]
]

def generate_full_faces(first_three_faces):
    for i in range(len(first_three_faces)):
        faces = []
        faces.extend(first_three_faces[i])
        faces.extend([0,0,0])
        faces[3] = 7 - first_three_faces[i][1]
        faces[4] = 7 - first_three_faces[i][2]
        faces[5] = 7 - first_three_faces[i][0]
        yield(faces)


def rotate_mid_section(a):
    yield a

    for i in range(3):
        a = rotate_mid_section_one_time(a[:])
        yield a


def rotate_mid_section_one_time(a):
    ''' Rotating only the middle section'''
    a[1], a[2], a[3], a[4] = a[2], a[3], a[4], a[1]
    return a


def get_colors(initial_color_string, rotated_position):
    new_color_string = ['' for i in range(6)]

    new_color_string[0] = initial_color_string[rotated_position[0]-1]
    new_color_string[1] = initial_color_string[rotated_position[1]-1]
    new_color_string[2] = initial_color_string[rotated_position[2]-1]
    new_color_string[3] = initial_color_string[rotated_position[4]-1] # changing into the i-th position
    new_color_string[4] = initial_color_string[rotated_position[3]-1] # changing into the i-th position
    new_color_string[5] = initial_color_string[rotated_position[5]-1]

    return new_color_string

def find_match(first_cube, second_cube):
    found = False
    for each_face in generate_full_faces(first_three_faces):
        for f in rotate_mid_section(each_face):
            #print(f)
            rotated_2nd_cube = get_colors(second_cube, f)
            #print(rotated_2nd_cube)
            if first_cube == rotated_2nd_cube:
                found = True
                break
        if found == True:
            break

    if found == True:
        print('TRUE')
    else:
        print('FALSE')
    return

import sys

for line in sys.stdin:
    two_cubes = line.strip()
    first_cube = list(two_cubes[0:6])
    second_cube = list(two_cubes[6:])
    find_match(first_cube, second_cube)
