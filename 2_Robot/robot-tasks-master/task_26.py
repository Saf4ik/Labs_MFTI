#!/usr/bin/python3

from pyrob.api import *

def cross():
    fill_cell()
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_right()
    move_up()
    fill_cell()
    move_up()
    move_left()
    fill_cell()
    move_right()

@task(delay=0.01)
def task_2_4():


    move_down()
    while not wall_is_on_the_right():
        cross()
        while not wall_is_on_the_right():
            move_right(2)
            move_down()
            cross()
        move_down(2)
        if wall_is_beneath():
            while not wall_is_on_the_left():
                move_left()
            move_up(2)
            break
        else:
            move_down(3)
            while not wall_is_on_the_left():
                move_left()



if __name__ == '__main__':
    run_tasks()
