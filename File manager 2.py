import os
import shutil
import easygui
import tkinter
from tkinter import filedialog
from tkinter import messagebox

def open_file():
    messagebox.showinfo(title="Open File", message="Select the file you want to open!")
    openFile = filedialog.askopenfilename()
    if openFile == "":
        messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
    else:
        try:
            os.startfile(openFile)
            messagebox.showinfo(title="File Opened", message="You have succesfully opened the file!")
        except OSError as openFileError:
            messagebox.showerror(title="File Error", message="The following error has occured:\n\n"+ str(openFileError) + "\n\nPlease try again!")

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
        except OSError as copyFileError:
            messagebox.showerror(title="File Error", message="The following error has occured:\n\n"+ str(copyFileError) + "\n\nPlease try again!")
            
def delete_file():
    messagebox.showinfo(title="Delete File", message="Select the file you want to delete!")
    fileNameDelete = filedialog.askopenfilename()
    if fileNameDelete == "":
        messagebox.showinfo(title="File Select Canceled", message="You have canceled the file selection!")
    else:
        try:
            os.remove(fileNameDelete)
            messagebox.showinfo(title="File Deleted", message="The file was succesfully deleted!")
        except OSError as deleteFileError:
            messagebox.showerror(title="File Error", message="The following error has occured:\n\n"+ str(deleteFileError) + "\n\nPlease try again!")

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
            renameFileInput = easygui.enterbox("Enter filename here:")
            if renameFileInput == "":
                messagebox.showwarning(title="No Input", message="You have not entered anything!")
            elif renameFileInput == None:
                messagebox.showinfo(title="File Renaming Canceled", message="You have canceled the file renaming!")
            else:
                newPath = os.path.join(namePath, renameFileInput + renameFileDestination)
                os.rename(renameFileSource, newPath)
                messagebox.showinfo(title="File Renamed", message="The file has succesfully been renamed!")
        except OSError as renameFileError:
            messagebox.showerror(title="File Error", message="The following error has occured:\n\n"+ str(renameFileError) + "\n\nPlease try again!")

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
        except OSError as moveFileError:
            messagebox.showerror(title="File Error", message="The following error has occured:\n\n"+ str(moveFileError) + "\n\nPlease try again!")

def delete_folder():
    messagebox.showinfo(title="Delete Folder", message="Select the folder you want to delete! \n\nWARNING: The folder must be empty!")
    deleteFolderName = filedialog.askdirectory()
    if deleteFolderName == "":
        messagebox.showinfo(title="Folder Select Canceled", message="You have canceled the folder selection!")
    else:
        try:
            os.rmdir(deleteFolderName)
            messagebox.showinfo(title="Folder Deleted", message="The folder was succesfully deleted!")
        except OSError as deleteFolderError:
            messagebox.showerror(title="Folder Error", message="The following error has occured:\n\n"+ str(deleteFolderError) + "\n\nPlease try again!")

def create_folder():
    messagebox.showinfo(title="Create Folder", message="Select the location where you want to create the folder!")
    createFolderSource = filedialog.askdirectory()
    if createFolderSource == "":
        messagebox.showinfo(title="Folder Select Canceled", message="You have canceled the folder selection!")
    else:
        try:
            messagebox.showinfo(title="Folder Name", message="Enter the name of the folder you want to create!")
            createFolderName = easygui.enterbox("Enter your folder name here: ")
            if createFolderName == "":
                messagebox.showwarning(title="No input", message="You have not entered anything!")
            elif createFolderName == None:
                messagebox.showinfo(title="Folder Naming Canceled", message="You have canceled the folder naming!")
            else:
                createFolder = os.path.join(createFolderSource, createFolderName)
                os.mkdir(createFolder)
                messagebox.showinfo(title="Folder Created", message="The folder was succesfully created!")
        except OSError as createFolderError:
            messagebox.showerror(title="Folder Error", message="The following error has occured:\n\n"+ str(createFolderError) + "\n\nPlease try again!")

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
        except OSError as listFilesError:
            messagebox.showerror(title="File Error", message="The following error has occured:\n\n"+ str(listFilesError) + "\n\nPlease try again!")

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

gui_window()
