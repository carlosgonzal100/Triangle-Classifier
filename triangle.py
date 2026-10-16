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

#Prompt used: the docustring for the is_invalid_triangle function
#wrote the valid function body as a suggestion of code. i then 
#pressed that to autocomplete and kept its suggestion.