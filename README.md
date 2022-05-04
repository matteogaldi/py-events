# Python EventEmitter

A very basic event emitter for Python.

### Installation

Download the latest release [here](https://github.com/matteogaldi/py-events/releases)

`pip install py_events-0.1.0-py3-none-any.whl`

### Getting Started

```python
import events

ee = events.EventEmitter()

# Register a listener
ee.on_('event', lambda: print('event'))

# Emit an event
ee.emit('event')

# Remove a listener
ee.remove_listener('event', lambda: print('event'))

# set max listeners for an event
ee.set_max_listeners('event', 1)


# Decorator
@ee.on('event')
def event():
    print('event')


# Decorator only once
@ee.once('event')
def event():
    print('event')
```

### Build instructions
`pip install build`

`python -m build`

