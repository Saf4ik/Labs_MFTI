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


@task
def task_2_2():
    move_down(2)
    for i in range(4):
        cross()
        move_right(3)
        move_down()
    cross()
    move_left()

if __name__ == '__main__':
    run_tasks()
