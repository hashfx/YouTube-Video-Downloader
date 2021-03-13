# # from tkinter import *
# # from pytube import YouTube
# # root = Tk()
# # root.geometry('500x300')
# # root.resizable(0,0)
# # root.title("YouTube Video Downloader")
# # Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
# #
# #
# # vid_link = StringVar()
# #
# # Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
# # link_enter = Entry(root, width = 70,textvariable = vid_link).place(x = 32, y = 90)
# #
# # def Downloader():
# #     try:
# #         url =YouTube(str(vid_link.get()))
# #         video = url.streams.first()
# #         video.download()
# #         Label(root, text = 'DOWNLOADED!\r Thanks for Using this Programme!', font = 'arial 15').place(x= 90 , y = 210) # (180,210)
# #     except:
# #         Label(root, text = 'Error While Downloading!', font = 'arial 15').place(x= 140 , y = 210) # (180,210)
# #         # print("Error while Downloading!")
# #
# # Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)
# #
# # root.mainloop()
# #
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
label = Label(root,text = 'Youtube Video Downloader', font ='arial 24 bold')
label.pack() # packed Label

vid_link = StringVar()
# TODO: Error; Center is not defined
Label(root, text = 'Paste Link Here:', font = 'arial 18').place(x= 160 , y = 60)
vlink_input = Entry(root, width = 70,textvariable = vid_link).place(x = 32, y = 90)
# Download Function
def Downloader():
    try:
        url =YouTube(str(vid_link.get()))
        video = url.streams.first()
        video.download()
        Label(root, text = 'DOWNLOADED!\r Thanks for Using this Programme!', font = 'arial 20 bold').place(x= 15 , y = 210) # (180,210)
    # if Video was unable to download, error will be shown
    except:
        Label(root, text = 'Error While Downloading!', font = 'arial 20').place(x= 120 , y = 210)
        # Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210) # Message after video is Downloaded

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2,
                               command = Downloader).place(x=180 ,y = 150) # Download Button
root.mainloop()

# # Import Libraries
# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
# from pytube import YouTube
# # GUI Main Window
# root = Tk()
# root.geometry('400x350') # size of UI window
# root.resizable(0,0) # checking window from resizing
# root.title("YouTube Video Downloader") # title
# # Components of UI
# label = Label(root,text = 'Youtube Video Downloader', font ='comic sans ms')
# label.pack() # packed Label
#
# vlink = StringVar()
#
# Label(root, text = 'Paste Link Here:', font = 'comic sans ms').place(x= 160 , y = 60)
# vlink_input = Entry(root, width = 70,textvariable = vlink).place(x = 32, y = 90)
# # Download Function
# def Downloader():
#     try:
#         url =YouTube(str(vid_link.get()))
#         video = url.streams.first()
#         video.download()
#         Label(root, text = 'DOWNLOADED!\r Thanks for Using this Programme!', font = 'arial 15').place(x= 90 , y = 210) # (180,210)
#     # if Video was unable to download, error will be shown
#     except:
#         Label(root, text = 'Error While Downloading!', font = 'arial 15').place(x= 140 , y = 210)
#
# Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210) # Message after video is Downloaded
# Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2,
#                                command = Downloader).place(x=180 ,y = 150) # Download Button
# root.mainloop()