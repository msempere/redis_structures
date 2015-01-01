
from base import Base

class PriorityQueue(Base):

    def __len__(self):
        return self.redis.zcard(self.name)

    def content(self):
        return [(self._loads(element), score) for element, score in self.redis.zrange(self.name, 0, -1, withscores=True)]

    def push(self, element, score):
        assert element
        assert type(score) == float
        try:
            self.redis.zadd(self.name, score, self._dumps(element))
            return True
        except:
            return False

    def pop(self):
        with self.redis.pipeline() as pipe:
            try:
                # from http://sunilarora.org/redis-lua-scripting/
                # simulating ZPOP
                pipe.zrevrange(self.name, 0, 0, withscores=True)
                pipe.zremrangebyrank(self.name, -1, -1)
                got = pipe.execute()

                if got:
                    element, score = got[0][0]
                    return (self._loads(element), score)
                else:
                    return (None, None)
            except:
                return (None, None)

    def addAll(self, collection=[]):
        assert type(collection) == list

        with self.redis.pipeline() as pipe:
            for element in collection:
                assert type(element) == tuple
                assert type(element[1]) == int or type(element[1] == float)
                try:
                    pipe.zadd(self.name, element[1], self._dumps(element[0]))
                except:
                    continue
            pipe.execute()

    def next(self):
        try:
            got = self.pop()
            if got[0] and got[1]:
                return got
            raise StopIteration
        except:
            raise StopIteration
