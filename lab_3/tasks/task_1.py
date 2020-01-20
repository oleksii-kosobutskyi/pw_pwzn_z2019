def parse_input(input):
    """
    Splits multiline string into list of lists with integers.
    Napisz funkcję przymującą wielolinijkowy ciąg znaków.
    a zwracającą listę list liczb całkowitych znajdujących się w podanym ciągu znaków.
    Nie używaj pętl for i while.
    String może zawierać puste linie na początku i końcu.
    :param input: string to parse
    :type input: str
    :return: list of parsed list of integers
    :rtype: list
    """
    output=input.strip() # usuwa puste znaki na początku i końcu
    output=output.split('\n') # dzieli linie na elementy
    output=list(map(lambda x: list(map(int, x.split(' '))), output)) # dzieli słowa w linii na elementy i zamienia na int
    return output


if __name__ == '__main__':
    _input = """
1 5
1 6 7
3 2
1 10
1 10
1 6
2 5
3 2
    
    
    """
    assert parse_input(_input) == [
        [1, 5], [1, 6, 7], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]
    ]
