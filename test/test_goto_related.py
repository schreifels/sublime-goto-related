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
        self.subject.show_goto = Mock()
        self.edit = Mock()

    def test_run(self):
        self.subject.run(self.edit)
        self.subject.show_goto.assert_called_with('hello')

if __name__ == '__main__':
    unittest.main()
