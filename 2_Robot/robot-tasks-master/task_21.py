#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    n = 13
    for k in range(6):
        for i in range(n):
            move_down()
            fill_cell()
        move_down()
        move_right()
        n -= 1
        for i in range(n):
            move_up()
            fill_cell()
        move_up()
        move_right()
        move_down()
        n -= 1
    move_down()
    fill_cell()
    move_down()
    move_left(12)






if __name__ == '__main__':
    run_tasks()
