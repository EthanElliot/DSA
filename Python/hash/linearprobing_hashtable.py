from hashtable import HashTable


class LinearHashTable(HashTable):
    """A simple linear probing HashTable
    Note: requires the HashTable class from Hashtable 
    """

    def __contains__(self, item: any) -> bool:
        found = False
        first_hash = self._hash(item)

        if self._table[first_hash] == item:
            found = True

        current_index = (first_hash+1) % self.n_slots
        while not found and self._table[current_index] is not None:
            if current_index == first_hash:
                break
            elif self._table[current_index] == item:
                found = True
            else:
                current_index = (current_index+1) % self.n_slots
        return found

    def store(self, item: any) -> None:
        '''stores an item in the hash table using chaning'''
        if self.is_full():
            raise IndexError('Hash table is full')

        current_index = self._hash(item)
        while self._table[current_index] is not None:
            current_index = (current_index+1) % self.n_slots
        self._table[current_index] = item

    def is_full(self) -> bool:
        '''returns true if the hashtable is full'''
        return self.n_slots == self.n_items

    def delete(self, index: int) -> None:
        '''deletes item from index in the hash table'''
        if index > self.n_slots or index < 0:
            raise IndexError("Index out of range")
        self._table[index] = None
