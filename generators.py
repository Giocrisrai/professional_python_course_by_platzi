import time

def fibo_gen(fibo_max):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            if aux <= fibo_max:
                n1, n2 = n2, aux
                counter += 1
                yield aux
            else:
                break

if __name__ == '__main__':
    fibo_max = int(input("Ingrese el número máximo  que desea visualizar de la sucesion de fibonacci: "))
    fibonacci = fibo_gen(fibo_max)
    for element in fibonacci:
        print(element)
        time.sleep