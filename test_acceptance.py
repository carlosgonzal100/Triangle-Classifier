from triangle import classify_triangle

"""Acceptance Criteria 1:
    given 3 side lengths from the customer(3,3,3), 
    when the 3 sides are tested for what the shape of the build will be,
    then return a message saying Equilateral"""

"""Acceptance criteria 2:
    given 3 side lengths from the customer(3, 4, 5),
    when the 3 sides are tested for a right angle 
    then return a message that says Right Scalene"""

"""Acceptance criteria 3:
    given the 3 side lengths from the customer(-1, 1, 3),
    when the 3 sides are tested to check if its buildable or not,
    then return a message saying Invalid instead of crashing"""

def test_acceptance_criteria():

    #Criteria 1
    assert classify_triangle(3,3,3) == "Equilateral"

    #Criteria 2
    assert classify_triangle(3,4,5) == "Right Scalene"

    #Criteria 3
    assert classify_triangle(-1,1,3) == "Invalid"