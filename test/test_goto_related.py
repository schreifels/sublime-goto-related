import unittest
from mock import Mock

import os, sys
root_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.insert(0, root_path)

from test.stubs import sublime, sublime_plugin
from goto_related import GotoRelatedCommand

class TestGotoRelated(unittest.TestCase):

    def setUp(self):
        self.subject = GotoRelatedCommand()
        self.edit = Mock()

    def test_run(self):
        self.assertEqual(self.subject.run(self.edit), 'Hello from GotoRelatedCommand')

if __name__ == '__main__':
    unittest.main()
