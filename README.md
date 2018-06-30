# MusixLI
`MusixLI` brings MusixMatch to the terminal, allowing you to **view** the following without leaving your command line:

* Songs
* Artists
* Albums
* Lyrics

## Installation

### Pip Installation

The following command will install `MusixLI`:

    $ pip3 install musixli

If you are not installing in a virtualenv, run with `sudo`:

    $ sudo pip3 install musixli

Once installed, run the optional `MusixLI` auto-completer with interactive help:

    $ musixli

Run commands:

    $ msx <command> [options] [args]

## Syntax

Usage:

    $ msx <command> [options] [args]

### Auto-Completer and Interactive Help

Optionally, you can enable fish-style completions and an auto-completion menu with interactive help:

    $ musixli

If available, the auto-completer also automatically displays commands through a pager.

Within the auto-completer, the same syntax applies:

    musixli:$>> msx <command> [options] [args]

## Commands:

### View Top Artists

Lists top 20 Artists at present from a specific Country.

Usage:

    $ msx artists --country [country name]  #default is US

Examples:

    $ msx artists
    $ msx artists --country 'in'


### View Top Songs

Lists top 20 Songs at present from a specific Country.

Usage:

    $ msx songs --country [country name]  #default is US

Example:

    $ msx songs
    $ msx songs --country 'in'


### Search by Artist Name or Song Name

Provides a detailed list based on the query.

Usage:

    $ msx search --song [song name] --artist-name [artist name]

Examples:

    $ msx search --song 'Lose Yourself'
    $ msx search --artist-name 'Eminem' --song 'Lose Yourself'

### Search Albums

Provides a list of albums associated with an artist.

Usage:

    $ msx albums --artist-name [artist name]

Examples:

    $ msx albums --artist-name 'Eminem'

### Find Similar Artists

Provides a list of artists similar to the specified artist.

Usage:

    $ msx related_artists --artist-name [artist name] --number [number of entries]  #default is 5

Examples:

    $ msx related_artists --artist-name 'Eminem'
    $ msx related_artists --artist-name 'Drake' --number 10

### Get Lyrics for a Specific Song

Opens a snippet of the lyrics of a specified song in the window itself or open the whole lyrics in the browser.

Usage:

    $ msx lyrics --artist-name [artist name] --song [song name] --browser [yes/no]  #default is no

Examples:

    $ msx lyrics --artist-name 'Eminem' --song 'Lose Yourself'
    $ msx lyrics --artist-name 'Eminem' --song 'Lose Yourself' --browser 'yes'

### Supported Python Versions

Python 3 and above.

## Libraries Used

- [Click](https://github.com/pallets/click)
- [python-prompt-toolkit](https://github.com/jonathanslenders/python-prompt-toolkit)
- [python-musixmatch](https://github.com/hudsonbrendon/python-musixmatch)
