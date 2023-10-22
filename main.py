from tkinter import *
from tkinter import filedialog as fd
from tkvideo import tkvideo


# function to browse the folder
def browse_folder():
    # using the askdirectory() method of the filedialog module to select the directory
    upload_path = fd.askopenfilename(initialdir="D:\Projects\General\YoutubeVideoDownloader\Downloads", title="Select the folder to upload video")
    # using the set() method to set the directory path in the entry field
    upload_dir.set(upload_path)
    browse_button_clicked.set(True)

# function to play video
def play_video():

    # get video file path
    upload_path = upload_dir.get()
    # create video object
    player = tkvideo(upload_path, body_label, loop=1)
    # play video
    player.play()


if __name__ == "__main__":

    # creating an object of the Tk() class
    gui_root = Tk()

    # setting the title of the window
    gui_root.title("Video player")

    # setting the size and position of the window
    gui_root.resizable(1,1)

    # create header frame to hold browse activity
    header_frame = Frame(gui_root, bg="#FEE4E3")
    # create body frame to create space to show video
    body_frame = Frame(gui_root, bg="#FEE4E3")
    # place the frames into the window
    header_frame.pack()
    body_frame.pack()

    # create label to display prompt, place it inside header frame
    src_label = Label(header_frame, text="Select video:", font=("verdana", "10"), bg="#FEE4E3", fg="#000000", anchor=SE)
    src_label.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    upload_dir = StringVar()

    # create text space for video upload path, placed inside header frame
    src_field = Entry(header_frame, textvariable=upload_dir, width=26, font=("verdana", "10"),
                      bg="#FFFFFF", fg="#000000", relief=GROOVE)
    src_field.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

    # create button to browse video, placed inside header frame
    browse_button = Button(header_frame, text="Browse", width=7, font=("verdana", "10"), bg="#FF9200",
                           fg="#FFFFFF", activebackground="#FFE0B7", activeforeground="#000000",
                           relief=GROOVE, command=browse_folder)
    browse_button.grid(row=0, column=3, padx=5, pady=5)

    # create boolean variable to detect browse button click, set to default 'False'
    browse_button_clicked = BooleanVar()
    browse_button_clicked.set(False)

    # create label to hold playing video, placed in body frame
    body_label = Label(body_frame, bg="#FEE4E3", fg="#000000", anchor=SE)
    body_label.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    # wait for 'Browse' button to be clicked
    browse_button.wait_variable(browse_button_clicked)

    # once video browsed and uploaded, play it
    if browse_button_clicked:
        play_video()

    gui_root.mainloop()