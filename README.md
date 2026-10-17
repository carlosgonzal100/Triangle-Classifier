# Triangle Classifier

**Title:** Triangle Classifier  
**Course:** CSC325 Software Engineering  
**Professor:** Ilknur Aydin  
**Author:** Carlos Gonzalez, with the assistance of GitHub Copilot and CLAUDE.AI

## Description

A simple Python program that takes 3 lengths for each side of a triangle. When the 3 lengths are given,
it first determines if the 3 lengths make a valid triangle by checking if all the given lengths are greater than 0 and
it checks if any of the pairs, when summed together, are less than or equal to the remaining third length, deeming the triangle invalid.
If the triangle is valid, the program then gets its shape classified based on the lengths of its sides. If all 3 sides
are equal to each other, it is an **Equilateral** triangle. If any 2 sides match each other, it is an **isosceles** triangle.
If the 3 sides do not match each other, it is a **scalene** triangle. The program also checks if the triangle satisfies the
Pythagorean theorem and uses a tolerance(`math.isclose`) to check for any rounding errors (e.g., 2 compared to 2.0000000004), 
causing a prefix to be added to the shape of the triangle. For example, triangle lengths (3, 4, 5)
would make this triangle a **Right Scalene** triangle. Finally, the program uses 2 test files that use pystest. `test_triangle.py`
runs unit tests on `classify_triangle` and `is_valid_triangle` functions. The `test_acceptance` class also uses pytest to 
test acceptance criteria that I derived from a user prompt in the assignment.

---

## How to Run the Tests (Section written by Claude)

1. (Optional) Create and activate a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
3. Run all tests:
   ```
   python -m pytest -v
   ```
   Expected result: **8 passed** (7 unit tests in `test_triangle.py`, 1 acceptance test in `test_acceptance.py`).

---

## Equivalence Classes and Boundaries (Section written by Claude)

| Equivalence class | Example input | Expected output |
|---|---|---|
| Invalid – a side is 0 | (0, 4, 5) | Invalid |
| Invalid – a side is negative | (-1, 4, 5) | Invalid |
| Invalid – two sides sum to less than the third | (1, 10, 12) | Invalid |
| Equilateral – all sides equal | (5, 5, 5) | Equilateral |
| Isosceles – exactly two sides equal (in any position) | (5, 5, 3), (5, 3, 5), (3, 5, 5) | Isosceles |
| Scalene – all sides different, not right | (3, 4, 6) | Scalene |
| Right Scalene – all sides different, satisfies Pythagorean theorem | (3, 4, 5) | Right Scalene |
| Right Isosceles – non-integer sides | (1, 1, √2) | Right Isosceles |

**Boundaries:**
- **Side = 0:** the boundary between a positive (valid) side and a non-positive (invalid) side.
- **Degenerate triangle (sum of two sides equals the third), e.g. (1, 2, 3):** the boundary of the triangle inequality. 1 + 2 = 3 makes a flat line, so it is Invalid.
- **Floating-point Pythagorean check, e.g. (1, 1, √2):** `math.sqrt(2) ** 2` is `2.0000000000000004` in Python, so `==` would fail. A tolerance (`math.isclose`) is required.

---

## Why an Equilateral Triangle Can Never Be Right (My words)

An equilateral triangle has all angles at 60 degrees, meaning it is not possible for it to become a right triangle. 

---

## Copilot Review Log (Formated by Claude, Reasons Written by me)

| Test | Copilot-suggested? | Kept / Edited / Rejected | Why |
|---|---|---|---|

| test_Equilateral_triangle | Yes | Kept | The code correctly tests for an Equilateral triangle where all sides are equal (e.g., (3, 3, 3)). |

| test_Isosceles_triangle | Yes | Kept | The code correctly tests for an Isosceles triangle where two sides are equal (e.g., (5, 5, 3)). |

| test_Scalene_triangle | Yes | **Edited** | This code was also used to test for a right scalene triangle. Thus, this test was supposed to 
                                              expect the output of a Right scalene triangle. Instead, it expects the output of a scalene triangle, which
                                              is not correct. I edited the values used to test for a scalene triangle to be 3, 4, 6 instead of 3, 4, 5 to 
                                              test for a purely scalene triangle |

| test_Right_Scalene_triangle | Yes | Kept | The code correctly tests for a right scalene triangle where all sides are different and satisfies the Pythagorean theorem |

| test_Right_Isosceles_triangle | Yes | Kept | The code correctly tests for a right isosceles triangle where two sides are equal and satisfies the Pythagorean theorem.
                                                I checked that in Python, math.sqrt(2) ** 2 comes out to 2.0000000000000004. But since my classify_triangle method
                                                in the triangle.py class uses math.isclose(), this rounding error is solved through the use of a tolerance, and this number is accepted
                                                as a 2 |

| test_invalid_triangle | Yes | Kept | The code correctly tests for invalid cases where the triangle sides are less than or equal to 0, the sum of any 2 sides is equal to the third side, or
                                        the sum of any 2 sides is less than the third side. |

| test_is_valid_triangle | Yes | Edited | Correctly tests the cases of a valid triangle. such as the right scalene triangle, the equilateral triangle, and the 
                                          isosceles triangle. I wanted to be more sure, so I added the test cases for the other types of triangles among the 
                                          1st 3 test cases GitHub Copilot suggested. I added the test cases for the pure scalene triangle, and a right 
                                          isosceles triangle |

---

## Acceptance Criteria 

From the customer requirement (stained-glass studio):

**Acceptance Criteria 1:**
Given 3 side lengths from the customer(3,3,3),
when the 3 sides are tested to determine what the shape of the build will be,
then return a message saying Equilateral

**Acceptance criteria 2:**
given 3 side lengths from the customer(3, 4, 5),
when the 3 sides are tested for a right angle
then return a message that says Right Scalene

**Acceptance criteria 3:**
given the 3 side lengths from the customer(-1, 1, 3),
when the 3 sides are tested to check if it's buildable or not,
then return a message saying Invalid instead of crashing

These are checked in `test_acceptance.py` by `test_acceptance_criteria()`. Part 3 was written without GitHub Copilot or Claude.ai.

---

## AI-Use Disclosure

- **GitHub Copilot (VS Code autocomplete):** used to draft the bodies of `is_valid_triangle` and `classify_triangle` in `triangle.py`
  from my docstrings, and to draft the unit tests in `test_triangle.py`.
  
  - *What I verified:* I checked every suggestion against the assignment's spec table. I edited `classify_triangle` because Copilot
    returned lowercase strings (my original docstring asked for lowercase); the spec requires "Invalid", "Equilateral", "Right Scalene",
    etc. I edited `test_Scalene_triangle` because it used a right triangle (see the review log). I ran all tests with pytest.
    
- **Claude (Anthropic):** used as a step-by-step guide for project setup (virtual environment, git, GitHub, pytest),
- to explain concepts (triangle inequality, the Pythagorean theorem, floating-point tolerance), to review my code and tests against the spec,
- to suggest some extra test values (e.g., (2, 3, 4)), and to help format this README.
- 
  - *What I verified:* I wrote the acceptance criteria and acceptance test myself, ran every test, and checked each test value against the spec.
 
  - Just to be sure:
  

     The inline prompt fed to GitHub Copilot to create a draft for the is_valid_triangle function in the triangle.py file.
    It was completed using autocomplete:

    """Any side ≤ 0, or triangle inequality fails 
    (includes the degenerate case: sum of two sides equals the third)
    should return False. Otherwise, return True."""


    The inline prompt fed to GitHub Copilot to create a draft for the classify_triangle function in the triangle.py file.
    It was completed using autocomplete:

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
