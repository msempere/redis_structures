
from base import Base

class Stack(Base):
    def pop(self):
        return self.loads(self.redis.lpop(self.name))

    def push(self, item):
        try:
            self.redis.lpush(self.name, self._dumps(item))
            return True
        except Exception as e:
            print e
            return False
