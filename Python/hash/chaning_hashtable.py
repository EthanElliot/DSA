'''chaning hash table'''
from hashtable import HashTable


class ChainingHashTable(HashTable):
    """A simple chaning HashTable
    Note: requires the HashTable class from Hashtable 
    """

    def __init__(self, slots: int = 11) -> None:
        super().__init__(slots)
        self._table = [[] for i in range(self.n_slots)]

    def __contains__(self, item: any) -> bool:
        item_hash = self._hash(item)

        for value in self._table[item_hash]:
            if value == item:
                return True
        return False

    def store(self, item: any) -> None:
        '''stores an item in the hash table using chaning'''
        item_hash = self._hash(item)
        self._table[item_hash].append(item)
        self.n_items += 1
