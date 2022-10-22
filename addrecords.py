from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime as datetime
from tkcalendar import *
import sqlite3
import tkinter as tk
import time
import ctypes

myappid = 'dreamboxtech.nhisrecordkeeper.mainwindow.2.02'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


window =  tk.Tk()
window.configure(bg ="#00c76a")
window.title("Record Addition")
window.geometry("13500x750+0+0")
window.iconbitmap(r'C:/Users/TOSHIBA/Desktop/tt/NHIS/logo.ico')



myMenu = Menu(window)
window.config(menu = myMenu)

fileMenu = Menu(myMenu)
myMenu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "Add Records")
fileMenu.add_command(label ="Exit", command = window.destroy)

processMenu = Menu(myMenu)
myMenu.add_cascade(label = "Process", menu = processMenu)
processMenu.add_command(label = "Sync")
processMenu.add_command(label = "Mail")


mframe = Frame(window, bg = "#00c76a")
mframe.grid()

tframe = Frame(mframe, bd =2, padx = 54, pady = 8, bg ="Ghost White", relief =RIDGE)
tframe.pack(side= TOP)

labeltitle = Label(tframe, font= ('arial', 15, 'bold'), text = 'Add Records to Database', bg ='Ghost White', fg = '#044728') 
labeltitle.grid()

butframe = Frame(mframe, bd =2, width = 1350, height =70, padx = 18, pady = 15, bg ="Ghost White", relief =RIDGE)
butframe.pack(side= BOTTOM)

dataframe = Frame(mframe, bd =1, width = 1300, height =400, padx =20, pady = 20, bg ="#00c76a", relief =RIDGE)
dataframe.pack(side= BOTTOM)

dataframeleft = LabelFrame(dataframe, bd =1, width = 500, height =300, padx = 20, pady =3, bg ="orange", relief =RIDGE, 
	font= ('tahoma', 12, 'bold'), text = 'HMO, Principal and Dependant Addition\n')
dataframeleft.grid(row= 0, column = 0, sticky = NW)
#dataframeleft.grid_propagate(1)
dataframeleft.pack_propagate(0)

dataframeright = LabelFrame(dataframe, bd =1, width = 600, height =300, padx = 31, pady = 3, bg ="Ghost White", relief =RIDGE, 
	font= ('tahoma', 12, 'bold'), text = 'Details\n')
dataframeright.grid(row=0, column =1, sticky =W)
dataframeright.grid_propagate(0)

dataframedown = LabelFrame(dataframe, bd =1, width = 600, height =600, padx = 20, bg ="Ghost White", relief =RIDGE, 
	font= ('tahoma', 12, 'bold'), fg = '#40054d', text = 'Services and Drugs\n')
dataframedown.grid(row= 1, column= 0, sticky =N, pady = 10)

dataframedr = LabelFrame(dataframe, bd =1, width = 600, height =600, padx = 20, bg ="Ghost White", relief =RIDGE, 
	font= ('tahoma', 12, 'bold'), fg = '#000000', text = 'Data Modification\n')
dataframedr.grid(row= 1, column= 1, sticky =N, pady = 10)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
HMO_ID = StringVar()
HMO_NAME = StringVar()

NHIS_NUMB =StringVar()
PRINCIPAL = StringVar()

DOB = StringVar()
GENDER = StringVar()






hmoidlabel = Label(dataframeleft, font= ('arial', 10), text = 'HMO ID:',padx =2, pady =2, bg ='orange') 
hmoidlabel.grid(row = 0, column = 0, sticky = E)
hmoidlabeltxt = Entry(dataframeleft, font= ('times new roman', 11), textvariable= HMO_ID, width =30) 
hmoidlabeltxt.grid(row = 0, column = 1, sticky = E)

hmonamelabel = Label(dataframeleft, font= ('arial', 10), text = 'HMO NAME:',padx =2, pady =2, bg ='orange') 
hmonamelabel.grid(row = 0, column = 2, sticky = E)
hmonamelabeltxt = Entry(dataframeleft, font= ('times new roman', 11), textvariable= HMO_NAME, width =30) 
hmonamelabeltxt.grid(row = 0, column = 3)



sepa = ttk.Separator(dataframeleft, orient = 'horizontal') 
sepa.grid(row = 2, column = 0, sticky="ew")
sepa = ttk.Separator(dataframeleft, orient = 'horizontal') 
sepa.grid(row = 2, column = 1, sticky="ew")
sepa = ttk.Separator(dataframeleft, orient = 'horizontal') 
sepa.grid(row = 2, column = 2, sticky="ew")
sepa = ttk.Separator(dataframeleft, orient = 'horizontal') 
sepa.grid(row = 2, column = 3, sticky="ew", pady = 8)


sepa = ttk.Separator(dataframedown, orient = 'horizontal') 
sepa.grid(row = 3, column = 0, sticky="ew")
sepa = ttk.Separator(dataframedown, orient = 'horizontal') 
sepa.grid(row = 3, column = 1, sticky="ew")
sepa = ttk.Separator(dataframedown, orient = 'horizontal') 
sepa.grid(row = 3, column = 2, sticky="ew")
sepa = ttk.Separator(dataframedown, orient = 'horizontal') 
sepa.grid(row = 3, column = 3, sticky="ew", pady = 8)



# sepa = ttk.Separator(dataframeleft, orient = 'horizontal') 
# sepa.grid(row = 5, column = 0, sticky="ew")
# sepa = ttk.Separator(dataframeleft, orient = 'horizontal') 
# sepa.grid(row = 5, column = 1, sticky="ew")
# sepa = ttk.Separator(dataframeleft, orient = 'horizontal') 
# sepa.grid(row = 5, column = 2, sticky="ew")
# sepa = ttk.Separator(dataframeleft, orient = 'horizontal') 
# sepa.grid(row = 5, column = 3, sticky="ew", pady = 8)
def delaster():
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	cur.execute("SELECT REPLACE(NHIS_NUMBER, '*', '') FROM principal")
	con.commit()
	con.close()


def loaddata():
	global nhislist
	global nhislabeltxt

	coll = cur.fetchall()
	for sub in coll:
		for item in sub:
			nhislist.append(item)
	
	cur.execute("SELECT S_NHIS_NUMB FROM spouse")
	coll2 = cur.fetchall()
	for sub in coll2:
		for item in sub:
			nhislist.append(item)
	nhislabeltxt = ttk.Combobox(dataframeleft, font= ('times new roman', 11), textvariable= NHIS_NUMB, width =13, value =nhislist) 
	nhislabeltxt.grid(row = 3, column = 1)

nhislist = []
con = sqlite3.connect('patient.db')
cur = con.cursor()
cur.execute("SELECT NHIS_NUMBER FROM principal")
coll = cur.fetchall()
for sub in coll:
	for item in sub:
		nhislist.append(item)
cur.execute("SELECT S_NHIS_NUMB FROM spouse")
coll2 = cur.fetchall()
for sub in coll2:
	for item in sub:
		nhislist.append(item)
con.close()


refreshbut = ttk.Button(dataframeleft, text= 'Load/Refresh Data', command = loaddata) 
refreshbut.grid(row = 9, column = 0, sticky = E, padx = 5)
im = PhotoImage(file ='C:/Users/TOSHIBA/Desktop/tt/NHIS/up2.png')
refreshbut.config(image =im, compound = RIGHT)


nhislabel = Label(dataframeleft, font= ('arial', 10), text = 'NHIS NUMBER:',padx =2, pady =2, bg ='orange') #ffc24f
nhislabel.grid(row = 3, column = 0, sticky = W)
nhislabeltxt = ttk.Combobox(dataframeleft, font= ('times new roman', 11), textvariable= NHIS_NUMB, width =13, value =nhislist) 
nhislabeltxt.grid(row = 3, column = 1)

princlabel = Label(dataframeleft, font= ('arial', 10), text = 'PATIENT NAME:',padx =2, pady =2, bg ='orange') 
princlabel.grid(row = 3, column = 2, sticky = W)
princlabeltxt = Entry(dataframeleft, font= ('times new roman', 11), textvariable= PRINCIPAL, width =30) 
princlabeltxt.grid(row = 3, column = 3)



doblabel = Label(dataframeleft, font= ('arial', 10), text = 'DATE OF BIRTH:',padx =2, pady = 2, bg ='orange') #ffc24f
doblabel.grid(row = 5, column = 0, sticky = W)
doblabeltxt = DateEntry(dataframeleft, font= ('times new roman', 11), textvariable = DOB, width =13, date_pattern='mm/dd/y') 
doblabeltxt.grid(row = 5, column = 1, pady =4)


gend = ['M', 'F']
genlabel = Label(dataframeleft, font= ('arial', 10), text = 'GENDER:',padx =2, pady =2, bg ='orange') 
genlabel.grid(row = 5, column = 2, sticky = W)
genlabeltxt = ttk.Combobox(dataframeleft, font= ('times new roman', 11), textvariable= GENDER, width =13, value = gend) 
genlabeltxt.grid(row = 5, column = 3, sticky = W)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def AddHmo():
	if (len(HMO_NAME.get()) != 0 ):
		hmo(HMO_ID.get(), HMO_NAME.get())
		tk.Label(dataframeleft, text = "HMO Registered Successfully", fg = 'green', height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =1, column = 1, sticky = W)
		hmoidlabeltxt.delete(0, END)
		hmonamelabeltxt.delete(0, END)
		window.after(2000, clearhmo)
	else:
		tk.Label(dataframeleft, text = "Check Parameters!", fg = 'red',  bd =0, relief = 'solid',  height = 1, width = 24, anchor ='w').grid(row =1, column = 1, sticky = W)

def clearhmo():
	tk.Label(dataframeleft, text = "", fg = 'green',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =1, column = 1, sticky = W)


def hmo(HMO_ID, HMO_NAME):
	alf = []
	con = sqlite3.connect('patient.db')
	cur = con.cursor()

	cur.execute("SELECT HMO_ID FROM hmo")
	coll = cur.fetchall()
	for sub in coll:
		for item in sub:
			alf.append(item)

	if str(HMO_ID) in alf:
		tk.Label(dataframeleft, text = "HMO Already Exists!", fg = 'red',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =1, column = 1, sticky = W)
		raise Exception("Already Existing!")

	#cur.execute("CREATE TABLE IF NOT EXISTS hmo (id INTEGER PRIMARY KEY, HMO_ID INTEGER, HMO_NAME TEXT)")
	cur.execute("INSERT INTO hmo VALUES (NULL, ?,?)", (HMO_ID, HMO_NAME))
	con.commit()
	con.close()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def clearprinc():
	tk.Label(dataframeleft, text = "", fg = 'green',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)

def Addprinc():
	if (len(NHIS_NUMB.get()) != 0 ):
		princtable(NHIS_NUMB.get(), PRINCIPAL.get(), DOB.get(), GENDER.get())
		tk.Label(dataframeleft, text = "PRINCIPAL Registered", fg = 'green', height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)
		nhislabeltxt.delete(0, END)
		princlabeltxt.delete(0, END)
		doblabeltxt.delete(0, END)
		genlabeltxt.delete(0, END)
		window.after(2000, clearprinc)
	else:
		tk.Label(dataframeleft, text = "Check Parameters!", fg = 'red',  bd =0, relief = 'solid',  height = 1, width = 24, anchor ='w').grid(row =9, column = 1, sticky = W)


def princtable(NHIS_NUMB, PRINCIPAL, DOB, GENDER):
	alf = []
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	cur.execute("SELECT NHIS_NUMBER FROM principal")
	coll = cur.fetchall()
	for sub in coll:
		for item in sub:
			alf.append(item)

	if str(NHIS_NUMB) in alf:
		tk.Label(dataframeleft, text = "NHIS NUMBER Already Exists!", fg = 'red',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)
		raise Exception("Already Existing!")

	cur.execute("INSERT INTO principal VALUES (NULL, ?,?,?,?)", (NHIS_NUMB, PRINCIPAL, DOB, GENDER))
	con.commit()
	con.close()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def clearspouse():
	tk.Label(dataframeleft, text = "", fg = 'green',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)

def AddSpouse():
	if (len(NHIS_NUMB.get()) != 0 ):
		spousetable(NHIS_NUMB.get(), PRINCIPAL.get(), DOB.get(), GENDER.get())
		tk.Label(dataframeleft, text = "Spouse Registered", fg = 'green', height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)
		nhislabeltxt.delete(0, END)
		princlabeltxt.delete(0, END)
		doblabeltxt.delete(0, END)
		genlabeltxt.delete(0, END)
		window.after(2000, clearspouse)
	else:
		tk.Label(dataframeleft, text = "Check Parameters!", fg = 'red',  bd =0, relief = 'solid',  height = 1, width = 24, anchor ='w').grid(row =9, column = 1, sticky = W)


def spousetable(NHIS_NUMB, PRINCIPAL, DOB, GENDER):
	alf = []
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	#cur.execute("CREATE TABLE IF NOT EXISTS principal (id INTEGER PRIMARY KEY, NHIS_NUMB INTEGER, PRINCIPAL TEXT)")
	cur.execute("SELECT S_NHIS_NUMB FROM spouse")
	coll = cur.fetchall()
	for sub in coll:
		for item in sub:
			alf.append(item)

	if str(NHIS_NUMB) in alf:
		tk.Label(dataframeleft, text = "NHIS NUMBER Already Exists!", fg = 'red',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)
		raise Exception("Already Existing!")

	cur.execute("INSERT INTO spouse VALUES (NULL, ?,?,?,?)", (NHIS_NUMB, PRINCIPAL, DOB, GENDER))
	con.commit()
	con.close()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def clearchild1():
	tk.Label(dataframeleft, text = "", fg = 'green',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)

def AddChild1():
	if (len(NHIS_NUMB.get()) != 0 ):
		childtable(NHIS_NUMB.get(), PRINCIPAL.get(), DOB.get(), GENDER.get())
		tk.Label(dataframeleft, text = "Child 1 Registered", fg = 'green', height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)
		nhislabeltxt.delete(0, END)
		princlabeltxt.delete(0, END)
		doblabeltxt.delete(0, END)
		genlabeltxt.delete(0, END)
		window.after(2000, clearchild1)
	else:
		tk.Label(dataframeleft, text = "Check Parameters!", fg = 'red',  bd =0, relief = 'solid',  height = 1, width = 24, anchor ='w').grid(row =9, column = 1, sticky = W)


def childtable(NHIS_NUMB, PRINCIPAL, DOB, GENDER):
	alf = []
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	#cur.execute("CREATE TABLE IF NOT EXISTS principal (id INTEGER PRIMARY KEY, NHIS_NUMB INTEGER, PRINCIPAL TEXT)")
	cur.execute("SELECT C1_NHIS_NUMBER FROM child1")
	coll = cur.fetchall()
	for sub in coll:
		for item in sub:
			alf.append(item)

	if str(NHIS_NUMB) in alf:
		tk.Label(dataframeleft, text = "NHIS NUMBER Already Exists!", fg = 'red',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)
		raise Exception("Already Existing!")

	cur.execute("INSERT INTO child1 VALUES (NULL, ?,?,?,?)", (NHIS_NUMB, PRINCIPAL, DOB, GENDER))
	con.commit()
	con.close()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def clearchild2():
	tk.Label(dataframeleft, text = "", fg = 'green',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)

def AddChild2():
	if (len(NHIS_NUMB.get()) != 0 ):
		child2table(NHIS_NUMB.get(), PRINCIPAL.get(), DOB.get(), GENDER.get())
		tk.Label(dataframeleft, text = "Child 2 Registered", fg = 'green', height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)
		nhislabeltxt.delete(0, END)
		princlabeltxt.delete(0, END)
		doblabeltxt.delete(0, END)
		genlabeltxt.delete(0, END)
		window.after(2000, clearchild2)
	else:
		tk.Label(dataframeleft, text = "Check Parameters!", fg = 'red',  bd =0, relief = 'solid',  height = 1, width = 24, anchor ='w').grid(row =9, column = 1, sticky = W)


def child2table(NHIS_NUMB, PRINCIPAL, DOB, GENDER):
	alf = []
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	#cur.execute("CREATE TABLE IF NOT EXISTS principal (id INTEGER PRIMARY KEY, NHIS_NUMB INTEGER, PRINCIPAL TEXT)")
	cur.execute("SELECT C2_NHIS_NUMBER FROM child2")
	coll = cur.fetchall()
	for sub in coll:
		for item in sub:
			alf.append(item)

	if str(NHIS_NUMB) in alf:
		tk.Label(dataframeleft, text = "NHIS NUMBER Already Exists!", fg = 'red',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)
		raise Exception("Already Existing!")

	cur.execute("INSERT INTO child2 VALUES (NULL, ?,?,?,?)", (NHIS_NUMB, PRINCIPAL, DOB, GENDER))
	con.commit()
	con.close()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def clearchild3():
	tk.Label(dataframeleft, text = "", fg = 'green',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)

def AddChild3():
	if (len(NHIS_NUMB.get()) != 0 ):
		child3table(NHIS_NUMB.get(), PRINCIPAL.get(), DOB.get(), GENDER.get())
		tk.Label(dataframeleft, text = "Child 3 Registered", fg = 'green', height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)
		nhislabeltxt.delete(0, END)
		princlabeltxt.delete(0, END)
		doblabeltxt.delete(0, END)
		genlabeltxt.delete(0, END)
		window.after(2000, clearchild3)
	else:
		tk.Label(dataframeleft, text = "Check Parameters!", fg = 'red',  bd =0, relief = 'solid',  height = 1, width = 24, anchor ='w').grid(row =9, column = 1, sticky = W)


def child3table(NHIS_NUMB, PRINCIPAL, DOB, GENDER):
	alf = []
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	#cur.execute("CREATE TABLE IF NOT EXISTS principal (id INTEGER PRIMARY KEY, NHIS_NUMB INTEGER, PRINCIPAL TEXT)")
	cur.execute("SELECT C3_NHIS_NUMBER FROM child3")
	coll = cur.fetchall()
	for sub in coll:
		for item in sub:
			alf.append(item)

	if str(NHIS_NUMB) in alf:
		tk.Label(dataframeleft, text = "NHIS NUMBER Already Exists!", fg = 'red',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)
		raise Exception("Already Existing!")

	cur.execute("INSERT INTO child3 VALUES (NULL, ?,?,?,?)", (NHIS_NUMB, PRINCIPAL, DOB, GENDER))
	con.commit()
	con.close()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def clearchild4():
	tk.Label(dataframeleft, text = "", fg = 'green',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)

def AddChild4():
	if (len(NHIS_NUMB.get()) != 0 ):
		child4table(NHIS_NUMB.get(), PRINCIPAL.get(), DOB.get(), GENDER.get())
		tk.Label(dataframeleft, text = "Child 4 Registered", fg = 'green', height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)
		nhislabeltxt.delete(0, END)
		princlabeltxt.delete(0, END)
		doblabeltxt.delete(0, END)
		genlabeltxt.delete(0, END)
		window.after(2000, clearchild4)
	else:
		tk.Label(dataframeleft, text = "Check Parameters!", fg = 'red',  bd =0, relief = 'solid',  height = 1, width = 24, anchor ='w').grid(row =9, column = 1, sticky = W)


def child4table(NHIS_NUMB, PRINCIPAL, DOB, GENDER):
	alf = []
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	#cur.execute("CREATE TABLE IF NOT EXISTS principal (id INTEGER PRIMARY KEY, NHIS_NUMB INTEGER, PRINCIPAL TEXT)")
	cur.execute("SELECT C4_NHIS_NUMBER FROM child4")
	coll = cur.fetchall()
	for sub in coll:
		for item in sub:
			alf.append(item)

	if str(NHIS_NUMB) in alf:
		tk.Label(dataframeleft, text = "NHIS NUMBER Already Exists!", fg = 'red',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)
		raise Exception("Already Existing!")

	cur.execute("INSERT INTO child4 VALUES (NULL, ?,?,?,?)", (NHIS_NUMB, PRINCIPAL, DOB, GENDER))
	con.commit()
	con.close()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def clearextra():
	tk.Label(dataframeleft, text = "", fg = 'green', height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)

def AddExtra():
	if (len(NHIS_NUMB.get()) != 0 ):
		extratable(NHIS_NUMB.get(), PRINCIPAL.get(), DOB.get(), GENDER.get())
		tk.Label(dataframeleft, text = "Extra Dependant Added", fg = 'green', height = 1, width = 24, anchor ='w', bg = '#d1ffda').grid(row =9, column = 1, sticky = W)
		nhislabeltxt.delete(0, END)
		princlabeltxt.delete(0, END)
		doblabeltxt.delete(0, END)
		genlabeltxt.delete(0, END)
		window.after(2000, clearextra)
	else:
		tk.Label(dataframeleft, text = "Check Parameters!", fg = 'red',  bd =0, relief = 'solid',  height = 1, width = 24, anchor ='w').grid(row =9, column = 1, sticky = W)


def extratable(NHIS_NUMB, PRINCIPAL, DOB, GENDER):
	alf = []
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	#cur.execute("CREATE TABLE IF NOT EXISTS principal (id INTEGER PRIMARY KEY, NHIS_NUMB INTEGER, PRINCIPAL TEXT)")
	cur.execute("SELECT EX_NHIS_NUMBER FROM extra")
	coll = cur.fetchall()
	for sub in coll:
		for item in sub:
			alf.append(item)

	if str(NHIS_NUMB) in alf:
		tk.Label(dataframeleft, text = "NHIS NUMBER Already Exists!", fg = 'red',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)
		raise Exception("Already Existing!")

	cur.execute("INSERT INTO extra VALUES (NULL, ?,?,?,?)", (NHIS_NUMB, PRINCIPAL, DOB, GENDER))
	con.commit()
	con.close()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def clearvol():
	tk.Label(dataframeleft, text = "", fg = 'green',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)

def AddVol():
	if (len(NHIS_NUMB.get()) != 0 ):
		voltable(NHIS_NUMB.get(), PRINCIPAL.get(), DOB.get(), GENDER.get())
		tk.Label(dataframeleft, text = "Voluntary Added", fg = 'green', height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)
		nhislabeltxt.delete(0, END)
		princlabeltxt.delete(0, END)
		doblabeltxt.delete(0, END)
		genlabeltxt.delete(0, END)
		window.after(2000, clearvol)
	else:
		tk.Label(dataframeleft, text = "Check Parameters!", fg = 'red',  bd =0, relief = 'solid',  height = 1, width = 24, anchor ='w').grid(row =9, column = 1, sticky = W)


def voltable(NHIS_NUMB, PRINCIPAL, DOB, GENDER):
	alf = []
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	#cur.execute("CREATE TABLE IF NOT EXISTS principal (id INTEGER PRIMARY KEY, NHIS_NUMB INTEGER, PRINCIPAL TEXT)")
	cur.execute("SELECT V_NHIS_NUMBER FROM voluntary")
	coll = cur.fetchall()
	for sub in coll:
		for item in sub:
			alf.append(item)

	if str(NHIS_NUMB) in alf:
		tk.Label(dataframeleft, text = "NHIS NUMBER Already Exists!", fg = 'red',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)
		raise Exception("Already Existing!")

	cur.execute("INSERT INTO voluntary VALUES (NULL, ?,?,?,?)", (NHIS_NUMB, PRINCIPAL, DOB, GENDER))
	con.commit()
	con.close()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SNHIS_CODE = StringVar()
DESCRIPTION =StringVar()
SPRICE =StringVar()



snhiscodelabel = Label(dataframedown, font= ('arial', 10), text = 'SERVICE CODE:',padx =2, pady =2, bg ='orange') #ffc24f
snhiscodelabel.grid(row = 0, column = 0, sticky = E)
snhiscodelabeltxt = ttk.Entry(dataframedown, font= ('times new roman', 11), textvariable= SNHIS_CODE, width =25) 
snhiscodelabeltxt.grid(row = 0, column = 1, padx = 5)

desclabel = Label(dataframedown, font= ('arial', 10), text = 'DESCRIPTION:',padx =2, pady =2, bg ='orange') 
desclabel.grid(row = 0, column = 2, sticky = E)
desclabeltxt = ttk.Entry(dataframedown, font= ('times new roman', 11), textvariable= DESCRIPTION, width =25) 
desclabeltxt.grid(row = 0, column = 3, padx = 3)

spricelabel = Label(dataframedown, font= ('arial', 10), text = 'PRICE:',padx =2, pady =2, bg ='orange') 
spricelabel.grid(row = 1, column = 0, sticky = W)
spricelabeltxt = ttk.Entry(dataframedown, font= ('times new roman', 11), textvariable= SPRICE, width =25) 
spricelabeltxt.grid(row = 1, column = 1)

def clearserv():
	tk.Label(dataframedown, text = "", fg = 'green',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'white').grid(row =2, column = 1, sticky = W)

def AddServ():
	if (len(SNHIS_CODE.get()) != 0 ):
		servtable(SNHIS_CODE.get(), DESCRIPTION.get(), SPRICE.get())
		tk.Label(dataframedown, text = "Service Added!", fg = 'green', height = 1, width = 24, anchor ='w', bg = 'white').grid(row =2, column = 1, sticky = W)
		snhiscodelabeltxt.delete(0, END)
		desclabeltxt.delete(0, END)
		spricelabeltxt.delete(0, END)
		window.after(2000, clearserv)
	else:
		tk.Label(dataframedown, text = "Check Parameters!", fg = 'red',  bd =0, relief = 'solid',  height = 1, width = 24, anchor ='w').grid(row =2, column = 1, sticky = W)


def servtable(SNHIS_CODE, DESCRIPTION, SPRICE):
	alf = []
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	#cur.execute("CREATE TABLE IF NOT EXISTS principal (id INTEGER PRIMARY KEY, NHIS_NUMB INTEGER, PRINCIPAL TEXT)")
	cur.execute("SELECT NHIS_CODE FROM service")
	coll = cur.fetchall()
	for sub in coll:
		for item in sub:
			alf.append(item)

	if str(SNHIS_CODE) in alf:
		tk.Label(dataframedown, text = "SERVICE CODE Already Exists!", fg = 'red',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =2, column = 1, sticky = W)
		raise Exception("Already Existing!")

	cur.execute("INSERT INTO service VALUES (NULL, ?,?,?)", (SNHIS_CODE, DESCRIPTION, SPRICE))
	con.commit()
	con.close()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DRNAME = StringVar()
DOSAGE =StringVar()
STRENGTH =StringVar()
PRESENTATION = StringVar()
DPRICE = StringVar()



druglabel = Label(dataframedown, font= ('arial', 10), text = 'DRUG NAME:',padx =2, pady =2, bg ='orange') #ffc24f
druglabel.grid(row = 4, column = 0, sticky = W)
druglabeltxt = ttk.Entry(dataframedown, font= ('times new roman', 11), textvariable= DRNAME, width =25) 
druglabeltxt.grid(row = 4, column = 1, padx = 5)

doslabel = Label(dataframedown, font= ('arial', 10), text = 'DOSAGE:',padx =2, pady =2, bg ='orange') 
doslabel.grid(row = 4, column = 2, sticky = W)
doslabeltxt = ttk.Entry(dataframedown, font= ('times new roman', 11), textvariable= DOSAGE, width =25) 
doslabeltxt.grid(row = 4, column = 3, padx = 3)

strlabel = Label(dataframedown, font= ('arial', 10), text = 'STRENGTH:',padx =2, pady =2, bg ='orange') 
strlabel.grid(row = 5, column = 0, sticky = W, pady =2)
strlabeltxt = ttk.Entry(dataframedown, font= ('times new roman', 11), textvariable= STRENGTH, width =25) 
strlabeltxt.grid(row = 5, column = 1)

preslabel = Label(dataframedown, font= ('arial', 10), text = 'PRESENTATION:',padx =2, pady =2, bg ='orange') 
preslabel.grid(row = 5, column = 2, sticky = W)
preslabeltxt = ttk.Entry(dataframedown, font= ('times new roman', 11), textvariable= PRESENTATION, width =25) 
preslabeltxt.grid(row = 5, column = 3)

dpricelabel = Label(dataframedown, font= ('arial', 10), text = 'PRICE:',padx =2, pady =2, bg ='orange') 
dpricelabel.grid(row = 6, column = 0, sticky = W)
dpricelabeltxt = ttk.Entry(dataframedown, font= ('times new roman', 11), textvariable= DPRICE, width =25) 
dpricelabeltxt.grid(row = 6, column = 1)



def cleardrug():
	tk.Label(dataframedown, text = "", fg = 'green',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'white').grid(row =7, column = 1, sticky = W)

def AddDrug():
	if (len(DRNAME.get()) != 0 ):
		drugtable(DRNAME.get(), DOSAGE.get(), STRENGTH.get(), PRESENTATION.get(), DPRICE.get())
		tk.Label(dataframedown, text = "Drug Added!", fg = 'green', height = 1, width = 24, anchor ='w', bg = 'white').grid(row =7, column = 1, sticky = W)
		druglabeltxt.delete(0, END)
		doslabeltxt.delete(0, END)
		strlabeltxt.delete(0, END)
		preslabeltxt.delete(0, END)
		dpricelabeltxt.delete(0, END)
		window.after(2000, cleardrug)
	else:
		tk.Label(dataframedown, text = "Check Parameters!", fg = 'red',  bd =0, relief = 'solid',  height = 1, width = 24, anchor ='w').grid(row =7, column = 1, sticky = W)


def drugtable(DRNAME, DOSAGE, STRENGTH, PRESENTATION, DPRICE):
	alf = []
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	#cur.execute("CREATE TABLE IF NOT EXISTS principal (id INTEGER PRIMARY KEY, NHIS_NUMB INTEGER, PRINCIPAL TEXT)")
	cur.execute("INSERT INTO drugs VALUES (NULL, ?,?,?,?,?)", (DRNAME, DOSAGE, STRENGTH, PRESENTATION, DPRICE))
	con.commit()
	con.close()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
chkpr = IntVar()
chksp = IntVar()
ch1 = IntVar()
ch2 = IntVar()
ch3 = IntVar()
ch4 = IntVar()
ext = IntVar()
voln = IntVar()


boxprinc = Checkbutton(dataframeleft, text = "Principal", variable = chkpr)
boxprinc.grid(row = 7, column = 0 )

boxsp = Checkbutton(dataframeleft, text = "Spouse", variable = chksp)
boxsp.grid(row = 7, column = 1)

boxc1 = Checkbutton(dataframeleft, text = "Child 1", variable = ch1)
boxc1.grid(row = 7, column = 2)

boxc2 = Checkbutton(dataframeleft, text = "Child 2", variable = ch2, width = 7, height =1)
boxc2.grid(row = 8, column = 0, pady = 5)

boxc3 = Checkbutton(dataframeleft, text = "Child 3", variable = ch3)
boxc3.grid(row = 8, column = 1, pady = 5)

boxc4 = Checkbutton(dataframeleft, text = "Child 4", variable = ch4)
boxc4.grid(row = 8, column = 2, pady = 5)

boxex = Checkbutton(dataframeleft, text = "Extra", variable = ext, width = 7, height =1)
boxex.grid(row = 7, column = 3, pady = 5)

boxvol = Checkbutton(dataframeleft, text = "Voluntary", variable = voln)
boxvol.grid(row = 8, column = 3, pady = 5)



def execute():
	pr = chkpr.get()
	sp = chksp.get()
	c1 = ch1.get()
	c2 = ch2.get()
	c3 = ch3.get()
	c4 = ch4.get()
	ex = ext.get()
	vol = voln.get()

	if pr == 1 and sp == 0 and c1 == 0 and c2 == 0 and c3 == 0 and c4 == 0 and ex == 0 and vol == 0:
		Addprinc()
	elif pr == 0 and sp == 1 and c1 == 0 and c2 == 0 and c3 == 0 and c4 == 0 and ex == 0 and vol == 0:
		AddSpouse()
	elif pr == 0 and sp == 0 and c1 == 1 and c2 == 0 and c3 == 0 and c4 == 0 and ex == 0 and vol == 0:
		AddChild1()
	elif pr == 0 and sp == 0 and c1 == 0 and c2 == 1 and c3 == 0 and c4 == 0 and ex == 0 and vol == 0:
		AddChild2()
	elif pr == 0 and sp == 0 and c1 == 0 and c2 == 0 and c3 == 1 and c4 == 0 and ex == 0 and vol == 0:
		AddChild3()
	elif pr == 0 and sp == 0 and c1 == 0 and c2 == 0 and c3 == 0 and c4 == 1 and ex == 0 and vol == 0:
		AddChild4()
	elif pr == 0 and sp == 0 and c1 == 0 and c2 == 0 and c3 == 0 and c4 == 0 and ex == 1 and vol == 0:
		AddExtra()
	elif pr == 0 and sp == 0 and c1 == 0 and c2 == 0 and c3 == 0 and c4 == 0 and ex == 0 and vol == 1:
		AddVol()

	else:
		tk.Label(dataframeleft, text = "Make single selection please", fg = 'red',  bd =0,  height = 1, width = 24, anchor ='w', bg = 'orange').grid(row =9, column = 1, sticky = W)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

reghmo = Button(dataframeleft, text = 'Register HMO', font = ('arial', 10), command=AddHmo, width = 12, height = 1, bd = 2)
reghmo.grid(row= 1, column = 3, sticky = E, pady = 5)

#regprinc = Button(dataframeleft, text = 'Register Principal', font = ('arial', 10), command=Addprinc, width = 14, height = 1, bd = 2)
#regprinc.grid(row = 4, column =3, sticky = NE)#place(x = 481, y = 90)

regbut = Button(dataframeleft, text = 'Register Patient', font = ('arial', 10), command=execute, width = 14, height = 1, bd = 2)
regbut.grid(row = 9, column =3, sticky = E, pady = 15)

servbut = Button(dataframedown, text = 'Register Service', font = ('arial', 10), command=AddServ, width = 14, height = 1, bd = 2)
servbut.grid(row = 1, column =3, sticky = E, pady = 7)

drugbut = Button(dataframedown, text = 'Register Drug', font = ('arial', 10), command=AddDrug, width = 14, height = 1, bd = 2)
drugbut.grid(row = 7, column =3, sticky = E, pady = 7)

servbut = Label(dataframedown, text = '', font = ('arial', 10))
servbut.grid(row = 2, column =1, sticky = E,)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def update(rows):
	tv.delete(*tv.get_children())
	for item in rows:
		tv.insert("", 'end', values= item)

def spousequery():
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	query = "SELECT S_NHIS_NUMB, SPOUSE_NAME, DATE_OF_BIRTH, GENDER FROM spouse"
	cur.execute(query)
	rows = cur.fetchall()
	update(rows)
	con.commit()
	con.close()
	
boxprinc = ttk.Button(dataframedr, text = "Spouse", command = spousequery)
boxprinc.grid(row = 1, column = 1)



tv = ttk.Treeview(dataframeright, columns = (1,2,3,4), show = 'headings', height = '12')
#tv.pack(expand=YES, fill=BOTH)
tv.pack(side = "left")


tv.heading(1, text = 'NHIS NUMBER')
tv.column("1", minwidth=0, width=110, stretch=NO)
tv.heading(2, text = 'PATIENT NAME')
tv.column("2", minwidth=0, width=200, stretch=NO)
tv.heading(3, text = 'DATE OF BIRTH')
tv.column("3", minwidth=0, width=100, stretch=NO)
tv.heading(4, text = 'GENDER')
tv.column("4", minwidth=0, width=100, stretch=NO)


vsb =  ttk.Scrollbar(dataframeright, orient= "vertical", command= tv.yview)
vsb.pack(side ="right", fill= "y")
tv.configure(yscrollcommand = vsb.set)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def search(*args):
	q = qsearch.get()
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	query = "SELECT NHIS_NUMBER, PRINCIPAL_NAME, DATE_OF_BIRTH, GENDER FROM principal WHERE NHIS_NUMBER LIKE '%"+q+"%' OR PRINCIPAL_NAME LIKE '%"+q+"%'"
	cur.execute(query)
	rows = cur.fetchall()
	update(rows)


qsearch = StringVar()
ent = ttk.Entry(dataframedr, textvariable = qsearch)
ent.bind('<Return>', search)
ent.grid(row = 0, column = 0, padx = 6)
searchbut = ttk.Button(dataframedr, text ="search", command =search)
searchbut.grid(row = 0, column = 1, padx = 6)


# HMO_ID = StringVar()
# HMO_NAME = StringVar()

# NHIS_NUMB =StringVar()
# PRINCIPAL = StringVar()

# DOB = StringVar()
# GENDER = StringVar()
def getrow(event):
	rowid = tv.identify_row(event.y)
	item = tv.item(tv.focus())
	NHIS_NUMB.set(str(item['values'][0]).rjust(8, '0'))
	PRINCIPAL.set(item['values'][1])
	DOB.set(item['values'][2])
	GENDER.set(item['values'][3])

tv.bind('<Button 1>', getrow)

def clear():
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	query = "SELECT NHIS_NUMBER, PRINCIPAL_NAME, DATE_OF_BIRTH, GENDER FROM principal"
	cur.execute(query)
	rows = cur.fetchall()
	update(rows)
	nhislabeltxt.delete(0, END)
	princlabeltxt.delete(0, END)
	doblabeltxt.delete(0, END)
	genlabeltxt.delete(0, END)



btnclear = ttk.Button(dataframedr, text ='clear', command =clear)
btnclear.grid(row = 0, column = 2, padx = 6)

def delete():
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	todel = NHIS_NUMB.get()
	if messagebox.askyesno('Comfirm Delete', 'Are you sure you want to delete this patient?'):
		query = "DELETE FROM principal WHERE NHIS_NUMBER = ?"
		cur.execute(query, (todel,))
		print("to delete is: ", todel)
		con.commit()
		clear()
		con.close()

		
	else:
		return True

delbtn = ttk.Button(dataframedr, text = 'Delete Patient', command= delete)
delbtn.grid(row = 0, column =3, padx = 6)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def UpdatePatient():
	con = sqlite3.connect('patient.db')
	cur = con.cursor()
	if messagebox.askyesno("Please Confirm Update", "Are you sure you want to update this patient data?"):
		cur.execute("UPDATE principal SET NHIS_NUMBER= ?, PRINCIPAL_NAME= ?, DATE_OF_BIRTH= ?, GENDER=? WHERE NHIS_NUMBER = ?", (NHIS_NUMB.get(), PRINCIPAL.get(), DOB.get(), GENDER.get(), NHIS_NUMB.get()))
	else:
		return True
	con.commit()
	con.close()
	clear()

upbtn = ttk.Button(dataframedr, text ='Update Record', command = UpdatePatient)
upbtn.grid(row =1, column = 3, padx =6, pady =6)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
con = sqlite3.connect('patient.db')
cur = con.cursor()
query = "SELECT NHIS_NUMBER, PRINCIPAL_NAME, DATE_OF_BIRTH, GENDER FROM principal"
cur.execute(query)
rows = cur.fetchall()
update(rows)
con.commit()
con.close()



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
window.mainloop()
