from collections.abc import Iterator


class Queue(Iterator):
    def __init__(self):
        self._data = []
        self.index = 0

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if len(self._data) != 0:
            return self._data.pop(0)
        else:
            return None

    def search(self, index):
        if index < 0 or index > len(self._data):
            raise IndexError("Invalid index")
        return self._data[index]

    def __next__(self):
        try:
            valor = self._data[self.index]
            self.index += 1
            return valor
        except IndexError:
            raise StopIteration
