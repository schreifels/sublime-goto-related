try:
    import sublime, sublime_plugin
except ImportError:
    from test.stubs import sublime, sublime_plugin

class GotoRelatedCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.show_goto(self.current_file_path())

    def current_file_path(self):
        return self.view.file_name()

    def show_goto(self, initial_text):
        self.view.window().run_command('show_overlay', { 'overlay': 'goto', 'text': initial_text })
