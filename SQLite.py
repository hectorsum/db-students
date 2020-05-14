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
        win.geometry('900x400') #Size

        ################## Menu Bar ################
        self.menu_bar = tk.Menu(win)
        self.my_dropdown_menu = tk.Menu(self.menu_bar,tearoff=0)
        ### Clear option
        self.my_dropdown_menu.add_command(label="New")
        self.menu_bar.add_cascade(label='File',menu=self.my_dropdown_menu)
        self.win.configure(menu=self.menu_bar)
        ################## Labels ##################
        tk.Label(win,text="Carrera: ").grid(row=1,column=2,sticky='W',ipadx=5) #Posicionar 5 a la derecha
        tk.Label(win,text='Código: ').grid(row=1,column=0,sticky='W',ipadx=5)
        tk.Label(win,text='Nombres: ').grid(row=2,column=0,sticky='W',ipadx=5)
        tk.Label(win,text='Apellidos: ').grid(row=3,column=0,sticky='W',ipadx=5)
        tk.Label(win,text='DNI: ').grid(row=4,column=0,sticky='W',ipadx=5)
        tk.Label(win,text='Fecha.Nac: ').grid(row=5,column=0,sticky='W',ipadx=5)
        tk.Label(win,text="Facultad: ").grid(row=2,column=2,sticky='W',ipadx=5)
        tk.Label(win,text="Ciclo: ").grid(row=3,column=2,sticky='W',ipadx=5)

        ################# TextBoxes ####################
        # r = "readonly"
        # w = "writeonly"
        self.codigo = tk.Entry(win)
        self.codigo.grid(row=1,column=1,sticky="W")
        self.nombres = tk.Entry(win) #Nombres
        self.nombres.grid(row=2,column=1,sticky="W")
        self.apell = tk.Entry(win) #Apellidos
        self.apell.grid(row=3,column=1,sticky="W")
        self.dni = tk.Entry(win)
        self.dni.grid(row=4,column=1,sticky="W")
        self.cboCarrera = ttk.Combobox(win,width=17)
        self.cboCarrera['values'] = ["Select..","Ing.Sistemas","Ing.Mecatronica","Ing.Civil","Arquitectura","Periodismo"]
        self.cboCarrera.current(0)
        self.cboCarrera.grid(row=1,column=3,sticky="W") 

        tk.Entry(win).grid(row=2,column=3,sticky="W") #Facultad
        tk.Spinbox(from_=1,to=10,width=5).grid(row=3,column=3,sticky="W")

        #Today's date
        self.date = dt.datetime.today()
        self.day = self.date.day
        self.month = self.date.month
        self.year = self.date.year

        self.cal = DateEntry(win,width=17,year=self.year,month=self.month,day=self.day,background='darkblue', foreground='white', borderwidth=2)
        self.cal.grid(row=5, column=1,sticky="W")
        self.date = self.cal.get_date()
        #print(str(date).split("-"))

        ############# TABLE ##################

        ###### http://tmml.sourceforge.net/doc/tk/ttk_treeview.html ###### CHEQUEAR 

        #### "browse" permite solo seleccionar 1 fila, "extended" permite seleccionar múltiples, "none" no permite seleccionar ninguna fila
        self.tree = ttk.Treeview(win,selectmode="browse",columns=(0,1,2,3,4,5,6),displaycolumns=("#all"))
        #self.tree.grid(row=7,column=0,columnspan=35,padx=10,sticky="W")
        ###### SCROLL BAR VERTICAL######
        self.vsb = ttk.Scrollbar(win,orient="vertical",command=self.tree.yview)
        self.hsb = ttk.Scrollbar(win,orient="horizontal",command=self.tree.xview)

        self.vsb.configure(command=self.tree.yview)

        self.tree.configure(yscrollcommand=self.vsb.set,xscroll=self.hsb.set)
        
        self.tree.grid(row=7,column=0,columnspan=5,pady=10,padx=5)
        self.vsb.grid(row=7,column=5,sticky="NS",pady=10)
        self.hsb.grid(row=9,column=0,columnspan=5,sticky="EW")

        ###### SCROLL BAR VERTICAL######
        # self.vsb2 = ttk.Scrollbar(win,orient="horizontal",command=self.tree.xview)        
        # self.vsb2.configure(command=self.tree.xview)
        # self.tree.configure(yscrollcommand=self.vsb2.set)
        # self.vsb2.grid(row=7,column=0,sticky="EW")


        ######
        self.tree.heading('#0',text='Codigo',anchor=tk.W)
        self.tree.column('#0',minwidth=0,width=100,stretch=tk.NO)
        ######
        self.tree.heading('#1',text='Nombres',anchor=tk.W)
        self.tree.column('#1',minwidth=0,width=100,stretch="NO")
        ######
        self.tree.heading('#2',text='Apellidos',anchor=tk.W)
        self.tree.column('#2',minwidth=0,width=100,stretch="NO")
        ######
        self.tree.heading('#3',text='DNI',anchor=tk.W)
        self.tree.column('#3',minwidth=0,width=100,stretch="NO")
        ######
        self.tree.heading('#4',text='Fec.Nac',anchor=tk.W)
        self.tree.column('#4',minwidth=0,width=80,stretch="NO")
        ######
        self.tree.heading('#5',text='Carrera',anchor=tk.W)
        self.tree.column('#5',minwidth=0,width=100,stretch="NO")
        ######
        self.tree.heading('#6',text='Facultad',anchor=tk.W)
        self.tree.column('#6',minwidth=0,width=100,stretch="NO")
        ######
        self.tree.heading('#7',text='Ciclo',anchor=tk.W)
        self.tree.column('#7',minwidth=0,width=60,stretch="NO")
        ######

    
        
        
        
        


    # def creatingDB():
    #     try:
    #         sql = '''CREATE TABLE ESTUDIANTE(        id_est int
    #                                                 ,nombres varchar(30)
    #                                                 ,apell varchar(30)
    #                                                 ,dni varchar(8)
    #                                                 ,fech_nac date
    #                                                 ,carrera varchar(20)
    #                                                 ,facultad varchar(20)
    #                                                 ,ciclo int
    #                                                 )'''
    #         run_query(sql)
    #     except Exception as e:
    #         print(e)

    # def insertingData():
    #     name = input('Nombres: ')
    #     last_name = input('Apellidos: ')
    #     dni = input('DNI: ')
    #     #Asking for three inputs
    #     ###Strip: elimina chars que se indique por el parametro
    #     ###Split: busca chart que se indique y los separa
    #     year,month,day = map(int,input("Fecha Ingreso (yy/mm/dd): ").split("/"))
    #     birth_date = dt.date(year,month,day)
    #     career = input('Carrera: ')
    #     faculty = input('Facultad: ')
    #     term = int(input('Ciclo: '))

    #     #Another way
    #     # day,month,year = input('Date (yy/mm/dd): ').split("/") #As string
    #     # print(dt.datetime(year,month,day))
        
    #     sql = '''
    #                         INSERT INTO ESTUDIANTE(nombres,apell,dni,fech_nac,carrera,facultad,ciclo) values(?,?,?,?,?,?,?)
    #                     '''
    #     data = (name,last_name,dni,birth_date,career,faculty,term)
    #     try: 
    #         run_query(sql,data)
    #         print("Student added successfully")
    #     except Exception as e:
    #         print(e)

    def run_query(self,query,parameters=()):
        with sqlite3.connect('data.db') as myConnection:
            myCursor = myConnection.cursor()
            result = myCursor.execute(query,parameters)
            myConnection.commit()
        return result

    def listStudents(self):
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

    # def searchStudent(self,cod):
    #     sql = f"SELECT * FROM ESTUDIANTE WHERE id_est = {cod}"
    #     myCursor.execute(sql)
    #     student = myCursor.fetchall()
    #     myConnection.commit()
    #     print(student)

    # def updateStudents(self,cod,dni):
    #     sql = f"UPDATE ESTUDIANTE SET dni={dni} WHERE id_est={cod}"
    #     try:
    #         myCursor.execute(sql)
    #         myConnection.commit()
    #         print("Student was updated successfully!")
    #         listStudents()
    #     except Exception as e:
    #         print(e)

    # def deleteStudent(self,cod):
    #     sql = f"DELETE FROM ESTUDIANTE WHERE id_est={cod}"
    #     try:
    #         myCursor.execute(sql)
    #         myConnection.commit()
    #         print("Student was deleted successfully!")
    #         listStudents()
    #     except Exception as e:
    #         print(e)

    # def clearBoxes():
    #     return "Clear selected!"
    

if __name__=="__main__":
    win = tk.Tk()
    app = student(win)
    app.listStudents()
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