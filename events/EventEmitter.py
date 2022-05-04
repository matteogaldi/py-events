class EventEmitter:
    """
    Creates an EventEmitter object.

    Attributes:
        events (dict): A dictionary of events and their listeners.
        max_listeners (int): The maximum number of listeners that can be attached to an event.
    """

    # TODO: add checks for max_listeners

    def __init__(self):
        self.max_listeners = None
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

    def remove_all_listeners(self, event):
        if event in self.events:
            del self.events[event]

    def remove_listener(self, event, callback):
        if event in self.events:
            self.events[event].remove(callback)

    def set_max_listeners(self, max_listeners):
        self.max_listeners = max_listeners

    def get_max_listeners(self):
        return self.max_listeners

    def listeners(self, event):
        if event in self.events:
            return self.events[event]
        return []

    def listener_count(self, event):
        if event in self.events:
            return len(self.events[event])
        return 0

    def event_names(self):
        return self.events.keys()

    def listener_count_for(self, event):
        return self.listener_count(event)

    def listeners_for(self, event):
        return self.listeners(event)

    def emit_for(self, event, *args):
        self.emit(event, *args)

    def event_exists(self, event):
        return event in self.events

    def event_count(self):
        return len(self.events)

    def event_names_for(self):
        return self.event_names()

    def event_exists_for(self, event):
        return self.event_exists(event)

    def event_count_for(self):
        return self.event_count()
