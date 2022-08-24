import os
import shutil
import easygui
import tkinter
from tkinter import filedialog
from tkinter import messagebox
from distutils.dir_util import copy_tree

def open_file():
    messagebox.showinfo(title="Open File", message="Select the file you want to open!")
    # File dialog box opens, returns path of selected file.
    srcPath = filedialog.askopenfilename() 
    # If file dialog box gets canceled, returns an empty string.
    if srcPath == "": 
        messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
    else:
        try:
            # Opens the selected filepath.
            os.startfile(srcPath) 
            messagebox.showinfo(title="File Opened", message="You have succesfully opened the file!")
            # Catches most errors, returns the error message in a messagebox.
        except OSError as fileError: 
            messagebox.showerror(title="File Error", message="The following error has occured:\n\n"+ str(fileError) + "\n\nPlease try again!")

def copy_file():
    messagebox.showinfo(title="Copy File", message="Select the file you want to copy!")
    srcPath = filedialog.askopenfilename()
    if srcPath == "":
        messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
    else:
        try:
            messagebox.showinfo(title="Copy File Location", message="Select the location you want to copy the file to!")
            # File dialog box opens, returns path of selected directory.
            destPath = filedialog.askdirectory() 
            if destPath == "":
                messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
            else:
                # Copies the source path to the destination path.
                shutil.copy2(srcPath, destPath)
                messagebox.showinfo(title="File Copied", message="The file was succesfully copied!")
        except OSError as fileError:
            messagebox.showerror(title="File Error", message="The following error has occured:\n\n"+ str(fileError) + "\n\nPlease try again!")

def copy_folder():
    messagebox.showinfo(title="Copy Folder", message="Select the folder you want to copy!")
    srcPath = filedialog.askdirectory()
    if srcPath == "":
        messagebox.showinfo(title="Folder Select Canceled", message="You have canceled the folder selection!")
    else:
        try:
            messagebox.showinfo(title="Copy Folder", message="Select the location you want to copy the folder to!")
            destPath = filedialog.askdirectory()
            if destPath == "":
                messagebox.showinfo(title="Folder Select Canceled", message="You have canceled the folder selection!")
            else:
                # Splits the path of the source in a head[0] and tail[1] part. The tail part is everything that comes after the last slash.
                srcPathSplit = os.path.split(srcPath)
                # Merges the destination path and the tail part of the source path together.
                joinedPath = os.path.join(destPath, srcPathSplit[1])
                # Creates a new directory with the same tail name as the source path, in the destination path.
                os.mkdir(joinedPath)
                # Copies the contents of the source path directory to the joinedPath directory.
                copy_tree(srcPath, joinedPath)
                messagebox.showinfo(title="Folder Copied", message="The folder was succesfully copied")
        except IOError as dirError:
            messagebox.showerror(title="Folder Error", message="The following error has occured:\n\n"+ str(dirError) + "\n\nPlease try again!")

def delete_file():
    messagebox.showinfo(title="Delete File", message="Select the file you want to delete!")
    srcPath = filedialog.askopenfilename()
    if srcPath == "":
        messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
    else:
        try:
            # Deletes the source path.
            os.remove(srcPath)
            messagebox.showinfo(title="File Deleted", message="The file was succesfully deleted!")
        except OSError as fileError:
            messagebox.showerror(title="File Error", message="The following error has occured:\n\n"+ str(fileError) + "\n\nPlease try again!")

def delete_folder():
    messagebox.showinfo(title="Delete Folder", message="Select the folder you want to delete!")
    srcPath = filedialog.askdirectory()
    if srcPath == "":
        messagebox.showinfo(title="Folder Select Canceled", message="You have canceled the folder selection!")
    else:
        try:
            # Deletes the source path.
            shutil.rmtree(srcPath)
            messagebox.showinfo(title="Folder Deleted", message="The folder was succesfully deleted!")
        except OSError as dirError:
            messagebox.showerror(title="Folder Error", message="The following error has occured:\n\n"+ str(dirError) + "\n\nPlease try again!")

def move_file():
    messagebox.showinfo(title="Move File", message="Select the file you want to move!")
    srcPath = filedialog.askopenfilename()
    if srcPath == "":
        messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
    else:
        try:
            messagebox.showinfo(title="Move File", message="Select the location you want to move the file to!")
            destPath = filedialog.askdirectory()
            if destPath == "":
                messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
            else:
                # Moves the source path to the destination path.
                shutil.move(srcPath, destPath)
                messagebox.showinfo(title="File Moved", message="The file has been succesfully moved!")
        except OSError as fileError:
            messagebox.showerror(title="File Error", message="The following error has occured:\n\n"+ str(fileError) + "\n\nPlease try again!")

def move_folder():
    messagebox.showinfo(title="Move Folder", message="Select the folder you want to move!")
    srcPath = filedialog.askdirectory()
    if srcPath == "":
        messagebox.showinfo(title="Folder Select Canceled", message="You have canceled the folder selection!")
    else:
        try:
            messagebox.showinfo(title="Move Folder", message="Select the location you want to move the folder to!")
            destPath = filedialog.askdirectory()
            if destPath == "":
                messagebox.showinfo(title="Folder Select Canceled", message="You have canceled the folder selection!")
            else:
                # Moves the source path to the destination path.
                shutil.move(srcPath, destPath)
                messagebox.showinfo(title="Folder Moved", message="The folder has been succesfully moved!")
        except OSError as dirError:
            messagebox.showerror(title="Folder Error", message="The following error has occured:\n\n"+ str(dirError) + "\n\nPlease try again!")

def rename_file():
    messagebox.showinfo(title="Rename File", message="Select the file you want to rename!")
    srcPath = filedialog.askopenfilename()
    if srcPath == "":
        messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
    else:
        try:
            # Returns path directory of source.
            dirSrcPath = os.path.dirname(srcPath)
            # Splits the source path into a root and an extension(file type).
            destPath = os.path.splitext(srcPath)[1]
            messagebox.showinfo(title="Rename File", message="Enter the new file name!")
            userInput = easygui.enterbox("Enter filename here:")
            if userInput == "":
                messagebox.showwarning(title="No Input", message="You have not entered anything!")
            # Easygui input box returns 'None' when user presses cancel.
            elif userInput == None:
                messagebox.showinfo(title="File Renaming Canceled", message="You have canceled the file renaming!")
            else:
                # Merges the directory source path with the user input and the extension of the source file.
                newPath = os.path.join(dirSrcPath, userInput + destPath)
                # Renames the source path to the merged destination path.
                os.rename(srcPath, newPath)
                messagebox.showinfo(title="File Renamed", message="The file has succesfully been renamed!")
        except OSError as fileError:
            messagebox.showerror(title="File Error", message="The following error has occured:\n\n"+ str(fileError) + "\n\nPlease try again!")

def create_folder():
    messagebox.showinfo(title="Create Folder", message="Select the location where you want to create the folder!")
    srcPath = filedialog.askdirectory()
    if srcPath == "":
        messagebox.showinfo(title="Folder Select Canceled", message="You have canceled the folder selection!")
    else:
        try:
            messagebox.showinfo(title="Folder Name", message="Enter the name of the folder you want to create!")
            userInput = easygui.enterbox("Enter your folder name here: ")
            if userInput == "":
                messagebox.showwarning(title="No input", message="You have not entered anything!")
            elif userInput == None:
                messagebox.showinfo(title="Folder Naming Canceled", message="You have canceled the folder naming!")
            else:
                # Merges the directory source path with the user input.
                newPath= os.path.join(srcPath, userInput)
                # Creates the directory at the new path that was merged.
                os.mkdir(newPath)
                messagebox.showinfo(title="Folder Created", message="The folder was succesfully created!")
        except OSError as dirError:
            messagebox.showerror(title="Folder Error", message="The following error has occured:\n\n"+ str(dirError) + "\n\nPlease try again!")

def listFiles_folder():
    messagebox.showinfo(title="List Files in Folder", message="Select the folder you want to list the files of!")
    srcPath = filedialog.askdirectory()
    if srcPath == "":
        messagebox.showinfo(title="Folder Select Canceled", message="You have canceled the folder selection!")
    else:
        try:
            # Lists all the files in directory path.
            listFilesDir = os.listdir(srcPath)
            # Adds a new line after each listed file.
            listFilesDir = "\n".join(listFilesDir)
            # Displays the listed files in a message box.
            messagebox.showinfo(title="Files Listed", message=listFilesDir)
            messagebox.showinfo(title="Files Listed", message="The files from the selected folder were succesfully listed!")
            # Displays the listed files in the terminal.
            print(listFilesDir)
        except OSError as dirError:
            messagebox.showerror(title="Folder Error", message="The following error has occured:\n\n"+ str(dirError) + "\n\nPlease try again!")

def gui_window():

    # The main window of the GUI.
    guiWindow = tkinter.Tk()

    # Displays the text at the top of the application.
    tkinter.Label(guiWindow, text="Lucas' Files Manager\n", fg="green", font=("", 40, "normal", "underline")).pack()
    
    # Displays all the individual buttons, that have the functions attached to them as a command.
    tkinter.Button(guiWindow, text="Open File", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=open_file).pack()
    tkinter.Button(guiWindow, text="Copy File", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=copy_file).pack()
    tkinter.Button(guiWindow, text="Copy Folder", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=copy_folder).pack()
    tkinter.Button(guiWindow, text="Delete File", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=delete_file).pack()
    tkinter.Button(guiWindow, text="Delete Folder", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=delete_folder).pack()
    tkinter.Button(guiWindow, text="Move File", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=move_file).pack()
    tkinter.Button(guiWindow, text="Move Folder", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=move_folder).pack()
    tkinter.Button(guiWindow, text="Rename File", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=rename_file).pack()
    tkinter.Button(guiWindow, text="Create Folder", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=create_folder).pack()
    tkinter.Button(guiWindow, text="List all files in folder", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=listFiles_folder).pack()
    tkinter.Button(guiWindow, text="Exit Program", width=25, height=1, bg="blue", fg="red", font=("", "20", "bold"), command=guiWindow.destroy).pack()

    guiWindow.mainloop()

# Calls the GUI function to start the application.
gui_window()
