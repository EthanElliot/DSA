'''Sequential search
A Searching algorithm where each element of a list is checked until the target is found
starting from the begining of the list.

Time complexity: O(n)
'''


def sequential_search(nums: list[int], target: int):
    '''Function for sequential search takes a list of ints and a
    target. Returns True if target in nums, False otherwise.

    >>> sequential_search([1,2,3,4,5,6,7,8,9,10],  6)
    True
    >>> sequential_search([1,2,3,4,5,6,7,8,9,10],  11)
    False
    '''
    for num in nums:
        if num == target:
            return True

    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 6
    print(sequential_search(nums, target))
