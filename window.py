# Stock Analysis

from tkinter import *
import sqlite3



# Create new window
window = Tk()
window.title('Stock Analysis')
window.geometry('400x400')

# Create a database or connect to one
conn = sqlite3.connect('stock_database.db')
# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE IF NOT EXISTS stock(
			code text,
			total int
		)""")




# --------------------------------- Main Function ---------------------------------
# 1. Create show function
def show():
	# Create new window
	window = Tk()
	window.title('Show')
	frame = LabelFrame(window, padx=20, pady=20)
	frame.pack(padx=10, pady=10)

	# Create a database or connect to one
	conn = sqlite3.connect('stock_database.db')
	# Create a cursor
	c = conn.cursor()


	#TODO
	# Show stock and criteria
	# show table column
	c.execute('SELECT * FROM stock')
	column_list = [data[0] for data in c.description]
	for i in range(2,len(column_list)):
		Label(frame, text=column_list[i]).pack()

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

# 2. Create edit function
def edit():
	# Create new window
	window = Tk()
	window.title('Edit')
	frame = LabelFrame(window, padx=20, pady=20)
	frame.pack(padx=10, pady=10)

	# Edit stock


	# Create a database or connect to one
	conn = sqlite3.connect('stock_database.db')
	# Create a cursor
	c = conn.cursor()

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

# 3. Create edit criteria function
def edit_criteria():
	# Create global variable for 3a and 3b function
	global criteria_entry	# Get anything from criteria_entry for new column name in database in function 3a
	global delete_num_entry	# Get id number to delete

	# Create new window
	window = Tk()
	window.title('Edit Criteria')
	window.geometry('750x400')

	# ----- Display -----
	# Frame 1 (Add Criteria)
	frame = LabelFrame(window, text='Add Criteria', padx=20, pady=20)
	frame.place(x=10, y=10)

	criteria_label = Label(frame, text='Criteria').grid(row=0, column=0, padx=5, pady=10)
	criteria_entry = Entry(frame, width=100)
	criteria_entry.grid(row=0, column=1, columnspan=2, pady=10)
	add_criteria_btn = Button(frame, text='Add', command=add_criteria).grid(row=1, column=1, columnspan=2, ipadx=50)
	
	# Frame 2 (Delete Criteria)
	frame2 = LabelFrame(window, text='Delete Criteria', padx=20, pady=20)
	frame2.place(x=10, y=150)

	delete_num_label = Label(frame2, text='Delete Criteria Number').grid(row=0, column=0, padx=10, pady=10, sticky=E)
	delete_num_entry = Entry(frame2, width=3)
	delete_num_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)
	crt_to_delete_btn = Button(frame2, text='Show', command=show_criteria).grid(row=0, column=2, sticky=W)
	crt_to_delete_entry = Entry(frame2, width=100).grid(row=1, column=0, columnspan=3, pady=10) #TODO edit entry
	delete_criteria_btn = Button(frame2, text='Delete', command=delete_criteria).grid(row=2, column=0, columnspan=3, padx=10, ipadx=50)

	# Create a database or connect to one
	conn = sqlite3.connect('stock_database.db')
	# Create a cursor
	c = conn.cursor()

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

# 3a. Create add criteria function
def add_criteria():
	# Create a database or connect to one
	conn = sqlite3.connect('stock_database.db')
	# Create a cursor
	c = conn.cursor()

	# Add criteria column to database
	c.execute('ALTER TABLE stock ADD COLUMN {} text'.format(criteria_entry.get()))

	# Delete criteria_entry box
	criteria_entry.delete(0, END)

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

# 3b. Create delete criteria function
def delete_criteria():
	# Create a database or connect to one
	conn = sqlite3.connect('stock_database.db')
	# Create a cursor
	c = conn.cursor()

	#TODO
	# Delete criteria column from database
	c.execute('ALTER TABLE stock DROP COLUMN {}'.format('wow'))

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

# 3c. Create show criteria function
def show_criteria():
	# Create a database or connect to one
	conn = sqlite3.connect('stock_database.db')
	# Create a cursor
	c = conn.cursor()

	#TODO
	# Show criteria to entry
	#c.execute('SELECT rowid FROM stock WHERE rowid ' + delete_num_entry.get())
	#c.fetchone()

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()



# --------------------------------- Main Display ---------------------------------

frame = LabelFrame(window, padx=20, pady=20)
frame.place(x=10, y=10)

# Create entry and label
code_label = Label(frame, text='Code').grid(row=0, column=0, pady=(0,5))
code_entry = Entry(frame, width=8)
code_entry.grid(row=0, column=1)

# Create show button
show_btn = Button(frame, text='Show', command=show).grid(row=1, column=0, columnspan=2)

# Create edit button
edit_btn = Button(frame, text='Edit', command=edit).grid(row=2, column=0, columnspan=2)

# Create add_criteria button
edit_criteria_btn = Button(frame, text='Edit Criteria', command=edit_criteria).grid(row=3, column=0, columnspan=2)



# Commit changes
conn.commit()
# Close connection
conn.close()

window.mainloop()
