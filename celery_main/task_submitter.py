from .task_receiver import do_work


if __name__ == '__main__':
    for i in range(10):
        result = do_work.delay(i)
        print('task submitted' + str(i))
