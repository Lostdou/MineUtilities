import os
import shutil
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
from script_info import *



## --------------- Functions -------------------
def create_modpack(directory_name): # Funcion para crear los modpacks, y en caso de que no exista tambien crea el directorio "Modpacks"
    modpacks_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'modpacks')
    if not os.path.exists(modpacks_dir):
        os.makedirs(modpacks_dir)
    new_modpack_dir = os.path.join(modpacks_dir, directory_name)
    if not os.path.exists(new_modpack_dir):
        os.makedirs(new_modpack_dir)

def callback(url):  # Funcion para abrir enlaces, por ahora se usa para el "by Lostdou". Podrias usarlo para la busqueda de mods igualmente
    webbrowser.open_new_tab(url)

def move_files(default_destination_folder): # Funcion para mover los mods a la carpeta de destino, aunque este espera que se le indique que carpeta. 
    #---------------------------------------- Deberias usar el boton "Move mods" de la v1.1 para poder mover mods con esta funcion
    #---------------------------------------- A menos que quieras modificar la funcion claro
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

