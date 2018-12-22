#!/usr/bin/python3

from pyrob.api import *

def lenght():
    len = 1
    while not wall_is_beneath():
        move_down()
        len +=1
    return len

def left_triangle(len):
    while len > 1:
        for i in range(len - 2):
            move_up()
            fill_cell()
        move_right()
        len -= 2
        if len == 1:
            break
        for i in range(len - 2):
            move_down()
            fill_cell()
        move_right()
        len -= 2

def top_triangle(len):
    while len > 1:
        for i in range(len - 2):
            move_right()
            fill_cell()
        move_down()
        len -= 2
        if len == 1:
            break
        for i in range(len - 2):
            move_left()
            fill_cell()
        move_down()
        len -= 2

def right_triangle(len):
    while len > 1:
        for i in range(len - 2):
            move_down()
            fill_cell()
        move_left()
        len -= 2
        if len == 1:
            break
        for i in range(len - 2):
            move_up()
            fill_cell()
        move_left()
        len -= 2

def bottom_triangle(len):
    while len > 1:
        for i in range(len - 2):
            move_left()
            fill_cell()
        move_up()
        len -= 2
        if len == 1:
            break
        for i in range(len - 2):
            move_right()
            fill_cell()
        move_up()
        len -= 2

@task(delay=0.1)
def task_9_3():
    len = lenght()
    left_triangle(len)
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()
    top_triangle(len)
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_right():
        move_right()
    right_triangle(len)
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_right():
        move_right()
    bottom_triangle(len)
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()

if __name__ == '__main__':
    run_tasks()
