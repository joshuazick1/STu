import math, sys
from plexapi.myplex import MyPlexAccount
from plexapi.playlist import Playlist
from plexapi.exceptions import NotFound

# Parse Arguments
if len(sys.argv) < 4:
    print("Arguments: PLEX_USER PLEX_PASS PLEX_SERVER [PLEX_PLAYLIST]")
    exit(1)

plex_user = sys.argv[1]
plex_pass = sys.argv[2]
plex_server = sys.argv[3]
plex_playlist = "Complete Star Trek Chronological Playlist"

if len(sys.argv) == 5:
    plex_playlist = sys.argv[4]


# Add a movie from plex to the playlist.
def addmovie(title):
    try:
        item = plex.library.section('Movies').get(title)
    except NotFound:
        errors.append(title)
        print("Failed to add %(title)s" % {'title': title })
    else:
        items.append(item)
        print("Added %(title)s" % {'title': title })

# Add a TV show episode or range of episodes from plex to the playlist.
def addtv(show, season, episode, end = False):
    if not end:
        end = episode
    end = end + 1
    show = "Star Trek: %(show)s" % { 'show': show }
    for number in range(episode, end):
        values = { 'show': show, 'season': season, 'number': number}
        try:
            item = plex.library.section('TV Shows').get(show).episode(season=season, episode=number)
        except NotFound:
            errors.append("%(show)s Season %(season)d Episode %(number)d" % values)
            print("Failed to add %(show)s Season %(season)s Episode %(number)s" % values)
        else:
            items.append(item)
            print("Added %(show)s Season %(season)s Episode %(number)s" % values)

# Login
try:
    account = MyPlexAccount(plex_user, plex_pass)
    plex = account.resource(plex_server).connect()
    print("Logged in to %(server)s as %(user)s" % {'server': plex_server, 'user': plex_user})
except:
    print("Failed to login to %(server)s as %(user)s" % {'server': plex_server, 'user': plex_user})
    exit()

# Delete existing playlist
try:
    plex.playlist(plex_playlist).delete()
    print("Removing existing playlist called '%(playlist)s" % {'playlist': plex_playlist})
except:
    print("No existing playlist called '%(playlist)s" % {'playlist': plex_playlist})

items = []
errors = []

# Order Source: http://thestartrekchronologyproject.blogspot.com/
# Rough Draft, will need to do individual episode ordering later

addtv("Enterprise", 1, 1, 26)
addtv("Enterprise", 2, 1, 26)
addtv("Enterprise", 3, 1, 24)
addtv("Enterprise", 4, 1, 17)
addtv("Enterprise", 4, 20, 21)
addtv("The Original Series", 0, 1, 1)
addtv("Discovery", 1, 1, 15)
addtv("Discovery", 2, 1, 14)
addtv("The Original Series", 1, 1, 29)
addtv("The Original Series", 1, 2, 26)
addtv("The Original Series", 3, 1, 9)
addtv("Enterprise", 4, 18, 19)
addtv("The Original Series", 3, 10, 24)
addmovie("Star Trek: The Motion Picture")
addtv("Lower Decks", 1, 1, 10)
addmovie("Star Trek")
addmovie("Star Trek Into Darkness")
addmovie("Star Trek Beyond")
addtv("Short Treks", 2, 6, 6)
addtv("Picard", 1, 1, 10)
addtv("Voyager", 4, 23, 23)
addtv("Discovery", 3, 1, 13)

print("----------------------------------------------------")

# Create playlist
if len(items) > 0:
    print("%(items)s" % { 'item': item })
    playlist = Playlist.create(plex, plex_playlist, items)
else:
    print("Script couldn't find any items to add to your Star Trek playlist")
    exit()

# Get playlist duration
hours = math.floor(playlist.duration / 1000 / 60 / 60)
time = "%(days)d days and %(hours)d hours" % { 'days': math.floor(hours / 24), 'hours': hours % 24 }

if len(errors) > 0:
    print("The following files could not be found to add to the playlist.")
    for item in errors:
        print("- %(item)s" % { 'item': item })
    print("Run the script again once these items are in Plex.")

print("----------------------------------------------------")
print("Enjoy %(time)s of Star Trek!" % {'time': time})
