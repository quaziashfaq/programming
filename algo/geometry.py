#!/usr/bin/env python3
import math


def find_three_angles_from_sides_of_triangle(a, b, c):
    '''
    Given length of 3 sides: a, b and c.
    Find out the 3 angles of triangle A, B, C
    '''
    C = math.acos((a*a + b*b - c*c) / (2*a*b)) * 180 / math.pi
    B = math.acos((a*a + c*c - b*b) / (2*a*c)) * 180 / math.pi
    A = math.acos((b*b + c*c - a*a) / (2*b*c)) * 180 / math.pi

    return (A, B, C)


def find_area_of_triangle_from_three_sides(a, b, c):
    '''
    Given length of 3 sides: a, b and c.
    Find out the area.
    '''
    p = (a + b + c) / 2.0
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area


def find_circumference_of_circle_from_radius(radius):
    '''
    Given the circle radius.
    Find the perimeter of circle
    '''
    return 2 * math.pi * radius


def find_nearest_integer_of_square_root_of_an_integer(xx):
    x = math.sqrt(xx)
    a = int(math.floor(x))
    b = a + 1

    if ((xx - a*a) < (b*b - xx)):
        return a
    else:
        return b


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def find_distance_between_2_points_in_2D_coordinates(a, b):
    '''
    Find distance between 2 points from their 2d coordinates.
    Function parameters: a, b. They are objects of Point class
    Each parameter is a tuple of 2 numbers having 2 coordinates (x, y)
    '''
    return math.sqrt( (a.x-b.x)**2 + (a.y-b.y)**2 )


def find_area_of_triangle_from_three_vertices(a, b, c):
    '''
    Parameters: a, b, c. They are objects of Point class.
    Calculate the triangle area
    '''
    return (a.x*(b.y-c.y) + b.x*(c.y-a.y) + c.x*(a.y-b.y)) / 2.0


a = Point(0,0)
b = Point(3,0)
c = Point(0,4)
print(find_area_of_triangle_from_three_vertices(a, b, c))

def find_quadrant(p):
    if p.x >= 0:
        if p.y >= 0:
            return 1
        else:
            return 2
    else:
        if p.y >= 0:
            return 4
        else:
            return 3
