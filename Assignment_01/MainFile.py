import csv

class Song:
    def __init__(self, learned, name, artist, year):
        self.learned = learned
        self.name = name
        self.artist = artist
        self.year = year

    def learn(self):
        self.learned = "*"

    def unlearn(self):
        self.learned = ""

    #delf printSong(self):
    #    print()

def appendSonglist(Song, SongArray):
    SongArray = []
    SongArray.append(Song)
    return SongArray

#Below is the main function:

csv_song_list_file = open("songs.csv", "r")
csv_song_list = csv.reader(csv_song_list_file)

a_song_str = []
songList = []

for line in csv_song_list:
    a_song_str = line
    a_song = Song(a_song_str[0], a_song_str[1], a_song_str[2], a_song_str[3],)
    print("{:>10s} {:<30s} {:<30s} {:>5s}".format(a_song.learned, a_song.name, a_song.artist, a_song.year))
    songList.append(a_song)

print()
print("-------------------")

print("{:<10s} {:<30s} {:<30s} {:>5s}".format("LEARNED?", "SONG NAME", "ARTIST", "YEAR"))

for element in songList:
    print("{:<10s} {:<30s} {:<30s} {:>5s}".format(element.learned, element.name, element.artist, element.year))