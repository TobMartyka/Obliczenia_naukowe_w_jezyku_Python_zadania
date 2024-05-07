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

def find_axis(v1, v2):
    v3 = v1.cross(v2)
    if v3.length() == 0:
        raise ValueError("v1 and v2 are parallel.")
    d = v3.length()
    v3.x, v3.y, v3.z =v3.x/d, v3.y/d, v3.z/d
    return v3

print(find_axis(Vector(2,0,0), Vector(0,3,0)))
