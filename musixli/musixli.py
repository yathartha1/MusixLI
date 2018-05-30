import click, json
from musixmatch import Musixmatch

musixmatch = Musixmatch('056655ef3170abe3621cfc1bf361b540')
@click.group()
def start():
    pass

@start.command()
@click.option('--country', default = 'US' , help = 'Specify the country, default is US.')
def artists(country):
    '''
    Lists top 20 artists.
    '''
    artist_json = musixmatch.chart_artists(country = country, page = 1, page_size = 20)
    artist_list = json.loads(json.dumps(artist_json['message']['body']['artist_list']))
    for i in range(0, len(artist_list)):
        print(click.style(str(i+1), fg = 'cyan', bold = True), end = '  ')
        print('  ' + artist_list[i]['artist']['artist_name'])

@start.command()
@click.option('--country', default = 'US' , help = 'Specify the country, default is US.')
def songs(country):
    '''
    Lists top 20 songs.
    '''
    songs_json = musixmatch.chart_tracks_get(country = country, page = 1, page_size = 20, f_has_lyrics = 1)
    songs_list = json.loads(json.dumps(songs_json['message']['body']['track_list']))
    for i in range(0, len(songs_list)):
        print(click.style(str(i+1), fg = 'cyan', bold = True), end = '  ')
        print(click.style('Song: ', bold = True, fg = 'green') + songs_list[i]['track']['track_name'])
        print(end = '   ')
        print(click.style('Album: ', bold = True, fg = 'blue') + songs_list[i]['track']['album_name'] + '\n' + click.style('   Artist: ', bold = True, fg = 'yellow') + songs_list[i]['track']['artist_name'] + '\n')

@start.command()
@click.option('--song', default = '', help = 'Search by song name.')
@click.option('--artist', default = '', help = 'Search by artist name.')
def search(song, artist):
    '''
    Provides a detailed list based on the query.
    '''
    if song != '' or artist != '':
        search_val = musixmatch.track_search(q_artist = artist, q_track = song, page = 1, page_size = 10, s_track_rating='desc')
        search_list = json.loads(json.dumps(search_val['message']['body']['track_list']))
        for i in range(0, len(search_list)):
            genre = json.loads(json.dumps(search_list[i]['track']['primary_genres']['music_genre_list']))
            print(click.style(str(i+1), fg = 'cyan', bold = True), end = '  ')
            print(click.style('Song: ', bold = True, fg = 'green') + search_list[i]['track']['track_name'])
            print(end = '   ')
            print(click.style('Album: ', bold = True, fg = 'blue') + search_list[i]['track']['album_name'] + '\n' + click.style('   Artist: ', bold = True, fg = 'yellow') + search_list[i]['track']['artist_name'])
            print(end = '   ')
            if len(genre) != 0:
                print(click.style('Genre: ', bold = True, fg = 'red') + genre[0]['music_genre']['music_genre_name'] + '\n')
            else:
                print(click.style('Genre: ', bold = True, fg = 'red') + 'No genre available\n')
    else:
        print(click.style('No song name or artist provided', blink = True, fg = 'red'))

@start.command()
@click.option('--artist-name', default = '', help = 'Search by artist name.')
def albums(artist_name):
    '''
    Provides list of albums associated with an artist
    '''
    if artist_name != '':
        track_val = musixmatch.track_search(q_artist = artist_name, q_track = '', page = 1, page_size = 1, s_track_rating='desc')
        track_list = json.loads(json.dumps(track_val['message']['body']['track_list']))
        artist_id = track_list[0]['track']['artist_id']
        artist_val = musixmatch.artist_albums_get(artist_id = artist_id, page = 1, page_size = 100, s_release_date = 'desc', g_album_name = 1)
        album_list = json.loads(json.dumps(artist_val['message']['body']['album_list']))
        for i in range(0, len(album_list)):
            print(click.style(str(i+1), fg = 'cyan', bold = True), end = '  ')
            print(click.style('Album Name: ', bold = True, fg = 'green') + album_list[i]['album']['album_name'])
            print(end = '   ')
            print(click.style('Number of Tracks: ', bold = True, fg = 'blue') + str(album_list[i]['album']['album_track_count']) + '\n' + click.style('   Release Date: ', bold = True, fg = 'yellow') + album_list[i]['album']['album_release_date'] + '\n')

@start.command()
def clear():
    '''
    Clears the entire screen.
    '''
    click.clear()
