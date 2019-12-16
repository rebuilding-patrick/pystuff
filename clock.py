
import ctypes
import time


class Clock:
   def __init__(self, rate):
      self.rate = rate
      self.time = ctypes.c_ulong(0) #Hack for free rollover
      self.last = time.time()

   def tick(self):
      now = time.time()
      if now - self.last > self.rate:
         self.last = now
         self.time.value += 1
         return True
      else:
         return False

   def value(self):
      now = time.time()
      value = now - self.last
      if value > self.rate:
         self.last = now
         self.time.value += 1
      return value

   def delta(self):
      now = time.time()
      value = now - self.last
      if value > self.rate:
         delta = value / self.rate
         self.time.value += 1
         self.last = now
         return delta
      else:
         return 0

