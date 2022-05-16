from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

# Definición de funciones
# Archivo
def nuevo_archivo():
	area_trabajo.delete(1.0,END)
def abrir_archivo():
	documento = askopenfile(filetypes=[("Archivos de texto","*.txt")]) # Typo faltante ,"*.cody"
	if documento != None:
		area_trabajo.insert(1.0, documento.read())
def guardar_archivo():
	documento = asksaveasfile(filetypes=[("Archivos de texto","*.txt")])
	print(documento.write(area_trabajo.get(1.0, END)))
# Edición
def accion_deshacer():
	area_trabajo.edit_undo()
def accion_rehacer():
	area_trabajo.edit_redo()
def accion_cortar():
	area_trabajo.clipboard_clear()
	area_trabajo.clipboard_append(area_trabajo.selection_get())
	area_trabajo.delete("sel.first", "sel.last")
def accion_copiar():
	area_trabajo.clipboard_clear()
	area_trabajo.clipboard_append(area_trabajo.selection_get())
def accion_pegar():
	area_trabajo.insert(INSERT, area_trabajo.clipboard_get())
# Acerca de 
def acerca_de():
	messagebox.showinfo("Acerca de PyNotes", "PyNotes es un programa desarrollado en Python,"
						"como practica para el desarrollo de programas con interfaz grafica "
						"basado en el codigo de Codigazo")


# Ventana Principal
if __name__ =="__main__":
	ventana = Tk()

	# Barra de menu
	menubar = Menu(ventana)
	
	# Submenu ARCHIVO
	archivo = Menu(menubar, tearoff=0)
	archivo.add_command(label="Nuevo	", command=nuevo_archivo)
	archivo.add_command(label="Abrir	", command=abrir_archivo)
	archivo.add_command(label="Guardar	", command=guardar_archivo)
	#archivo.add_command(label="Eliminar	", command=eliminar_archivo)
	archivo.add_separator()
	archivo.add_command(label="Salir	", command=ventana.quit)
	menubar.add_cascade(label="Archivo", menu=archivo)

	# Submenu EDITAR
	editar = Menu(menubar, tearoff=0)
	editar.add_command(label="Deshacer	", command=accion_deshacer)
	editar.add_command(label="Rehacer	", command=accion_rehacer)
	editar.add_separator()
	editar.add_command(label="Copiar	", command=accion_copiar)
	editar.add_command(label="Cortar 	", command=accion_cortar)
	editar.add_command(label="Pegar 	", command=accion_pegar)
	menubar.add_cascade(label="Edición", menu=editar)

	#Submenu AYUDA
	ayuda = Menu(menubar, tearoff=0)
	ayuda.add_command(label="Acerca de PyNotes Z", command=acerca_de)
	menubar.add_cascade(label="Ayuda", menu=ayuda)

	# Area de trabajo
	area_trabajo = Text(ventana, undo="true")
	area_trabajo.pack(side=TOP, fill=BOTH, expand=1)


	ventana.title("PyNotes")     		# Ventana Titulo
	ventana.geometry("640x480")  		# Ventana Tamaño
	ventana.config(menu=menubar) 		# Insertar Barra de menu
	ventana.mainloop()         			# Bucle para la función main

