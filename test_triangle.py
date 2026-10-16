import math
import pytest
from triangle import is_valid_triangle, classify_triangle

"""Copilot suggested: Yes
    Suggestion KEPT
    Reason: The code correctly tests for an Equilateral triangle 
    where all sides are equal"""
def test_Equilateral_triangle():
    # Test equilateral triangle
    assert classify_triangle(5, 5, 5) == "Equilateral"

"""Copilot suggested: Yes
    Suggestion KEPT
    Reason: The code correctly tests for an Isosceles triangle 
    where two sides are equal"""
def test_Isosceles_triangle():
    # Test isosceles triangle
    assert classify_triangle(5, 5, 3) == "Isosceles"
    assert classify_triangle(5, 3, 5) == "Isosceles"
    assert classify_triangle(3, 5, 5) == "Isosceles"

"""Copilot suggested: Yes
    Suggestion EDITED
    reason: this code was also used to test for a right scalene triangle.
    thus, this test was supposed to expect the output of a Right scalene 
    triangle. Instead, it expects the output of a scalene triangle, which
    is not correct. I edited the values used to test for a scalene triangle
    to be 3, 4, 6 instead of 3, 4, 5 to test for a purely scalene triangle.
"""
def test_Scalene_triangle():
    # Test scalene triangle
    assert classify_triangle(3, 4, 6) == "Scalene"

"""Copilot suggested: Yes
    Suggestion KEPT
    Reason: The code correctly tests for a right scalene triangle 
    where all sides are different and satisfies the pythagorean theorem"""
def test_Right_Scalene_triangle():
    # Test right scalene triangle
    assert classify_triangle(3, 4, 5) == "Right Scalene"

"""Copilot suggested: Yes
    Suggestion KEPT
    Reason: The code correctly tests for a right isosceles triangle 
    where two sides are equal and satisfies the pythagorean theorem.
    i checked that in python, math.sqrt(2) ** 2 comes out to 
    2.0000000000000004. But, since my classify_triangle method
    in the triangle.py class uses math.isclose(), this rounding error
    is solved through the use of a tolerance and this number is accpeted
    as a 2"""
def test_Right_Isosceles_triangle():
    # Test right isosceles triangle
    assert classify_triangle(1, 1, math.sqrt(2)) == "Right Isosceles"

"""Copilot suggested: Yes
    Suggestion KEPT
    Reason: the code correctly test for invalid cases where the triangle side
    are less than or equal to 0, the sum of any 2 sides are equal to the third side, or
    the sum of any 2 sides is less than the third side."""
def test_invalid_triangle():
    # Test invalid triangles
    assert classify_triangle(0, 4, 5) == "Invalid"
    assert classify_triangle(-1, 4, 5) == "Invalid"
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(1, 10, 12) == "Invalid"

"""copilot suggested: yes
    Suggestion EDIT
    Reason: Correctly tests the cases of a valid triangle. such as
    the right scalene triangle, the equilateral triangle and the 
    isosceles triangle. I wanted to be more sure so i added the test
    cases for the other types of triangles among the 1st 3 test cases
    github copilot suggested. I added the test cases for the pure scalence
     triangle, and a right isosceles triangle"""
def test_is_valid_triangle():
    # Test valid triangles
    assert is_valid_triangle(3, 4, 5) == True
    assert is_valid_triangle(5, 5, 5) == True
    assert is_valid_triangle(5, 5, 3) == True
    assert is_valid_triangle(2, 3, 4) == True
    assert is_valid_triangle(1, 1, math.sqrt(2)) == True


