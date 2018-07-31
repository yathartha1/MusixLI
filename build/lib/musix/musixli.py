#!/usr/bin/env python3
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.interface import CommandLineInterface, AcceptAction
from prompt_toolkit.application import Application
from prompt_toolkit.key_binding.manager import KeyBindingManager
from prompt_toolkit.shortcuts import create_default_layout, create_eventloop
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.filters import Always
from prompt_toolkit.keys import Keys
from pygments.token import Token
from pygments.styles.tango import TangoStyle
from prompt_toolkit.styles import style_from_pygments
import subprocess, sys

class musixli:
    musix_completer = WordCompleter(['artists', 'songs', 'search', 'albums', 'related_artists', 'lyrics', 'clear', '--country', '--song', '--artist-name', '--number', '--browser'], ignore_case = True)
    def __init__(self):
        def get_toolbar(self):
            return [(Token.Toolbar.Status.Key, '[msx] Help      [ctrl+q] Exit')]

        updated_style = style_from_pygments(TangoStyle, {
            Token.Menu.Completions.Completion.Current: 'bg:#acba36 #000000',
            Token.Menu.Completions.Completion: 'bg:#008888 #ffffff',
            Token.Menu.Completions.ProgressBar: 'bg:#acba36',
            Token.Scrollbar: 'bg:#acba36',
            Token.Scrollbar.Button: 'bg:#003333',
            Token.Toolbar: '#ffffff bg:#333333',
            Token: '#00ffff bold',
            Token.Toolbar.Status.Key: '#ff0000'
        })
        history = InMemoryHistory()
        layout = create_default_layout(
            message = u'musixli:$>> ',
            get_bottom_toolbar_tokens = get_toolbar
        )
        cli_buffer = Buffer(
            history = history,
            auto_suggest = AutoSuggestFromHistory(),
            enable_history_search=True,
            completer = self.musix_completer,
            complete_while_typing = Always(),
            accept_action=AcceptAction.RETURN_DOCUMENT
            )
        loop = create_eventloop()
        self.manager = KeyBindingManager()

        @self.manager.registry.add_binding(Keys.ControlQ, eager = True)
        def exit_(event):
            sys.exit()

        application = Application(  key_bindings_registry = self.manager.registry,
                                    layout = layout,
                                    mouse_support = False,
                                    buffer = cli_buffer,
                                    style = updated_style,
                                    ignore_case = True,
                                    )
        self.cli = CommandLineInterface(application = application, eventloop = loop)

    def commands(self,document):
        command = document.text
        subprocess.call(command, shell = True)

    def start(self):
        while True:
            document = self.cli.run(reset_current_buffer=True)
            self.commands(document)
