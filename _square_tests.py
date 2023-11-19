import unittest
import square

class SquareTests(unittest.TestCase):
    def test_degenerate_SquareArea(self):
        self.assertEqual(square.area(0), 0) #degenerate
    def test_normal_SquareArea(self):
        self.assertEqual(square.area(32), 1024) #normal
    def test_decimal_SquareArea(self):
        self.assertEqual(square.area(2.72), 7.3984) #decimal
    def test_fraction_SquareArea(self):
        self.assertEqual(square.area(23/13), 529/169) #fraction
    def test_big_args_SquareArea(self):
        self.assertEqual(square.area(10 ** 1000), 10 ** 2000) #big arg

    def test_error_if_negative_arg_SquareArea(self):    
        self.assertRaises(ValueError, square.area, -100) #negative arg        
    def test_error_if_non_Q_arg_SquareArea(self):
        self.assertRaises(TypeError, square.area, "hello world") #non-Q arg
        
        
    def test_degenerate_SquarePerimeter(self):
        self.assertEqual(square.perimeter(0), 0) #degenerate
    def test_normal_SquarePerimeter(self):
        self.assertEqual(square.perimeter(32), 128) #normal
    def test_decimal_SquarePerimeter(self):
        self.assertEqual(square.perimeter(3.14), 12.56) #decimal
    def test_fraction_SquarePerimeter(self):
        self.assertEqual(square.perimeter(23/13), (92/13)) #fraction
    def test_big_arg_SquarePerimeter(self):
        self.assertEqual(square.perimeter(10 ** 1000), 4 * 10 ** 1000) #big arg
        
    def test_error_if_negative_arg_SquarePerimeter(self):
        self.assertRaises(ValueError, square.perimeter, -100) #negative arg
        
    def test_error_if_non_Q_arg_SquarePerimeter(self):
        self.assertRaises(TypeError, square.perimeter, "hello world") # non-Q arg
        
if __name__ == "__main__":
  unittest.main()