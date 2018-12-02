#!/usr/bin/python3

from pyrob.api import *

def cross():
    move_right()
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
    move_left()


@task
def task_2_1():
    move_down(2)
    cross()



if __name__ == '__main__':
    run_tasks()
