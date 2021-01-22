from functools import reduce
from math import atan


class Vector:
    """
    A vector class which has many useful vector methods.
    """
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
    
    def get_dir(self):
        return atan(self.y / self.x)
    
    def get_angle(self):
        return self.get_dir()

    def get_mag(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def set_mag(self, mag):
        ratio = mag / self.get_mag()
        self.mult(ratio)

    def add(self, vec):
        if isinstance(vec, Vector):
            self.x += vec.x
            self.y += vec.y
        
    def sub(self, vec):
        if isinstance(vec, Vector):
            self.x -= vec.x
            self.y -= vec.y
        
    def div(self, scalar, floor=False):
        if isinstance(scalar, int) or isinstance(scalar, float):
            if floor:
                self.x //= scalar
                self.y //= scalar
            else:
                self.x /= scalar
                self.y /= scalar

    def mult(self, val):
        if isinstance(val, int) or isinstance(val, float):
            self.x *= val
            self.y *= val
        
    def dot(self, vec):
        if isinstance(vec, Vector):
            return self * vec

    def __add__(self, vec):
        if isinstance(vec, Vector):
            return Vector(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec):
        if isinstance(vec, Vector):
            return Vector(self.x - vec.x, self.y - vec.y)

    def __truediv__(self, scalar):
        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vector(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar):
        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vector(self.x // scalar, self.y // scalar)

    def __mul__(self, val):
        if isinstance(val, Vector):
            return self.x * val.x + self.y * val.y
        elif isinstance(val, int) or isinstance(val, float):
            return Vector(self.x * val, self.y * val)

    def __eq__(self, vec):
        if isinstance(vec, Vector):
            return vec.x == self.x and vec.y == self.y

    def __ne__(self, vec):
        if isinstance(vec, Vector):
            return vec.x != self.x and vec.y != self.y

    def __repr__(self):
        return f"Vector at ({self.x}, {self.y}), angle: {self.angle}"


def is_prime(num):
    if num & 1 == 0:
        return True
    d = 3
    while d ** 2 <= num:
        if num % d == 0:
            return True
        d += 2
    return False


def find_factors(num, sort=True):
    step = 2 if num % 2 else 1
    factors = ([i, num // i] for i in range(1, int(num ** 0.5) + 1, step) if num % i == 0)
    rv = set(reduce(list.__add__, factors))
    return sorted(rv) if sort else rv
