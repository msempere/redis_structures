from redis_containers import Stack, Queue
from unittest import TestCase

class TestContainers(TestCase):

    def test_empty_stack(self):
        s = Stack('a_stack')
        assert len(s) == 0

    def test_empty_queue(self):
        q = Queue('a_queue')
        assert len(q) == 0

    def test_push_stack(self):
        s = Stack('b_stack')
        s.push('a_element')
        assert len(s) == 1

    def test_push_queue(self):
        q = Queue('b_queue')
        q.push('a_element')
        assert len(q) == 1

    def test_pop_stack(self):
        s = Stack('c_stack')
        assert len(s) == 0
        s.push('a_element')
        assert len(s) == 1
        s.pop()
        assert len(s) == 0

    def test_pop_queue(self):
        q = Queue('c_queue')
        assert len(q) == 0
        q.push('a_element')
        assert len(q) == 1
        q.pop()
        assert len(q) == 0

    def test_pop_empty_stack(self):
        s = Stack('d_stack')
        assert len(s) == 0
        s.pop()
        assert len(s) == 0

    def test_pop_empty_queue(self):
        q = Queue('d_queue')
        assert len(q) == 0
        q.pop()
        assert len(q) == 0

    def test_clear_stack(self):
        s = Stack('e_stack')
        s.push('a_element')
        assert len(s) == 1
        s.clear()
        assert len(s) == 0

    def test_clear_queue(self):
        q = Queue('e_queue')
        q.push('a_element')
        assert len(q) == 1
        q.clear()
        assert len(q) == 0

    def test_content_stack(self):
        s = Stack('f_stack')
        s.push('a_element')
        s.push('b_element')
        s.push('c_element')
        assert len(s) == 3
        assert s.content() == ['c_element', 'b_element', 'a_element']
        s.pop()
        assert len(s) == 2
        assert s.content() == ['b_element', 'a_element']

    def test_content_queue(self):
        q = Queue('f_queue')
        q.push('a_element')
        q.push('b_element')
        q.push('c_element')
        assert len(q) == 3
        assert q.content() == ['c_element', 'b_element', 'a_element']
        q.pop()
        assert len(q) == 2
        assert q.content() == ['c_element', 'b_element']

