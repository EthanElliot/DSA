#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int value;
    struct node *next;
} node_t;

void insert_node(int value);
void delete_node();
void print_linked_list(node_t *head);

node_t *head = NULL;

int main()
{
    print_linked_list(head);

    insert_node(7);

    insert_node(9);

    insert_node(4);
    print_linked_list(head);
    delete_node();
    delete_node();
    print_linked_list(head);
}

// inserts node at the front of the linked list
void insert_node(int value)
{
    node_t *new = (node_t *)malloc(sizeof(node_t));

    if (new == NULL)
    {
        printf("\nCannot create the Node");
        return;
    }

    new->value = value;
    new->next = head;
    head = new;
}

// inserts node from the front of the linked list
void delete_node()
{
    if (head == NULL)
    {
        printf("\nlist is empty");
        return;
    }
    node_t *temp = head;
    head = head->next;
    free(temp);
}

void print_linked_list(node_t *head)
{

    node_t *current = head;
    printf("\nstart -> ");
    while (current != NULL)
    {
        printf("%d -> ", current->value);
        current = current->next;
    }
    printf("NULL \n");
}