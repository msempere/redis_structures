from redis_containers import Stack
from unittest import TestCase

class TestContainers(TestCase):

    def test_empty_stack(self):
        s = Stack('a_stack')
        assert len(s) == 0

    def test_push_stack(self):
        s = Stack('b_stack')
        s.push('a_element')
        assert len(s) == 1

    def test_pop_stack(self):
        s = Stack('c_stack')
        assert len(s) == 0
        s.push('a_element')
        assert len(s) == 1
        s.pop()
        assert len(s) == 0

    def test_pop_empty_stack(self):
        s = Stack('d_stack')
        assert len(s) == 0
        s.pop()
        assert len(s) == 0

