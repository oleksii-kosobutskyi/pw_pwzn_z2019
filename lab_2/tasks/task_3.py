def unique(values):
    """
    Funkcja zwraca listę unikatowych wartości.
    Utrudnienie: Funkcja zwraca unikatowe wartości w kolejności wystąpienia.

    :param values: List of values to check.
    :type values: list
    :return: Unique values in order of appear.
    :rtype: list
    """
    unique_vals = set()
    unique_ordered = []
    for element in values:
        if element not in unique_vals:
            unique_vals.add(element)
            unique_ordered.append(element)
    return unique_ordered


if __name__ == "__main__":
    assert unique([1, 5, 3, 5, 6, 7, 2, 1, 4, 1, 5]) == [1, 5, 3, 6, 7, 2, 4]
