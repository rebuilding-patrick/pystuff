
class Index:
   def __init__(self):
      self.count = 0
      self.free = []
      
   def get(self):
      if len(self.free) == 0:
         self.count += 1
         return self.count
      else:
         value = self.free[-1]
         self.free.pop()
         return value
         
   def delete(value):
      if value >= self.count:
         self.free.append(value)
      
