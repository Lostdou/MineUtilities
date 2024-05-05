import os
import shutil
import tkinter
import zipfile
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
from script_info import *




## --------------- Functions -------------------
def copy_to_clipboard(text): # Funcion para copiar texto en el portapapeles
    root = Tk()
    root.withdraw()  # Para evitar que aparezca la ventana de Tk
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()  # Ahora el texto está en el portapapeles

def create_modpack(directory_name): # Funcion para crear los modpacks, y en caso de que no exista tambien crea el directorio "Modpacks"
    modpacks_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'modpacks')
    if not os.path.exists(modpacks_dir):
        os.makedirs(modpacks_dir)
    new_modpack_dir = os.path.join(modpacks_dir, directory_name)
    if not os.path.exists(new_modpack_dir):
        os.makedirs(new_modpack_dir)

def callback(url):  # Funcion para abrir enlaces, por ahora se usa para el "by Lostdou". Podrias usarlo para la busqueda de mods igualmente
    webbrowser.open_new_tab(url)

def move_files(modpack_path, default_destination_folder): # Funcion para mover los archivos al .minecraft, puede que haya que hacerle otro rework a la hora de mover resourcepacks
    # Obtener la lista de todos los mods en la carpeta del modpack
    files = [f for f in os.listdir(modpack_path) if os.path.isfile(os.path.join(modpack_path, f))]
    destination_folder = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", ".minecraft", default_destination_folder)
    # Borrar todos los archivos en la carpeta de destino
    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)
    # Crear la carpeta de destino si es necesario
    os.makedirs(destination_folder, exist_ok=True)
    for file in files:
        shutil.copy(os.path.join(modpack_path, file), destination_folder)

def erase_mods(modpack_path): # Funcion para seleccionar y borrar los mods del modpack
    file_paths = filedialog.askopenfilenames(initialdir=modpack_path, title="Selecciona los mods para eliminar")

    # Eliminar los archivos seleccionados
    for file_path in file_paths:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Archivo {file_path} eliminado con éxito.")
        else:
            print(f"El archivo {file_path} no existe.")

def create_zip_file(input_folder, output_file): # Funcion para crear el .zip de los mods
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path == output_file:
                    continue  # No agregamos el archivo zip de salida
                zipf.write(file_path, 
                           os.path.relpath(file_path, 
                           os.path.join(input_folder, '..')))

def ask_if_import_or_search(modpack_path): # Pregunta al usuario si quiere importar mods o buscarlos en CurseForge
    import_or_search = messagebox.askquestion("Import or search for mods", "Do you want to import mods from a local folder (Yes) or search for them in CurseForge? (No)", icon='warning')

    if import_or_search == 'yes':
        files = filedialog.askopenfilenames(title="Select mods to move", multiple=True)
        destination_folder = modpack_path
        for file in files:
            if file:
                shutil.move(file, destination_folder)
    else:
        callback("https://www.curseforge.com/minecraft/search?page=1&pageSize=20&sortBy=relevancy&class=mc-mods")

def delete_modpack(): # Borra el modpack elegido por el usuario
    modpack = filedialog.askdirectory(title="Select the modpack to erase", initialdir="modpacks")
    modpack_name = os.path.basename(modpack)
    if modpack:
        verification = messagebox.askquestion("Warning", f"Are you sure you want to delete the {modpack_name} modpack?", icon='warning')
        if verification == 'yes':
            shutil.rmtree(modpack)
        else:
            pass
    else:
        pass


'''
----------------------- Notas de Desarrollo ---------------------
#03/05/24 
- Cambios:
    - Nuevas funciones: 
                        copy_to_clipboard()
                        erase_mods()
                        create_zip_file()

    - Funciones modificadas: 
                        move_files()


    Lo que hacen y sus cambios ya ha sido comentado

#05/05/24
- Cambios:
    - Nuevas funciones:
                        delete_modpack()
    - Funciones movidas del main.py a functions.py:
                        ask_if_import_or_search()
    

'''