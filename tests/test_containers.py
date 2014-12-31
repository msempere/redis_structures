from redis_containers import Stack, Queue, PriorityQueue
from unittest import TestCase

class TestStack(TestCase):

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
        assert s.pop() == 'a_element'
        assert len(s) == 0

    def test_pop_empty_stack(self):
        s = Stack('d_stack')
        assert len(s) == 0
        s.pop()
        assert len(s) == 0

    def test_clear_stack(self):
        s = Stack('e_stack')
        s.push('a_element')
        assert len(s) == 1
        s.clear()
        assert len(s) == 0

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

    def test_addall_stack(self):
        s = Stack('g_stack')
        assert len(s) == 0
        s.addAll(collection=['a_element', 'another_element', 'one_more_element'])
        assert len(s) == 3
        assert s.content() == ['one_more_element', 'another_element', 'a_element']


class TestPriorityQueue(TestCase):

    def test_empty_priority_queue(self):
        q = PriorityQueue('a_pq')
        assert len(q) == 0

    def test_push_priority_queue(self):
        q = PriorityQueue('b_pq')
        q.push('a_element', 50.0)
        assert len(q) == 1

    def test_pop_empty_priority_queue(self):
        q = PriorityQueue('d_pq')
        assert len(q) == 0
        q.pop()
        assert len(q) == 0

    def test_pop_priority_queue(self):
        q = PriorityQueue('c_pq')
        assert len(q) == 0
        q.push('a_element', 50.0)
        assert len(q) == 1
        assert q.pop() == ('a_element', 50.0)
        assert len(q) == 0

    def test_content_priority_queue(self):
        s = PriorityQueue('f_pr')
        s.push('a_element', 50.0)
        s.push('b_element', 20.0)
        s.push('c_element', 100.0)
        assert len(s) == 3
        assert s.content() == [('b_element', 20.0), ('a_element', 50.0), ('c_element', 100.0)]
        assert s.pop() == ('c_element', 100.0)
        assert len(s) == 2
        print s.content()
        assert s.content() == [('b_element', 20.0), ('a_element', 50.0)]

    def test_addall_priority_queue(self):
        s = PriorityQueue('g_pr')
        assert len(s) == 0
        s.addAll(collection=[('a_element', 50.0), ('another_element', 20.0), ('one_more_element', 100.0)])
        assert len(s) == 3
        assert s.content() == [('another_element', 20.0), ('a_element', 50.0), ('one_more_element', 100.0)]


class TestQueue(TestCase):

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

    def test_clear_queue(self):
        q = Queue('e_queue')
        q.push('a_element')
        assert len(q) == 1
        q.clear()
        assert len(q) == 0

    def test_pop_empty_queue(self):
        q = Queue('d_queue')
        assert len(q) == 0
        q.pop()
        assert len(q) == 0

    def test_empty_queue(self):
        q = Queue('a_queue')
        assert len(q) == 0

    def test_push_queue(self):
        q = Queue('b_queue')
        q.push('a_element')
        assert len(q) == 1

    def test_pop_queue(self):
        q = Queue('c_queue')
        assert len(q) == 0
        q.push('a_element')
        assert len(q) == 1
        assert q.pop() == 'a_element'
        assert len(q) == 0

