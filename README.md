# Overview

<img src="https://raw.githubusercontent.com/schreifels/sublime-goto-related/master/screenshot/screenshot.png" width="550" alt="">

By default, Goto Related can be activated with `Goto > Goto Related` or by
pressing `⌘+.` (OSX only).

# Configuration

You can change the default keybinding in
`Sublime Text > Preferences > Key Bindings - User`. For example:

```json
[
    { "keys": ["ctrl+shift+down"], "command": "goto_related" }
]
```

# Development

To run the test suite:

```bash
pip install -r requirements.txt
python test/test_goto_related.py
```
