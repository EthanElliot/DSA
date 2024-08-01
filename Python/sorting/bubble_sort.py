'''Sequential search
A sorting algorithm where the maximum is filtered up to the front of the list

Time complexity: O(n^2)
'''


def bubble_sort(nums: list[int]):
    '''Function for bubble sort takes a list of ints.
    Returns a sorted list.

    >>> nums = [5,6,7,4,3,8,2,1,9,10]
    >>> bubble_sort(nums)
    >>> nums
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 9, 1]
    >>> bubble_sort(nums)
    >>> nums
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10]
    '''
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


if __name__ == "__main__":
    nums = [5, 10, 7, 4, 3, 8, 2, 1, 9, 6]
    bubble_sort(nums)
    print(nums)
