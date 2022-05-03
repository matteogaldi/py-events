class EventEmitter:
    def __init__(self):
        self.events = {}

    def on_(self, event, callback):
        if event not in self.events:
            self.events[event] = []
        self.events[event].append(callback)

    def emit(self, event, *args):
        if event in self.events:
            for callback in self.events[event]:
                callback(*args)

    def off(self, event, callback):
        if event in self.events:
            self.events[event].remove(callback)

    def once_(self, event, callback):
        def on_once(*args):
            callback(*args)
            self.off(event, on_once)

        self.on_(event, on_once)

    def on(self, event):
        def decorator(callback):
            self.on_(event, callback)
            return callback

        return decorator

    def once(self, event):
        def decorator(callback):
            self.once_(event, callback)
            return callback

        return decorator
