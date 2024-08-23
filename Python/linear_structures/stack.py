'''Stack'''


class stack(object):
    '''Provides a stack with associated stack operations.
    Internally the stack is stored as plain Python list.'''

    def __init__(self) -> None:
        self._data = []

    def push(self, item: any) -> None:
        '''push new element to stack'''
        self._data.append(item)

    def pop(self) -> any:
        '''pop element from top of stack'''
        return self._data.pop()

    def peek(self) -> any:
        '''returns what element is on the top of the stack'''
        if self.is_empty():
            raise IndexError('Can\'t pop from empty stack!')
        return self._data[-1]

    def is_empty(self) -> bool:
        '''returns true if stack is empty'''
        return not self._data

    def __str__(self) -> bool:
        return 'Bottom -> '+self._data+' <- Top'

    def __len__(self) -> int:
        return len(self._data)
