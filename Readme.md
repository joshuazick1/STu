# CMCUCP: The Complete Star Trek Chronological Playlist

This is a simple script that generates a Plex playlist with everything in your library from Star Trek, in chronological order (according to [this page](http://thestartrekchronologyproject.blogspot.com/)).

Fun fact: This is about infinate days of continuous video.

## The new fancy docker way

- `docker run --rm ghcr.io/pjnes/cmcucp PLEX_USER PLEX_PASS PLEX_SERVER [PLEX_PLAYLIST]`

## The old manual way
### Requirements
- Python 3.
- PIP.
- A Plex server somewhere.
- An unhealthily large collection of Marvel videos.

### Setup
- Clone this repo somewhere. Anywhere. Use your imagination.
- Install the dependencies with `pip install -r requirements.txt`.

### Usage
- Just run `python stu.py PLEX_USER PLEX_PASS PLEX_SERVER`.
- Wait.
- It will create a new playlist in your Plex library and report any items it couldn't find.
