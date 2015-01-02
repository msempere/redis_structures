# Redis_Structures [![Build Status](https://travis-ci.org/msempere/redis_structures.svg?branch=master)] (https://travis-ci.org/msempere/redis_structures)

Data structures for Redis

## Structures:

* Queue
* Priority queue
* Stack
* Circular buffer
* Deque

## Setup:
```
pip install -r requirements.txt
```
```
python setup.py install
```

## Usage:
* **STACK**: LIFO data structure
```python
>>> from redis_structures import Stack
>>> stack = Stack(name='dummy_stack', host='127.0.0.1', port=6379)
>>> len(stack)
0
>>> stack.push('a_element')
>>> stack.push('another_element')
>>> stack.push('one_more_element') 
# same as doing stack.addAll(['a_element', 'another_element', 'one_more_element'])
>>> len(stack)
3
>>> stack.content()
['one_more_element', 'another_element', 'a_element']
>>> stack.pop()
'one_more_element'
>>> stack.content()
['another_element', 'a_element']
>>> stack.clear()
True
>>> stack.content()
[]
```

* **QUEUE**: FIFO data structure
```python
>>> from redis_structures import Queue
>>> queue = Queue(name='dummy_queue', host='127.0.0.1', port=6379)
>>> len(queue)
0
>>> queue.push('a_element')
>>> queue.push('another_element')
>>> queue.push('one_more_element')
# same as doing queue.addAll(['a_element', 'another_element', 'one_more_element'])
>>> len(queue)
3
>>> queue.content()
['one_more_element', 'another_element', 'a_element']
>>> queue.pop()
'a_element'
>>> queue.content()
['one_more_element', 'another_element']
>>> queue.clear()
True
>>> queue.content()
[]
`````

* **PRIORITY QUEUE**: Abstract data type where each element has a priority associated
```python
>>> from redis_structures import PriorityQueue
>>> priority_queue = PriorityQueue(name='dummy_queue', host='127.0.0.1', port=6379)
>>> len(priority_queue)
0
>>> priority_queue.push('a_element', 20.0)
>>> priority_queue.push('another_element', 40.0)
>>> priority_queue.push('one_more_element', 10.0)
# same as doing priority_queue.addAll([('a_element', 20.0), ('another_element', 40.0), ('one_more_element', 10.0)])
>>> len(priority_queue)
3
>>> priority_queue.content()
[('one_more_element', 10.0), ('a_element', 20.0), ('another_element', 40.0)]
>>> priority_queue.pop()
('another_element', 40.0)
>>> priority_queue.content()
[('one_more_element', 10.0), ('a_element', 20.0)]
>>> priority_queue.clear()
True
>>> priority_queue.content()
[]
```

* **CIRCULAR BUFFER**: Fixed-size buffer with connected end-to-end
```python
>>> from redis_structures import CircularBuffer
>>> circular_buffer = CircularBuffer(name='dummy_cbuffer', size=3, host='127.0.0.1', port=6379)
>>> len(circular_buffer)
0
>>> circular_buffer.push('a_element')
>>> circular_buffer.push('another_element')
>>> circular_buffer.push('one_more_element')
# same as doing circular_buffer.addAll(['a_element', 'another_element', 'one_more_element'])
>>> len(circular_buffer)
3
>>> circular_buffer.content()
['one_more_element', 'another_element', 'a_element']
>>> circular_buffer.push('other_element!!') # overwriting old data because size=3
>>> len(circular_buffer)
3
>>> circular_buffer.content()
['other_element!!', 'one_more_element', 'another_element']
>>> circular_buffer.pop()
'another_element'
>>> circular_buffer.content()
['other_element!!', 'one_more_element',]
>>> circular_buffer.clear()
True
>>> circular_buffer.content()
[]
```

* **DEQUE**: Double-ended queue also called head-tail linked list
```python
>>> from redis_structures import Deque
>>> deque = Deque(name='dummy_cbuffer', host='127.0.0.1', port=6379)
>>> len(deque)
0
>>> deque.back_push('a_element')
>>> deque.back_push('another_element')
>>> deque.back_push('one_more_element')
# same as doing deque.addAll(['one_more_element', 'another_element', 'a_element'], back=True)
>>> len(deque)
3
>>> deque.content()
['one_more_element', 'another_element', 'a_element']
>>> deque.front_push('other_element!!')
>>> len(deque)
3
>>> deque.content()
['one_more_element', 'another_element', 'a_element', 'other_element!!']
>>> deque.back_pop()
'one_more_element'
>>> deque.content()
['another_element', 'a_element', 'other_element!!']
>>> deque.clear()
True
>>> deque.content()
[]
```
