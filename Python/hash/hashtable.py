'''basic hashtable class'''


class HashTable(object):
    '''Hash table object'''

    def __init__(self, slots: int = 11) -> None:
        self._table = [None for i in range(slots)]
        self.n_slots = slots
        self.n_items = 0

    def _hash(self, item: any) -> int:
        '''returns a hash value using a simple has function'''
        return hash(item) % self.n_slots

    def __str__(self) -> str:
        string = 'The Table \n'
        for (i, value) in enumerate(self._table):
            string += f'{i:5}  =  {str(value)}\n'
        return string

    def load_factor(self) -> float:
        '''returns the load factor of a hash table'''
        return self.n_items/self.n_slots
