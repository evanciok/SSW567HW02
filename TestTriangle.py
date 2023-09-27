# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

from datetime import datetime
def my_brand(assignment):
  datetime_obj = datetime.now()
  datetime_string = datetime_obj.strftime("%d/%m/%Y %H:%M:%S")
  print("=*=*=*= Evan Ciok =*=*=*=")
  print("=*=*=*= 2023F SSW 567-A =*=*=*=")
  print("=*=*=*= " + assignment + " =*=*=*=")
  print("=*=*=*= " + datetime_string + " =*=*=*=")
assignment_name = "HW 02a"

import unittest
from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidBigA(self): 
        self.assertEqual(classifyTriangle(205,190,150),'InvalidInput','205 > 200 A is too large')

    def testInvalidBigB(self): 
        self.assertEqual(classifyTriangle(190,205,150),'InvalidInput','205 > 200 B is too large')
    
    def testInvalidBigC(self): 
        self.assertEqual(classifyTriangle(190,150,205),'InvalidInput','205 > 200 C is too large')
    
    def testInvalidSmallA(self): 
        self.assertEqual(classifyTriangle(-5,3,4),'InvalidInput','-5 < 0 A is too small')

    def testInvalidSmallB(self): 
        self.assertEqual(classifyTriangle(3,-5,4),'InvalidInput','-5 < 0 B is too small')

    def testInvalidSmallC(self): 
        self.assertEqual(classifyTriangle(3,4,-5),'InvalidInput','-5 < 0 C is too small')
    
    def testInvalidIntA(self): 
        self.assertEqual(classifyTriangle('x',4,5),'InvalidInput','x is not int A is invalid')
    
    def testInvalidIntB(self): 
        self.assertEqual(classifyTriangle(4,'x',5),'InvalidInput','x is not int B is invalid')
    
    def testInvalidIntC(self): 
        self.assertEqual(classifyTriangle(4,5,'x'),'InvalidInput','x is not int C is invalid')

    def testInvalidTriangleA(self): 
        self.assertEqual(classifyTriangle(12,5,6),'NotATriangle','5+6 is not >= 12 A is too big')

    def testInvalidTriangleB(self): 
        self.assertEqual(classifyTriangle(5,12,6),'NotATriangle','5+6 is not >= 12 B is too big')

    def testInvalidTriangleC(self): 
        self.assertEqual(classifyTriangle(5,6,12),'NotATriangle','5+6 is not >= 12 C is too big')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(3,5,4),'Right','3,5,4 is a Right triangle')
    
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testEquilateralTriangle(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is an Equilateral Triangle')

    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(5,6,10),'Scalene','5,6,10 is a Scalene Triangle')

    def testIsoscelesTriangle(self): 
        self.assertEqual(classifyTriangle(5,5,8),'Isosceles','5,5,8 is an Isosceles Triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()