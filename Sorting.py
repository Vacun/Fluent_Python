# list.sort sorted()

fruits = 'grape raspberry apple banana'.split()


sorted(fruits)

print(fruits)  # unchanged

sorted(fruits, reverse=True)

sorted(fruits, key=len)

sorted(fruits, key=len, reverse=True)

print(fruits)

fruits.sort()

print(fruits)  # changed

# Managing ordered sequences with bisect

import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

# given a test score, grade() returns the corresponding letter grade


def grade(score, boundries=[60, 70, 80, 90], grades='FDCBA'):
    position = bisect.bisect(boundries, score)
    grade = grades[position]
    print(grade)


def grade_(score, boundries=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(boundries, score)
    return(grades[i])

# this function is from 'bisect module documentation', look into
# docs for faster replacements for the index method

# INSERTING with bisect.insort

# Sorting is expensive, so once sorted, it's good to keep things
# that way when adding items
