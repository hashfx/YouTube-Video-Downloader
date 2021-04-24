# Import Libraries
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
# GUI Main Window
root = Tk()
root.geometry('500x300') # size of UI window
root.resizable(0,0) # checking window from resizing
root.title("YouTube Video Downloader") # title
# Components of UI
label = Label(root,text = 'Youtube Video Downloader', font ='arial 24 bold', fg='#FF0000')
label.pack() # packed Label

vid_link = StringVar()
# TODO: Error; Center is not defined
Label(root, text = 'Paste Link Here:', font = 'arial 18', fg='green').place(x= 160 , y = 60)
vlink_input = Entry(root, width = 70,textvariable = vid_link).place(x = 32, y = 90)
# Download Function
def Downloader():
    try:
        url =YouTube(str(vid_link.get()))
        video = url.streams.first()
        video.download()
        Label(root, text = 'DOWNLOADED!\r Thanks for Using this Programme!', font = 'arial 20 bold', bg='green', fg='white').place(x= 15 , y = 210) # (180,210)
    # if Video was unable to download, error will be shown
    except:
        Label(root, text = 'Error While Downloading!', font = 'arial 20', bg='red', fg='white').place(x= 95 , y = 210)
        # Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210) # Message after video is Downloaded

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'yellow', fg='red', padx = 2,
                               command = Downloader).place(x=180 ,y = 150) # Download Button
root.mainloop()
