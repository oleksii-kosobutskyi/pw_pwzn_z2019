"""
Częśćć 1 (1 pkt): Uzupełnij klasę Vector tak by reprezentowała wielowymiarowy wektor.
Klasa posiada przeładowane operatory równości, dodawania, odejmowania,
mnożenia (przez liczbę i skalarnego), długości
oraz nieedytowalny (własność) wymiar.
Wszystkie operacje sprawdzają wymiar.
Część 2 (1 pkt): Klasa ma statyczną metodę wylicznia wektora z dwóch punktów
oraz metodę fabryki korzystającą z metody statycznej tworzącej nowy wektor
z dwóch punktów.
Wszystkie metody sprawdzają wymiar.
"""


class Vector:
    dim = None  # Wymiar vectora
    def __init__(self, *args):
        if len(args)==0:
            self.values = (0,0)
        else:
            self.values = args
            dim = len(args)

    # dodawanie wektorów
    def __add__(self, another):
        if isinstance(another,Vector):
            if self.dim == another.dim:
                output = tuple(a+b for a,b in zip(self.values, another.values))
                return Vector(*output)
            else:
                raise ValueError("Różne wymiary wektorów")
        else:
            raise ValueError("Obiekt jest innego typu niż Vector")

    # odejmowanie wektorów
    def __sub__(self, another):
        if isinstance(another,Vector):
            if self.dim == another.dim:
                output = tuple(a-b for a,b in zip(self.values, another.values))
                return Vector(*output)
            else:
                raise ValueError("Różne wymiary wektorów")
        else:
            raise ValueError("Obiekt jest innego typu niż Vector")
    
    # mnożenie wektorów
    def __mul__(self, another):
        if isinstance(another,Vector):
            if self.dim == another.dim:
                output = sum(a*b for a,b in zip(self.values, another.values))
                return output
            else:
                raise ValueError("Różne wymiary wektorów")
        else:
            output = tuple(a*another for a in self.values)
            return Vector(*output)

    # równosć wektorów
    def __eq__(self, another):
        if isinstance(another,Vector):
            if self.dim == another.dim:
                return self.values == another.values
            else:
                raise ValueError("Różne wymiary wektorów")
        else:
            raise ValueError("Obiekt jest innego typu niż Vector")

    # długosć wektora
    def __len__(self):
        length=sum(tuple(a**2 for a in self.values))**0.5
        return int(length)
    
    @staticmethod
    def calculate_vector(beg, end):
        """
        Calculate vector from given points

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: Calculated vector
        :rtype: tuple
        """
        v_beg=Vector(*beg)
        v_end=Vector(*end)
        if v_beg.dim == v_end.dim:
            output = v_end-v_beg
            return tuple(output.values)
        else:
            raise ValueError("Różne wymiary wektorów")

    @classmethod
    def from_points(cls, beg, end):
        """"""
        """
        Generate vector from given points.

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: New vector
        :rtype: tuple
        """
        v_beg=Vector(*beg)
        v_end=Vector(*end)
        if v_beg.dim == v_end.dim:
            return v_end-v_beg
        else:
            raise ValueError("Różne wymiary wektorów")


if __name__ == '__main__':
    v1 = Vector(1,2,3)
    v2 = Vector(1,2,3)
    assert v1 + v2 == Vector(2,4,6)
    assert v1 - v2 == Vector(0,0,0)
    assert v1 * 2 == Vector(2,4,6)
    assert v1 * v2 == 14
    assert len(Vector(3,4)) == 5.
    assert Vector.calculate_vector([0, 0, 0], [1,2,3]) == (1,2,3)
    assert Vector.from_points([0, 0, 0], [1,2,3]) == Vector(1,2,3)
