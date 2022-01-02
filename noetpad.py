from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openfile():
    global file
    file = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            #save as file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
            #save file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad Developed By MIJANUR RAHMAN")

if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled _ Notepad")
    # root.wm_iconbitmap("notepad.ico")
    root.geometry("500x400")

    #add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)
    #create menu bar
    MenuBar = Menu(root)

    FileMenu = Menu(MenuBar, tearoff=0)
    #open new file
    FileMenu.add_command(label="New", command=newfile)
    #open already existing file
    FileMenu.add_command(label="Open", command=openfile)
    #save file
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Ecit", command=quitApp)
    #add all features
    MenuBar.add_cascade(label ="File", menu = FileMenu)

    #edit menu
    EditMenu = Menu(MenuBar, tearoff=0)
    #cut feature
    EditMenu.add_command(label="Cut", command=cut)
    #copy feature
    EditMenu.add_command(label="Copy", command=copy)
    #paste feature
    EditMenu.add_command(label="Paste", command=paste)
    #add all features
    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    #help menu
    HelpMenu = Menu(MenuBar, tearoff=0)
    #about feature
    HelpMenu.add_command(label="About Notepad", command=about)
    #add all features
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu = MenuBar)

    #add scroll bar
    ScrollBar = Scrollbar(TextArea)
    ScrollBar.pack(side = RIGHT, fill=Y)
    ScrollBar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=ScrollBar.set)
    root.mainloop()