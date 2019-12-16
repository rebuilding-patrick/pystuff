


class Pool:
    def __init__(self, size, value):
        self.size = size
        self.value = value

        self.index = 0
        self.pool = []
        for i in range(size):
            self.populate(i)

    def populate(self, i):
        self.pool.append(self.value())

    def resize(self, size):
        if size > 0:
            for i in range(size):
                self.populate(i)
        else:
            for i in range(size):
                self.pool.remove(-i)

    def get_item(self):
        item = self.pool[self.index]
        self.index += 1
        if self.index >= self.size:
            self.index = self.index % self.size
        return item

    def get(self):
        return self.get_item()


class LockedPool(Pool):
    def __init__(self, size, obj):
        Pool.__init__(self, size, obj)

        self.free_pool =[]
        for item in self.pool:
            self.free_pool.append(item)

    def get(self):
        if self.free_pool:
            item = self.free_pool[0]
            self.free_pool.remove(0)
        else:
            item = False

        return item

    def free(self, index):
        item = self.pool[index]
        if item not in self.free_pool:
            self.free_pool.append(self.pool[index])