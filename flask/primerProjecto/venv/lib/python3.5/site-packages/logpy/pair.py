
class pair(tuple):
    def __new__(cls, head, tail):
        obj = tuple.__new__(cls)
        obj.head = head
        obj.tail = tail
        return obj

    def __getitem__(self, key):
        if key == 0:
            return self.head
        raise NotImplementedError()

    def __getslice__(self, a, b):
        if a == 1 and b > 100:
            return self.tail
        raise NotImplementedError()

    def __iter__(self):
        yield self.head
        for i in self.tail:
            yield i


def test_pair():
    x = var()
    y = var()
    c = pair(x, y)
    assert c[0] == x
    assert c[1:] == y
    assert next(iter(c)) == x

