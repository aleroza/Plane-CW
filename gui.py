from tkinter import *
from tkinter import ttk, Frame

def solve():
	rawdata=[]
	list=[]
	for node in txtlist:
		print(node[1].get())
	# for y in range(1,1+int(spiny.get())):
	# 	print(y)
	# 	list=[]
	# 	for x in range(7,7+int(spinx.get())):
	# 		print(x)
	# 		list.append([frmtxt.grid_slaves(y)[0].get()])
	# 	rawdata.append(list)

	fake=[[[0,0],[1,0]],[[0,1],[1,1]]]
	print(fake)
	print(rawdata)

def randsolve():
	pass

def show_grid():
	vertsep = ttk.Separator(window, orient='vertical')
	vertsep.grid(column=5, row=0, rowspan=10, sticky="ns")
	lblenter = Label(window, text="Введите начальные данные:", font=("Roboto", 14), justify="left", padx=5, pady=5)
	lblenter.grid(column=6, row=0, columnspan=5)
	btnend = Button(window, text="Решить", bg="gray", command=solve, padx=5, pady=5)
	btnrand = Button(window, text="Подставить случайные значения и решить", bg="gray", command=randsolve, padx=5,
	                 pady=5)
	btnend.grid(column=0, row=2, columnspan=5, sticky="w")
	btnrand.grid(column=1, row=2, columnspan=5, sticky="e")
	for widget in frmtxt.winfo_children():
		widget.destroy()


	for y in range(int(spiny.get())):
		for x in range(int(spinx.get())):
			xx, yy="x","y"
			txt = Text(frmtxt, height=1, width=3, font=10)
			if y==0:
				yy=0
			if x==0:
				xx=0
			txt.insert(1.0, f"{xx}, {yy}")
			txt.grid(column=7 + x, row=1 - y + int(spiny.get()), padx=5, pady=5)
			txtlist.append(txt)
	# for x in range(7, 7 + int(spinx.get()) * 2 - 1, 2):
	# 	for y in reversed(range(1,1+int(spiny.get())*2-1,2)):
	# 		print(x-6,y)
			# if x+1>=7+int(spinx.get())*2-1:
			# 	frmtxt.grid_slaves(x+1,y).configure(width="3")
	# [print(child.) for child in frmtxt.winfo_children()]

	# txtnodelist = {}
	# vertedgelist = {}
	# horizedgelist = {}
	# for y in range(1, int(spiny.get()) * 2, 2):
	# 	for x in range(1, int(spinx.get()) * 2, 2):
	# 		txtnodelist[f"{x - 1}{y - 1}"] = Text(frmtxt, height=1, width=3, font=10)
	# 		txtnodelist[f"{x - 1}{y - 1}"].insert(1.0, f"{x-1},{y-1}")
	# 		txtnodelist[f"{x - 1}{y - 1}"].configure(state="disable")
	# 		txtnodelist[f"{x - 1}{y - 1}"].grid(column=7 + x - 1, row=1 - y + int(spiny.get())-1, padx=5, pady=5)
		# if x+1 <int(spinx.get()):
		# 	vertedgelist[f"{x}{y}"] = Text(frmtxt, height=1, width=3)
		# 	txtnodelist[f"{x}{y}"].insert(1.0, f"{x},{y}")
		# 	vertedgelist[f"{x}{y}"].grid(column=7 + x + 1, row=int(spiny.get()) - y*2, padx=5, pady=5)
		#
		# if y+1<int(spiny.get()):
		# 	horizedgelist[f"{x}{y}"] = Text(frmtxt, height=1, width=3)
		# 	txtnodelist[f"{x}{y}"].insert(1.0, f"{x},{y}")
		# 	horizedgelist[f"{x}{y}"].grid(column=7 + x +1, row=int(spiny.get()) - y, padx=5, pady=5)


window = Tk()
window.title("Задача минимизации расхода горючего самолетом")
# window.geometry('350x200')

frmtxt: Frame = Frame(window)
frmgreet = Frame(window)
frmxy = Frame(window)
lbl = Label(window, text="Введите размерность ввода начальных данных...", font=("Roboto", 14), wraplength=300,
            justify="left", padx=5, pady=5)
lblx = Label(window, text="x=", padx=5, pady=5)
lbly = Label(window, text="y=", padx=5, pady=5)
btnstart = Button(window, text="Готово", bg="gray", command=show_grid, padx=5, pady=5)
spinx = Spinbox(window, from_=2, to=9, width=5)
spiny = Spinbox(window, from_=2, to=9, width=5)
txtlist = []

# frmgreet.pack(side="left")
# lbl.pack(side="left")
# btnstart.pack(side="left")
# frmxy.pack(side="left")
# spinx.pack(side="left")
# spiny.pack(side="left")

# frmgreet.grid()
frmtxt.grid(column=7, row=1)
lbl.grid(column=0, row=0, columnspan=3)
btnstart.grid(column=4, row=0)
lblx.grid(column=0, row=1, sticky="E")
spinx.grid(column=1, row=1, sticky="W")
lbly.grid(column=2, row=1, sticky="E")
spiny.grid(column=3, row=1, sticky="W")

window.mainloop()
