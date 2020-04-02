from bubble_sort import *

def test_bubble_sort():
    assert bubble_sort([1, 4, 3, 7, 9]) == [1, 3, 4, 7, 9]
    assert bubble_sort([9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9]
    assert bubble_sort([0, 7, 6, 5, 8]) == [0, 5, 6, 7, 8]
    assert bubble_sort([-1, -2, -3, 0]) == [-3, -2, -1, 0]
    assert bubble_sort([6, -3, -9, -7]) == [-9, -7, -3, 6]
