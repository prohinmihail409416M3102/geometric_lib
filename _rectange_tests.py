import unittest
import rectangle

class RectangleTests(unittest.TestCase):
    def test_degenerate_RectangleArea(self):
        self.assertEqual(rectangle.area(1000, 0), 0) #degenerate
    def test_normal_RectangleArea(self):
        self.assertEqual(rectangle.area(32, 64), 2048) #normal
    def test_decimal_RectangleArea(self):
        self.assertEqual(rectangle.area(3.14, 2.72), 8.5408) #decimal
    def test_fraction_RectangleArea(self):
        self.assertEqual(rectangle.area(2/3, 25/7), 50/21) #fraction
    def test_big_args_RectangleArea(self):
        self.assertEqual(rectangle.area(10 ** 2000, 10 ** 1000), 10 ** 3000) #big args
    
    def test_error_if_1st_negative_arg_RectangleArea(self):
        self.assertRaises(ValueError, rectangle.area, -100, 100) #1st negative
    def test_error_if_2nd_negative_arg_RectangleArea(self):      
        self.assertRaises(ValueError, rectangle.area, 314, -159) #2nd negative
    def test_error_if_both_negative_args_RectangleArea(self):
        self.assertRaises(ValueError, rectangle.area, -20, -34) #both negative
    
    def test_error_if_1st_non_Q_arg_RectangleArea(self):
        self.assertRaises(TypeError, rectangle.area, "input", 10) #1st non-Q not(int/float/Fraction/Decimal)
    def test_error_if_2nd_non_Q_arg_RectangleArea(self):
        self.assertRaises(TypeError, rectangle.area, 10, "input") #2nd non-Q
    def test_error_if_both_non_Q_args_RectangleArea(self):
        self.assertRaises(TypeError, rectangle.area, "hello", "world") #both non-Q
        
        
    def test_degenerate_RectanglePerimeter(self):
        self.assertEqual(rectangle.perimeter(1000, 0), 2000) #degenerate
    def test_normal_RectanglePerimeter(self):
        self.assertEqual(rectangle.perimeter(32, 64), 192) #normal
    def test_decimal_RectanglePerimeter(self):
        self.assertEqual(rectangle.perimeter(3.14, 2.72), 11.72) #decimal
    def test_fraction_RectanglePerimeter(self):
        self.assertEqual(rectangle.perimeter(2/3, 25/7), 178/21) #fraction
    def test_big_args_RectanglePerimeter(self):
        self.assertEqual(rectangle.perimeter(10 ** 1000, 10 ** 1000), 4 * 10 ** 1000) #big args
    
    def test_error_if_1st_negative_arg_RectanglePerimeter(self): 
        self.assertRaises(ValueError, rectangle.perimeter, -100, 100) #1st negative
    def test_error_if_2nd_negative_arg_RectanglePerimeter(self):     
        self.assertRaises(ValueError, rectangle.perimeter, 314, -159) #2nd negative
    def test_error_if_both_negative_args_RectanglePerimeter(self): 
        self.assertRaises(ValueError, rectangle.perimeter, -20, -34) #both negative
    
    def test_error_if_1st_non_Q_arg_RectanglePerimeter(self):
        self.assertRaises(TypeError, rectangle.perimeter, "input", 10) #1st non-Q
    def test_error_if_2nd_non_Q_arg_RectanglePerimeter(self):
        self.assertRaises(TypeError, rectangle.perimeter, 10, "input") #2nd non-Q
    def test_error_if_both_non_Q_args_RectanglePerimeter(self):
        self.assertRaises(TypeError, rectangle.perimeter, "hello", "world") #both non-Q
        
if __name__ == "__main__":
  unittest.main()