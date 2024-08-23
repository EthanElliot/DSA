"""Queue"""


class Queue(object):
    """Implements a Queue using a Python list.
    Internally the queue is stored as plain Python list. 
    >>> q = Queue()
    >>> q.enqueue('a')
    >>> q.dequeue()
    'a'
    >>> q.enqueue('a')
    >>> q.enqueue('b')
    >>> len(q)
    2
    >>> q.dequeue()
    'a'
    >>> len(q)
    1
    >>> q.dequeue()
    'b'
    >>> q.dequeue()
    Traceback (most recent call last):
    ...
    IndexError: Can't dequeue from an empty queue!
    >>> q.enqueue('a')
    >>> q.enqueue('b')
    >>> q.enqueue('c')
    >>> q.enqueue('a')
    >>> q.enqueue('d')
    >>> print(q)
    Front -> a  b  c  a  d <- Rear
    >>> q.dequeue()
    'a'
    >>> print(q)
    Front -> b  c  a  d <- Rear
    """

    def __init__(self) -> None:
        self._data = []

    def __str__(self) -> str:
        return 'Front -> '+'  '.join(self._data)+' <- Rear'

    def __len__(self) -> int:
        return len(self._data)

    def enqueue(self, item: any) -> None:
        '''adds and item to the queue'''
        self._data.append(item)

    def dequeue(self) -> any:
        '''pops the item at the start of the queue'''
        if self.is_empty():
            raise IndexError('Can\'t dequeue from an empty queue!')
        return self._data.pop(0)

    def peek(self) -> any:
        '''peeks at what is at the start of the queue'''
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        '''returns true if the list is empty'''
        return not self._data
