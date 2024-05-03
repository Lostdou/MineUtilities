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

    # Labels Globales
    label = Label(root, text=project_name, font='minecraft 20', cursor="hand2")
    label.place(x=20, y=20)
    label.bind("<Button-1>", lambda: callback("https://github.com/Lostdou/MineUtilities/tree/main"))
    widgets.append(label)
    label = Label(root, text=made_by, font='minecraft 7', cursor="hand2")
    label.pack()
    label.bind("<Button-1>", lambda: callback("https://github.com/Lostdou"))
    label.place(x=20, y=80)
    widgets.append(label)
    label = Label(root, text=script_ver, font='minecraft 10')
    label.place(x=1000, y=670)
    widgets.append(label)

    # Botones Globales
    btn_home = Button(canvas, text="Main Menu", font='minecraft 10', cursor="hand2", command=home_window)
    btn_home.place(x=400, y=25)
    widgets.append(btn_home)
    btn_modpack = Button(canvas, text="Modpacks", font='minecraft 10', cursor="hand2", command=open_modpack_window)
    btn_modpack.place(x=550, y=25)
    widgets.append(btn_modpack)

def open_modpack_window(): # Es el menú de Modpacks, desde aca se deberia poder crear/modificar/borrar "perfiles" o modpacks. Ademas de volver al menu principal
    global canvas
    destroy_widgets()
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Labels Globales
    label = Label(root, text=project_name, font='minecraft 20', cursor="hand2")
    label.place(x=20, y=20)
    label.bind("<Button-1>", lambda: callback("https://github.com/Lostdou/MineUtilities/tree/main"))
    widgets.append(label)
    label = Label(root, text='by lostdou', font='minecraft 7', cursor="hand2")
    label.pack()
    label.bind("<Button-1>", lambda: callback("https://github.com/Lostdou"))
    label.place(x=20, y=80)
    widgets.append(label)
    label = Label(root, text=script_ver, font='minecraft 10')
    label.place(x=1000, y=670)
    widgets.append(label)

    #Labels Locales
    label = tkinter.Label(root, text="Modpacks", font='minecraft 15')
    label.place(x=20, y=150)
    widgets.append(label)

    # Botones Globales
    btn_home = Button(canvas, text="Main Menu", font='minecraft 10', cursor="hand2", command=home_window)
    btn_home.place(x=400, y=25)
    widgets.append(btn_home)
    btn_modpack = Button(canvas, text="Modpacks", font='minecraft 10', cursor="hand2", command=open_modpack_window)
    btn_modpack.place(x=550, y=25)
    widgets.append(btn_modpack)

    # Botones Locales
    btn_newdatapack = Button(canvas, text="Create new Modpack", font='minecraft 10', cursor="hand2", command=new_modpack_window)
    btn_newdatapack.place(x=20, y=300)
    widgets.append(btn_newdatapack)
    btn_newdatapack = Button(canvas, text="Edit an existent Modpack", font='minecraft 10', cursor="hand2", command=choose_modpack)
    btn_newdatapack.place(x=20, y=350)
    widgets.append(btn_newdatapack)
    
def new_modpack_window(): # Es un menú emergente para crear los perfiles/modpacks. Los deja en la carpeta "modpacks", y si no existe la crea
    new_window = tkinter.Toplevel(root)
    new_window.title("Create modpack")
    new_window.configure(bg='#000000')
    new_window.tk.call('tk', 'scaling', 2.0)
    new_window.resizable(0, 0)
    label = tkinter.Label(new_window, text="Create modpack", font='minecraft 15')
    label.pack(pady=20)
    directory_name = StringVar()
    label = Label(new_window, text='Name the modpack:', font='minecraft 10')
    label.pack(pady=10)
    directory_name_enter = Entry(new_window, width=20, textvariable=directory_name)
    directory_name_enter.pack(pady=8)
    
    # Cuando se presiona el botón "Enter", se crea el modpack y se cierra la ventana
    btn_newdatapack = Button(new_window, text="Enter", font='minecraft 10', cursor="hand2", 
                             command=lambda: [create_modpack(directory_name.get()), new_window.destroy()])
    btn_newdatapack.pack(pady=10)

def created_modpack_window(modpack_name, modpack_path): # Es el menu para editar un modpack, aca se podrian agregar/quitar/importar mods
    global canvas
    destroy_widgets()
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Labels Globales
    label = Label(root, text=project_name, font='minecraft 20', cursor="hand2")
    label.place(x=20, y=20)
    label.bind("<Button-1>", lambda: callback("https://github.com/Lostdou/MineUtilities/tree/main"))
    widgets.append(label)
    label = Label(root, text=made_by, font='minecraft 7', cursor="hand2")
    label.pack()
    label.bind("<Button-1>", lambda: callback("https://github.com/Lostdou"))
    label.place(x=20, y=80)
    widgets.append(label)
    label = Label(root, text=script_ver, font='minecraft 10')
    label.place(x=1000, y=670)
    widgets.append(label)

    # Labels Locales
    label = tkinter.Label(root, text=modpack_name, font='minecraft 15')
    label.place(x=20, y=150)
    widgets.append(label)
    label = tkinter.Label(root, text=modpack_path, font='minecraft 5')
    label.place(x=20, y=200)
    widgets.append(label)
    label_widget = tkinter.Label(root, text="IMPORTANT:\nThis program does NOT\n automatically download to the\n modpack directory.\nSo you can copy the path\n to the directory to paste it\n when downloading the mod(s)", height=10, width=25, font='minecraft 6')
    label_widget.place(x=800, y=220)  
    widgets.append(label_widget)

    # Botones Globales
    btn_home = Button(canvas, text="Main Menu", font='minecraft 10', cursor="hand2", command=home_window)
    btn_home.place(x=400, y=25)
    widgets.append(btn_home)
    btn_modpack = Button(canvas, text="Modpacks", font='minecraft 10', cursor="hand2", command=open_modpack_window)
    btn_modpack.place(x=550, y=25)
    widgets.append(btn_modpack)

    # Botones Locales
    btn_new_mod= Button(canvas, text="Add Mod", font='minecraft 10', cursor="hand2", command=lambda:ask_if_import_or_search(modpack_path))
    btn_new_mod.place(x=20, y=300)
    widgets.append(btn_new_mod)
    btn_delete_mod=Button(canvas, text="Delete Mod", font='minecraft 10', cursor="hand2", command=lambda:erase_mods(modpack_path))
    btn_delete_mod.place(x=20, y=350)
    widgets.append(btn_delete_mod)
    btn_export_mod= Button(canvas, text="Export Modpack to Minecraft", font='minecraft 10', cursor="hand2", command=lambda:move_files(modpack_path, "mods"))
    btn_export_mod.place(x=20, y=400)
    widgets.append(btn_export_mod)
    nombre_carpeta = os.path.basename(modpack_path)
    modpack_path_rar = os.path.join(modpack_path, f"{nombre_carpeta}.zip")
    btn_export_rar_mod= Button(canvas, text="Export Modpack as .zip", font='minecraft 10', cursor="hand2", command=lambda:create_zip_file(modpack_path, modpack_path_rar))
    btn_export_rar_mod.place(x=20, y=450)
    widgets.append(btn_export_rar_mod)
    btn_copy_dir= Button(canvas, text="Copy directory path", font='minecraft 5', cursor="hand2", command=lambda:copy_to_clipboard(modpack_path))
    btn_copy_dir.place(x=840,y=400)
    widgets.append(btn_copy_dir)

def choose_modpack(): # Funcion para elegir modpacks, no tiene mucho misterio. Devuelve el nombre del modpack y este deberia poder modificarse desde la funcion created_modpack_window()
    modpack = filedialog.askdirectory(title="Select the modpack", initialdir="modpacks") 
    modpack_path = modpack
    modpack_name = os.path.basename(modpack)
    if modpack:
        created_modpack_window(modpack_name, modpack_path) 
    else:
        pass

def ask_if_import_or_search(modpack_path):
    # Pregunta al usuario si quiere importar mods o buscarlos en CurseForge
    import_or_search = messagebox.askquestion("Import or search for mods", "Do you want to import mods from a local folder (Yes) or search for them in CurseForge? (No)", icon='warning')

    if import_or_search == 'yes':
        files = filedialog.askopenfilenames(title="Select mods to move", multiple=True)
        destination_folder = modpack_path
        for file in files:
            if file:
                shutil.move(file, destination_folder)
    else:
        callback("https://www.curseforge.com/minecraft/search?page=1&pageSize=20&sortBy=relevancy&class=mc-mods")


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
# Labels Globales
label = Label(root, text=project_name, font='minecraft 20', cursor="hand2")
label.place(x=20, y=20)
label.bind("<Button-1>", lambda: callback("https://github.com/Lostdou/MineUtilities/tree/main"))
widgets.append(label) #------------------------------------------------------- Todos los labels y botones se guardarán en la lista "widgets" para poder ser borrados despues,
#----------------------------------------------------------------------------- lo mismo ocurre en todas las funciones de menús gracias a la funcion destroy_widgets()
label = Label(root, text='by lostdou', font='minecraft 7', cursor="hand2")
label.pack()
label.bind("<Button-1>", lambda: callback("https://github.com/Lostdou"))
label.place(x=20, y=80)
widgets.append(label)
label = Label(root, text=script_ver, font='minecraft 10')
label.place(x=1000, y=670)
widgets.append(label)
# Botones Globales
btn_home = Button(canvas, text="Main Menu", font='minecraft 10', cursor="hand2", command=home_window)
btn_home.place(x=400, y=25)
widgets.append(btn_home)
btn_modpack = Button(canvas, text="Modpacks", font='minecraft 10', cursor="hand2", command=open_modpack_window)
btn_modpack.place(x=550, y=25)
widgets.append(btn_modpack)

root.mainloop()

'''
----------------------- Notas de Desarrollo ---------------------
#03/05/24 
- Cambios:
    - Cambio en la GUI, ahora todas las pestañas del programa tienen Labels y Botones globales.
    Estos son Botones o texto que son parte imborrable de la GUI y son accesibles en todo momento.
    - Ahora la pestaña para modificar un modpack (created_modpack_window()) ya permite la instalación de mods de forma
    local y mediante CurseForge.
    - GUI del editor de modpacks terminada
    - 3 funciones nuevas y una modificada. Más info en functions.py

'''