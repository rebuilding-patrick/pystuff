

class SpatialHash:
  def __init__(self, size):
    self.grid = {}
    self.size = size
  
  def scale(self, x, y):
    return (x // self.size, y // self.size)

  def get_pos(self, x, y):
    return self.get(scale(x, y))
  
  def get(self, area):
    if area not in self.grid:
      self.grid[area] = []
    return self.grid[area]

  def add(self, item, area):
    if area not in self.grid:
      self.grid[area] = []
    self.grid[area].append(item)
    #print(f"SpatialHash: item added to {area[0]}:{area[1]} with {len(self.grid[area])} others")
  
  def delete(self, item, area):
    #print(f"SpatialHash: item deleted from {area[0]}:{area[1]}")
    if area in self.grid:
      if item in self.grid[area]:
        self.grid[area].remove(item)
        if len(self.grid[area]) == 0:
          #print(f"Grid is empty...")
          del self.grid[area]
        else:
          pass
          #print(f"{len(self.grid[area])} remain in grid...")
      else:
        pass
        #print(f"Item isn't in grid...")
    else:
      pass
      #print(f"Grid isn't there...")
      