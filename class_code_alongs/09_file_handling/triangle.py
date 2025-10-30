from numbers import Number

class Triangle:
    # x & y optional
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        if not isinstance(value, Number):
            raise TypeError("must be a number")
        self._base = value

        if value <= 0:
            raise ValueError("base must be larger than zero")
        self._base = value


    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, Number):
            raise TypeError("must be a number")
        self._base = value


    @property
    def area(self):
        pass

    #@property
    #def perimeter(self):
    #    pass

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __repr__(self):
        pass


