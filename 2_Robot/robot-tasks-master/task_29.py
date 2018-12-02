#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():

    flag = 0

    while not wall_is_on_the_right():
        if cell_is_filled():
            flag +=1
            if flag < 3:
                move_right()
            else:
                break
        else:
            flag = 0
            if not wall_is_on_the_right():
                move_right()



if __name__ == '__main__':
    run_tasks()
