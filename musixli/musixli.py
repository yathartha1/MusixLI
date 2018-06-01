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
from .msx_cli import msx_cli
import subprocess, sys

class musixli(object):
    musix_completer = WordCompleter(['artists', 'songs', 'search', 'albums', 'clear', '--country', '--song', '--artist', '--artist-name'])
    def __init__(self):
        self.hacker_news_cli = msx_cli()
        history = InMemoryHistory()
        layout = create_default_layout(
            message = u'> '
        )
        cli_buffer = Buffer(
            history = history,
            auto_suggest=AutoSuggestFromHistory(),
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
                                    ignore_case = True
                                    )
        self.cli = CommandLineInterface(application = application, eventloop = loop)

    def commands(self,document):
        command = document.text
        subprocess.call(command, shell = True)

    def start(self):
        while True:
            document = self.cli.run(reset_current_buffer=True)
            self.commands(document)
