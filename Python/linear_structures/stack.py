'''Stack'''


class Stack(object):
    """Provides a stack with associated stack operations.
    Internally the stack is stored as plain Python list.

    >>> s = Stack()
    >>> s.push('a')
    >>> s.peek()
    'a'
    >>> s.pop()
    'a'
    >>> s.push('a')
    >>> s.push('b')
    >>> s.peek()
    'b'
    >>> len(s)
    2
    >>> s.pop()
    'b'
    >>> len(s)
    1
    >>> s.pop()
    'a'
    >>> s.pop()
    Traceback (most recent call last):
    ...
    IndexError: Can't pop from empty stack!
    >>> print(s.peek())
    None
    >>> s.push('a')
    >>> s.push('b')
    >>> s.push('c')
    >>> s.push('a')
    >>> print(s)
    Bottom -> a  b  c  a <- Top
    >>> s.pop()
    'a'
    >>> print(s)
    Bottom -> a  b  c <- Top
    """

    def __init__(self) -> None:
        self._data = []

    def push(self, item: any) -> None:
        '''push new element to stack'''
        self._data.append(item)

    def pop(self) -> any:
        '''pop element from top of stack'''
        if self.is_empty():
            raise IndexError('Can\'t pop from empty stack!')
        return self._data.pop()

    def peek(self) -> any:
        '''returns what element is on the top of the stack'''
        if self.is_empty():
            return None

        return self._data[-1]

    def is_empty(self) -> bool:
        '''returns true if stack is empty'''
        return not self._data

    def __str__(self) -> str:
        return 'Bottom -> '+'  '.join(self._data)+' <- Top'

    def __len__(self) -> int:
        return len(self._data)
