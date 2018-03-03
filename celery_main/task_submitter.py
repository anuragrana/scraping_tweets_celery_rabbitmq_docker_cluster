from .task_receiver import do_work
import database
import time


def submit_handles(handles):
    for handle in handles:
        handle = handle.strip()
        handle = handle.strip(".!,")
        do_work.delay(handle)
        print("submitted " + handle)


if __name__ == '__main__':
    handles = list()
    with open("handles.txt", "r") as f:
        handles = f.readlines()

    submit_handles(handles)
