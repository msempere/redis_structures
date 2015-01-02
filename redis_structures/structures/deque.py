
from base import Base

class Deque(Base):

    def front_pop(self):
        return self._loads(self.redis.rpop(self.name))

    def back_pop(self):
        return self._loads(self.redis.lpop(self.name))

    def back_push(self, item):
        try:
            self.redis.lpush(self.name, self._dumps(item))
            return True
        except:
            return False

    def front_push(self, item):
        try:
            self.redis.rpush(self.name, self._dumps(item))
            return True
        except:
            return False

    def addAll(self, collection=[], back=True):
        assert type(collection) == list
        with self.redis.pipeline() as pipe:
            for item in collection:
                try:
                    if back:
                        pipe.lpush(self.name, self._dumps(item))
                    else:
                        pipe.rpush(self.name, self._dumps(item))
                except:
                    continue
            pipe.execute()

    def next(self):
        try:
            got = self.front_pop()
            if got:
                return got
            raise StopIteration
        except:
            raise StopIteration

