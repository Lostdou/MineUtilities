import os
import shutil
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

## --------------- Functions -------------------
def callback(url):
    webbrowser.open_new(url)

def move_files(default_destination_folder):

    files = filedialog.askopenfilenames(title="Select Files to Move", multiple=True) 

    change_destination = messagebox.askyesno("Select", "Do you want to change the destination folder?")

    if change_destination:
        destination_folder = filedialog.askdirectory(title="Select Destination Folder")
    else:
        destination_folder = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", ".minecraft", default_destination_folder)

    os.makedirs(destination_folder, exist_ok=True) #Create destination folder if necessary
    for file in files: 
        if file:
            shutil.copy(file, destination_folder)
    messagebox.showinfo("Info", "Completed")


            
## ---------------- Window ----------------------
root = Tk()
root.tk.call('tk', 'scaling', 2.0)
root.geometry('590x500')
root.resizable(0, 0)
root.title('MineUtilities v1.1')
root.configure(bg='#000000')

### ----------------- GUI -----------------------
## ------------- Add Background -----------------
'''
Load background image,
We create a Canvas with the resolution of the tab.
and we enter the image
'''
bg_image = Image.open("background.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tkinter.Canvas(root, width=590, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")
# We keep the image in memory
root.image = bg_photo

## ----------- Labels y Buttons -----------------
# Labels
label = Label(root, text='MineUtilities', font='minecraft 20')
label.place(x=20, y=20)
label = Label(root, text='by lostdou', font='minecraft 7', cursor="hand2")
label.pack()
label.bind("<Button-1>", lambda e: callback("https://github.com/Lostdou"))
label.place(x=20, y=80)
label = Label(root, text='v1.1', font='minecraft 10')
label.place(x=520, y=450)

# Buttons
btn_mover_rp = Button(root, text="Move Resource Pack", font='minecraft 10', cursor="hand2", command=lambda: move_files("resourcepacks"))
btn_mover_rp.place(x=20, y=170)

btn_mover_mod = Button(root, text="Move Mod", font='minecraft 10', cursor="hand2", command=lambda: move_files("mods"))
btn_mover_mod.place(x=20, y=220)

root.mainloop()
