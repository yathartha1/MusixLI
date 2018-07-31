#!/usr/bin/env python3
import json, webbrowser
from .config import config
from musixmatch import Musixmatch
import click
from textwrap import fill

cfg = config()
key = cfg.get_key()
musixmatch = Musixmatch(key)

class msx:

    def artists(country):
        artist_json = musixmatch.chart_artists(country = country, page = 1, page_size = 20)
        artist_list = json.loads(json.dumps(artist_json['message']['body']['artist_list']))
        for i in range(0, len(artist_list)):
            wrapped = fill(artist_list[i]['artist']['artist_name'], width=71, subsequent_indent=' '*7)
            print('     ' + wrapped)

    def songs(country):
        songs_json = musixmatch.chart_tracks_get(country = country, page = 1, page_size = 20, f_has_lyrics = 1)
        songs_list = json.loads(json.dumps(songs_json['message']['body']['track_list']))
        for i in range(0, len(songs_list)):
            wrapped = fill(songs_list[i]['track']['track_name'], width=71, subsequent_indent=' '*7)
            print('     ' + click.style('Song: ', bold = True, fg = 'green') + wrapped)
            wrapped = fill(songs_list[i]['track']['artist_name'], width=71, subsequent_indent=' '*7)
            print('     ' + click.style('Album: ', bold = True, fg = 'blue') + songs_list[i]['track']['album_name'] + '\n' + click.style('     Artist: ', bold = True, fg = 'yellow') + wrapped + '\n')

    def search(song, artist):
        if song != '' or artist != '':
            search_val = musixmatch.track_search(q_artist = artist, q_track = song, page = 1, page_size = 10, s_track_rating='desc')
            search_list = json.loads(json.dumps(search_val['message']['body']['track_list']))
            if len(search_list) == 0:
                print('     ' + 'No Data Available')
            for i in range(0, len(search_list)):
                genre = json.loads(json.dumps(search_list[i]['track']['primary_genres']['music_genre_list']))
                wrapped = fill(search_list[i]['track']['track_name'], width=71, subsequent_indent=' '*7)
                print('     ' + click.style('Song: ', bold = True, fg = 'green') + wrapped)
                wrapped = fill(search_list[i]['track']['artist_name'], width=71, subsequent_indent=' '*7)
                print('     ' + click.style('Album: ', bold = True, fg = 'blue') + search_list[i]['track']['album_name'] + '\n' + click.style('     Artist: ', bold = True, fg = 'yellow') + wrapped)
                if len(genre) != 0:
                    wrapped = fill(genre[0]['music_genre']['music_genre_name'], width=71, subsequent_indent=' '*7)
                    print('     ' + click.style('Genre: ', bold = True, fg = 'red') + wrapped + '\n')
                else:
                    print('     ' + click.style('Genre: ', bold = True, fg = 'red') + 'No genre available\n')
        else:
            print('     ' + click.style('No song name or artist provided', blink = True, fg = 'magenta'))

    def albums(artist_name):
        if artist_name != '':
            track_val = musixmatch.track_search(q_artist = artist_name, q_track = '', page = 1, page_size = 1, s_track_rating='desc')
            track_list = json.loads(json.dumps(track_val['message']['body']['track_list']))
            artist_id = track_list[0]['track']['artist_id']
            artist_val = musixmatch.artist_albums_get(artist_id = artist_id, page = 1, page_size = 100, s_release_date = 'desc', g_album_name = 1)
            album_list = json.loads(json.dumps(artist_val['message']['body']['album_list']))
            if len(album_list) == 0:
                print('     ' + 'No Album Data Available')
            for i in range(0, len(album_list)):
                wrapped = fill(album_list[i]['album']['album_name'], width=71, subsequent_indent=' '*7)
                print('     ' + click.style('Album Name: ', bold = True, fg = 'green') + wrapped)
                print('     ' + click.style('Number of Tracks: ', bold = True, fg = 'blue') + str(album_list[i]['album']['album_track_count']) + '\n' + click.style('       Release Date: ', bold = True, fg = 'yellow') + album_list[i]['album']['album_release_date'] + '\n')
        else:
            print('     ' + click.style('No artist provided', blink = True, fg = 'magenta'))

    def related_artists(artist_name, number):
        if artist_name != '':
            track_val = musixmatch.track_search(q_artist = artist_name, q_track = '', page = 1, page_size = 1, s_track_rating='desc')
            track_list = json.loads(json.dumps(track_val['message']['body']['track_list']))
            artist_id = track_list[0]['track']['artist_id']
            r_artist_val = musixmatch.artist_related_get(artist_id = artist_id, page = 1, page_size = number)
            r_artist_list = json.loads(json.dumps(r_artist_val['message']['body']['artist_list']))
            print('Artists Similar to ' + artist_name + ' :\n')
            if len(r_artist_list) == 0:
                print('     ' + 'No Data Available')
            for i in range(0, len(r_artist_list)):
                wrapped = fill(r_artist_list[i]['artist']['artist_name'], width=71, subsequent_indent=' '*7)
                print('     ' + click.style('Artist Name: ', bold = True, fg = 'green') + wrapped + '\n')
        else:
            print('     ' + click.style('No artist provided', blink = True, fg = 'magenta'))

    def lyrics(song, artist_name, browser):
        if song != '' and artist_name != '':
            match_val = musixmatch.matcher_track_get(q_track = song, q_artist = artist_name)
            if browser == 'yes':
                match_val = musixmatch.matcher_track_get(q_track = song, q_artist = artist_name)
                match_url = json.loads(json.dumps(match_val['message']['body']['track']['track_share_url']))
                webbrowser.open(match_url)
            elif browser == 'no':
                match_val = musixmatch.matcher_lyrics_get(q_track = song, q_artist = artist_name)
                match_lyrics = json.loads(json.dumps(match_val['message']['body']['lyrics']['lyrics_body']))
                click.echo_via_pager(match_lyrics)
        else:
            print('     ' + click.style('Song name and artist not provided', blink = True, fg = 'magenta'))
