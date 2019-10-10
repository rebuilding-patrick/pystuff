

class SpatialHash:
    def __init__(self, size):
        self.size = size
        self.grid = {}

    def hash(self, x, y):
        x = int(x / self.size)
        y = int(y / self.size)
        return (x, y)

    def add(self, x, y, value):
        key = self.hash(x, y)
        self.add_key(key, value)

    def add_key(self, key, value):
        if key in self.grid:
            self.grid[key].append(value)
        else:
            self.grid[key] = [value]

    def get(self, x, y):
        key = self.hash(x, y)
        return self.get_key(key)

    def get_key(self, key):
        results = []
        if key in self.grid:
            results = self.grid[key]
        return results

    def get_near(self, x, y, distance):
        key = self.hash(x, y)
        return self.get_near_key(key, distance)

    def get_near_key(self, key, distance):
        x_min = key[0] - distance
        x_max = key[0] + distance
        y_min = key[1] - distance
        y_max = key[1] + distance
        results = []
        for x in range(x_min, x_max):
            for y in range(y_min, y_max):
                bucket = self.get_key((x, y))
                for item in bucket:
                    results.append(item)

        return results

    def empty(self, x, y):
        key = self.hash(x, y)
        return self.empty_key(key)

    def empty_key(self, key):
        results = []
        if key in self.grid:
            results = self.grid[key]
            del self.grid[key]

        return results

    def remove(self, x, y, value):
        key = self.hash(x, y)
        return self.remove_key(key, value)

    def remove_key(self, key, value):
        results = False
        if key in self.grid:
            if value in self.grid[key]:
                self.grid[key].remove(value)
                results = True

        return results

    def find(self, value):
        results = False
        for key in self.grid:
            if value in self.grid[key]:
                results = key
                break

        return results
