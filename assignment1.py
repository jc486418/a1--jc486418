"""
Replace the contents of this module docstring with your own details.
"""


def main():
    songs=[]
    user=str(input('Enter your name: '))
    print("Welcome {}".format(user))
    print("Songs To Learn 1.0 - by {}".format(user))

    load_song(songs)
    print("{} songs loaded".format(len(songs)))
    menu=getmenu(songs)
    while menu !="Q":
        pass

def show_menu():
    print("Menu: ")
    print("L - List songs")
    print("A - Add new xsong")
    print("C - Complete a song")
    print("Q - Quit")

def getmenu(songs):
    menu=show_menu()
    menu = str(input()).upper()
    if menu == "L":
        count_learn = 0
        count_tolearn = 0
        for i, song in enumerate(songs):
            if song[3] == "y":
                leanrd = "*"
                count_tolearn += 1
            else:
                leanrd = " "
                count_learn += 1
            print("{}. {} {:<30s} - {:<25s} {:<15d}".format(i, leanrd, song[0], song[1], song[2]))
        print("{} songs learned, {} songs still to learn".format(count_learn, count_tolearn))
        menu=getmenu(songs)
    elif menu =="A":
        menu=add_song(songs)
        menu = getmenu(songs)
    elif menu =="C":
        menu=complete_song(songs)
        menu = getmenu(songs)
    elif menu =="Q":
        menu=save_song(songs)


    else:
        print("Invalid menu choice")
        menu = getmenu(songs)
def load_song(songs):

    with open("songs.csv", 'r+') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            song = [parts[0], parts[1], int(parts[2]), parts[3]]
            songs.append(song)
def add_song(songs):
    add = []
    print('Input can not be blank')
    title = input("Title: ")

    while title == "":
        print('Input can not be blank')
        title = input("Title: ")
    add.append(title)
    artist=input("Artist: ")
    while artist =="":
        artist = input("Artist: ")
    add.append((artist))
    while True:
        try:
            year=int(input("Year: "))
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            break
    while year <=0:
        print("Number must be >= 0")
        year = int(input("Year: "))
    add.append(year)
    add.append("y")
    print("{} by {} ({}) added to song list".format(add[0], add[1], add[2]))

    songs.append(add)
    print(songs)
def complete_song(songs):
    count_end=0
    for i, song in enumerate(songs):
        if song[3]=="n":
            count_end+=1
    if count_end >= len(songs):
        print("No more songs to learn!")
    else:

        while True:
            try:
                numbersong=int(input("Enter the number of a song to mark as learned: "))
            except ValueError:
                print("Invalid input; enter a valid number")
            else:
                break
        while numbersong<0:
                    print("Number must be >= 0")
                    numbersong = int(input("Enter the number of a song to mark as learned: "))


        if songs[numbersong][3] == "n":
                        print (songs[numbersong][3])
                        print("You have already learned {}".format(songs[numbersong][0]))
        else:
                        songs[numbersong][3] = "n"
                        print("{} by {} learnd".format(songs[numbersong][0], songs[numbersong][1]))

def save_song(songs):
    print("{} songs saved to songs.csv".format(len(songs)))
    print("Have a nice day :)")
main()

