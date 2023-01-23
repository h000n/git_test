from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
root = Tk()
root.title("Title")

root.geometry("600x600+600+250")

# photo = PhotoImage(file="guis\img.png")
# def commands():
#     print(" ")
# btn1 = Button(root,image=photo,fg="black",bg="red",padx=10,pady=10, text="button",command=commands)
# btn1.pack()

# label1 = Label(root,text="lable")
# label1.config(text=" ")

# txt = Text(root, width=10,height=3)
# txt.pack()
# txt.insert(END,"hr")

# ent = Entry(root)
# ent.pack()
# ent.insert(END,"\"enterX\"")

# def gets():
#     print(txt.get("1.0",END))
#     print(ent.get())
#     txt.delete("1.0",END)
#     ent.delete(0,END)

# btn = Button(root,command=gets)
# btn.pack()

# listbox = Listbox(root,selectmode="extended",height=0)
# listbox.insert(0,"a")
# listbox.insert(END,"z")
# listbox.pack()
# print(listbox.get(0,1))
# print(listbox.size())
# print(listbox.curselection())
# listbox.delete(END)

# chv = IntVar()
# chb = Checkbutton(root,text="ch",variable=chv)
# chb.select()
# chb.pack()
# print(chv.get())


# Label(root,text="slell").pack()
# rbv = IntVar()
# rbs = StringVar()
# rb = Radiobutton(root,text="a",value=1,variable=rbv)
# rb2 = Radiobutton(root,text="a",value=2,variable=rbv)
# rb3 = Radiobutton(root,text="a",value="a",variable=rbs)
# rb3.select()
# rb.pack()
# rb2.pack()
# rb3.pack()
# print(rbv.get())
# print(rbs.get())

# values = [str(i) for i in range(1,31)]
# cb = ttk.Combobox(root,height=5,values =values,state="readonly")
# cb.set("s")
# cb.current(0)
# cb.pack()
# print(cb.get())

# bar = ttk.Progressbar(root,maximum=100,mode="determinate")
# bar.start(100) #move every ms
# bar.stop()
# barv = DoubleVar()
# bar2 = ttk.Progressbar(root,maximum=100,length=200,mode="determinate",variable=barv) 
# bar2.pack()
# bar.pack()
# def bt():
#     for i in range(101):
#         time.sleep(0.01)
#         barv.set(i)
#         bar2.update()
#     print("END")
# Button(root,command=bt).pack()


# def news():
#     pass

# menus = Menu(root)

# menu_file = Menu(menus,tearoff=0)
# menu_file.add_command(label="new file",command=root.quit)
# menu_file.add_separator()
# menu_file.add_command(label="new",command=news,state="disable")
# menus.add_cascade(label="files",menu=menu_file)

# menu_rad = Menu(menus,tearoff=0)
# menu_rad.add_radiobutton(label="korean")
# menu_rad.add_radiobutton(label="english")
# menus.add_cascade(label="lang",menu=menu_rad)

# menu_che = Menu(menus,tearoff=0)
# menu_che.add_checkbutton(label="1")
# menu_che.add_checkbutton(label="2")
# menus.add_cascade(label="ch",menu=menu_che)

# root.config(menu=menus)

# def info():
#     msg.showinfo("title","message")
#     msg.showwarning("title","message")
#     msg.showerror("title","message")
#     resp = msg.askokcancel("title","message")
#     msg.askretrycancel("title","message")
#     msg.askyesnocancel("title","message")
#     msg.askyesno(None,"message")
#     if resp == 1:
#         print("y")

# but = Button(root,command=info,text="ale").pack()

# frame = Frame(root,relief="solid",bd=1)
# frame.pack(side="right",expand=True,fill="both")
# Button(frame,text="a").pack()
# Button(frame,text="b").pack()

# frame2 = LabelFrame(root,text="as")
# frame2.pack(side="left",expand=True,fill="both")
# Button(frame2,text="a").pack()
# Button(frame2,text="b").pack()


# frame = Frame(root)
# frame.pack()
# scr = Scrollbar(frame)
# scr.pack(side = 'right',fill="y")
# listbox = Listbox(frame,selectmode="extended",height=10,yscrollcommand=scr.set)
# for i in range(1,32):
#     listbox.insert(END,str(i)+"a")
# listbox.pack(side="left")
# scr.config(command=listbox.yview)


# btn1 = Button(root, text="1",width=10,height=10)
# btn2 = Button(root, text="2",width=10,height=10)
# btn3 = Button(root, text="3",width=10,height=10)
# btn4 = Button(root, text="4",padx=10,pady=10)
# btn5 = Button(root, text="5",padx=10,pady=10)# 글자 기준 여백
# btn6 = Button(root, text="6",padx=10,pady=10)
# btn7 = Button(root, text="7",padx=10,pady=10)
# btn8 = Button(root, text="8",padx=10,pady=10)
# btn1.grid(row= 0,column=0,sticky=N+E+W+S, padx=3, pady= 3)
# btn2.grid(row= 0,column=1,sticky=N+E+W+S, padx=3, pady= 3)
# btn3.grid(row= 0,column=2,sticky=N+E+W+S, padx=3, pady= 3)
# btn4.grid(row= 1,column=0,rowspan=2,sticky=N+E+W+S, padx=3, pady= 3)
# btn5.grid(row= 1,column=1,sticky=N+E+W+S, padx=3, pady= 3)
# btn6.grid(row= 1,column=2,sticky=N+E+W+S, padx=3, pady= 3)
# btn7.grid(row= 3,column=0,sticky=N+E+W+S, padx=3, pady= 3)
# btn8.grid(row= 2,column=1,columnspan=2,sticky=N+E+W+S, padx=3, pady= 3)


root.mainloop()