"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_n_positive(n, number):
    """
    No iteration needed
    formula: n(n+1)/2
    https://brilliant.org/wiki/sum-of-n-n2-or-n3/#sum-of-first-n-positive-integers
    https://gmatclub.com/forum/sum-of-n-positive-integers-formula-for-consecutive-integers-163301.html
    """
    how_many_n_items = number / n
    return n * (how_many_n_items * (how_many_n_items + 1)/2)

sum_each_3d = sum_n_positive(3, 1000)
sum_each_5th = sum_n_positive(5, 1000)
sum_intersections = sum_n_positive(3*5, 1000)
print 'Formula only: %s' % str(sum_each_3d + sum_each_5th - sum_intersections)


# iterate over list , sum only items which match (number % 3)
# Complexity: O(n)
sum_a = sum([number for number in range(1, 1000) if number % 3 == 0 or number % 5 == 0])
print 'Iterate over list: %s' % sum_a


def func(n, m, arr):
    """
    Answer 2: Sum only each 3d and 5th element of arr
    Complexity: O(n/3)
    """
    left_step = n
    right_step = m
    # Unique items: each 3d and 5th
    items_to_sum = set()
    while n <= len(arr):
        items_to_sum.add(arr[n - 1])
        n += left_step
        if m >= len(arr):
            continue
        items_to_sum.add(arr[m - 1])
        m += right_step
    return sum(items_to_sum)

sum_b = func(3, 5, list(range(1, 1000)))
print 'Iterate over each 3d: %s' % sum_b
assert sum_a == sum_b, '{} is not equal {}'.format(sum_a, sum_b)
