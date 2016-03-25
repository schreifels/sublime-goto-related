try:
    import sublime, sublime_plugin
except ImportError:
    from test.stubs import sublime, sublime_plugin

class GotoRelatedCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        return 'Hello from GotoRelatedCommand'
