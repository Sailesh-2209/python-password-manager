from tkinter import *
from tkinter.messagebox import showinfo, showerror
import sqlite3

#-----------------------------------GLOBAL-----------------------------------------

root = Tk()
mainFrame = Frame(root)
mainFrame.pack()
conn = sqlite3.connect('passwords.db')
cur = conn.cursor()

try:
	cur.execute("""CREATE TABLE passwords (service varchar, email varchar, password varchar)""")
except: 
	pass


temp_fetch_list = []
#-------------------------------END OF GLOBAL---------------------------------------

#---------------------------------FRAME ONE-----------------------------------------

frame_one = Frame(mainFrame)
frame_one.pack(side=TOP, fill=BOTH, expand=YES)
frame_one.config()
frame_one_lab1 = Label(frame_one, text="What do you want to do?")
frame_one_lab1.pack(side=TOP, expand=YES, fill=BOTH)

frame_one_sub_frame = Frame(frame_one)
frame_one_sub_frame.pack(side=BOTTOM, fill=BOTH, expand=YES)
frame_one_sub_frame.config()

inner_frame_1 = Frame(frame_one_sub_frame)
inner_frame_2 = Frame(frame_one_sub_frame)
inner_frame_1.pack(side=LEFT, expand=YES, fill=BOTH)
inner_frame_2.pack(side=RIGHT, expand=YES, fill=BOTH)

button1 = Button(inner_frame_1, text='Fetch a password', command= (lambda: fetchMenu()))
button2 = Button(inner_frame_2, text='Add a new password', command= (lambda: addMenu()))
button3 = Button(inner_frame_1, text='Remove a password', command=(lambda: removeMenu()))
button4 = Button(inner_frame_2, text='Fetch All', command=(lambda: fetchAll()))

button1.pack(side=TOP, fill=X, expand=YES)
button2.pack(side=TOP, fill=X, expand=YES)
button3.pack(side=TOP, fill=X, expand=YES)
button4.pack(side=TOP, fill=X, expand=YES)

#------------------------------END OF FRAME ONE------------------------------------

#-------------------------------BUTTON COMMANDS------------------------------------
def fetchMenu():
	fetchBox = Toplevel(root)
	fetchBox_frame_main = Frame(fetchBox)
	fetchBox_frame_main.pack()
	cur.execute("SELECT * FROM passwords")
	fetch_pw_list = cur.fetchall()
	fetchBox_frame_1 = Frame(fetchBox_frame_main)
	fetchBox_frame_2 = Frame(fetchBox_frame_main)
	fetchBox_frame_3 = Frame(fetchBox_frame_main)
	fetchBox_frame_4 = Frame(fetchBox_frame_main)
	fetchBox_frame_1.pack(side=TOP, fill=X, expand=YES)
	fetchBox_frame_4.pack(side=BOTTOM, fill=X, expand=YES)
	fetchBox_frame_2.pack(side=LEFT, fill=BOTH, expand=YES)
	fetchBox_frame_3.pack(side=RIGHT, fill=BOTH, expand=YES)
	
	main_lab = Label(fetchBox_frame_1, text='Choose the Service and the Email address')
	main_lab.pack(fill=BOTH, expand=YES)

	
	def handleServiceList(event):
		label1 = service_listbox.get(ACTIVE)
		temp_fetch_list.append(label1)

	def handleMailList(event):
		label2 = mail_listbox.get(ACTIVE)
		temp_fetch_list.append(label2)

	def fetch():
		cur.execute("SELECT * FROM passwords WHERE service=? AND email=?", (temp_fetch_list[0], temp_fetch_list[1]))
		disp_val = cur.fetchone()

		try:
			disp = 'Your password is ' + str(disp_val[2])
			showinfo('Password', disp)
		except:
			showerror('Error', 'Password not found...')

		fetchBox.destroy()


	sub_lab_1 = Label(fetchBox_frame_2, text='Service')
	sub_lab_1.pack(side=TOP, fill=X, expand=YES)
	service_listbox = Listbox(fetchBox_frame_2, relief=SUNKEN)
	service_scrollbar = Scrollbar(fetchBox_frame_2)
	service_scrollbar.config(command=service_listbox.yview)
	service_listbox.config(yscrollcommand=service_scrollbar.set)
	service_listbox.pack(side=LEFT, fill=BOTH, expand=YES)
	service_scrollbar.pack(side=RIGHT, fill=Y, expand=YES)
	pos1 = 0
	for tup in fetch_pw_list:
		service_listbox.insert(pos1, tup[0])
		pos1 += 1
	service_listbox.bind('<Button-1>', handleServiceList)

	sub_lab_2 = Label(fetchBox_frame_3, text='Email address')
	sub_lab_2.pack(side=TOP, fill=X, expand=YES)
	mail_listbox = Listbox(fetchBox_frame_3, relief=SUNKEN)
	mail_scrollbar = Scrollbar(fetchBox_frame_2)
	mail_scrollbar.config(command=mail_listbox.yview)
	mail_listbox.config(yscrollcommand=mail_scrollbar.set)
	mail_listbox.pack(side=LEFT, fill=BOTH, expand=YES)
	service_scrollbar.pack(side=LEFT, fill=Y, expand=YES)
	pos2 = 0
	for tup in fetch_pw_list:
		mail_listbox.insert(pos2, tup[1])
		pos2 += 1
	mail_listbox.bind('<Button-1>', handleMailList)

	fetch_button = Button(fetchBox_frame_4, text='OK', command= (lambda: fetch()))
	fetch_button.pack(fill=BOTH, expand=YES)


def addMenu():
	addBox = Toplevel(root)
	addBox_frame_main = Frame(addBox)
	addBox_frame_main.pack()
	addMenuButton = Button(addBox_frame_main, text='Add Password', relief=SUNKEN)
	addMenuButton.pack(side=BOTTOM, fill=BOTH, expand=YES)
	addBox_frame1 = Frame(addBox_frame_main)
	addBox_frame2 = Frame(addBox_frame_main)
	addBox_frame1.pack(side=LEFT, fill=BOTH, expand=YES)
	addBox_frame2.pack(side=RIGHT, fill=BOTH, expand=YES)
	addBox_lab1 = Label(addBox_frame1, text='Service')
	addBox_lab2 = Label(addBox_frame1, text='Email address')
	addBox_lab3 = Label(addBox_frame1, text='Password')
	addBox_lab1.pack(side=TOP, expand=YES, fill=BOTH)
	addBox_lab2.pack(side=TOP, expand=YES, fill=BOTH)
	addBox_lab3.pack(side=TOP, expand=YES, fill=BOTH)
	ent1 = Entry(addBox_frame2, width=50)
	ent2 = Entry(addBox_frame2, width=50)
	ent3 = Entry(addBox_frame2, width=50)
	var1 = StringVar()
	var2 = StringVar()
	var3 = StringVar()
	ent1.config(textvariable=var1)
	ent2.config(textvariable=var2)
	ent3.config(textvariable=var3)
	ent1.pack(side=TOP, expand=YES, fill=BOTH)
	ent2.pack(side=TOP, expand=YES, fill=BOTH)
	ent3.pack(side=TOP, expand=YES, fill=BOTH)
	entList = [var1, var2, var3]
	addMenuButton.config(command= (lambda: storePw(entList, addBox)))

def removeMenu():
	removeWindow = Toplevel(root)
	remove_frame_main = Frame(removeWindow)
	remove_frame_main.pack()
	remove_lab = Label(remove_frame_main, text='Select the service')
	remove_lab.pack(side=TOP, expand=YES, fill=X)
	remove_button = Button(remove_frame_main, text='OK', relief=SUNKEN)
	remove_button.pack(side=BOTTOM, fill=X, expand=YES)

	def removeSelector():
		label = remove_listbox.get(ACTIVE)

		with conn:
			cur.execute("DELETE FROM passwords WHERE service=?", (label,))

		del_mes = 'Your password for ' + str(label) + ' has been deleted!'
		showinfo('Delete message', del_mes)

		removeWindow.destroy()

	remove_listbox = Listbox(remove_frame_main, relief=SUNKEN)
	remove_scrollbar = Scrollbar(remove_frame_main)
	remove_listbox.pack(side=LEFT, fill=BOTH, expand=YES)
	remove_scrollbar.pack(side=RIGHT, fill=Y, expand=YES)
	remove_scrollbar.config(command=remove_listbox.yview)
	remove_listbox.config(yscrollcommand=remove_scrollbar.set) 

	cur.execute("SELECT * FROM passwords")
	fetch_pw_list = cur.fetchall()
	pos = 0
	for tup in fetch_pw_list:
		remove_listbox.insert(pos, tup[0])
		pos += 1
	remove_listbox.bind('<Double-1>', removeSelector)
	remove_button.config(command= lambda: removeSelector())



def fetchAll():
	passWindow = Toplevel(root)
	passFrame = Frame(passWindow)
	passFrame.pack()
	cur.execute("SELECT * FROM passwords")
	fetch_pw_list = cur.fetchall()
	textbox = Text(passFrame)
	allscroll = Scrollbar(passFrame)
	textbox.config(yscrollcommand=allscroll.set)
	allscroll.config(command=textbox.yview)
	textbox.pack(side=LEFT, fill=BOTH, expand=YES)
	allscroll.pack(side=LEFT, fill=Y, expand=YES)

	for tup in fetch_pw_list:
		printstring = 'Service: ' + str(tup[0]) + ', Email-address: ' + str(tup[1]) + ', Password: ' + str(tup[2]) + ';\n'
		textbox.insert(END, printstring)
#-----------------------------END OF BUTTON COMMANDS--------------------------------


#-------------------------------BUTTON SUB COMMANDS---------------------------------

def storePw(pwList, addBox):
	dbList = []
	for pw in pwList:
		dbList.append(pw.get())

	with conn: 
		cur.execute("INSERT INTO passwords VALUES (:service, :email, :password)", {'service': dbList[0], 'email': dbList[1], 'password': dbList[2]})

	addBox.destroy()

#---------------------------END OF BUTTON SUB COMMANDS------------------------------

conn.commit()
root.mainloop()