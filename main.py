import os
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from functions import *
from script_info import *

widgets = []

## --------------- Functions -------------------

def destroy_widgets(): # Limpia los Labels y Botones de la ventana anterior
    for widget in widgets:
        widget.destroy()
    widgets.clear()

def home_window(): # Es el menú principal hecho funcion, no se puede volver al original asi que esta es la alternativa
    global canvas
    destroy_widgets()
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    label = Label(root, text=project_name, font='minecraft 20')
    label.place(x=20, y=20)
    widgets.append(label)
    label = Label(root, text=made_by, font='minecraft 7', cursor="hand2")
    label.pack()
    label.bind("<Button-1>", lambda e: callback("https://github.com/Lostdou"))
    label.place(x=20, y=80)
    widgets.append(label)
    label = Label(root, text=script_ver, font='minecraft 10')
    label.place(x=1000, y=670)
    widgets.append(label)
    btn_new_window = tkinter.Button(root, text="Modpacks", font='minecraft 10', command=open_modpack_window)
    btn_new_window.pack()
    btn_new_window.place(x=20, y=270)
    widgets.append(btn_new_window)

def open_modpack_window(): # Es el menú de Modpacks, desde aca se deberia poder crear/modificar/borrar "perfiles" o modpacks. Ademas de volver al menu principal
    global canvas
    destroy_widgets()
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    label = tkinter.Label(root, text="Modpacks", font='minecraft 15')
    label.place(x=265, y=20)
    widgets.append(label)
    btn_newdatapack = Button(canvas, text="Create new Modpack", font='minecraft 10', cursor="hand2", command=new_modpack_window)
    btn_newdatapack.place(x=20, y=200)
    widgets.append(btn_newdatapack)
    btn_newdatapack = Button(canvas, text="Edit an existent Modpack", font='minecraft 10', cursor="hand2", command=choose_modpack)
    btn_newdatapack.place(x=20, y=250)
    widgets.append(btn_newdatapack)
    btn_home = Button(canvas, text="Home", font='minecraft 10', cursor="hand2", command=home_window)
    btn_home.place(x=20, y=300)
    widgets.append(btn_home)

def new_modpack_window(): # Es el menu para crear los modpacks, lo ideal seria que fuera una pestaña aparte y se cierre al terminar, deberias arreglarlo
    global canvas
    destroy_widgets()
    canvas.delete("all")
    label = tkinter.Label(root, text="Create modpack", font='minecraft 15')
    label.place(x=110, y=20)
    widgets.append(label)
    directory_name = StringVar()
    label = Label(root, text='Name the modpack:', font='minecraft 10')
    label.place(x=100, y=90)
    widgets.append(label)
    directory_name_enter = Entry(root, width=32, textvariable=directory_name)
    directory_name_enter.place(x=32, y=120)
    widgets.append(directory_name_enter)
    btn_newdatapack = Button(root, text="Enter", font='minecraft 10', cursor="hand2", command=lambda: create_modpack(directory_name.get()))
    btn_newdatapack.place(x=150, y=150)
    widgets.append(btn_newdatapack)
    btn_newdatapack = Button(root, text="Back", font='minecraft 10', cursor="hand2", command=open_modpack_window)
    btn_newdatapack.place(x=125, y=200)
    widgets.append(btn_newdatapack)

def created_modpack_window(modpack_name): # Es el menu para modificar Modpacks creados, deberias poder buscar mods, añadirlos, borrarlos e importarlos a la carpeta mods
    global canvas
    destroy_widgets()
    canvas.delete("all")
    label = Label(root, text=modpack_name, font='minecraft 15')
    label.place(anchor='center', relx=0.5, y=20)
    widgets.append(label)

def choose_modpack(): # Funcion para elegir modpacks, no tiene mucho misterio. Devuelve el nombre del modpack y este deberia poder modificarse desde la funcion created_modpack_window()
    modpack = filedialog.askdirectory(title="Select the modpack", initialdir="modpacks") 
    modpack_name = os.path.basename(modpack)
    if modpack:
        created_modpack_window(modpack_name) 
    else:
        pass

## ---------------- Window ----------------------
# Creamos la ventana
root = Tk()
root.tk.call('tk', 'scaling', 2.0)
root.geometry('1080x720')
root.resizable(0, 0)
root.title(script_name)
root.configure(bg='#000000')
# Aplicamos fondo
bg_image = Image.open("background_1080.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tkinter.Canvas(root, width=1080, height=720)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")
root.image = bg_photo
# Labels
label = Label(root, text=project_name, font='minecraft 20')
label.place(x=20, y=20)
widgets.append(label) #------------------------------------------------------- Todos los labels y botones se guardarán en la lista "widgets" para poder ser borrados despues,
#----------------------------------------------------------------------------- lo mismo ocurre en todas las funciones de menús gracias a la funcion destroy_widgets()
label = Label(root, text='by lostdou', font='minecraft 7', cursor="hand2")
label.pack()
label.bind("<Button-1>", lambda e: callback("https://github.com/Lostdou"))
label.place(x=20, y=80)
widgets.append(label)
label = Label(root, text=script_ver, font='minecraft 10')
label.place(x=1000, y=670)
widgets.append(label)
# Botones
btn_new_window = tkinter.Button(root, text="Modpacks", font='minecraft 10', command=open_modpack_window)
btn_new_window.pack()
btn_new_window.place(x=20, y=270)
widgets.append(btn_new_window)
root.mainloop()