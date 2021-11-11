from datetime import datetime, time
from typing import final

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass

@execution_time
def sum(a: int, b: int) -> int:
    return a + b

@execution_time
def greeting(name="Cesar"):
    print("Hola " + name)

random_func()
sum(5, 5)
greeting("Giocrisrai")