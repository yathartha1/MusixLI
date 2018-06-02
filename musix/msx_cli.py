#!/usr/bin/env python3
import click
from .msx import msx

class msx_cli:
    @click.group()
    def begin():
        '''
        A little tool that lets you search for different artists, albums, songs and their lyrics with just entering certain commands.
        '''

    @begin.command()
    @click.option('--country', default = 'US' , help = 'Specify the country, default is US.')
    def artists(country):
        '''
        Lists top 20 artists.
        '''
        msx.artists(country)

    @begin.command()
    @click.option('--country', default = 'US' , help = 'Specify the country, default is US.')
    def songs(country):
        '''
        Lists top 20 songs.
        '''
        msx.songs(country)

    @begin.command()
    @click.option('--song', default = '', help = 'Search by song name. Must be in quotes.')
    @click.option('--artist-name', default = '', help = 'Search by artist name. Must be in quotes.')
    def search(song, artist_name):
        '''
        Provides a detailed list based on the query.
        '''
        msx.search(song, artist_name)

    @begin.command()
    @click.option('--artist-name', default = '', help = 'Search by artist name. Must be in quotes.')
    def albums(artist_name):
        '''
        Provides a list of albums associated with an artist
        '''
        msx.albums(artist_name)

    @begin.command()
    @click.option('--artist-name', default = '', help = 'Search by artist name. Must be in quotes.')
    @click.option('--number', default = 5, help = 'Specify the number of artists. Default is 5.')
    def related_artists(artist_name, number):
        '''
        Provides a list of artists similar to the specified artist
        '''
        msx.related_artists(artist_name, number)

    @begin.command()
    @click.option('--song', default = '', help = 'Specify the name of the song.')
    @click.option('--artist-name', default = '', help = 'Specify the name of the artist')
    @click.option('--browser', default = 'no', help = 'Open in a browser or not: (yes/no). Default is no', type = click.Choice(['yes', 'no']))
    def lyrics(song, artist_name, browser):
        '''
        Opens a snippet of the lyrics of a specified song in the window itself or open the whole lyrics in the browser.
        '''
        msx.lyrics(song, artist_name, browser)

    @begin.command()
    def clear():
        '''
        Clears the entire screen.
        '''
        click.clear()
