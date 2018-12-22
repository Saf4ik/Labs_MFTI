#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_8_30():
    while not wall_is_on_the_left():
        if wall_is_beneath():
            while wall_is_beneath() and not wall_is_on_the_left():
                move_left()
            while not wall_is_beneath():
                move_down()
            while not wall_is_on_the_right() and not wall_is_on_the_left():
                move_right()
        else:
            while not wall_is_beneath():
                move_down()
            while not wall_is_on_the_right():
                move_right()
if __name__ == '__main__':
    run_tasks()
