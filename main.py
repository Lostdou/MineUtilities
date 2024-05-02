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

def new_modpack_window(): # Es un menú emergente para crear los perfiles/modpacks. Los deja en la carpeta "modpacks", y si no existe la crea
    new_window = tkinter.Toplevel(root)
    new_window.title("Create modpack")
    new_window.configure(bg='#000000')
    label = tkinter.Label(new_window, text="Create modpack", font='minecraft 15')
    label.pack(pady=20)
    directory_name = StringVar()
    label = Label(new_window, text='Name the modpack:', font='minecraft 10')
    label.pack(pady=10)
    directory_name_enter = Entry(new_window, width=32, textvariable=directory_name)
    directory_name_enter.pack(pady=10)
    
    # Cuando se presiona el botón "Enter", se crea el modpack y se cierra la ventana
    btn_newdatapack = Button(new_window, text="Enter", font='minecraft 10', cursor="hand2", 
                             command=lambda: [create_modpack(directory_name.get()), new_window.destroy()])
    btn_newdatapack.pack(pady=10)


def created_modpack_window(modpack_name):
    # Crear una nueva ventana
    new_window = tkinter.Toplevel(root)
    new_window.title(f"Modpack: {modpack_name}")
    new_window.tk.call('tk', 'scaling', 2.0)
    new_window.geometry('500x350')
    new_window.resizable(0, 0)

    new_window.configure(bg='#000000')
    label = Label(new_window, text=modpack_name, font='minecraft 15')
    label.pack(pady=20)
    # Modificar para poder agregar/borrar y demas
    # Idea: Al agregar mods, podria preguntar si lo quiere agregar de forma local o si quiere buscar en internet

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
