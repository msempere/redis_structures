from redis_structures import Stack, Queue, PriorityQueue, CircularBuffer, Deque
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


class TestCircularBuffer(TestCase):

    def test_empty_circular_buffer(self):
        cb = CircularBuffer('a_cb', size=3)
        assert len(cb) == 0

    def test_push_circular_buffer(self):
        cb = CircularBuffer('b_cb', size=3)
        cb.push('a_element')
        assert len(cb) == 1

    def test_pop_circular_buffer(self):
        cb = CircularBuffer('c_cb', size=3)
        assert len(cb) == 0
        cb.push('a_element')
        assert len(cb) == 1
        assert cb.pop() == 'a_element'
        assert len(cb) == 0

    def test_pop_empty_circular_buffer(self):
        cb = CircularBuffer('d_cb', size=3)
        assert len(cb) == 0
        assert cb.pop() == None
        assert len(cb) == 0

    def test_clear_circular_buffer(self):
        cb = CircularBuffer('e_cb', size=3)
        cb.push('a_element')
        assert len(cb) == 1
        cb.clear()
        assert len(cb) == 0

    def test_content_circular_buffer(self):
        cb = CircularBuffer('f_cb', size=3)
        cb.push('a_element')
        cb.push('b_element')
        cb.push('c_element')
        assert len(cb) == 3
        assert cb.content() == ['c_element', 'b_element', 'a_element']
        assert cb.pop() == 'a_element'
        assert len(cb) == 2
        assert cb.content() == ['c_element', 'b_element']

    def test_addall_circular_buffer(self):
        cb = CircularBuffer('g_cb', size=3)
        assert len(cb) == 0
        cb.addAll(collection=['a_element', 'another_element', 'one_more_element'])
        assert len(cb) == 3
        assert cb.content() == ['one_more_element', 'another_element', 'a_element']

    def test_overwrite_circular_buffer(self):
        cb = CircularBuffer('h_cb', size=3)
        assert len(cb) == 0
        cb.addAll(collection=['a_element', 'another_element', 'one_more_element'])
        assert len(cb) == 3
        cb.push('overwrite_element')
        assert len(cb) == 3
        assert cb.content() == ['overwrite_element', 'one_more_element', 'another_element']

class TestDeque(TestCase):

    def test_empty_deque(self):
        dq = Deque('a_deque')
        assert len(dq) == 0

    def test_front_push_deque(self):
        dq = Deque('b_deque')
        dq.front_push('a_element')
        assert len(dq) == 1

    def test_back_push_deque(self):
        dq = Deque('b2_deque')
        dq.back_push('a_element')
        assert len(dq) == 1

    def test_front_pop_deque(self):
        dq = Deque('c_deque')
        assert len(dq) == 0
        dq.front_push('a_element')
        assert len(dq) == 1
        assert dq.front_pop() == 'a_element'
        assert len(dq) == 0

    def test_back_pop_deque(self):
        dq = Deque('c2_deque')
        assert len(dq) == 0
        dq.back_push('a_element')
        assert len(dq) == 1
        assert dq.back_pop() == 'a_element'
        assert len(dq) == 0

    def test_front_pop_empty_deque(self):
        dq = Deque('d_deque')
        assert len(dq) == 0
        assert dq.front_pop() == None
        assert len(dq) == 0

    def test_back_pop_empty_deque(self):
        dq = Deque('d2_deque')
        assert len(dq) == 0
        assert dq.back_pop() == None
        assert len(dq) == 0

    def test_clear_deque(self):
        dq = Deque('e_deque')
        dq.front_push('a_element')
        assert len(dq) == 1
        dq.clear()
        assert len(dq) == 0

    def test_content_deque(self):
        dq = Deque('f_deque')
        dq.front_push('a_element')
        dq.front_push('b_element')
        dq.back_push('c_element')
        assert len(dq) == 3
        assert dq.content() == ['c_element', 'a_element', 'b_element']
        assert dq.back_pop() == 'c_element'
        assert len(dq) == 2
        assert dq.content() == ['a_element', 'b_element']

    def test_addall_deque(self):
        dq = Deque('g_deque')
        assert len(dq) == 0
        dq.addAll(collection=['a_element', 'another_element', 'one_more_element'])
        assert len(dq) == 3
        assert dq.content() == ['one_more_element', 'another_element', 'a_element']
        dq.addAll(collection=['x_element', 'y_element'], back=False)
        assert dq.content() == ['one_more_element', 'another_element', 'a_element', 'x_element', 'y_element']
        dq.addAll(collection=['t_element', 'u_element'], back=True)
        assert dq.content() == ['u_element', 't_element', 'one_more_element', 'another_element', 'a_element', 'x_element', 'y_element']

