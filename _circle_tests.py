import unittest
from math import pi
import circle

class CircleTests(unittest.TestCase):
    def test_degenerate_CircleArea(self):
        self.assertEqual(circle.area(0), 0) #degenerate
    def test_normal_CircleArea(self):
        self.assertEqual(circle.area(32), 1024 * pi) #normal
    def test_decimal_CircleArea(self):
        self.assertEqual(circle.area(2.72), 7.3984 * pi) #decimal
    def test_fraction_CircleArea(self):
        self.assertEqual(circle.area(23/13), pi * 529/169) #fraction
    def test_big_arg_CircleArea(self):
        self.assertEqual(circle.area(10 ** 1000), pi * 10 ** 2000) #big arg
    
    def test_error_if_negative_arg_CircleArea(self):
        self.assertRaises(ValueError, circle.area, -100) #negative        
    
    def test_error_if_non_Q_arg_CircleArea(self):
        self.assertRaises(TypeError, circle.area, "hello world") #non-Q
        
        
    def test_degenerate_CirclePerimeter(self):
        self.assertEqual(circle.perimeter(0), 0) #degenerate
    def test_normal_CirclePerimeter(self):
        self.assertEqual(circle.perimeter(32), pi * 64) #normal
    def test_decimal_CirclePerimeter(self):
        self.assertEqual(circle.perimeter(2.72), pi * 5.44) #decimal
    def test_fraction_CirclePerimeter(self):
        self.assertEqual(circle.perimeter(23/13), pi * (46/13)) #fraction
    def test_big_arg_CirclePerimeter(self):
        self.assertEqual(circle.perimeter(10 ** 1000), 2 * pi * 10 ** 1000) #big arg
        
    def test_error_if_negative_arg_CirclePerimeter(self):
        self.assertRaises(ValueError, circle.perimeter, -100) #negative
        
    def test_error_if_non_Q_arg_CirclePerimeter(self):
        self.assertRaises(TypeError, circle.perimeter, "hello world") # non-Q
        
if __name__ == "__main__":
  unittest.main()