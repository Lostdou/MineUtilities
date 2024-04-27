import os
import shutil
from tkinter import *
from tkinter import filedialog, simpledialog

def move_files(default_destination_folder):
    files = filedialog.askopenfilenames(title="Select Files to Move", multiple=True) 

    change_destination = simpledialog.askstring("Input", "Do you want to change the destination folder? (y/n)",
                                                parent=root)

    if change_destination.lower() == 'y':
        destination_folder = filedialog.askdirectory(title="Select Destination Folder")
    else:
        destination_folder = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", ".minecraft", default_destination_folder)

    os.makedirs(destination_folder, exist_ok=True)
    for file in files: 
        if file:
            shutil.copy(file, destination_folder)

'''
Implementacion agregada por matiasdante para que aprazca un texto de completado una vez finalizada la operacion :D
'''
    # Mostrar mensaje de operacion completada 
    message_label.config(text="Completed!")
    # Programar para que desaparezca despues de 5 segundos.
    root.after(5000, hide_message)

# Funcion para ocultar el mensaje
def hide_message():
    message_label.config(text="")

root = Tk()
root.tk.call('tk', 'scaling', 2.0)
root.geometry('590x500')
root.resizable(0, 0)
root.title('MineUtilities v1.0')
root.configure(bg='#000000')

Label(root, text='MineUtilities', font='arial 20', bg='#7D2181').place(x=190, y=30)

btn_mover_rp = Button(root, text="Move Resource Pack", command=lambda: move_files("resourcepacks"))
btn_mover_rp.place(x=190, y=150)

btn_mover_mod = Button(root, text="Move Mod", command=lambda: move_files("mods"))
btn_mover_mod.place(x=190, y=200)

# Etiqueta para mostrar mensajes
message_label = Label(root, text="", bg='#000000', fg='#1FD655')    # Crear etiqueta
message_label.place(x=0, y=400, width=590)                          # Posicion etiqueta

root.mainloop()
