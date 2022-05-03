import events.EventEmitter as EventEmitter

ee = EventEmitter.EventEmitter()


@ee.on('event')
def event_handler(arg):
    print('event_handler:', arg)


@ee.once('event')
def only_once_event_handler(arg):
    print('only_once_event_handler:', arg)


ee.emit('event', 'hello')
ee.emit('event', 'world')

for i in range(10):
    ee.emit('event', i)
