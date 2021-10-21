from music_collection import SongCollection
from music import Music

def cls() -> None:
    print("\033[H\033[J", end="")

def print_song(index: int, song: Music) -> None:
    print("%5s] %-45s %-15s %15s" % (index, song.get_title(), song.get_performer(), song.get_duration()))

def print_header(data: str) -> None:
    cls()
    print("%45s" % (data))

def print_alert(alert):
    if alert != "":
        print()
        print(alert)
        print()

def print_menu(header: str, options, alert: str = "") -> None:
    print_header(header)
    print_alert(alert)
    for x in range(1, len(options) + 1):
        print("[%-5s] %-20s" % (x, options[x - 1]))

def print_song_header():
    print("%5s] %-45s %-15s %15s" % ("Index", "Song Name", "Performer", "Duration (s)"))

def print_song_tree(col: SongCollection):
    print_song_header()
    c = 1
    for x in col:
        print_song(c, x)
        c += 1

def prompt(header: str, prompts, alert: str = ""):
    print_header(header)
    print_alert(alert)
    data = []
    for x in range(1, len(prompts) + 1):
        data.append(input("[%-5s] %s: " % (x, prompts[x-1])))
    return data

def song_prompt(header: str, prompts, col: SongCollection, alert: str = ""):
    print_header(header)
    print_alert(alert)
    print_song_tree(col)
    print()
    data = []
    for x in range(1, len(prompts) + 1):
        data.append(input("[%-5s] %s: " % (x, prompts[x-1])))
    return data

def single_song_prompt(header: str, prompts, song: Music, alert: str = ""):
    print_header(header)
    print_alert(alert)
    print_song_header()
    print_song(1, song)
    print()
    data = []
    for x in range(1, len(prompts) + 1):
        data.append(input("[%-5s] %s: " % (x, prompts[x-1])))
    return data

def main():
    print_menu("Music Machine", ["Press enter to start"])

    input()

    col = SongCollection()
    options = ["Add Song"]
    options.append("Remove Song")
    options.append("List Songs")
    options.append("Search By Title")
    options.append("Search By Performer")
    options.append("Edit Song Details")
    options.append("Shutdown")
    print_menu("Music Machine", options)

    data = input()

    while data != "7":
        alert = ""
        if data == "1":
            alert = add_song(col)
        elif data == "2":
            alert = remove_song(col)
        elif data == "3":
            alert = list_songs(col)
        elif data == "4":
            alert = title_search(col)
        elif data == "5":
            alert = performer_search(col)
        elif data == "6":
            alert = edit(col)
        else:
            alert = "A value between 1 and 7 must be entered."

        print_menu("Music Machine", options, alert)
        data = input()

    cls()
    print("Music Machine Shutting Down...")

def add_song(col: SongCollection) -> str:
    prompts = ["Enter the name of the song to add"]
    prompts.append("Enter the performer of the song")
    prompts.append("Enter the runtime of the song in seconds")
    data = prompt("Add Song", prompts)

    try:
        seconds = int(data[2])
        song = Music(data[0], data[1], seconds)
        col.append(song)
        return "Added the song: {a}".format(a = song)
    except Exception as ex:
        return "An invalid time in seconds was etered"

def remove_song(col: SongCollection) -> str:
    prompts = ["Enter the ID of the song to remove"]
    data = song_prompt("Remove Song", prompts, col)

    index = None
    try:
        index = int(data[0])
    except:
        return "The song index must be a number."

    try:
        res = col.remove(index - 1)
        return "Removed the song: {a}".format(a = res) 
    except IndexError:
        return "The selection does not exist!"

def list_songs(col: SongCollection) -> str:
    song_prompt("Song List", ["Press enter to close"], col)
    return ""

def title_search(col: SongCollection) -> str:
    data = prompt("Title Search", ["Enter a title to search for"])
    song = col.find_by_title(data[0])

    if song is None:
        return "No song found by that title."
    else:
        single_song_prompt("Found Track", ["Press enter to close"], song)
        return ""

def performer_search(col: SongCollection) -> str:
    data = prompt("Performer Search", ["Enter a performer to search for"])
    song = col.find_by_performer(data[0])

    if song is None:
        return "No song found by that title."
    else:
        single_song_prompt("Found Track", ["Press enter to close"], song)
        return ""

def edit(col: SongCollection) -> str:
    data = song_prompt("Edit Song", ["Select a Song to Edit"], col)

    index = None
    try:
        index = int(data[0])
    except:
        return "The song index must be a number."

    song = None
    try:
        song = col[index - 1]
    except:
        return "The selected index does not exist!"

    prompts = ["Enter the new song name"]
    prompts.append("Enter the new song performer")
    prompts.append("Enter the new song runtime")
    data = single_song_prompt("Edit Song", prompts, song)

    seconds = None
    try:
        seconds = int(data[2])
    except Exception as ex:
        return "An invalid time in seconds was etered"

    old = "Edited {} ".format(song)

    song.set_duration(seconds)
    song.set_title(data[0])
    song.set_performer(data[1])

    return old + "to {}".format(song)

if __name__ == "__main__":
    main()