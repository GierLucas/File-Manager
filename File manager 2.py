import os
import shutil
import tkinter
from tkinter import filedialog
from tkinter import messagebox

def open_file():
    messagebox.showinfo(title="Open File", message="Select the file you want to open!")
    openFile = filedialog.askopenfilename()
    if openFile == "":
        messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
    else:
        os.startfile(openFile)
        messagebox.showinfo(title="File Opened", message="You have succesfully opened the file!")

def copy_file():
    messagebox.showinfo(title="Copy File", message="Select the file you want to copy!")
    copyFileSource = filedialog.askopenfilename()
    if copyFileSource == "":
        messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
    else:
        try:
            messagebox.showinfo(title="Copy File Location", message="Select the location you want to copy the file to!")
            copyFileDestination = filedialog.askdirectory()
            if copyFileDestination == "":
                messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
            else:
                shutil.copy2(copyFileSource, copyFileDestination)
                messagebox.showinfo(title="File Copied", message="The file was succesfully copied!")
        except IOError:
            messagebox.showinfo(title="Same Folder Select", message="You have selected the same folder as the source file.\nPlease select another folder!")

def delete_file():
    messagebox.showinfo(title="Delete File", message="Select the file you want to delete!")
    fileNameDelete = filedialog.askopenfilename()
    if fileNameDelete == "":
        messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
    else:
        try:
            os.remove(fileNameDelete)
            messagebox.showinfo(title="File Deleted", message="The file was succesfully deleted!")
        except OSError:
            messagebox.showinfo(title="Delete File Error", message="An unknown error has occured, please try again!")

def rename_file():
    messagebox.showinfo(title="Rename File", message="Select the file you want to rename!")
    renameFileSource = filedialog.askopenfilename()
    if renameFileSource == "":
        messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
    else:
        try:
            namePath = os.path.dirname(renameFileSource)
            renameFileDestination = os.path.splitext(namePath)[1]
            messagebox.showinfo(title="Rename File", message="Enter the new file name!")
            renameFileInput = input("Enter the new file name here: ")
            if renameFileInput == "":
                messagebox.showinfo(title="No input", message="You have not entered anything!")
            else:
                newPath = os.path.join(namePath, renameFileInput + renameFileDestination)
                os.rename(renameFileSource, newPath)
                messagebox.showinfo(title="File Renamed", message="The file has succesfully been renamed!")
        except IOError or OSError:
            messagebox.showinfo(title="File Error", message="An unknown error has occured, please try again!")

def move_file():
    messagebox.showinfo(title="Move File", message="Select the file you want to move!")
    moveFileSource = filedialog.askopenfilename()
    if moveFileSource == "":
        messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
    else:
        try:
            messagebox.showinfo(title="Move File", message="Select the location you want to move the file to!")
            moveFileDestination = filedialog.askdirectory()
            if moveFileDestination == "":
                messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
            else:
                shutil.move(moveFileSource, moveFileDestination)
                messagebox.showinfo(title="File Moved", message="The file has been succesfully moved!")
        except IOError or OSError:
            messagebox.showinfo(title="File Error", message="An unknown error has occured, please try again!")

def delete_folder():
    messagebox.showinfo(title="Delete Folder", message="Select the folder you want to delete! \n\nWARNING: The folder must be empty!")
    deleteFolderName = filedialog.askdirectory()
    if deleteFolderName == "":
        messagebox.showinfo(title="Folder Select Canceled", message="You have canceled the folder selection!")
    else:
        try:
            os.rmdir(deleteFolderName)
            messagebox.showinfo(title="Folder Deleted", message="The folder was succesfully deleted!")
        except IOError or OSError:
            messagebox.showinfo(title="File Error", message="An unknown error has occured, please try again!")

def create_folder():
    messagebox.showinfo(title="Create Folder", message="Select the location where you want to create the folder!")
    createFolderSource = filedialog.askdirectory()
    if createFolderSource == "":
        messagebox.showinfo(title="Folder Select Canceled", message="You have canceled the folder selection!")
    else:
        try:
            messagebox.showinfo(title="Folder Name", message="Enter the name of the folder you want to create!")
            createFolderName = input("Enter your folder name here: ")
            if createFolderName == "":
                messagebox.showinfo(title="No input", message="You have not entered anything!")
            else:
                createFolder = os.path.join(createFolderSource, createFolderName)
                os.mkdir(createFolder)
                messagebox.showinfo(title="Folder Created", message="The folder was succesfully created!")
        except IOError or OSError:
            messagebox.showinfo(title="File Error", message="An unknown error has occured, please try again!")

def listFiles_folder():
    messagebox.showinfo(title="List Files in Folder", message="Select the folder you want to list the files of!")
    listFilesName = filedialog.askdirectory()
    if listFilesName == "":
        messagebox.showinfo(title="Folder Select Canceled", message="You have canceled the folder selection!")
    else:
        try:
            listFilesFolder = os.listdir(listFilesName)
            listFilesFolder = "\n".join(listFilesFolder)
            messagebox.showinfo(title="Files Listed", message=listFilesFolder)
            messagebox.showinfo(title="Files Listed", message="The files from the selected folder were succesfully listed!")
            print(listFilesFolder)
        except IOError or OSError:
            messagebox.showinfo(title="File Error", message="An unknown error has occured, please try again!")

def gui_window():
    guiWindow = tkinter.Tk()
    tkinter.Label(guiWindow, text="Lucas' Files Manager\n", fg="green", font=("", 40, "normal", "underline")).pack()
    
    tkinter.Button(guiWindow, text="Open File", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=open_file).pack()
    tkinter.Button(guiWindow, text="Copy File", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=copy_file).pack()
    tkinter.Button(guiWindow, text="Delete File", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=delete_file).pack()
    tkinter.Button(guiWindow, text="Rename File", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=rename_file).pack()
    tkinter.Button(guiWindow, text="Move File", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=move_file).pack()
    tkinter.Button(guiWindow, text="Delete Folder", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=delete_folder).pack()
    tkinter.Button(guiWindow, text="Create Folder", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=create_folder).pack()
    tkinter.Button(guiWindow, text="List all files in selected folder", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=listFiles_folder).pack()
    tkinter.Button(guiWindow, text="Exit Program", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=guiWindow.destroy).pack()

    guiWindow.mainloop()

'''
def entry_box():
    entryBox = tkinter.Tk()

    def callback():
        renameFileInput = entryInput.get()
        print(renameFileInput)
        entryBox.destroy()

    tkinter.Label(entryBox, text="Enter data here: ").pack()
    entryInput = tkinter.Entry(entryBox)
    entryInput.pack()
    btn = tkinter.Button(entryBox, text="GO!", width=3, height=1, command=callback)
    btn.pack()

    entryBox.mainloop()
'''

gui_window()