#Academix Integrity statement
#Name: Zhenyi He
#Student ID: 521332
#Email: 521332@learning.eynesbury.edu.au
#This program is my own work as defined by the Academic Integrity
import unittest
from temperature_converter import *

class TestConverter(unittest.TestCase):

    def test_fahrenheit_to_celsius(self):
        # Test freezing temperature
        self.assertEqual(f_to_c(32), 0)
        # Test boiling temperature
        self.assertEqual(f_to_c(212), 100)
        # Test float
        self.assertAlmostEqual(f_to_c(31.0), -0.5555555555)
        # Test errors
        self.assertRaises(TypeError, f_to_c, 'freezing')

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(c_to_f(0), 32)
        self.assertEqual(c_to_f(100), 212)
        self.assertAlmostEqual(c_to_f(-0.5555555555), 31.0)
        self.assertRaises(TypeError, c_to_f, "freezing")

unittest.main()