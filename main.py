import os
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from functions import *
from script_info import *

widgets = []

## ------------------------------ Functions ---------------------------

def destroy_widgets(): # Limpia los Labels y Botones de la ventana anterior
    for widget in widgets:
        widget.destroy()
    widgets.clear()

def global_labels_buttons(): # Todos los labels y botones que siempre aparecen en la interfaz
    # Labels Globales
    label = Label(root, text=project_name, font='minecraft 20', cursor="hand2")
    label.place(x=20, y=20)
    label.bind("<Button-1>", lambda event: callback("https://github.com/Lostdou/MineUtilities/tree/main"))
    widgets.append(label)
    label = Label(root, text=made_by, font='minecraft 7', cursor="hand2")
    label.pack()
    label.bind("<Button-1>", lambda event: callback("https://github.com/Lostdou"))
    label.place(x=20, y=80)
    widgets.append(label)
    label = Label(root, text=script_ver, font='minecraft 10')
    label.place(x=1000, y=670)
    widgets.append(label)

    # Botones Globales
    btn_home = Button(canvas, text="Main Menu", font='minecraft 10', cursor="hand2", command=mainmenu_window)
    btn_home.place(x=400, y=25)
    widgets.append(btn_home)
    btn_modpack = Button(canvas, text="Modpacks", font='minecraft 10', cursor="hand2", command=open_modpack_window)
    btn_modpack.place(x=545, y=25)
    widgets.append(btn_modpack)
    btn_resource_pack = Button(canvas, text="Resource Packs", font='minecraft 10', cursor="hand2", command=open_rp_window)
    btn_resource_pack.place(x=693, y=25)
    widgets.append(btn_resource_pack)
    btn_about_me = Button(canvas, text="About me", font='minecraft 10', cursor="hand2", command=aboutme_window)
    btn_about_me.place(x=920, y=25)
    widgets.append(btn_about_me)

# ------------------------------- MainMenu ---------------------------

def mainmenu_window(): # Es el menú principal hecho funcion, no se puede volver al original asi que esta es la alternativa 
    global canvas
    destroy_widgets()
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    global_labels_buttons()

    # Labels Locales
    label = Label(root, text="Main menu", font='minecraft 15')
    label.place(x=20, y=150)
    widgets.append(label)
    # ---- Descripcion ----
    label_widget = Label(root, text="", height=8, width=110, font='minecraft 6', background="#000000")
    label_widget.place(x=40, y=210)  
    widgets.append(label_widget)
    label = Label(root, text="MineUtilities v1.2", font='minecraft 8')
    label.place(x=50, y=220)  
    widgets.append(label)
    label = Label(root, text="-Now you can move your mods, modpacks and resource packs to be managed by the program", font='minecraft 8')
    label.place(x=50, y=250)  
    widgets.append(label)
    label = Label(root, text="-GUI improved", font='minecraft 8')
    label.place(x=50, y=280)  
    widgets.append(label)
    label = Label(root, text="-Now you can search directly from CurseForge your mods and resourcepacks", font='minecraft 8')
    label.place(x=50, y=310)  
    widgets.append(label)
    label = Label(root, text="To report any bug/error, please contact me", font='minecraft 8')
    label.place(x=50, y=370)  
    widgets.append(label)
    label = Label(root, text="More info on 'About Me'", font='minecraft 8')
    label.place(x=50, y=400)  
    widgets.append(label)

# ------------------------------- Modpacks ---------------------------

def open_modpack_window(): # Es el menú de Modpacks, desde aca se deberia poder crear/modificar/borrar "perfiles" o modpacks. Ademas de volver al menu principal
    global canvas
    destroy_widgets()
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    global_labels_buttons()

    #Labels Locales
    label = Label(root, text="Modpacks", font='minecraft 15')
    label.place(x=20, y=150)
    widgets.append(label)

    # Botones Locales
    btn_newdatapack = Button(canvas, text="Create new Modpack", font='minecraft 10', cursor="hand2", command=new_modpack_window)
    btn_newdatapack.place(x=20, y=300)
    widgets.append(btn_newdatapack)
    btn_editmodpack = Button(canvas, text="Edit an existent Modpack", font='minecraft 10', cursor="hand2", command=choose_modpack)
    btn_editmodpack.place(x=20, y=350)
    widgets.append(btn_editmodpack) 
    btn_deletemodpack=Button(canvas, text="Delete Modpack", font='minecraft 10', cursor="hand2", command=delete_modpack)
    btn_deletemodpack.place(x=20, y=400)
    widgets.append(btn_deletemodpack)

def choose_modpack(): # Funcion para elegir modpacks, no tiene mucho misterio. Devuelve el nombre del modpack y este deberia poder modificarse desde la funcion created_modpack_window()
    modpack = filedialog.askdirectory(title="Select the modpack", initialdir="modpacks") 
    modpack_path = modpack
    modpack_name = os.path.basename(modpack)
    if modpack:
        created_modpack_window(modpack_name, modpack_path) 
    else:
        pass

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
    global_labels_buttons()

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

    # Botones Locales
    btn_new_mod= Button(canvas, text="Add Mod", font='minecraft 10', cursor="hand2", command=lambda:add_mods(modpack_path))
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

# ---------------------------- ResourcePacks ------------------------

def open_rp_window(): # Es el menu de resource packs, aqui deberia poder agregar/mover/buscar/borrar los resource packs
    global canvas
    destroy_widgets()
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    global_labels_buttons()

    # Labels locales
    label = Label(root, text="Resource packs", font='minecraft 15')
    label.place(x=20, y=150)
    widgets.append(label)

    # Botones Locales
    btn_add_rp= Button(canvas, text="Add Resource Pack", font='minecraft 10', cursor="hand2", command=add_resource_pack)
    btn_add_rp.place(x=20, y=300)
    widgets.append(btn_add_rp)
    btn_exportrp_mc= Button(canvas, text="Export Resource Pack to Minecraft", font='minecraft 10', cursor="hand2", command=choose_rp)
    btn_exportrp_mc.place(x=20,y=350)
    widgets.append(btn_exportrp_mc)
    btn_deleterp= Button(canvas, text="Delete Resource Pack", font='minecraft 10', cursor="hand2", command=delete_rp)
    btn_deleterp.place(x=20, y=400)
    widgets.append(btn_deleterp)

#------------------------------ About Me ----------------------------

def aboutme_window():
    global canvas
    destroy_widgets()
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    global_labels_buttons()

    # Labels locales
    label_widget = Label(root, text="", height=4, width=90, font='minecraft 6')
    label_widget.place(x=50, y=220)  
    widgets.append(label_widget)
    label = Label(root, text="About MineUtilities", font='minecraft 15')
    label.place(x=20, y=150)
    widgets.append(label)
    # ---- Descripcion ----
    label = Label(root, text="MineUtilities is an open source program for managing files related to Minecraft.\n", font='minecraft 8')
    label.place(x=50, y=220)  
    widgets.append(label)
    label = Label(root, text="-From create/modify/delete modpacks and resourcepacks. \n             -As well as easily import them to the .minecraft folder. Easy as that", font='minecraft 8')
    label.place(x=50, y=245)  
    widgets.append(label)
    # ---- Creditos ----
    label = tkinter.Label(root, text="Developed by: Lostdou", font='minecraft 8')
    label.place(x=50, y=300)  
    widgets.append(label)
    label = tkinter.Label(root, text="Socials:", font='minecraft 8')
    label.place(x=50, y=340)  
    widgets.append(label)
    label = tkinter.Label(root, text="GitHub: Lostdou", font='minecraft 8', cursor="hand2")
    label.pack()
    label.bind("<Button-1>", lambda event: callback("https://github.com/Lostdou"))
    label.place(x=50, y=370)  
    widgets.append(label)
    label = tkinter.Label(root, text="Twitter/X: @nosoylostdou", font='minecraft 8', cursor="hand2")
    label.pack()
    label.bind("<Button-1>", lambda event: callback("https://twitter.com/nosoylostdou"))
    label.place(x=50, y=400)  
    widgets.append(label)
    label = tkinter.Label(root, text="Twitch: lostdou", font='minecraft 8', cursor="hand2")
    label.pack()
    label.bind("<Button-1>", lambda event: callback("https://www.twitch.tv/lostdou"))
    label.place(x=50, y=430)  
    widgets.append(label)

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
## ----------------------------------------------
mainmenu_window()

root.mainloop()

