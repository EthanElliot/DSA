'''Sequential search
A sorting algorithm where the minium is found and put to the start of the list.

Time complexity: O(n^2)
'''


def selection_sort(nums: list[int]):
    '''Function for selection sort takes a list of ints.
    Returns a sorted list.

    >>> nums = [5,6,7,4,3,8,2,1,9,10]
    >>> selection_sort(nums)
    >>> nums
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> selection_sort(nums)
    >>> nums
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    '''
    for i in range(len(nums)):
        minimum_index = i  # index of the minimum element from i to len(nums-1)
        for j in range(i, len(nums)):
            if nums[j] < nums[minimum_index]:
                minimum_index = j
        nums[i], nums[minimum_index] = nums[minimum_index], nums[i]


if __name__ == "__main__":
    nums = [5, 6, 7, 4, 3, 8, 2, 1, 9, 10]
    selection_sort(nums)
    print(nums)
