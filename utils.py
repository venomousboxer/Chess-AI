
class heap_item:
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        return self.data[0] < other.data[0]


class tt_entry:
    __slots__ = ('lower_bound', 'upper_bound', 'move', 'depth')

    def __init__(self, lb, ub, move, depth):
        self.lower_bound = lb
        self.upper_bound = ub
        self.move = move
        self.depth = depth
