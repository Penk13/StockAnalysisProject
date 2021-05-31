# Stock Analysis

from tkinter import *
import sqlite3



# Create new window
window = Tk()
window.title('Stock Analysis')
frame = LabelFrame(window, padx=20, pady=20)
frame.pack(padx=10, pady=10)

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
	window.title('Edit')
	frame = LabelFrame(window, padx=20, pady=20)
	frame.pack(padx=10, pady=10)

	# Show stock and criteria


	# Create a database or connect to one
	conn = sqlite3.connect('stock_database.db')
	# Create a cursor
	c = conn.cursor()

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
	# Create new window
	window = Tk()
	window.title('Edit Criteria')
	frame = LabelFrame(window, padx=20, pady=20)
	frame.pack(padx=10, pady=10)

	# ----- Display -----
	criteria_label = Label(frame, text='Criteria').grid(row=0, column=0, pady=(0,5))
	criteria_entry = Entry(frame, width=100)
	criteria_entry.grid(row=0, column=1, columnspan=3)

	add_criteria_btn = Button(frame, text='Add', command=add_criteria).grid(row=1, column=1, columnspan=3, ipadx=50)
	
	delete_num_label = Label(frame, text='Delete Criteria Number').grid(row=2, column=1)
	delete_num_entry = Entry(frame, width=3)
	delete_num_entry.grid(row=2, column=2, sticky=W)
	delete_criteria_btn = Button(frame, text='Delete', command=delete_criteria).grid(row=2, column=3, sticky=W)

	# Create a database or connect to one
	conn = sqlite3.connect('stock_database.db')
	# Create a cursor
	c = conn.cursor()

	# Commit changes
	conn.commit()
	# Close connection
	conn.close()

# 3a. Create add criteria function
# Add criteria to stock_database
def add_criteria():
	pass

# 3b. Create delete criteria function
# Delete criteria from stock_database
def delete_criteria():
	pass





# --------------------------------- Main Display ---------------------------------


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
