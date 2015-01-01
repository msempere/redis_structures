from base import Base

class CircularBuffer(Base):
    def __init__(self, name, size, host='127.0.0.1', port=6379):
        super(CircularBuffer, self).__init__(name, host, port)
        self.size = size

    def __len__(self):
        return self.redis.llen(self.name)

    def push(self, item):
        assert item
        try:
            self.redis.lpush(self.name, self._dumps(item))
            self.redis.ltrim(self.name, 0, self.size - 1)
            return True
        except:
            return False

    def pop(self):
        return self._loads(self.redis.rpop(self.name))

    def addAll(self, collection=[]):
        assert type(collection) == list
        with self.redis.pipeline() as pipe:
            for element in collection:
                try:
                    pipe.lpush(self.name, self._dumps(element))
                    pipe.ltrim(self.name, 0, self.size - 1)
                except:
                    continue
            pipe.execute()

