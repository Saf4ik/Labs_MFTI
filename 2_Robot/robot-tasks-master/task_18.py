#!/usr/bin/python3

from pyrob.api import *

def finish():
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()

@task
def task_8_28():
    while wall_is_above() and not wall_is_on_the_left():
        move_left()
    if not wall_is_above():
        finish()
    else:
        while wall_is_above():
            move_right()
        finish()






if __name__ == '__main__':
    run_tasks()
