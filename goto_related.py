try:
    import sublime, sublime_plugin
except ImportError:
    from test.stubs import sublime, sublime_plugin

import os

class GotoRelatedCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        filename = self.clean_path(self.current_file_path())
        self.show_goto(filename)

    def clean_path(self, path):
        return os.path.basename(path)

    def current_file_path(self):
        return self.view.file_name()

    def show_goto(self, initial_text):
        self.view.window().run_command('show_overlay', { 'overlay': 'goto', 'text': initial_text })
