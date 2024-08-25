#include <stdio.h>
#include <stdlib.h>

void selection_sort(int *list, int size);

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

    selection_sort(list, size);

    printf("The sorted list is:\n");
    for (int i = 0; i < size; i++)
    {
        printf("%d\n", list[i]);
    }

    free(list);
}

void selection_sort(int *list, int size)
{
    for (int i = 0; i < size; i++)
    {
        int min_index, temp;

        min_index = i;
        for (int j = i; j < size; j++)
        {
            if (list[j] < list[min_index])
            {
                min_index = j;
            }
        }
        temp = list[i];
        list[i] = list[min_index];
        list[min_index] = temp;
    }
}