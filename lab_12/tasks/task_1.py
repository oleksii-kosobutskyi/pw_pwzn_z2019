def generate_fibonacci(n=100):
    if (not isinstance(n, int) or n > 100 or n < 1):
        raise RuntimeError

    number1 = 0
    number2 = 1
    for i in range(0, n):
        yield number1
        [number1, number2] = [number2, number1 + number2]


if __name__ == '__main__':
    assert list(generate_fibonacci(1)) == [0]
    assert list(generate_fibonacci(2)) == [0, 1]
    assert sum(generate_fibonacci(10)) == 88
    ii = 0
    for ii in generate_fibonacci():
        pass
    assert ii == 218922995834555169026
    try:
        generate_fibonacci(0)
    except Exception as exc:
        assert isinstance(exc, RuntimeError)
