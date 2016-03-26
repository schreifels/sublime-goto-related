# Overview

In a large project, related files often have similar names. Goto Related is a
shortcut to show the Goto Anything overlay with the current filename
pre-populated.

For example, if you are viewing `app/views/rocket_launch.html.erb` and press
`⌘+.`, the fuzzy file finder palette appears with `rocket_launch`
pre-populated.*

<img src="https://raw.githubusercontent.com/schreifels/sublime-goto-related/master/screenshot/screenshot.png" width="550" alt="">

\* This assumes that you have Goto Related
[configured to strip file extensions](#discarding-patterns).

# Installation

TODO

# Configuration

## Discarding patterns

Goto Related can be configured to discard parts of the current filename using
regular expressions. This is done in your project settings
(`Project > Edit Project`) or your global settings
(`Sublime Text > Preferences > Settings - User`). For example:

```json
"goto_related_patterns_to_strip": [
    "^_",
    "\\..+$",
    "_spec$",
    "_controller$"
]
```

will strip leading underscores, file extensions, and a couple suffixes, so:

* `_partial.html.erb` becomes `partial`
* `utilities_helper_spec.rb` becomes `utilities_helper`
* `rocket_launch_controller_spec.rb` becomes `rocket_launch`

Project-level configuration overrides global configuration. The regular
expressions are executed in the order they are defined.

## Custom key binding

You can change the default keyboard shortcut in
`Sublime Text > Preferences > Key Bindings - User`. This defaults to:

```json
[
    { "keys": ["super+."], "command": "goto_related" }
]
```

# Development

To run the test suite:

```bash
pip install -r requirements.txt
python test/test_goto_related.py
```
