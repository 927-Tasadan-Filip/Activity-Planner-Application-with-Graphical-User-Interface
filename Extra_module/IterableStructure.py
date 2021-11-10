class IterableDataStruct(object):
    class MyIterator:
        def __init__(self, col):
            self._colection = col
            self._index = 0

        def __next__(self):
            if self._index < len(self._colection._record):
                self._index += 1
                return self._colection._record[self._index - 1]
            raise StopIteration

    def __init__(self):
        self._record = []

    def __iter__(self):
        return self.MyIterator(self)

    def __getitem__(self, index):
        return self._record[index]

    def __delitem__(self, index):
        del self._record[index]

    def append_iter(self, new_entity):
        self._record.append(new_entity)

    def get_length(self):
        return len(self._record)

