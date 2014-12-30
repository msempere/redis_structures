Redis_Containers
================

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
>>> stack.clear()
True
```
