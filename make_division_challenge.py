def make_division_by(n: int):
    """This closure returns a function that returns the division of an x number by n"""
    assert n > 0, "El valor debe ser mayor a cero"
    def divisor(x: int) -> float:
        return x/n
    return divisor

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))      # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))    # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))    # The expected output is 3 

if __name__ == '__main__':
    run()