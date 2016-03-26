import unittest
from mock import Mock

import os, sys
root_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.insert(0, root_path)

from test.stubs import sublime, sublime_plugin
from goto_related import GotoRelatedCommand

class TestGotoRelatedCommand(unittest.TestCase):

    def assert_goto(self, current_file_path, patterns_to_strip, expected_overlay_text):
        subject = GotoRelatedCommand()

        subject.show_goto = Mock()
        subject.current_file_path = Mock(return_value=current_file_path)
        subject.patterns_to_strip = Mock(return_value=patterns_to_strip)

        subject.run(Mock())
        subject.show_goto.assert_called_with(expected_overlay_text)

    def test_run(self):
        self.assert_goto('/path/to/main.rb',              [],                  'main.rb')
        self.assert_goto('/path/to/main_test.rb',         [],                  'main_test.rb')
        self.assert_goto('/path/to/my_test_test.rb',      ['_test'],           'my.rb')
        self.assert_goto('/path/to/my_test_test.rb',      ['_test$'],          'my_test_test.rb')
        self.assert_goto('/path/to/my_test_test.rb',      ['\..+$', '_test$'], 'my_test')
        self.assert_goto('/path/to/home.html.erb',        ['\..+$'],           'home')
        self.assert_goto('/path/to/_my_partial.html.erb', ['^_', '\..+$'],     'my_partial')

if __name__ == '__main__':
    unittest.main()
