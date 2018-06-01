#!/usr/bin/env python3
import click
from .msx import msx

class msx_cli:
    @click.group()
    def begin():
        pass

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
    @click.option('--artist', default = '', help = 'Search by artist name. Must be in quotes.')
    def search(song, artist):
        '''
        Provides a detailed list based on the query.
        '''
        msx.search(song, artist)

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
    def clear():
        '''
        Clears the entire screen.
        '''
        click.clear()
