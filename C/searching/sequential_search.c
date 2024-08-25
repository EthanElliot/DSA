#include <stdio.h>
#include <stdlib.h>

int sequential_search(int *list, int size, int searchvalue);

int main(void)
{
    int size, searchvalue, found;
    printf("Number of elements in the list: ");
    scanf("%d", &size);

    int *list = (int *)malloc(sizeof(int) * size);

    printf("Enter %d integers for the list: \n", size);
    for (int i = 0; i < size; i++)
    {
        scanf("%d", &list[i]);
    }

    printf("What is the value you want to search for: ");
    scanf("%d", &searchvalue);

    found = sequential_search(list, size, searchvalue);
    if (found == -1)
    {
        printf("Item was not in list\n");
    }
    else
    {
        printf("Item was found in list at index %d\n", found);
    }

    free(list);
}

int sequential_search(int *list, int size, int searchvalue)
{
    for (int i = 0; i < size; i++)
    {
        if (list[i] == searchvalue)
        {
            return i;
        }
    }

    return -1;
}