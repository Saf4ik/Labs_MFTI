#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    for k in range(6):
        for k in range(27):
            move_right()
            fill_cell()
        move_right()
        move_down()
        for k in range(27):
            move_left()
            fill_cell()
        move_left()
        move_down()
    move_right()

if __name__ == '__main__':
    run_tasks()
