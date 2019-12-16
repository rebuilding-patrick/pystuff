
from threading import Lock


class Messenger:
   def __init__(self):
      self.lock = Lock()
      self.messages = []
        
   def give(self, message):
      #self.lock.acquire() Single operation doesn't need a lock
      self.messages.append(message)
      #self.lock.release()
        
   def get(self):
      self.lock.acquire()
      messages = self.messages
      self.messages = []
      self.lock.release()
      return messages

