# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertNotEqual(classifyTriangle(5,3,4),'Right','5,3,4 is Not Right triangle')

    def testEquilateralA(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesA(self):
        self.assertEqual(classifyTriangle(5, 3, 3), "Isosceles", "5,3,3 should be isosceles")

    def testIsoscelesB(self):
        self.assertEqual(classifyTriangle(7, 7, 2),"Isosceles", "7,7,2 should be isosceles")

    def testScaleneA(self):
        self.assertEqual(classifyTriangle(4, 7, 3), "Scalene", "4,7,3 should be scalene")

    def testEquilateralB(self):
        self.assertEqual(classifyTriangle(3, 3, 3), "Equilateral", '3,3,3 should be equilateral')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle("a", 6, 6), "InvalidInput")

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle("a", "4", 6), "InvalidInput")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

