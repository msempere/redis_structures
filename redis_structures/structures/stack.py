
from base import Base

class Stack(Base):

    def pop(self):
        return self._loads(self.redis.lpop(self.name))

    def push(self, item):
        assert item
        try:
            self.redis.lpush(self.name, self._dumps(item))
            return True
        except:
            return False
