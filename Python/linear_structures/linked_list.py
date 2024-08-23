'''linked list'''


class Node(object):
    '''Node class for a node of a linked list'''

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList():
    '''Linked list class'''

    def __init__(self) -> None:
        self.head = None

    def __len__(self) -> int:
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def __str__(self) -> str:
        string = 'Head '

        if self.is_empty():
            string += '-> None'
            return string

        current_node = self.head
        while current_node:
            string += f'-> {current_node.data} '
            current_node = current_node.next

        return string

    def add(self, item: any) -> None:
        '''Add and item to the linked list
        Note: adds node to the beggining or the head of the linked list.'''
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def remove(self, item: any) -> None:
        '''Finds and removes an item from list'''
        found = False
        current = self.head
        previous = None
        while not found and current:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if not found:
            raise IndexError("Item not found.")
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def pop(self) -> None:
        '''Pops first item from linked list'''
        if self.is_empty():
            raise IndexError("Can't pop from empty list.")

        temp = self.head.next
        self.head = temp

    def contains(self, item: any) -> bool:
        '''Checks if the item is in the linked list and returns true if it is false otherwise'''
        found = False
        current_node = self.head
        while not found and current_node:
            if current_node.data == item:
                found = True
            current_node = current_node.next
        return found

    def is_empty(self) -> bool:
        '''returns true if the list is empty'''
        return self.head is None
