import math

def is_valid_triangle(a, b, c) -> bool:
    """Any side ≤ 0, or triangle inequality fails 
    (includes the degenerate case: sum of two sides equals the third)
    should return False. Otherwise, return True."""
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True
#KEPT: this code was suggested by github copilot and is a 
#valid implementation of the checking if a triangle
#is truly a triangle.

#Prompt used: the docstring for the is_valid_triangle function
#wrote the valid function body as a suggestion of code. i then 
#pressed that to autocomplete and kept its suggestion.

def classify_triangle(a, b, c) -> str:
    """Return a string that describes a triangle based on the lengths of its sides.
    if the triangle is invalid, return "Invalid", 
    if all the triangles sides are equal, return "Equilateral",
    if exactly 2 sides are equal, return "Isosceles",
    if all sides are different, return "Scalene",
    Finally, check if the triangle satisfies the pythagorean theorem
    and uses a tolerance instead of == to check for equality. if the triangle also
    counts as a right triangle, add a prefix to the triangles type such as a 
    "Right Isosceles" or "Right Scalene". note that an equilateral
    triangle as all angles would be 60 degrees, meaning it is not possible for it to become
    a right triangle. 
    """
    if not is_valid_triangle(a, b, c):
        return "Invalid"
    
    # Check for right triangle using Pythagorean theorem
    sides = sorted([a, b, c])
    tolerance = 1e-9
    is_right = math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2, abs_tol=tolerance)
    
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    
    if is_right:
        triangle_type = f"Right {triangle_type}"
    
    return triangle_type

#KEPT:The code that was autocompleted to check for the types of triangles was correct 
#and correctly identifies the types of triangles. It also checks for right angles by 
#sorting all of the triangles sides, with all the sides being sorted and the largest 
#side being put as the last element in the list, which is the hypotenuse of the triangle.
#It also added a tolerance to handle rounding errors when checking for right triangles.

#EDIT: when the github copilot autocompleted the code for this function, i realized that it
#did not capitalize the triangle types that it returned, so i capitalized all the strings that 
#returned those triangle types as per the assignments instructions. This happened because my
#original docstring for the function had the triangle types in lowercase, so i edited both
#code and my docustring prompt to have the triangle types in uppercase. 