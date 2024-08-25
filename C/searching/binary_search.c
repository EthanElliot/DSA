#include <stdio.h>
#include <stdlib.h>

int binary_search(int *list, int size, int searchvalue);

int main(void)
{
    int size, searchvalue, found;
    printf("Number of elements in the list: ");
    scanf("%d", &size);

    int *list = (int *)malloc(sizeof(int) * size);

    printf("Enter %d integers for the list(Note: numbers should be in sorted order): \n", size);
    for (int i = 0; i < size; i++)
    {
        scanf("%d", &list[i]);
    }

    printf("What is the value you want to search for: ");
    scanf("%d", &searchvalue);

    found = binary_search(list, size, searchvalue);
    if (found == -1)
    {
        printf("Item was not in list\n");
    }
    else
    {
        printf("Item was found in list at index %d\n", found);
    }
}

int binary_search(int *list, int size, int searchvalue)
{
    int left, right, mid;

    left = 0;
    right = size - 1;
    while (left <= right)
    {
        mid = (left + right) / 2;

        if (list[mid] == searchvalue)
        {
            return mid;
        }
        else if (list[mid] < searchvalue)
        {
            left = mid + 1;
        }
        else
        {
            right = mid;
        }
    }

    return -1;
}