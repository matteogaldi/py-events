# Python EventEmitter

A very basic event emitter for Python.

### Installation

Download the latest release [here](https://github.com/matteogaldi/py-events/releases)

`pip install py_events-0.1.0-py3-none-any.whl`

### Getting Started

```python
import events

ee = events.EventEmitter()


def my_event_handler(e):
    print(f"Event received: {e}")


# Register a listener
ee.on_('event', my_event_handler)

# Emit an event
ee.emit('event')

# Remove a listener
ee.remove_listener('event', my_event_handler)
ee.off('event', my_event_handler)

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

