class Node:

    def __init__(self, info, nxt):
        self._info = info
        self._nxt = nxt

    def set_info(self, val):
        self._info = val

    def set_nxt(self, nxt):
        self._nxt = nxt

    def get_info(self):
        return self._info

    def get_nxt(self):
        return self._nxt

    def __str__(self):
        return f'Info: {self._info}'


class List:

    def __init__(self):
        self._head = None

    def append(self, value: int):
        if self._head is None:
            self._head = Node(value, None)
        else:
            p = self._head
            while p.get_nxt() is not None:
                p = p.get_nxt()
            p.set_nxt(Node(value, None))

    def __iter__(self):
        self._current = self._head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        x = self._current
        self._current = self._current.get_nxt()
        return x
