class EventEmitter:
    """
    Creates an EventEmitter object.

    Attributes:
        events (dict): A dictionary of events and their listeners.
        max_listeners (int): The maximum number of listeners that can be attached to an event.
    """

    def __init__(self):
        self.events = {}
        self.max_listeners = {}

    def on_(self, event, callback):
        """
        Adds a listener to an event. If the event does not exist, it is created;
        :param event: The event to listen to;
        :param callback: The callback to execute when the event is emitted;
        """
        if event not in self.events:
            self.events[event] = []
        if event in self.max_listeners:
            if len(self.events[event]) >= self.max_listeners[event]:
                print("Max listeners reached for event: " + event)
                raise (ValueError("Max listeners reached"))
        self.events[event].append(callback)

    def emit(self, event, *args):
        """
        Emits an event;
        :param event: The event to emit;
        :param args: The arguments to pass to the listeners;
        """
        if event in self.events:
            for callback in self.events[event]:
                callback(*args)

    def off(self, event, callback):
        """
        Removes a listener from an event;
        :param event: The event to remove the listener from;
        :param callback: The callback to remove;
        """
        if event in self.events:
            self.events[event].remove(callback)

    def once_(self, event, callback):
        """
        Adds a listener to an event that will only be called once;
        :param event: event to listen to;
        :param callback: function to execute when event is emitted;
        """

        def on_once(*args):
            callback(*args)
            self.off(event, on_once)

        self.on_(event, on_once)

    def on(self, event):
        """
        Adds a listener to an event. If the event does not exist, it is created; Decorator.
        :param event: event to listen to;
        """

        def decorator(callback):
            self.on_(event, callback)
            return callback

        return decorator

    def once(self, event):
        """
        Adds a listener to an event that will only be called once. Decorator.
        :param event: event to listen to;
        """

        def decorator(callback):
            self.once_(event, callback)
            return callback

        return decorator

    def remove_all_listeners(self, event):
        """
        Removes all listeners from an event.
        :param event: event to remove listeners from;
        """
        if event in self.events:
            del self.events[event]

    def remove_listener(self, event, callback):
        """
        Removes a listener from an event.
        :param event: event to remove listener from;
        :param callback: listener to remove;
        """
        if event in self.events:
            self.events[event].remove(callback)

    def set_max_listeners(self, event, max_listeners):
        """
        Sets the maximum number of listeners that can be attached to an event.
        :param event: event to set max listeners for;
        :param max_listeners: max number of listeners;
        """
        self.max_listeners[event] = max_listeners

    def get_max_listeners(self, event):
        """
        Gets the maximum number of listeners that can be attached to an event.
        :param event: event to get max listeners for;
        :return: max number of listeners;
        """
        return self.max_listeners[event]

    def listeners(self, event):
        """
        Returns the number of listeners for an event.
        :param event: event to get listeners for;
        :return: listeners for event;
        """
        if event in self.events:
            return self.events[event]
        return []

    def listener_count(self, event):
        """
        Returns the number of listeners for an event.
        :param event: event to get listeners for;
        :return: number of listeners for event;
        """
        if event in self.events:
            return len(self.events[event])
        return 0

    def event_names(self):
        """
        Returns the names of all events.
        :return: names of all events;
        """
        return self.events.keys()

    def listener_count_for(self, event):
        """
        Returns the number of listeners for an event.
        :param event: event to get listeners for;
        :return: number of listeners for event;
        """
        return self.listener_count(event)

    def listeners_for(self, event):
        """
        Returns the listeners for an event.
        :param event: event to get listeners for;
        :return: listeners for event;
        """
        return self.listeners(event)

    def event_exists(self, event):
        """
        Returns whether an event exists.
        :param event: event to check;
        :return: True if event exists, False otherwise;
        """
        return event in self.events

    def event_count(self):
        """
        Returns the number of events.
        :return: number of events;
        """
        return len(self.events)

    def count_all_listeners(self):
        """
        Returns the number of listeners.
        :return: number of listeners;
        """
        count = 0
        for event in self.events:
            count += len(self.events[event])
        return count
