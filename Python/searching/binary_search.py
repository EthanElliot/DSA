'''binary search
A Searching algorithm where half of the data is discared each time based
on if the target is less or greater than

Time complexity: O(log(n))
'''
import time
import random


def binary_search(nums: list[int], target: int):
    '''Function for binary search takes a list of sorted ints and a
    target. Returns True if target in nums, False otherwise.

    >>> binary_search([1,2,3,4,5,6,7,8,9,10],  6)
    True
    >>> binary_search([1,2,3,4,5,6,7,8,9,10],  11)
    False
    >>> binary_search([2,4,6,8,10,12,14,16,18,20],  11)
    False
    '''
    # initilise pointers at left and right of array
    PtrL = 0
    PtrR = len(nums)-1

    # if pointers have swapped positions the target must not be in list
    while PtrL < PtrR:

        # find element between the two pointers
        PtrM = (PtrR+PtrL)//2
        MidElement = nums[PtrM]

        # return True if the mid element is the target
        if MidElement == target:
            return True

        # if  mid element is less than the target the then the target must be on the left of the mid element
        if MidElement < target:
            PtrL = PtrM+1

        # if  mid element is greater than the target the then the target must be on the left of the mid element
        else:
            PtrR = PtrM-1

    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 3
    print(binary_search(nums, target))
