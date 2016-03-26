try:
    import sublime, sublime_plugin
except ImportError:
    from test.stubs import sublime, sublime_plugin

import os, re

class GotoRelatedCommand(sublime_plugin.TextCommand):

    DEBUG = False

    def run(self, edit):
        current_path = self.current_file_path()

        if self.DEBUG:
            print('GotoRelated: transforming %s' % current_path)

        filename = self.clean_path(current_path)
        self.show_goto(filename)

    def clean_path(self, path):
        filename = os.path.basename(path)

        for pattern in self.patterns_to_strip():
            if self.DEBUG:
                print('  - Replacing /%s/ in "%s"' % (pattern, filename))
            filename = re.sub(pattern, '', filename)

        return filename

    def current_file_path(self):
        return self.view.file_name() or ''

    def patterns_to_strip(self):
        return self.view.window().project_data().get('goto_related_patterns_to_strip') or \
                    self.view.settings().get('goto_related_patterns_to_strip') or \
                    []

    def show_goto(self, initial_text):
        self.view.window().run_command('show_overlay', { 'overlay': 'goto', 'text': initial_text })
