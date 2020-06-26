from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

import os
import shutil

def get_categories():
    lista=[]
    md=os.listdir('category')
    for file in md:
        temp=file.replace('.md','')
        lista.append(temp)
        
    return lista;

def UploadImage(event=None):
    global filename
    filename = filedialog.askopenfilename()
    global imagen
    imagen.set(os.path.split(filename)[1])
    
def addProduct():
    global imagen
    global filename
    if nombre.get() != "" and combo.get() != "" and imagen.get() != 'Ninguna imagen seleccionada' and descripcion.get('1.0', END) != "" and precio.get() != "":
        plantilla=("---\n"
        "name: "+nombre.get()+"\n"
        "categories: "+combo.get()+"\n"
        "description_markdown: >-\n"
        "  "+descripcion.get('1.0', END)+"\n"
        "price: \'"+precio.get()+"\'\n"
        "styles:\n"
        "  - name: Color\n"
        "    color: \'#dfd3c2\'\n"
        "    image: /images/products/"+imagen.get()+"\n"
        "---")
        n_archivo=nombre.get()
        n_archivo=n_archivo.replace(" ","_")
        n_archivo=n_archivo.lower()+".md"
        f_end= open("_products/"+n_archivo,"w+")
        f_end.write(plantilla)
        f_end.close()
        shutil.copy2(filename,"images/products/"+imagen.get())
        print(plantilla)
        print(n_archivo)
        messagebox.showinfo(message="Producto realizado con éxito", title="Producto")
        # reset de campos
        nombre.set("")
        combo.set("")
        descripcion.delete('1.0', END)
        precio.set("")
        imagen.set("")
        filename=''
        imagen.set('Ninguna imagen seleccionada')
    else:
        messagebox.showinfo(message="ERROR: Debe llenar todos los campos", title="Producto")
    
filename=''
app=Tk()
app.title('Crear Producto')
        
app.rowconfigure(0,weight=5)
app.columnconfigure(0, weight=1)
        

#Nombre del equipo
Label(app, text='Equipo: ').grid(row=0, column=0, sticky=E)
nombre=StringVar()
Entry(app, textvariable=nombre).grid(row=0, column=1, sticky=W,pady=5, padx=5)

# Categorias        
Label(app, text='Categoría: ').grid(row=1, column=0, sticky=E)
combo=ttk.Combobox(app, state="readonly")
combo.grid(row=1, column=1, sticky=W,pady=5, padx=5)
combo["values"] = get_categories()
imagen=StringVar()
imagen.set('Ninguna imagen seleccionada')
Button(app, text='Añadir imagen', command=UploadImage).grid(row=2, column=0, sticky=E)
Label(app, textvariable=imagen).grid(row=2, column=1, sticky=W,pady=5, padx=5)


Label(app, text='Descripción: ').grid(row=3, column=0, sticky=E)
descripcion=Text(app, height=10, width=40)
descripcion.grid(row=3,column=1, sticky=W, pady=5, padx=5)

Label(app, text='Precio: ').grid(row=4, column=0, sticky=E)
precio=StringVar()
Entry(app, textvariable=precio).grid(row=4, column=1, sticky=W,pady=5, padx=5)

Button(app, text='Añadir', command=addProduct).grid(row=5, column=0,pady=5)
Button(app, text='Salir', command=quit).grid(row=5, column=1,pady=5)

app.mainloop()
    
    
