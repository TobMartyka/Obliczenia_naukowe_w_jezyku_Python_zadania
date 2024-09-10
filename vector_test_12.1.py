import math
import unittest

#vector from homework 6
class Vector:
    def __init__(self, x, y, z):
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
        return math.sqrt(self * self)  # Uses the dot product with itself to find the length

    def __hash__(self):
        return hash((self.x, self.y, self.z))


class TestVector(unittest.TestCase):

    def setUp(self):
        self.v = Vector(6, 3, 1)
        self.w = Vector(7, -4, 8)

    def test_repr(self):
        self.assertEqual(repr(self.v), "Vector(6,3,1)")
        self.assertEqual(repr(self.w), "Vector(7,-4,8)")

    def test_eq(self):
        self.assertNotEqual(self.v, self.w)
        v_copy = Vector(6, 3, 1)
        self.assertEqual(self.v, v_copy)

    def test_add(self):
        result = self.v + self.w
        expected = Vector(13, -1, 9)
        self.assertEqual(result, expected)

    def test_sub(self):
        result = self.v - self.w
        expected = Vector(-1, 7, -7)
        self.assertEqual(result, expected)

    def test_mul_vector(self):
        result = self.v * self.w
        expected = 38
        self.assertEqual(result, expected)

    def test_mul_scalar(self):
        result = self.v * 3
        expected = Vector(18, 9, 3)
        self.assertEqual(result, expected)

    def test_rmul_scalar(self):
        result = 3 * self.v
        expected = Vector(18, 9, 3)
        self.assertEqual(result, expected)

    def test_cross(self):
        result = self.v.cross(self.w)
        expected = Vector(28, -41, -45)
        self.assertEqual(result, expected)

    def test_length(self):
        result = self.v.length()
        expected = math.sqrt(46)
        self.assertAlmostEqual(result, expected)

    def test_hash(self):
        vector_set = {self.v, self.w, Vector(6, 3, 1)}
        self.assertEqual(len(vector_set), 2)


if __name__ == "__main__":
    unittest.main()
