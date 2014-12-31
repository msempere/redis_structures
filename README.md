# Redis_Containers [![Build Status](https://travis-ci.org/msempere/redis_containers.svg?branch=master)] (https://travis-ci.org/msempere/redis_containers)

Container data structures for Redis

## Structures:

* Queue
* Priority queue
* Stack
* Deque (TODO)

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
>>> from redis_containers import Stack
>>> stack = Stack(name='dummy_stack', host='127.0.0.1', port=6379)
>>> len(stack)
0
>>> stack.push('a_element')
>>> stack.push('another_element')
>>> stack.push('one_more_element') 
# same as doing stack.addAll(['a_element', 'another_element', 'one_more_element']
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
>>> from redis_containers import Queue
>>> queue = Queue(name='dummy_queue', host='127.0.0.1', port=6379)
>>> len(queue)
0
>>> queue.push('a_element')
>>> queue.push('another_element')
>>> queue.push('one_more_element')
# same as doing queue.addAll(['a_element', 'another_element', 'one_more_element']
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
>>> from redis_containers import PriorityQueue
>>> pq = PriorityQueue(name='dummy_queue', host='127.0.0.1', port=6379)
>>> len(pq)
0
>>> pq.push('a_element', 20.0)
>>> pq.push('another_element', 40.0)
>>> pq.push('one_more_element', 10.0)
# same as doing pq.addAll([('a_element', 20.0), ('another_element', 40.0), ('one_more_element', 10.0)]
>>> len(pq)
3
>>> pq.content()
[('one_more_element', 10.0), ('a_element', 20.0), ('another_element', 40.0)]
>>> pq.pop()
('another_element', 40.0)
>>> queue.content()
[('one_more_element', 10.0), ('a_element', 20.0)]
>>> pq.clear()
True
>>> pq.content()
[]
`````
