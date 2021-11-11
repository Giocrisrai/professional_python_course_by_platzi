def is_prime(number: int) -> bool:
    result_list = [x for x in range(2, number + 1) if number % x == 0]
    return len(result_list) == 0


def run():
    number: int = 15
    if is_prime(number):
       print("Es primo")
    else:
        print("No es primo")


if __name__ == '__main__':
    run()