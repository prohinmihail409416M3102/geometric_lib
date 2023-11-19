import unittest
import triangle

class TriangleTests(unittest.TestCase):
    def test_degenerate_TriangleArea(self):
        self.assertEqual(triangle.area(1000, 0), 0) #degenerate
    def test_normal_TriangleArea(self):
        self.assertEqual(triangle.area(5, 4), 10) #normal
    def test_decimal_TriangleArea(self):
        self.assertEqual(triangle.area(3.14, 2.72), 4.2704) #decimal
    def test_fraction_TriangleArea(self):
        self.assertEqual(triangle.area(2/3, 25/7), 25/21) #fraction
    def test_big_args_TriangleArea(self):
        self.assertEqual(triangle.area(10 ** 2000, 10 ** 1000), 5 * 10 ** 2999) #big args
    
    def test_error_if_1st_negative_arg_TriangleArea(self):
        self.assertRaises(ValueError, triangle.area, -100, 100) #1st negative 
    def test_error_if_2nd_negative_arg_TriangleArea(self):       
        self.assertRaises(ValueError, triangle.area, 314, -159) #2nd negative
    def test_error_if_both_negative_args_TriangleArea(self):
        self.assertRaises(ValueError, triangle.area, -20, -34) #both negative
    
    def test_error_if_1st_non_Q_arg_TriangleArea(self):
        self.assertRaises(TypeError, triangle.area, "input", 10) #1st non-Q not(int/float/Fraction/Decimal)
    def test_error_if_2nd_non_Q_arg_TriangleArea(self):
        self.assertRaises(TypeError, triangle.area, 10, "input") #2nd non-Q
    def test_error_if_both_non_Q_args_TriangleArea(self):
        self.assertRaises(TypeError, triangle.area, "hello", "world") #both non-Q
        
        
    def test_degenerate_TrianglePerimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 7), 14) #degenerate
    def test_normal_TrianglePerimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12) #normal
    def test_decimal_TrianglePerimeter(self):
        self.assertEqual(triangle.perimeter(3.14, 2.72, 1.62), 7.48) #decimal
    def test_fraction_TrianglePerimeter(self):
        self.assertEqual(triangle.perimeter(2/3, 3/7, 5/9), 104/63) #fraction
    
    def test_error_if_1st_negative_arg_TrianglePerimeter(self):
        self.assertRaises(ValueError, triangle.perimeter, -10, 10, 10) #1st negative   
    def test_error_if_2nd_negative_arg_TrianglePerimeter(self):     
        self.assertRaises(ValueError, triangle.perimeter, 10, -10, 10) #2nd negative
    def test_error_if_3rd_negative_arg_TrianglePerimeter(self):
        self.assertRaises(ValueError, triangle.perimeter, 10, 10, -10) #3rd negative
    def test_error_if_all_negative_args_TrianglePerimeter(self):
        self.assertRaises(ValueError, triangle.perimeter, -10, -10, -10) # all negative
        
    def test_error_if_1st_non_Q_arg_TrianglePerimeter(self):
        self.assertRaises(TypeError, triangle.perimeter, "input", 10, 10) #1st non-Q
    def test_error_if_2nd_non_Q_arg_TrianglePerimeter(self):
        self.assertRaises(TypeError, triangle.perimeter, 10, "input", 10) #2nd non-Q
    def test_error_if_3rd_non_Q_arg_TrianglePerimeter(self):
        self.assertRaises(TypeError, triangle.perimeter, 10, 10, "input") #3rd non-Q
    def test_error_if_all_non_Q_args_TrianglePerimeter(self):
        self.assertRaises(TypeError, triangle.perimeter, "hello", "world", "!") #all non-Q
        
if __name__ == "__main__":
  unittest.main()