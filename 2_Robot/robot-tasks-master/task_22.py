#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    # проверка на одноклеточное поле
    if wall_is_beneath and wall_is_on_the_right():
        fill_cell()

    while not wall_is_beneath():
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
        fill_cell()
        if not wall_is_beneath():
            move_down()
        while not wall_is_on_the_left():
            fill_cell()
            move_left()
        fill_cell()
        if not wall_is_beneath():
            move_down()

            if wall_is_beneath():
                while not wall_is_on_the_right():
                    fill_cell()
                    move_right()
                fill_cell()
                while not wall_is_on_the_left():
                    move_left()

if __name__ == '__main__':
    run_tasks()
