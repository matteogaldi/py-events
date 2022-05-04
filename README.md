# Python EventEmitter

A very basic event emitter for Python.

### Installation

`pip install NO_NAME`

### Getting Started

```python
import eventemitter

ee = eventemitter.EventEmitter()

# Register a listener
ee.on('event', lambda: print('event'))

# Emit an event
ee.emit('event')

# Remove a listener
ee.remove_listener('event', lambda: print('event'))


# Decorator
@ee.on('event')
def event():
    print('event')
```

