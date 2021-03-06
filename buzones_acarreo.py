from tkinter import *
from tkinter import messagebox
import sqlite3

# FUNCIONES

def licencia():
    messagebox.showinfo("Licencia","Propiedad de Luchini.")

def conexionBBDD():
    mi_conexion=sqlite3.connect("Buzones Acarreo")
    mi_cursor=mi_conexion.cursor()

    try:
        mi_cursor.execute('''
            CREATE TABLE DATOS_BUZONES (
            BUZON VARCHAR(10) PRIMARY KEY,
            MODELO_PLC VARCHAR(25),
            CONVERSOR_DATOS VARCHAR(30),
            CONVERSOR_VIDEO VARCHAR(30),
            FUENTE_24 VARCHAR(30),
            FUENTE_12 VARCHAR(30),
            LUZ_INTERIOR VARCHAR(30),
            CAMARA_SUPERIOR VARCHAR(30),
            FOCO_SUPERIOR VARCHAR(30),
            CAMARA_INFERIOR VARCHAR(30),
            FOCO_INFERIOR VARCHAR(30),
            FABRICANTE VARCHAR(30)
            )''')

        messagebox.showinfo("BBDD","BBDD creada con exito.")
    except:
        messagebox.showwarning("Atención","La BBDD ya existe.")

def salir_aplicacion():
    valor=messagebox.askquestion("Salir","Desea salir de la aplicación.")

    if valor == "yes":
        root.destroy()

def limpiar_campos():

    buzon.set("")
    PLC.set("")
    conversor_datos.set("")
    conversores_video.set("")
    fuente_24.set("")
    fuente_12.set("")
    luz_interior.set("")
    camara_sup.set("")
    foco_sup.set("")
    camara_inf.set("")
    foco_inf.set("")
    fabricante.set("")

def crear():
    mi_conexion=sqlite3.connect("Buzones Acarreo")
    mi_cursor=mi_conexion.cursor()

    datos=buzon.get(),PLC.get(),conversor_datos.get(),
    conversores_video.get(),fuente_24.get(),
    fuente_12.get(),luz_interior.get(),camara_sup.get(),
    foco_sup.get(),camara_inf.get(),foco_inf.get(),
    fabricante.get()

    mi_cursor.execute("INSERT INTO DATOS_BUZONES VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(datos))

    mi_conexion.commit()

    messagebox.showinfo("BBDD","Registro insertado con exito.")


def leer():
    mi_conexion=sqlite3.connect("Buzones Acarreo")
    mi_cursor=mi_conexion.cursor()
    mi_cursor.execute("SELECT * FROM DATOS_BUZONES WHERE  BUZON="+buzon.get())

    el_buzon=mi_cursor.fetchall()

    for bzn in el_buzon:
            buzon.set(bzn[0])
            PLC.set(bzn[1])
            conversor_datos.set(bzn[2])
            conversores_video.set(bzn[3])
            fuente_24.set(bzn[4])
            fuente_12.set(bzn[5])
            luz_interior.set(bzn[6])
            camara_sup.set(bzn[7])
            foco_sup.set(bzn[8])
            camara_inf.set(bzn[9])
            foco_inf.set(bzn[10])
            fabricante.set(bzn[11])

    mi_conexion.commit()


def actualizar():
    mi_conexion=sqlite3.connect("Buzones Acarreo")
    mi_cursor=mi_conexion.cursor()

    datos=buzon.get(),PLC.get(),conversor_datos.get(),
    conversores_video.get(),fuente_24.get(),
    fuente_12.get(),luz_interior.get(),camara_sup.get(),
    foco_sup.get(),camara_inf.get(),foco_inf.get(),
    fabricante.get()

    mi_cursor.execute("""UPDATE DATOS_BUZONES SET MODELO_PLC=?,CONVERSOR_DATOS=?,
                      CONVERSOR_VIDEO=?,FUENTE_24=?,FUENTE_12=?,
                      LUZ_INTERIOR=?,CAMARA_SUPERIOR=?,FOCO_SUPERIOR=?,
                      CAMARA_INFERIOR=?,FOCO_INFERIOR=?,FABRICANTE=?"""+
                      "WHERE BUZON="+buzon.get(),(datos))

    mi_conexion.commit()

    messagebox.showinfo("BBDD", "Registro actualizado con exito.")


root=Tk()

root.title("Buzones Acarreo")

barra_menu=Menu(root)
root.config(menu=barra_menu, width=300, height=300)

bbdd_menu=Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar", command=conexionBBDD)
bbdd_menu.add_command(label="Salir", command=salir_aplicacion)

borrar_menu=Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Borrar Campos", command=limpiar_campos)

crud_menu=Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Crear", command=crear)
crud_menu.add_command(label="Leer")
crud_menu.add_command(label="Actualizar")
crud_menu.add_command(label="Borrar")

ayuda_menu=Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Imprimir")
ayuda_menu.add_command(label="Licencia", command=licencia)

barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
barra_menu.add_cascade(label="Borrar", menu=borrar_menu)
barra_menu.add_cascade(label="CRUD", menu=crud_menu)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

# ACA COMIENZA LOS CAMPOS DE LA VENTANA

mi_frame = Frame(root)
mi_frame.pack()

buzon=StringVar()
PLC=StringVar()
conversor_datos=StringVar()
conversores_video=StringVar()
fuente_24=StringVar()
fuente_12=StringVar()
luz_interior=StringVar()
camara_sup=StringVar()
foco_sup=StringVar()
camara_inf=StringVar()
foco_inf=StringVar()
fabricante=StringVar()

cuadro_buzon=Entry(mi_frame, textvariable=buzon)
cuadro_buzon.grid(row=0, column=1, padx=10, pady=10)

cuadro_plc=Entry(mi_frame, textvariable=PLC)
cuadro_plc.grid(row=1, column=1, padx=10, pady=10)

cuadro_datos=Entry(mi_frame, textvariable=conversor_datos)
cuadro_datos.grid(row=2, column=1, padx=10, pady=10)

cuadro_video=Entry(mi_frame, textvariable=conversores_video)
cuadro_video.grid(row=3, column=1, padx=10, pady=10)

cuadro_F24=Entry(mi_frame, textvariable=fuente_24)
cuadro_F24.grid(row=4, column=1, padx=10, pady=10)

cuadro_F12=Entry(mi_frame, textvariable=fuente_12)
cuadro_F12.grid(row=5, column=1, padx=10, pady=10)

cuadro_luz=Entry(mi_frame, textvariable=luz_interior)
cuadro_luz.grid(row=0, column=3, padx=10, pady=10)

cuadro_Csup=Entry(mi_frame, textvariable=camara_sup)
cuadro_Csup.grid(row=1, column=3, padx=10, pady=10)

cuadro_focoS=Entry(mi_frame, textvariable=foco_sup)
cuadro_focoS.grid(row=2, column=3, padx=10, pady=10)

cuadro_Cinf=Entry(mi_frame, textvariable=camara_inf)
cuadro_Cinf.grid(row=3, column=3, padx=10, pady=10)

cuadro_focoI=Entry(mi_frame, textvariable=foco_inf)
cuadro_focoI.grid(row=4, column=3, padx=10, pady=10)

cuadro_fabricante=Entry(mi_frame, textvariable=fabricante)
cuadro_fabricante.grid(row=5, column=3, padx=10, pady=10)

# ACA COMIENZAN LOS Label

buzon_lbl=Label(mi_frame,text="N° Buzon")
buzon_lbl.grid(row=0, column=0, sticky="e", padx=10, pady=10)

plc_lbl=Label(mi_frame, text="Modelo PLC")
plc_lbl.grid(row=1, column=0, sticky="e", padx=10, pady=10)

datos_lbl=Label(mi_frame, text="Conversor Datos")
datos_lbl.grid(row=2, column=0, sticky="e", padx=10, pady=10)

video_lbl=Label(mi_frame, text="Conversor Video")
video_lbl.grid(row=3, column=0, sticky="e", padx=10, pady=10)

fuente24_lbl=Label(mi_frame, text="Fuente 24v")
fuente24_lbl.grid(row=4, column=0, sticky="e", padx=10, pady=10)

fuente12_lbl=Label(mi_frame, text="Fuente 12v")
fuente12_lbl.grid(row=5, column=0, sticky="e", padx=10, pady=10)

luz_lbl=Label(mi_frame, text="Luz Interior")
luz_lbl.grid(row=0, column=2, sticky="e", padx=10, pady=10)

camaraS_lbl=Label(mi_frame, text="Camara Superior")
camaraS_lbl.grid(row=1, column=2, sticky="e", padx=10, pady=10)

focoS_lbl=Label(mi_frame, text="Foco Superior")
focoS_lbl.grid(row=2, column=2, sticky="e", padx=10, pady=10)

camaraI_lbl=Label(mi_frame, text="Camara Inferior")
camaraI_lbl.grid(row=3, column=2, sticky="e", padx=10, pady=10)

focoI_lbl=Label(mi_frame, text="Foco Inferior")
focoI_lbl.grid(row=4, column=2, sticky="e", padx=10, pady=10)

fabricante_lbl=Label(mi_frame, text="Fabricante/Etapa")
fabricante_lbl.grid(row=5, column=2, sticky="e", padx=10, pady=10)

# ACA CON LOS BOTONES

mi_frame2 = Frame(root)
mi_frame2.pack()

comentario_lbl=Label(mi_frame2, text="Comentarios")
comentario_lbl.grid(row=0, column=0, sticky="e", padx=10, pady=10)

texto_comentario=Text(mi_frame2, width=25, height=5)
texto_comentario.grid(row=0, column=1, padx=10, pady=10)
scroll_vert=Scrollbar(mi_frame2, command=texto_comentario.yview)
scroll_vert.grid(row=0, column=4, sticky="nsew")

texto_comentario.config(yscrollcommand=scroll_vert.set)

mi_frame3 = Frame(root)
mi_frame3.pack()

btn_anadir=Button(mi_frame3, text="Añadir")
btn_anadir.grid(row=0, column=0, sticky="e", padx=10, pady=10)

btn_modificar=Button(mi_frame3, text="Modificar")
btn_modificar.grid(row=0, column=1, sticky="e", padx=10, pady=10)

btn_ver=Button(mi_frame3, text="Ver")
btn_ver.grid(row=0, column=2, sticky="e", padx=10, pady=10)

btn_borrar=Button(mi_frame3, text="Borrar Campos")
btn_borrar.grid(row=0, column=3, sticky="e", padx=10, pady=10)

root.mainloop()
