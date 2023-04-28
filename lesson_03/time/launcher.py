import subprocess

PROCESS = []

while True:
    ACTION = input(f'Выберите действие: \nq - выход\ns - запустить сервер и клиенты \nx - закрыть все окна'
                   f'\nВвод действия: ')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        PROCESS.append(subprocess.Popen('python time_server.py',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))
        for i in range(5):
            PROCESS.append(subprocess.Popen('python time_client.py',
                                            creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif ACTION == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()
