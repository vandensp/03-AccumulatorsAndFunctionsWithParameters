"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Samuel VanDenburgh.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math as m

def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_cosines()
    run_test_sum_square_roots()


def run_test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # -------------------------------------------------------------------------
    # Done: 2. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')

    #Test 1
    expected = 0.13416
    actual = sum_cosines(3)
    print("Test 1")
    print("expected", expected)
    print('actual', actual)

    #Test 2
    expected = 1
    actual = sum_cosines(0)
    print("Test 2")
    print("expected", expected)
    print('actual', actual)

    #print(m.cos(1) + m.cos(2))

    #Test 3
    expected = 1.24155
    actual = sum_cosines(2)
    print("Test 3")
    print("expected", expected)
    print('actual', actual)

def sum_cosines(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------
    total = 0
    for k in range (n + 1):
        total = total + m.cos(k)

    return total

def run_test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # -------------------------------------------------------------------------
    # Done: 4. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')

    # Test 1
    expected = 11.8544
    actual = sum_square_roots(5)
    print("Test 1")
    print("expected", expected)
    print('actual', actual)

    # Test 2
    expected = 3.4142
    actual = sum_square_roots(2)
    print("Test 2")
    print("expected", expected)
    print('actual', actual)

    # Test 3
    expected = 5.8637
    actual = sum_square_roots(3)
    print("Test 3")
    print("expected", expected)
    print('actual', actual)

def sum_square_roots(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the square roots of the integers
       2, 4, 6, 8, ... 2n    inclusive, for the given n.
           So if n is 7, the last term of the sum is
           the square root of 14 (not 7).
    Side effects:   None.
    Example:
      If n is 5, this function returns
         sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
      which is about 11.854408.
    """
    # -------------------------------------------------------------------------
    # Done: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------
    total = 0
    for k in range (n + 1):
        total = total + m.sqrt(k * 2)
    return total

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
