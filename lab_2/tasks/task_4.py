def count_letters(msg):
    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """
    # tworzenie dwóch tablic w jednej litery (bez powtórzeń) w drugiej ile razy
    listofletters = []
    listofcounts = []
    iter_1 = 0
    for mark in msg:
        frequency = 1
        iter_2 = 0
        firstTime = True
        for counting in msg:
            if iter_2 != iter_1:
                if counting == mark:
                    frequency += 1
                    if iter_2 < iter_1: firstTime=False
            iter_2 += 1
        if firstTime:
            listofletters.append(mark)
            listofcounts.append(frequency)
        iter_1 += 1

    # sprawdzenie, która litera ma więcej zliczeń i ta kwestia z alfabetem
    maxIndex=0
    maxCount=1
    count=0
    for whereIsTheWinner in listofcounts:
        if whereIsTheWinner > maxCount:
            maxCount = whereIsTheWinner
            maxIndex = count
        elif whereIsTheWinner == maxCount:
            if listofletters[whereIsTheWinner] < listofletters[maxIndex]:
                maxCount=whereIsTheWinner
                maxIndex=count
        count+=1

    myFirstTupla = listofletters[maxIndex], listofcounts[maxIndex]
    return myFirstTupla



if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ('a', 4)
    assert count_letters('za') == ('a', 1)
    