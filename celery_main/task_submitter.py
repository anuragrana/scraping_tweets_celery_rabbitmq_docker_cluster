from .task_receiver import longtime_add


if __name__ == '__main__':
    for i in range(10):
        result = longtime_add.delay(i)
        print('task submitted ' + str(i))
