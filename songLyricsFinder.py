'''
Topic: Finding songs lyrics using tkinter for user interface and
lyricsgenius for searching songs lyrics
'''

from tkinter import *  # Importing tkinter module
from PIL import ImageTk, Image # Import PIL for using jpeg image in background
import lyricsgenius as lg # Import lyricsgenius

# Creating Tk object
root = Tk()

# Setting up root width and height
root.geometry("600x800")

# root title
root.title("Lyrics Finder")

# Disenabling root resize property
root.resizable(0, 0)

# Setting up background image and placing it
bgImg = Image.open("Img/musicbg.jpg") # image path
bgPhoto = ImageTk.PhotoImage(bgImg)
bgLbl = Label(root, image=bgPhoto)
bgLbl.place(x=0, y=0, relwidth=1, relheight=1)


def back_to_main():
    '''
    This function will take user back to main_func
    '''

    # Deleting widgets of show_lyrics function
    del2_list = [scroll_x, scroll_y, song_textbox, back_btn]
    for i in del2_list:
        i.destroy()

    main_func()

# Function to show lyrics
def show_lyrics():
    '''
    This function will show lyrics of the song
    '''

    global scroll_x, scroll_y, song_textbox, back_btn

    # Deleting widgets of main_func
    del_list = [main_lbl, entry_box, sub_lbl, go_btn]
    for i in del_list:
        i.destroy()

    # Getting song name from song_var and setting it to root title
    song_name = song_var.get().title()
    root.title(song_name)

    # Scroll bar for horizontal and vertical axis
    scroll_x = Scrollbar(root, orient="horizontal")
    scroll_y = Scrollbar(root, orient="vertical")

    # Packing scrollbar at required position
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)

    # Textbox where lyrics will be showe up
    song_textbox = Text(root, width=69, height=40, bg="black", fg="purple", xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set, font="time 10 bold")
    song_textbox.place(x=20, y=20)

    # Searching for song lyrics
    genius = lg.Genius('k5xSXuJ5pvl3FeoHBO7AuenYt7BZDfMYdI4QkYMJBrcp8uY4SPSKCBKntUP80ku4',
                        skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                        remove_section_headers=True)


    song = genius.search_song(song_name)

    # Inserting lyrics in song_textbox
    song_textbox.insert(END, song.artist)
    song_textbox.insert(END, "\n\n")

    for i in song.lyrics:
        song_textbox.insert(END, i)

    song_textbox.insert(END, "\n\n")

    # Connecting scrollbar to song_textbox widget
    scroll_x.config(command=song_textbox.xview)
    scroll_y.config(command=song_textbox.yview)

    # Buttton to return back to main screen
    back_btn = Button(root, text="Back", bg="black", fg="purple", font="time 15 bold", width=10, command=back_to_main)
    back_btn.place(x=20, y=680)


def main_func():
    '''
    This is the main function
    '''

    global main_lbl, entry_box, sub_lbl, go_btn, song_var

    # Main heading
    main_lbl = Label(root, text="Lyrics Finder", font="harrington 40 bold underline", fg="purple", bg="black")
    main_lbl.place(x=150, y=170)

    song_var = StringVar() # Variabel for storing user input

    # Entry box for taking user input
    entry_box = Entry(root, textvar=song_var, width=50, bg="lightgrey", fg="black", font="time 15 bold")
    entry_box.place(x=25, y=300, height=60)

    sub_lbl = Label(root, text="Type the name of the song in the above box...", font="harrington 17 bold italic", fg="purple", bg="black")
    sub_lbl.place(x=25, y=380)

    # Go button will take the user where lyrics are
    go_btn = Button(root, text="Go-->", bg="black", fg="purple", font="time 15 bold", width=10, command=show_lyrics)
    go_btn.place(x=240, y=500)


main_func() # Calling main function
root.mainloop() # Calling root.mainloop() to run our program
