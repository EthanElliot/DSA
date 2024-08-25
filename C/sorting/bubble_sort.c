#include <stdio.h>
#include <stdlib.h>

void bubble_sort(int *list, int size);

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

    bubble_sort(list, size);

    printf("The sorted list is:\n");
    for (int i = 0; i < size; i++)
    {
        printf("%d\n", list[i]);
    }

    free(list);
}

void bubble_sort(int *list, int size)
{
    for (int i = 0; i < size; i++)
    {
        int temp;

        for (int j = 0; j < size - i - 1; j++)
        {
            if (list[j] > list[j + 1])
            {
                temp = list[j];
                list[j] = list[j + 1];
                list[j + 1] = temp;
            }
        }
    }
}