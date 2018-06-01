#!/usr/bin/env python3
import json
from .api_key import key
from musixmatch import Musixmatch
import click

key = key.get_key()
musixmatch = Musixmatch(key)

class msx:
    def artists(country):
        artist_json = musixmatch.chart_artists(country = country, page = 1, page_size = 20)
        artist_list = json.loads(json.dumps(artist_json['message']['body']['artist_list']))
        for i in range(0, len(artist_list)):
            print(click.style(str(i+1), fg = 'cyan', bold = True), end = '      ')
            print('  ' + artist_list[i]['artist']['artist_name'])

    def songs(country):
        songs_json = musixmatch.chart_tracks_get(country = country, page = 1, page_size = 20, f_has_lyrics = 1)
        songs_list = json.loads(json.dumps(songs_json['message']['body']['track_list']))
        for i in range(0, len(songs_list)):
            print(click.style(str(i+1), fg = 'cyan', bold = True), end = '      ')
            print(click.style('Song: ', bold = True, fg = 'green') + songs_list[i]['track']['track_name'])
            print(end = '       ')
            print(click.style('Album: ', bold = True, fg = 'blue') + songs_list[i]['track']['album_name'] + '\n' + click.style('       Artist: ', bold = True, fg = 'yellow') + songs_list[i]['track']['artist_name'] + '\n')

    def search(song, artist):
        if song != '' or artist != '':
            search_val = musixmatch.track_search(q_artist = artist, q_track = song, page = 1, page_size = 10, s_track_rating='desc')
            search_list = json.loads(json.dumps(search_val['message']['body']['track_list']))
            for i in range(0, len(search_list)):
                genre = json.loads(json.dumps(search_list[i]['track']['primary_genres']['music_genre_list']))
                print(click.style(str(i+1), fg = 'cyan', bold = True), end = '      ')
                print(click.style('Song: ', bold = True, fg = 'green') + search_list[i]['track']['track_name'])
                print(end = '       ')
                print(click.style('Album: ', bold = True, fg = 'blue') + search_list[i]['track']['album_name'] + '\n' + click.style('       Artist: ', bold = True, fg = 'yellow') + search_list[i]['track']['artist_name'])
                print(end = '       ')
                if len(genre) != 0:
                    print(click.style('Genre: ', bold = True, fg = 'red') + genre[0]['music_genre']['music_genre_name'] + '\n')
                else:
                    print(click.style('Genre: ', bold = True, fg = 'red') + 'No genre available\n')
        else:
            print(click.style('No song name or artist provided', blink = True, fg = 'red'))

    def albums(artist_name):
        if artist_name != '':
            track_val = musixmatch.track_search(q_artist = artist_name, q_track = '', page = 1, page_size = 1, s_track_rating='desc')
            track_list = json.loads(json.dumps(track_val['message']['body']['track_list']))
            artist_id = track_list[0]['track']['artist_id']
            artist_val = musixmatch.artist_albums_get(artist_id = artist_id, page = 1, page_size = 100, s_release_date = 'desc', g_album_name = 1)
            album_list = json.loads(json.dumps(artist_val['message']['body']['album_list']))
            for i in range(0, len(album_list)):
                print(click.style(str(i+1), fg = 'cyan', bold = True), end = '      ')
                print(click.style('Album Name: ', bold = True, fg = 'green') + album_list[i]['album']['album_name'])
                print(end = '       ')
                print(click.style('Number of Tracks: ', bold = True, fg = 'blue') + str(album_list[i]['album']['album_track_count']) + '\n' + click.style('       Release Date: ', bold = True, fg = 'yellow') + album_list[i]['album']['album_release_date'] + '\n')