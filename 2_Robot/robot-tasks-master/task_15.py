#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_on_the_left():
        while not wall_is_on_the_right():
            move_right()
    else:
        while not wall_is_on_the_left():
            move_left()
    if wall_is_above():
        while not wall_is_beneath():
            move_down()
    else:
        while not wall_is_above():
            move_up()


if __name__ == '__main__':
    run_tasks()


'''
 if wall_is_on_the_left():
        if wall_is_above():
            while not wall_is_on_the_right():
                move_down()
                move_right()
        else:
            while not wall_is_on_the_right():
                move_up()
                move_right()
    elif wall_is_on_the_right():
        if wall_is_above():
            while not wall_is_on_the_left():
                move_down()
                move_left()
        else:
            while not wall_is_on_the_left():
                move_up()
                move_left()
   
'''