# Redis_Containers [![Build Status](https://travis-ci.org/msempere/redis_containers.svg?branch=master)] (https://travis-ci.org/msempere/redis_containers)

Container data structures for Redis

## Structures:

* Queue (TODO)
* Priority queue (TODO)
* Stack
* Deque (TODO)

## Usage:
* **STACK**: LIFO data structure
```python
>>> from redis_containers import Stack
>>> stack = Stack('dummy_stack')
>>> len(stack)
0
>>> stack.push('a_element')
>>> stack.push('another_element')
>>> len(stack)
2
>>> stack.pop()
another_element
>>> stack.content()
[‘another_element’, ‘a_element’]
>>> stack.clear()
True
```
