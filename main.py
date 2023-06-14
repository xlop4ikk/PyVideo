from pytube import YouTube
import tkinter as tk
from tkinter import END

def download_video():
    link = text_box_1.get()
    quality = text_box_2.get()
    folder = text_box_3.get()
    from_link = YouTube(link)
    video_to_download = from_link.streams.get_by_resolution(quality)
    video_to_download.download(folder)

    if link and quality and folder:
        #print("Success!")
        success.pack()
    else:
        #print("Error!")
        error.pack()

def clear():
    text_box_1.delete(0, END)
    text_box_2.delete(0, END)
    text_box_3.delete(0, END)

root = tk.Tk()
root.title("PyVideo")
root.geometry("600x200")
root.resizable(False, False)
root.configure(bg="white")

label_1 = tk.Label(root, text="Input video link:",
                   bg="white", fg="black", font="Consolas")
text_box_1 = tk.Entry(root)

label_2 = tk.Label(root, text="Input video quality: 1080p / 720p / 480p / 360p / 240p / 144p",
                   bg="white", fg="black", font="Consolas")
text_box_2 = tk.Entry(root)

label_3 = tk.Label(root, text="Input folder:",
                   bg="white", fg="black", font="Consolas")
text_box_3 = tk.Entry(root)

button_1 = tk.Button(root, text="Click!", command=download_video)
button_2 = tk.Button(root, text="Clear!", command=clear)

success = tk.Label(root, text="Success!")
error = tk.Label(root, text="Error!")

label_1.pack()
text_box_1.pack()
label_2.pack()
text_box_2.pack()
label_3.pack()
text_box_3.pack()
button_1.pack(ipadx=10, ipady=10, side="left")
button_2.pack(ipadx=10, ipady=10, side="right")

root.mainloop()