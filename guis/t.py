from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import io
import os
root = Tk()
root.title("Meno")
root.geometry("600x600+600+250")

def open():
    if os.path.isfile("file.txt"):
        with io.open("file.txt", "r", encoding="utf8") as file:
            txt.insert(END,file.read())
    else:
        msg.showerror("ERROR","No such File")
def save():
    with io.open("file.txt","w",encoding="utf8") as files:
        files.write(txt.get("1.0",END))
def end():
    resp = msg.askokcancel("title","END?")
    print(resp)
    if resp:
        root.quit()

scr = Scrollbar(root,width=20)
scr.pack(side = 'right',fill="y")

txt = Text(root,yscrollcommand=scr.set)
txt.pack(fill="both",expand=True)
scr.config(command=txt.yview)


menus = Menu(root)
menu_file = Menu(menus,tearoff=0)
menu_file.add_command(label="open",command=open)
menu_file.add_command(label="save",command = save)
menu_file.add_command(label="end",command = end)
menus.add_cascade(label="FILE",menu=menu_file)
menu_rad = Menu(menus,tearoff=0)
menu_rad.add_cascade(label="q")
menus.add_cascade(label="EDIT",menu=menu_rad)
menu_che = Menu(menus,tearoff=0)
menus.add_cascade(label="VIEW",menu=menu_che)
root.config(menu=menus)


root.mainloop()