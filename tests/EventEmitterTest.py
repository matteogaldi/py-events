import unittest
from events import EventEmitter


class EventEmitterTest(unittest.TestCase):
    def setUp(self):
        self.emitter = EventEmitter()
        self.on_test_called = 0

    def test_emit(self):
        self.emitter.on_('test', self.on_test)
        self.emitter.emit('test')
        self.assertEqual(self.on_test_called, 1)

    def on_test(self):
        self.on_test_called += 1

    def test_once(self):
        self.emitter.once_('test', self.on_test)
        self.emitter.emit('test')
        self.emitter.emit('test')
        self.assertEqual(self.on_test_called, 1)

    def test_off(self):
        self.emitter.on_('test', self.on_test)
        self.emitter.off('test', self.on_test)
        self.emitter.emit('test')
        self.assertEqual(self.on_test_called, 0)

    def test_remove_all(self):
        self.emitter.on_('test', self.on_test)
        self.emitter.remove_all_listeners('test')
        self.emitter.emit('test')
        self.assertEqual(self.on_test_called, 0)

    def test_max_listeners(self):
        self.emitter.set_max_listeners('test', 1)
        self.emitter.on_('test', self.on_test)
        self.assertRaises(ValueError, self.emitter.on_, 'test', self.on_test)

    def test_listener_count_all(self):
        self.emitter.on_('test', self.on_test)
        self.emitter.on_('test', self.on_test)
        self.assertEqual(self.emitter.listener_count('test'), 2)


if __name__ == '__main__':
    unittest.main()
