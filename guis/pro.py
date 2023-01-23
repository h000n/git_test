from tkinter import filedialog
from tkinter import *
from PIL import Image
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import os
root = Tk()
root.title("Title")

root.geometry("600x700+600+150")
class MadeError(Exception):
    pass
def add():
    files = filedialog.askopenfiles(title="selectfiles",filetypes=(("png","*.png"),("all","*.*")),initialdir=r"C:\Users\hoon\Downloads")
    for file in files:
        list_file.insert(END,file)
def dels():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)
def save():
    folder = filedialog.askdirectory()
    if folder == "":
        return 
    name.delete(0,END)
    name.insert(0,folder)  
def start():
    try:
        prog_var.set(0)
        img_width = cb_width.get()
        images = [Image.open(x.split("name=")[1].replace("'","").split(" mode")[0]) for x in list_file.get(0,END)]
        if img_width == "original":
            img_width = -1
        try:
            int(img_width)-1
        except:
            msg.showerror("ERROR","only intergal")
        else:
            img_width = int(img_width)
        img_space = cb_space.get()
        if img_space == space_value[0]:
            img_space = 30
        elif img_space == space_value[1]:
            img_space = 60
        elif img_space == space_value[2]:
            img_space = 90
        else:
            img_space = 0
        
        img_format = cb_format.get().lower()

        if list_file.size() ==0:
            msg.showerror("ERROR","No Files")
            return
        if len(name.get()) ==0:
            msg.showerror("ERROR","No path")
            return

        image_size = []
        if img_width > -1:
            image_size = [(int(img_width),int(img_width * x.size[1] / x.size[0] )) for x in images]
        else:
            image_size = [(x.size[0],x.size[1]) for x in images]
        
        # widths = [x.size[0] for x in images]
        # heights = [x.size[1] for x in images]
        widths,heights = zip(*image_size)
        resu_img = Image.new("RGB",(max(widths),sum(heights)+img_space),(255,255,255))
        y_offset = 0
        for idx, img in enumerate(images):
            if img_width > -1:
                img = img.resize(image_size[idx])
            resu_img.paste(img,(0,y_offset))
            y_offset += (img.size[1] + img_space)

            progress = (idx+1)/len(images) *100
            prog_var.set(progress)
            prog_bar.update()
        if names.get() =="":
            raise MadeError
        resu_img.save(os.path.join(name.get(),"{}.".format(names.get())+img_format))
    except MadeError:
        msg.showerror("ERROR","Please enter Name")
        prog_var.set(0)
    except Exception as err:
        msg.showerror("ERROR",err)
        prog_var.set(0)

def end():
    resp = msg.askokcancel("title","END?")
    if resp:root.quit() 

file_frame = Frame(root)
file_frame.pack(fill="both",padx=8,pady=8)
btn_add = Button(file_frame,text="add",padx=10,pady=10,width=10,command=add)
btn_del = Button(file_frame,text="del",padx=10,pady=10,width=10,command=dels)
btn_add.pack(side="left",padx=8,pady=8)
btn_del.pack(side="right",padx=8,pady=8)

list_frame = Frame(root)
list_frame.pack(fill="both",padx=8,pady=8)
scr = Scrollbar(list_frame)
scr.pack(side="right",fill="y",padx=8,pady=8)
list_file = Listbox(list_frame,selectmode="extended",height=10,yscrollcommand=scr.set)
list_file.pack(side="left",fill="both",expand=True,padx=8,pady=8)
scr.config(command = list_file.yview)

save_frame = LabelFrame(root,text="save")
save_frame.pack(fill="both",padx=8,pady=8)
name = Entry(save_frame)
name.insert(END,"C:/Users/hoon/Downloads")
name.pack(side="left",fill="x",expand=True,padx=8,pady=8)
save_find_btn = Button(save_frame,text="find",width=10,command=save)
save_find_btn.pack(side="right",padx=8,pady=8)

option_frame = LabelFrame(root,text= "option")
option_frame.pack(fill="both",padx=8,pady=8)
lb_width = Label(option_frame,text="width",width=5)
lb_width.pack(side="left",padx=8,pady=8)
width_value = ["original","100","640"]
cb_width = ttk.Combobox(option_frame, values=width_value, width=10)
cb_width.current(0)
cb_width.pack(side="left",padx=8,pady=8)

lb_space = Label(option_frame,text="space",width=5)
lb_space.pack(side="left",padx=8,pady=8)
space_value = ["small","big","very big"]
cb_space = ttk.Combobox(option_frame,state="readonly", values=space_value, width=10)
cb_space.current(0)
cb_space.pack(side="left",padx=8,pady=8)

lb_format = Label(option_frame,text="format",width=5)
lb_format.pack(side="left",padx=8,pady=8)
format_value = ["png","jpg"]
cb_format = ttk.Combobox(option_frame,state="readonly", values=format_value, width=10)
cb_format.current(0)
cb_format.pack(side="left",padx=8,pady=8)

prog_frame = LabelFrame(root,text= "progress")
prog_frame.pack(fill="x",padx=8,pady=8,ipady=5)
prog_var = DoubleVar()
prog_bar = ttk.Progressbar(prog_frame,maximum=100, variable=prog_var)
prog_bar.pack(fill="x",padx=8,pady=8,ipady=5)

names_frame = LabelFrame(root,text="name")
names_frame.pack(fill="both",padx=8,pady=8)
names = Entry(names_frame)
names.insert(END,"result")
names.pack(side="left",fill="x",expand=True,padx=8,pady=8)

run_frame = Frame(root)
run_frame.pack(fill="both",padx=8,pady=8)
start_btn = Button(run_frame,text="run",padx=15,pady=15,command=start)
end_btn = Button(run_frame,text="close",padx=15,pady=15,command=end)
start_btn.pack(side = "right",padx=8,pady=8)
end_btn.pack(side = "right",padx=8,pady=8)


root.resizable(False,False)
root.mainloop()