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




## ------------------------------ Functions ---------------------------

def copy_to_clipboard(text): # Funcion para copiar texto en el portapapeles
    root = Tk()
    root.withdraw()  # Para evitar que aparezca la ventana de Tk
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()  # Ahora el texto está en el portapapeles

def callback(url):  # Funcion para abrir enlaces
    webbrowser.open_new_tab(url)

def move_files(source_path, default_destination_folder): # Funcion para mover archivos, sirve tanto para modpacks como para resourcepacks
    destination_folder = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", ".minecraft", default_destination_folder)
    
    # Crear la carpeta de destino si es necesario
    os.makedirs(destination_folder, exist_ok=True)
    
    if default_destination_folder == "mods":
        # Obtener la lista de todos los mods en la carpeta del modpack
        files = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))]
        
        # Borrar todos los archivos en la carpeta de destino
        if os.path.exists(destination_folder):
            shutil.rmtree(destination_folder)
            os.makedirs(destination_folder, exist_ok=True)
        
        # Copiar todos los archivos en la carpeta de destino
        for file in files:
            shutil.copy(os.path.join(source_path, file), destination_folder)
    elif default_destination_folder == "resourcepacks":
        # Para resourcepacks, source_path es la ruta del archivo
        shutil.copy(source_path, destination_folder)

# ------------------------------- Modpacks ---------------------------

def create_modpack(directory_name): # Funcion para crear los modpacks, y en caso de que no exista tambien crea el directorio "Modpacks"
    modpacks_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'modpacks')
    if not os.path.exists(modpacks_dir):
        os.makedirs(modpacks_dir)
    new_modpack_dir = os.path.join(modpacks_dir, directory_name)
    if not os.path.exists(new_modpack_dir):
        os.makedirs(new_modpack_dir)


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

def add_mods(modpack_path): # Pregunta al usuario si quiere importar mods o buscarlos en CurseForge
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

# ---------------------------- ResourcePacks ------------------------

def add_resource_pack(): # Funcion para agregar Resource Packs, pregunta si quiere moverlo o descargarlo y crea la carpeta en caso de que no exista
    resourcepacks_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resourcepacks')
    destination_folder = resourcepacks_path
    os.makedirs(destination_folder, exist_ok=True)
    import_or_search = messagebox.askquestion("Import or search for mods", "Do you want to import Resource Packs from a local folder (Yes) or search for them in CurseForge? (No)", icon='warning')
    if import_or_search == 'yes':
        files = filedialog.askopenfilenames(title="Select Resource Packs to move", multiple=True)
        for file in files:
            if file:
                shutil.move(file, destination_folder)
    else:
        callback("https://www.curseforge.com/minecraft/search?page=1&pageSize=20&sortBy=relevancy&class=texture-packs.")

def choose_rp():
    rps = filedialog.askopenfiles(title="Select the resource pack/s", initialdir="resourcepaks") 
    if rps:
        for rp in rps:
            move_files(rp.name, "resourcepacks")
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
    
#10/05/24
- Cambios:
    - Nuevas funciones:
                        add_resource_pack()
                        choose_rp()
    - Funciones modificadas:
                        move_files()
                        ask_if_import_or_search() (nombre cambiado a add_mods())
    - Funciones movidas del main.py a functions.py:
                        
    Lo que hacen y sus cambios ya ha sido comentado

'''