# Redis_Containers [![Build Status](https://travis-ci.org/msempere/redis_containers.svg?branch=master)] (https://travis-ci.org/msempere/redis_containers)

Container data structures for Redis

## Structures:

* Queue
* Priority queue (TODO)
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
