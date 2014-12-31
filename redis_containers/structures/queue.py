
from base import Base

class Queue(Base):

    def pop(self):
        return self._loads(self.redis.rpop(self.name))

    def push(self, item):
        try:
            self.redis.lpush(self.name, self._dumps(item))
            return True
        except:
            return False
