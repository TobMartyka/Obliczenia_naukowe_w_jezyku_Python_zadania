import math
class Vector:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x},{self.y},{self.z})"

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vector(self.x * other, self.y * other, self.z * other)

    __rmul__ = __mul__

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)
    def length(self):
        return math.sqrt(self*self)
    def __hash__(self):
        return hash((self.x, self.y, self.z))

v = Vector(6, 3, 1)
w = Vector(7, -4, 8)
assert v != w
assert v + w == Vector(13, -1, 9)
assert v - w == Vector(-1, 7, -7)
assert v * w == 38
assert v.cross(w) == Vector(28, -41, -45)
assert v.length() == math.sqrt(46)
S = set([v, v, w])
assert len(S) == 2

print("Tests passed")
