"""
Run unit tests with discovery (-m) or from __main__() with verbosity level 2
 - python -m unittest
 - python test_expressions.py

Output with verbosity level < 2:
================================
...........
----------------------------------------------------------------------
Ran 11 tests in 0.002s
OK
<unittest.runner.TextTestResult run=11 errors=0 failures=0>
"""
from unittest import TestCase
# from . import Expressions

from src.expressions.expressions import Expressions



"""
tested objects (objects "under test", "ut") as instances of the Expressions class
"""
ut1 = Expressions(Expressions.default_numbers)  # [4, 12, 3, 8, 17, 12, 1, 8, 7]
ut2 = Expressions([1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67, 6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8])
ut3 = Expressions([6, 67, 6, 8, 17, 3, 6, 8])
ut4 = Expressions([8, 3, 9])
ut5 = Expressions([1, 1, 1])
ut6 = Expressions([0, 0])
ut7 = Expressions([0])
ut8 = Expressions([])


class Test_case(TestCase):
    """
    Top-level class that inherits from class unittest.TestCase
    and injects test data into derived classes for test cases.
    Sub-classes are discovered as unit tests.
    """
    def setUp(self):
        self.ut1 = ut1
        self.ut2 = ut2
        self.ut3 = ut3
        self.ut4 = ut4
        self.ut5 = ut5
        self.ut6 = ut6
        self.ut7 = ut7
        self.ut8 = ut8


# disable tests by assigning Python's Abstract Base Class (ABC) to test
# case classes, which will not be discovered as unit tests
# Test_case_a = Test_case_b = Test_case_c = Test_case_d = \
# Test_case_e = Test_case_f = Test_case_g = Test_case_h = \
# Test_case_i = Test_case_j = Test_case_k = abc.ABC


# assign Test_case class (above) as subclass of unittest.TestCase and with
# attributes of tested objects (self.ut1...ut8)
# uncomment tests one after another as you progress with expressions
Test_case_a = Test_case   # test a) passes, solution is given in numbers.py
Test_case_b = Test_case
Test_case_c = Test_case
Test_case_d = Test_case
Test_case_e = Test_case
Test_case_f = Test_case
Test_case_g = Test_case
Test_case_h = Test_case
Test_case_i = Test_case
Test_case_j = Test_case
Test_case_k = Test_case


class TestCase_a_number_of_numbers(Test_case_a):
    # 
    # tests a): number of numbers tests (lengths of numbers lists)
    def test_a_number_of_numbers(self):
        self.assertEqual(self.ut1.a, 9)
        self.assertEqual(self.ut2.a, 22)
        self.assertEqual(self.ut3.a, 8)
        self.assertEqual(self.ut4.a, 3)
        self.assertEqual(self.ut5.a, 3)
        self.assertEqual(self.ut6.a, 2)
        self.assertEqual(self.ut7.a, 1)
        self.assertEqual(self.ut8.a, 0)


class TestCase_b_first_three_numbers(Test_case_b):
    # 
    # tests b): first three numbers
    def test_b_first_three_numbers(self):
        self.assertEqual(self.ut1.b, [4, 12, 3])
        self.assertEqual(self.ut2.b, [1, 4, 6])
        self.assertEqual(self.ut3.b, [6, 67, 6])
        self.assertEqual(self.ut4.b, [8, 3, 9])
        self.assertEqual(self.ut5.b, [1, 1, 1])
        self.assertEqual(self.ut6.b, [0, 0])
        self.assertEqual(self.ut7.b, [0])
        self.assertEqual(self.ut8.b, [])


class TestCase_c_last_three_numbers(Test_case_c):
    # 
    # tests c): last three numbers
    def test_c_last_three_numbers(td):
        td.assertEqual(td.ut1.c, [1, 8, 7])
        td.assertEqual(td.ut2.c, [67, 6, 8])
        td.assertEqual(td.ut3.c, [3, 6, 8])
        td.assertEqual(td.ut4.c, [8, 3, 9])
        td.assertEqual(td.ut5.c, [1, 1, 1])
        td.assertEqual(td.ut6.c, [0, 0])
        td.assertEqual(td.ut7.c, [0])
        td.assertEqual(td.ut8.c, [])


class TestCase_d_last_threeClass_in_reverse(Test_case_d):
    # 
    # tests d): last three numbers in reverse
    def test_d_last_threeClass_in_reverse(td):
        td.assertEqual(td.ut1.d, [7, 8, 1])
        td.assertEqual(td.ut2.d, [8, 6, 67])
        td.assertEqual(td.ut3.d, [8, 6, 3])
        td.assertEqual(td.ut4.d, [9, 3, 8])
        td.assertEqual(td.ut5.d, [1, 1, 1])
        td.assertEqual(td.ut6.d, [0, 0])
        td.assertEqual(td.ut7.d, [0])
        td.assertEqual(td.ut8.d, [])


class TestCase_e_odd_numbers(Test_case_e):
    # 
    # tests e): odd numbers, order must be preserved
    def test_e_odd_numbers(td):
        td.assertEqual(td.ut1.e, [3, 17, 1, 7])
        td.assertEqual(td.ut2.e, [1, 67, 23, 49, 67, 23, 37, 67, 19, 67])
        td.assertEqual(td.ut3.e, [67, 17, 3])
        td.assertEqual(td.ut4.e, [3, 9])
        td.assertEqual(td.ut5.e, [1, 1, 1])
        td.assertEqual(td.ut6.e, [])
        td.assertEqual(td.ut7.e, [])
        td.assertEqual(td.ut8.e, [])


class TestCase_f_number_of_odd_numbers(Test_case_f):
    # 
    # tests f): number of odd numbers
    def test_f_number_of_odd_numbers(td):
        td.assertEqual(td.ut1.f, 4)
        td.assertEqual(td.ut2.f, 10)
        td.assertEqual(td.ut3.f, 3)
        td.assertEqual(td.ut4.f, 2)
        td.assertEqual(td.ut5.f, 3)
        td.assertEqual(td.ut6.f, 0)
        td.assertEqual(td.ut7.f, 0)
        td.assertEqual(td.ut8.f, 0)


class TestCase_g_sum_of_odd_numbers(Test_case_g):
    # 
    # tests g): sum of odd numbers
    def test_g_sum_of_odd_numbers(td):
        td.assertEqual(td.ut1.g, 28)
        td.assertEqual(td.ut2.g, 420)
        td.assertEqual(td.ut3.g, 87)
        td.assertEqual(td.ut4.g, 12)
        td.assertEqual(td.ut5.g, 3)
        td.assertEqual(td.ut6.g, 0)
        td.assertEqual(td.ut7.g, 0)
        td.assertEqual(td.ut8.g, 0)


class TestCase_h_duplicateClass_removed(Test_case_h):
    # 
    # tests h): duplicate numbers removed - use set() to accept any order
    def test_h_duplicateClass_removed(td):
        td.assertEqual(set(td.ut1.h), {4, 12, 3, 8, 17, 1, 7})
        td.assertEqual(set(td.ut2.h), {1, 4, 6, 67, 8, 23, 34, 49, 37, 19})
        td.assertEqual(set(td.ut3.h), {6, 67, 8, 17, 3})
        td.assertEqual(set(td.ut4.h), {8, 3, 9})
        td.assertEqual(td.ut5.h, [1])
        td.assertEqual(td.ut6.h, [0])
        td.assertEqual(td.ut7.h, [0])
        td.assertEqual(td.ut8.h, [])


class TestCase_i_number_of_duplicate_numbers(Test_case_i):
    # 
    # tests i): number of duplicate numbers
    def test_i_number_of_duplicate_numbers(td):
        td.assertEqual(td.ut1.i, 2)
        td.assertEqual(td.ut2.i, 12)
        td.assertEqual(td.ut3.i, 3)
        td.assertEqual(td.ut4.i, 0)
        td.assertEqual(td.ut5.i, 2) # [1, 1, 1] has 2 duplicates 1
        td.assertEqual(td.ut6.i, 1) # [0, 0] has one duplicate number 0
        td.assertEqual(td.ut7.i, 0)
        td.assertEqual(td.ut8.i, 0)


class TestCase_j_ascending_squaredClass_no_duplicates(Test_case_j):
    # 
    # tests j): ascending list of squared numbers with no duplicates
    def test_j_ascending_squaredClass_no_duplicates(td):
        td.assertEqual(set(td.ut1.j), {1, 9, 16, 49, 64, 144, 289})
        td.assertEqual(set(td.ut2.j), {1, 16, 36, 64, 361, 529, 1156, 1369, 2401, 4489})
        td.assertEqual(set(td.ut3.j), {9, 36, 64, 289, 4489})
        td.assertEqual(set(td.ut4.j), {9, 64, 81})
        td.assertEqual(td.ut5.j, [1])
        td.assertEqual(td.ut6.j, [0])
        td.assertEqual(td.ut7.j, [0])
        td.assertEqual(td.ut8.j, [])


class TestCase_k_classifyClass_as_odd_even_empty(Test_case_k):
    # 
    # tests k): classify as "ODD_LIST", "EVEN_LIST" or "EMPTY_LIST" depending on numbers length
    def test_k_classifyClass_as_odd_even_empty(td):
        td.assertEqual(td.ut1.k, "ODD_LIST")
        td.assertEqual(td.ut2.k, "EVEN_LIST")
        td.assertEqual(td.ut3.k, "EVEN_LIST")
        td.assertEqual(td.ut4.k, "ODD_LIST")
        td.assertEqual(td.ut5.k, "ODD_LIST")
        td.assertEqual(td.ut6.k, "EVEN_LIST")
        td.assertEqual(td.ut7.k, "ODD_LIST")
        td.assertEqual(td.ut8.k, "EMPTY_LIST")
