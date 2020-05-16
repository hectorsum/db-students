import sqlite3
import datetime as dt
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

class student:

    def __init__(self,win):        
        self.win = win
        self.win.title("Registro Estudiante")
        self.win.resizable(0,0) #Quitar el rezisable

        ################## Menu Bar ################
        self.menu_bar = tk.Menu(win)
        self.my_dropdown_menu = tk.Menu(self.menu_bar,tearoff=1)
        ### Clear option
        self.my_dropdown_menu.add_command(label="New")
        self.menu_bar.add_cascade(label='File',menu=self.my_dropdown_menu)
        self.win.configure(menu=self.menu_bar)
        ################## Labels ################## ipadx=genera espaciamiento entre el elemento X
        tk.Label(win,text="Carrera: ").grid(row=1,column=2,sticky='W',ipadx=5) 
        #tk.Label(win,text='Código: ').grid(row=1,column=0,sticky='W',ipadx=5)
        tk.Label(win,text='Nombres: ').grid(row=1,column=0,sticky='W',ipadx=5)
        tk.Label(win,text='Apellidos: ').grid(row=2,column=0,sticky='W',ipadx=5)
        tk.Label(win,text='DNI: ').grid(row=3,column=0,sticky='W',ipadx=5)
        tk.Label(win,text='Fecha.Nac: ').grid(row=4,column=0,sticky='W',ipadx=5)
        tk.Label(win,text="Facultad: ").grid(row=2,column=2,sticky='W',ipadx=5)
        tk.Label(win,text="Ciclo: ").grid(row=3,column=2,sticky='W',ipadx=5)

        ################# TextBoxes ####################
        self.read = "readonly"
        self.normal = "normal"
        #self.codigo = tk.Entry(win)
        # self.codigo.grid(row=1,column=1,sticky="W")
        self.nombre = tk.Entry(win,state=self.read) #Nombres
        self.nombre.grid(row=1,column=1,sticky="W")
        self.apell = tk.Entry(win,state=self.read) #Apellidos
        self.apell.grid(row=2,column=1,sticky="W")
        self.dni = tk.Entry(win,state=self.read)
        self.dni.grid(row=3,column=1,sticky="W")
        self.cboCarrera = ttk.Combobox(win,width=17,state="disabled",values=("Select..","Ing.Sistemas","Ing.Mecatronica","Ing.Civil","Arquitectura","Periodismo"))
        self.cboCarrera.current(0)        
        self.cboCarrera.grid(row=1,column=3,sticky="W") 
        self.cboCarrera.bind("<<ComboboxSelected>>", self.news_election)


        self.facultad = tk.Entry(win,bg="#cdcdcd",state=self.read)
        self.facultad.grid(row=2,column=3,sticky="W") #Facultad                
        

        self.ciclo = tk.Spinbox(from_=1,to=10,width=5,state=self.read)
        self.ciclo.grid(row=3,column=3,sticky="W")
        
        self.fec_nac = DateEntry(win,width=17,background='darkblue', foreground='white', borderwidth=2,date_pattern="dd/MM/yyyy",state="disabled")
        self.fec_nac.grid(row=4, column=1,sticky="W")
        #self.fec_nac.get_date()
        #print(str(date).split("-"))

        ############# TABLE ##################
        #### "browse" permite solo seleccionar 1 fila, "extended" permite seleccionar múltiples, "none" no permite seleccionar ninguna fila
        self.tree = ttk.Treeview(win,selectmode="browse",columns=(0,1,2,3,4,5,6))        
        #self.tree.grid(row=7,column=0,columnspan=35,padx=10,sticky="W")
        ###### SCROLL BAR VERTICAL && HORIZONTAL ######
        self.vsb = ttk.Scrollbar(win,orient="vertical",command=self.tree.yview)
        self.vsb.grid(row=7,column=5,sticky="NS",pady=10)
        self.hsb = ttk.Scrollbar(win,orient="horizontal",command=self.tree.xview)
        self.hsb.grid(row=9,column=0,columnspan=5,sticky="EW")
        
        self.tree.configure(yscrollcommand=self.vsb.set,xscroll=self.hsb.set)
        self.tree.grid(row=7,column=0,columnspan=5,pady=10,padx=5)

        ###### COLUMNS ######
        self.tree.heading('#0',text='Codigo',anchor="center") #Posicionar el centro el contenido
        self.tree.column('#0',minwidth=0,width=60,stretch=tk.NO,anchor="center")
        ######
        self.tree.heading('#1',text='Nombres',anchor="center")
        self.tree.column('#1',minwidth=0,width=100,stretch="NO",anchor="center")
        ######
        self.tree.heading('#2',text='Apellidos',anchor="center")
        self.tree.column('#2',minwidth=0,width=100,stretch="NO",anchor="center")
        ######
        self.tree.heading('#3',text='DNI',anchor="center")
        self.tree.column('#3',minwidth=0,width=100,stretch="NO",anchor="center")
        ######
        self.tree.heading('#4',text='Fec.Nac',anchor="center")
        self.tree.column('#4',minwidth=0,width=80,stretch="NO",anchor="center")
        ######
        self.tree.heading('#5',text='Carrera',anchor="center")
        self.tree.column('#5',minwidth=0,width=100,stretch="NO",anchor="center")
        ######
        self.tree.heading('#6',text='Facultad',anchor=tk.CENTER)
        self.tree.column('#6',minwidth=0,width=100,stretch="NO",anchor="center")
        ######
        self.tree.heading('#7',text='Ciclo',anchor="center")
        self.tree.column('#7',minwidth=0,width=60,stretch="NO",anchor="center")
        ######

        ############### BUTTONS ############### (ipadx genera alargamiento horizontal del elemento)
        ttk.Button(win,text="Nuevo",command=self.unlocking_boxes).grid(row=1,column=4,ipadx=50,sticky=tk.W+tk.E)
        ttk.Button(win,text="Grabar",command=self.insert_data).grid(row=2,column=4,sticky=tk.W+tk.E)
        ttk.Button(win,text="Editar",command=self.update_student).grid(row=3,column=4,sticky=tk.W+tk.E)
        ttk.Button(win,text="Eliminar",command=self.delete_student).grid(row=4,column=4,sticky=tk.W+tk.E)

        ############## SELECTION ################
        #if(self.cboCarrera['values']=="Ing.Sistemas"):
            #self.facultad.configure(text="Ingenieria")
    
    def news_election(self,event):
        response=str(event.widget.get())
        if response.startswith("Ing."):
            self.facultad.delete(0,tk.END)            
            self.facultad.insert(0,"Ingenieria")
        elif response.startswith("Arquitectura"):            
            self.facultad.delete(0,tk.END)
            self.facultad.insert(0,"Arquitectura")
        elif response.startswith("Periodismo"):
            self.facultad.delete(0,tk.END)
            self.facultad.insert(0,"Comunicaciones")
        #print('selected:', event.widget.get())

    def unlocking_boxes(self):                            
        # if self.cboCarrera.current()==0:
        #     self.facultad.configure(text="Seleccionado")
        return self.nombre.configure(state=self.normal), self.apell.configure(state=self.normal), self.dni.configure(state=self.normal), self.fec_nac.configure(state=self.normal), self.cboCarrera.configure(state=self.normal), self.facultad.configure(state=self.normal), self.ciclo.configure(state=self.normal),self.fec_nac.configure(state=self.normal)
        
    def locking_boxes(self):
        return self.nombre.configure(state=self.read), self.apell.configure(state=self.read), self.dni.configure(state=self.read), self.fec_nac.configure(state="disabled"), self.cboCarrera.configure(state="disabled"), self.facultad.configure(state=self.read), self.ciclo.configure(state=self.read)

    # def create_table():
    #     try:
    #         sql = '''CREATE TABLE ESTUDIANTE(        id_est int NOT NULL AUTOINCREMENT
    #                                                 ,nombres varchar(30)
    #                                                 ,apell varchar(30)
    #                                                 ,dni varchar(8)
    #                                                 ,fech_nac date
    #                                                 ,carrera varchar(20)
    #                                                 ,facultad varchar(20)
    #                                                 ,ciclo int
    #                                                 ,PRIMARY KEY(id_est))'''
    #         run_query(sql)
    #     except Exception as e:
    #         print(e)

    def clear_boxes(self):
        #self.codigo.delete(0,tk.END)
        self.nombre.delete(0,tk.END)
        self.apell.delete(0,tk.END)
        self.dni.delete(0,tk.END)
        self.cboCarrera.delete(0,tk.END)
        self.facultad.delete(0,tk.END)
        self.ciclo.delete(0,tk.END)

    def insert_data(self):        
        sql = '''
                            INSERT INTO ESTUDIANTE(nombres,apell,dni,fech_nac,carrera,facultad,ciclo) values(?,?,?,?,?,?,?)
                        '''
        data = (self.nombre.get(),self.apell.get(),self.dni.get(),self.fec_nac.get_date(),self.cboCarrera.get(),self.facultad.get(),self.ciclo.get())
        try: 
            self.run_query(sql,data)
            print("Student added successfully")
            self.clear_boxes()            
            self.list_students()
            self.locking_boxes()
        except Exception as e:
            print(e)

    def db_connect(self):
        try:
            myConnection = sqlite3.connect('data.db')
            return myConnection
        except Exception as e:
            tk.messagebox(e)

    def run_query(self,query,parameters=()):
        with sqlite3.connect('data.db') as myConnection:            
            myCursor = myConnection.cursor()
            result = myCursor.execute(query,parameters)
            myConnection.commit()
        return result

    def list_students(self):
        records = self.tree.get_children()
        #Cleaning table
        for element in records:
            self.tree.delete(element)
        #Querying data
        sql = "SELECT * FROM ESTUDIANTE"
        tb_rows = self.run_query(sql)
        # myCursor.execute(sql)
        # students = myCursor.fetchall()
        for row in tb_rows:
            self.tree.insert('',0,text=row[0],values=row[1:]) #Comienza del elem 0, luego aplica apartir del primer campo hasta el final

    # def search_student(self,cod):
    #     sql = f"SELECT * FROM ESTUDIANTE WHERE id_est = {cod}"
    #     myCursor.execute(sql)
    #     student = myCursor.fetchall()
    #     myConnection.commit()
    #     print(student)

    def update_student(self):
    
        row = self.tree.item(self.tree.selection())['text']
        old_name = self.tree.item(self.tree.selection())['values'][0]
        old_lastname = self.tree.item(self.tree.selection())['values'][1]
        old_dni = self.tree.item(self.tree.selection())['values'][2]
        old_datebirth = self.tree.item(self.tree.selection())['values'][3]
        old_career = self.tree.item(self.tree.selection())['values'][4]
        old_faculty = self.tree.item(self.tree.selection())['values'][5]
        old_term = self.tree.item(self.tree.selection())['values'][6]
        self.edit_wind = tk.Toplevel()
        self.edit_wind.title("Modifying Student")
        
        #### OLD ####
        tk.Label(self.edit_wind,text="Old Name: ").grid(row=0,column=1)
        tk.Entry(self.edit_wind,textvariable=tk.StringVar(self.edit_wind,value=old_name),state="readonly").grid(row=0,column=2)
        tk.Label(self.edit_wind,text="Old Last Name: ").grid(row=1,column=1)
        tk.Entry(self.edit_wind,textvariable=tk.StringVar(self.edit_wind,value=old_lastname),state="readonly").grid(row=1,column=2)
        tk.Label(self.edit_wind,text="Old DNI: ").grid(row=2,column=1)
        tk.Entry(self.edit_wind,textvariable=tk.StringVar(self.edit_wind,value=old_dni),state="readonly").grid(row=2,column=2)
        tk.Label(self.edit_wind,text="Old Birth Date: ").grid(row=3,column=1)
        tk.Entry(self.edit_wind,textvariable=tk.StringVar(self.edit_wind,value=old_datebirth),state="readonly").grid(row=3,column=2)
        tk.Label(self.edit_wind,text="Old Career: ").grid(row=4,column=1)
        tk.Entry(self.edit_wind,textvariable=tk.StringVar(self.edit_wind,value=old_career),state="readonly").grid(row=4,column=2)
        tk.Label(self.edit_wind,text="Old Faculty: ").grid(row=5,column=1)
        tk.Entry(self.edit_wind,textvariable=tk.StringVar(self.edit_wind,value=old_faculty),state="readonly").grid(row=5,column=2)
        tk.Label(self.edit_wind,text="Old Term: ").grid(row=6,column=1)
        tk.Entry(self.edit_wind,textvariable=tk.StringVar(self.edit_wind,value=old_term),state="readonly").grid(row=6,column=2)

        #### NEW ONE ####
        tk.Label(self.edit_wind,text="New Name: ").grid(row=0,column=3)
        new_name = tk.Entry(self.edit_wind)
        new_name.grid(row=0,column=4)
        #######
        tk.Label(self.edit_wind,text="New Last Name: ").grid(row=1,column=3)
        new_lastname = tk.Entry(self.edit_wind)
        new_lastname.grid(row=1,column=4)
        ####### 
        tk.Label(self.edit_wind,text="New DNI: ").grid(row=2,column=3)
        new_dni = tk.Entry(self.edit_wind)
        new_dni.grid(row=2,column=4)
        #######
        tk.Label(self.edit_wind,text="New Fec.Nac: ").grid(row=3,column=3)
        new_fec_nac = DateEntry(self.edit_wind,width=17,background='darkblue', foreground='white', borderwidth=2,date_pattern="dd/MM/yyyy")        
        new_fec_nac.grid(row=3, column=4)
        #######
        def news_election(self,event):
            response=str(event.widget.get())
            if response.startswith("Ing."):
                new_faculty.delete(0,tk.END)            
                new_faculty.insert(0,"Ingenieria")
            elif response.startswith("Arquitectura"):            
                new_faculty.delete(0,tk.END)
                new_faculty.insert(0,"Arquitectura")
            elif response.startswith("Periodismo"):
                new_faculty.delete(0,tk.END)
                new_faculty.insert(0,"Comunicaciones")
        #######
        tk.Label(self.edit_wind,text="New Career: ").grid(row=4,column=3)
        new_career = ttk.Combobox(self.edit_wind,width=17,values=('Ing.Sistemas','Ing.Mecatronica','Ing.Civil','Arquitectura','Periodismo'))
        new_career.current(0)
        new_career.grid(row=4,column=4)
        new_career.bind("<<ComboboxSelected>>", self.news_election)
        #######
        tk.Label(self.edit_wind,text="New Faculty: ").grid(row=5,column=3)
        new_faculty = tk.Entry(self.edit_wind,bg="#cdcdcd")
        new_faculty.grid(row=5,column=4)
        #######
        tk.Label(self.edit_wind,text="New Term: ").grid(row=6,column=3)
        new_term = tk.Spinbox(self.edit_wind,from_=1,to=10,width=5)
        new_term.grid(row=6,column=4)
                
        ####### BUTTONS #######
        tk.Button(self.edit_wind,text="Save").grid(row=7,column=0,columnspan=3,sticky=tk.E+tk.W)
        tk.Button(self.edit_wind,text="Cancel").grid(row=7,column=3,columnspan=2,sticky=tk.E+tk.W)
        # sql = f"UPDATE ESTUDIANTE SET dni={dni} WHERE id_est={cod}"
        # try:
        #     myCursor.execute(sql)
        #     myConnection.commit()
        #     print("Student was updated successfully!")
        #     listStudents()
        # except Exception as e:
        #     print(e)

    def delete_student(self):        
        try: 
            row = self.tree.item(self.tree.selection())['text']
            sql = f"DELETE FROM ESTUDIANTE WHERE id_est = ?"
            self.run_query(sql,(row, ))
            #tk.messagebox.showinfo(title=None, message="Student deleted successfully")
            self.list_students()
        except:
            tk.messagebox.showinfo(title=None, message="Error")

        

if __name__=="__main__":
    win = tk.Tk()
    app = student(win)
    app.list_students()
    # myConnection = sqlite3.connect('data.db')
    # myCursor = myConnection.cursor()
    # interface()
    win.mainloop()
    

    #creatingDB()
    #insertingData()
    #cod = int(input('Codigo: '))
    # dni = input('Nuevo DNI: ')
    #searchStudent(cod)
    #updateStudents(cod,dni)
    #listStudents()
    #deleteStudent(cod)
    #myConnection.close()