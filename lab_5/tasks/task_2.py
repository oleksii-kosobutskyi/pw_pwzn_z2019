"""
Na (1 pkt.):
- Zaimplementuj klasy: Rectangle, Square, Circle dziedziczące z klasy Figure
oraz definiujące jej metody:
    - Rectangle powinien mieć dwa atrybuty odpowiadające bokom (a i b)
    - Klasa Square powinna dziedziczyć z Rectangle.
    - Circle ma posiadać tylko atrybut r (radius).
- Przekształć metody area i perimeter we własności (properties).
---------
Na (2 pkt.):
- Zwiąż ze sobą boki a i b klasy Square (tzn. modyfikacja boku a lub boku b
powinna ustawiać tę samą wartość dla drugiego atrybutu).
- Zaimplementuj metody statyczne pozwalające na obliczenie
pola (get_area) i obwodu (get_perimeter) figury
na podstawie podanych parametrów.
- Zaimplementuj classmethod "name" zwracającą nazwę klasy.
---------
Na (3 pkt.):
- Zaimplementuj klasę Diamond (romb) dziedziczącą z Figure,
po której będzie dziedziczyć Square,
tzn. Square dziediczy i z Diamond i Rectangle.
- Klasa wprowadza atrybuty przekątnych (e i f) oraz metody:
-- are_diagonals_equal: sprawdź równość przekątnych,
-- to_square: po sprawdzeniu równości przekątnych zwróci instancję
klasy Square o takich przekątnych lub None (jeżeli przekątne nie są równe).
- Zwiąż ze sobą atrybuty a, b, e i f w klasie Square.
"""
from numbers import Number
from math import pi, sqrt



class Figure:
    
    @property
    def area(self): # public
        raise NotImplementedError

    @property
    def perimeter(self): # public
        raise NotImplementedError

    @classmethod
    def name(cls): # public
        return cls.__name__

    def __str__(self): # magic
        return (
            f'{self.name()}: area={self.area:.3f}, '
            f'perimeter={self.perimeter:.3f}'
        )



class Circle(Figure):
    
    __r = 1 # private

    def __init__(self, r): # magic
        self.r = r

    @property
    def r(self): # public
        return self._r
    
    @r.setter
    def r(self, x): # public
        if isinstance(x, Number):
            self._r = x
        else:
            print("Not number value!")

    @property
    def area(self): # public
        return pi*self.r**2

    @property
    def perimeter(self): # public
        return 2*pi*self.r

    @staticmethod
    def get_area(radius): # public
        return pi*radius**2

    @staticmethod
    def get_perimeter(radius): # public
        return 2*pi*radius



class Rectangle(Figure):
    
    _a = 1
    _b = 1

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_a(self):
        return self._a
    def set_a(self, x):
        if isinstance(x, Number):
            self._a = x
        else:
            print("Not number value!")
    a = property(get_a, set_a)

    def get_b(self):
        return self._b
    def set_b(self, x):
        if isinstance(x, Number):
            self._b = x
        else:
            print("Not number value!")
    b = property(get_b, set_b)
    
    @property
    def area(self):
        return self.a*self.b
    
    @property
    def perimeter(self):
        return 2*(self.a+self.b)

    @staticmethod
    def get_area(a, b):
        return a*b

    @staticmethod
    def get_perimeter(a, b):
        return 2*(a+b)



class Diamond(Figure):
    _e = 1
    _f = 1

    def __init__(self, e, f):
        self._e = e
        self._f = f

    def get_e(self):
        return self._e
    def set_e(self, x):
        if isinstance(x, Number):
            self._e = x
        else:
            print("Not number value!")
    e = property(get_e, set_e)

    def get_f(self):
        return self._f
    def set_f(self, x):
        if isinstance(x, Number):
            self._f = x
        else:
            print("Not number value!")
    f = property(get_f, set_f)

    @property
    def area(self):
        return self.e*self.f/2
    
    @property
    def perimeter(self):
        return 4*sqrt((self.e**2+self.f**2)/4)

    @staticmethod
    def get_area(e,f):
        return e*f/2

    @staticmethod
    def get_perimeter(e,f):
        return 4*sqrt((e**2+f**2)/4)

    def are_diagonals_equal(self):
            return self.e==self.f

    def to_square(self):
        if self.are_diagonals_equal():
            a = self.e/sqrt(2)
            return Square(a)
        else:
            print("Not a square!")
            return None



class Square(Rectangle, Diamond):
    
    def __init__(self, a):
        self.a = a
        self.e = a*sqrt(2)
        
    def set_a(self, x):
        if isinstance(x, Number):
            self._a = x
            self._b = x
        else:
            print("Not number value!")
    a = property(Rectangle.get_a, set_a)
    
    def set_b(self, x):
        if isinstance(x, Number):
            self._b = x
            self._a = x
        else:
            print("Not number value!")
    b = property(Rectangle.get_b, set_b)

    def set_e(self, x):
        if isinstance(x, Number):
            self._e = x
            self._f = x
        else:
            print("Not number value!")
    e = property(Diamond.get_e, set_e)

    def set_f(self, x):
        if isinstance(x, Number):
            self._f = x
            self._e = x
        else:
            print("Not number value!")
    f = property(Diamond.get_f, set_f)

    @staticmethod
    def get_area(a):
        return a**2

    @staticmethod
    def get_perimeter(a):
        return 4*a



if __name__ == '__main__':
    kolo1 = Circle(1)
    assert str(kolo1) == 'Circle: area=3.142, perimeter=6.283'

    rec_1 = Rectangle(2, 4)
    assert str(rec_1) == 'Rectangle: area=8.000, perimeter=12.000'

    sqr_1 = Square(4)
    assert str(sqr_1) == 'Square: area=16.000, perimeter=16.000'

    diam_1 = Diamond(6, 8)
    assert str(diam_1) == 'Diamond: area=24.000, perimeter=20.000'

    diam_2 = Diamond(1, 1)
    assert str(diam_2) == 'Diamond: area=0.500, perimeter=2.828'

    sqr_3 = diam_2.to_square()
    assert str(sqr_3) == 'Square: area=0.500, perimeter=2.828'
    