import pytest

from lab_11.tasks.tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)


@pytest.fixture()
def calculator(scope='module'):
    return Calculator()

@pytest.mark.parametrize(
    ('operator', 'arg1', 'arg2', 'expected'),
    [
        pytest.param('+', '2', '2', 4),
        pytest.param('+', '1', '-2', -1),
        pytest.param('-', '3', '1', 2),
        pytest.param('-', '2', '-3', 5),
        pytest.param('*', '2', '2', 4),
        pytest.param('*', '-2', '-1.5', 3),
        pytest.param('/', '6', '2', 3),
        pytest.param('/', '-2', '0.5', -4)
    ],
)
def test_calculations(calculator, operator, arg1, arg2, expected):
    assert calculator.run(operator, arg1, arg2) == expected

@pytest.mark.parametrize(
    ('operator', 'arg1', 'arg2', 'expected'),
    [
        pytest.param("/", 4, 0, CalculatorError),
        pytest.param('+', 2, None, EmptyMemory),
        pytest.param('^', 2, 3, WrongOperation),
        pytest.param('*', 5, 'a', NotNumberArgument),
        pytest.param('*', 'a', 5, NotNumberArgument)
    ]
)
def test_exceptions(calculator, operator, arg1, arg2, expected):
    try:
        calculator.run(operator, arg1, arg2)
    except CalculatorError as exc:
        assert type(exc) == expected
    else:
        raise AssertionError

def test_memorize(calculator):
        calculator.run('+', 1, 1)
        calculator.memorize()
        assert calculator.memory == 2

def test_emptyMemory1(calculator):
    try:
        calculator.in_memory()
    except CalculatorError as exc:
        assert type(exc) == EmptyMemory
    else:
        raise AssertionError

def test_emptyMemory2(calculator):
    try:
        calculator.run("+", 1)
    except CalculatorError as exc:
        assert type(exc) is EmptyMemory
    else:
        raise AssertionError

def test_emptyMemory3(calculator):
    try:
        calculator.run('+', 1, 1)
        calculator.memorize()
        calculator.clean_memory()
        calculator.run('+', 2)
    except CalculatorError as exc:
        assert type(exc) == EmptyMemory
    else:
        raise AssertionError

def test_zeroDivisionError(calculator):
    try:
        calculator.run('/', 3, 0)
    except CalculatorError as exc:
        assert type(exc.__cause__) == ZeroDivisionError
    else:
        raise AssertionError
