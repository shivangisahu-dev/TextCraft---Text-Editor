from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

root=Tk()
root.geometry("900x600")
root.title(" Notepad editor")
root.iconbitmap(r"C:\Users\DELL\Desktop\python\Notpad Project\notepad.ico")

#================Variable for text area===================
current_font="Arial"
current_size=12

#======================SCROLLBAR================
scroll=Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)


#===============MAIN MENUBAR===================
main_menu=Menu(root)
root.config(menu=main_menu)

#================FILE MENU============

file_menu=Menu(main_menu,tearoff=0)
main_menu.add_cascade(label="File",menu=file_menu)

#==============================IMAGE MENU=====================================

 #==============FILE IMAGE===================

new_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\add-folder.png")
new_img=new_img.resize((20,20),Image.LANCZOS)
new=ImageTk.PhotoImage(new_img)

open_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\openfolder.png")
open_img=open_img.resize((20,20),Image.LANCZOS)
openn=ImageTk.PhotoImage(open_img)

save_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\save.png")
save_img=save_img.resize((20,20),Image.LANCZOS)
save=ImageTk.PhotoImage(save_img)


saveas_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\Saveas.png")
saveas_img=saveas_img.resize((20,20),Image.LANCZOS)
saveas=ImageTk.PhotoImage(saveas_img)

exit_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\exit.png")
exit_img=exit_img.resize((20,20),Image.LANCZOS)
exitt=ImageTk.PhotoImage(exit_img)

  #================EDIT IMAGE ====================

copy_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\copy.png")
copy_img=copy_img.resize((20,20),Image.LANCZOS)
copy=ImageTk.PhotoImage(copy_img)

paste_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\pastefolder.png")
paste_img=paste_img.resize((20,20),Image.LANCZOS)
paste=ImageTk.PhotoImage(paste_img)

cut_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\cut-file.png")
cut_img=cut_img.resize((20,20),Image.LANCZOS)
cut=ImageTk.PhotoImage(cut_img)


clear_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\clear.png")
clear_img=clear_img.resize((20,20),Image.LANCZOS)
clear=ImageTk.PhotoImage(clear_img)

undo_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\undo.png")
undo_img=undo_img.resize((20,20),Image.LANCZOS)
undo=ImageTk.PhotoImage(undo_img)


redo_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\redo.png")
redo_img=redo_img.resize((20,20),Image.LANCZOS)
redo=ImageTk.PhotoImage(redo_img)

find_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\find.png")
find_img=find_img.resize((20,20),Image.LANCZOS)
find=ImageTk.PhotoImage(find_img)

#================VIEW IMAGE==============

zoomin_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\zoom-in.png")
zoomin_img=zoomin_img.resize((20,20),Image.LANCZOS)
zoomin=ImageTk.PhotoImage(zoomin_img)


zoomout_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\zoom-out.png")
zoomout_img=zoomout_img.resize((20,20),Image.LANCZOS)
zoomout=ImageTk.PhotoImage(zoomout_img)

status_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\status.png")
status_img=status_img.resize((20,20),Image.LANCZOS)
status=ImageTk.PhotoImage(status_img)

#==================THEME IMAGE===================

default_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\defaultcolour.png")
default_img=default_img.resize((20,20),Image.LANCZOS)
default=ImageTk.PhotoImage(default_img)


light_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\white.png")
light_img=light_img.resize((20,20),Image.LANCZOS)
light=ImageTk.PhotoImage(light_img)

black_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\black.png")
black_img=black_img.resize((20,20),Image.LANCZOS)
black=ImageTk.PhotoImage(black_img)


red_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\red.png")
red_img=red_img.resize((20,20),Image.LANCZOS)
red=ImageTk.PhotoImage(red_img)

monokai_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\monokai.png")
monokai_img=monokai_img.resize((20,20),Image.LANCZOS)
monokai=ImageTk.PhotoImage(monokai_img)


blue_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\bluecircle.png")
blue_img=blue_img.resize((20,20),Image.LANCZOS)
blue=ImageTk.PhotoImage(blue_img)

#========================ABOUT IMAGE====================
about_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\aboutus.png")
about_img=about_img.resize((20,20),Image.LANCZOS)
about=ImageTk.PhotoImage(about_img)

#===========================FILE MENU FUNCTIONS=====================
File=None
def new_func():
    global File
    root.title("Untitled -Notepad")
    text_area.delete(1.0,END)


def open_func():
    global File
    
    File=filedialog.askopenfilename(filetypes=[("text file","*.txt"),("All file","*.*")])
    if File == "":
            File=None
    else:
        root.title(os.path.basename(File),+" ~Notepad")
        text_area.delete(1.0,END)
        f=open(File,"r")
        text_area.insert(1.0,f.read())
        f.close()

def save_func():
    if File is None:
        saveas_func()
    else:
        f=open(File,"w")
        f.write(text_area.get(1.0,END))
        f.close()

def saveas_func():
    global File
    File=filedialog.asksaveasfilename(defaultextension="*.txt",filetypes=[("text file","*.txt"),("All file","*.*")])
    if File:
        f=open(File,"w")
        f.write(text_area.get(1.0,END))
        f.close()
        root.title(os.path.basename(File)+" ~Notepad")
        messagebox.showinfo("Notepad","File Saved Successfully")
         
def exitt_func():
    root.destroy()


#============================EDIT MENU FUNCTIONS=========================
def copy_func():
    text_area.event_generate("<<Copy>>")


def paste_func():
    text_area.event_generate("<<Paste>>")

def cut_func():
    text_area.event_generate("<<Cut>>")

def clear_func():
    text_area.delete("1.0",END)

def undo_func():
   try:
       text_area.edit_undo()
   except:
       pass

def redo_func():
    try:
           text_area.edit_redo()
    except:
           pass

#=======================VIEW MENU FUNCTIONS====================


def zoomin_func():
    global current_size
    global current_font
    current_font=font_text.get()
    current_size=font_size.get()
    current_size+=2
    font_text.set(current_font)
    font_size.set(current_size)
    text_area.config(font=(current_font,current_size))


def zoomout_func():
    global current_size
    global current_font
    current_font=font_text.get()
    current_size=font_size.get()
    if current_size>8:
       current_size-=2
       font_text.set(current_font)
       font_size.set(current_size)
       text_area.config(font=(current_font,current_size))
    

def zoom_func():
    global current_font
    text_area.config(font=(current_font,12))


#=======================HELP MENU FUNCTION===============
def about_func():
    messagebox.showinfo("Notepad","""Windows Notepad 11.2606.15.0
                        © 2026 Microsoft. All rights reserved""")


#===============NEW FILE =====================
file_menu.add_command(label="New",
                      image=new,
                      compound=LEFT,
                      accelerator="Ctrl+N",
                      command=new_func)
root.bind("<Control-N>",new_func)

file_menu.add_command(label="Open",
                      image=openn,
                      compound=LEFT,
                      accelerator="Ctrl+o",
                      command=open_func)
root.bind("<Control-o>",open_func)

file_menu.add_command(label="Save",
                      image=save,
                      compound=LEFT,
                      accelerator="Ctrl+s",
                      command=save_func)
root.bind("<Control-s>",save_func)
file_menu.add_command(label="Save as",
                      image=saveas,
                      compound=LEFT,
                      accelerator="Ctrl+Alt+s",
                      command=saveas_func)
file_menu.add_separator()
root.bind("<Control-Alt-s>",saveas_func)

file_menu.add_command(label="Exit",
                      image=exitt,
                      compound=LEFT,
                      accelerator="Ctrl+",
                      command=exitt_func)
root.bind("<Control-+>",exitt_func)


#==================EDIT MENU=============
edit_menu=Menu(main_menu,tearoff=0)#======Check it=========
main_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Copy",
                      image=copy,
                      compound=LEFT,
                      accelerator="Ctrl+c",
                      command=copy_func)

root.bind("<Control-c>",copy_func)

edit_menu.add_command(label="Paste",
                      image=paste,
                      compound=LEFT,
                      accelerator="Ctrl+v",
                      command=paste_func)
root.bind("<Control-v>",paste_func)

edit_menu.add_command(label="Cut",
                      image=cut,
                      compound=LEFT,
                      accelerator="Ctrl+x",command=cut_func)
root.bind("<Control-x>",cut_func)

edit_menu.add_command(label="Clear all",
                      image=clear,
                      compound=LEFT,
                      accelerator="Ctrl+Alt+x",
                      command=clear_func)

root.bind("<Control-Alt-x>",clear_func)
edit_menu.add_separator()

edit_menu.add_command(label="Undo",
                      image=undo,
                      compound=LEFT,
                      accelerator="Ctrl+Z",command=undo_func)
root.bind("<Control-z>",undo_func)

edit_menu.add_command(label="Redo",
                      image=redo,
                      compound=LEFT,
                      accelerator="Ctrl+Y",command=redo_func)

root.bind("<Control-y>",redo_func)
#===============VIEW MENU==================

view_menu=Menu(main_menu,tearoff=0)
main_menu.add_cascade(label="View",menu=view_menu)
view_menu.add_command(label="Zoom in",
                      image=zoomin,
                      compound=LEFT,
                      accelerator="Ctrl+Plus",
                      command=zoomin_func)

root.bind("<Control-equal>",zoomin_func)

view_menu.add_command(label="Zoom out",
                      image=zoomout,
                      accelerator="ctrl+Minus",
                      compound=LEFT,
                      command=zoomout_func
                      )

root.bind("<Control-minus>",zoomout_func)

view_menu.add_command(label="Restore Default Zoom",
                      accelerator="Ctrl+0",
                      command=zoom_func)

root.bind("<Control-0>",zoom_func)

view_menu.add_separator()

def wrap_func():
    text_area.config(wrap="word")


view_menu.add_command(label="Word Wrap",
                      command=wrap_func)

#===============COLOR THEME MENU=================
color_theme=Menu(main_menu,tearoff=0)
main_menu.add_cascade(label="Color Theme",menu=color_theme)
#==============TUPLE FOR STORE IMAGES=================
colors=(default,light,black,red,monokai,blue)

#====================DICTIONARY FOR STORING COLOURS VALUE TOGETHER===================
color_dict={"Light Default" :("#000000","#ffffff"),
             "Light Plus":("#474747","#e0e0e0"),
             "Dark" :("#c4c4c4","#2d2d2d"),
             "red" :("#2d2d2d","#ffe8e8"),
             "monokai" :("#474747","#d3b774"),
             "Night Blue" :("#ededed","#6b9dc2")
            }
#----------------------Function of change theme================

my_value=StringVar()
def change_theme():
   color_choose=color_dict[my_value.get()]
   text_area.config(fg=color_choose[0],bg=color_choose[1])


#===============FOR LOOP ------------------
count=0
for i in color_dict:
   color_theme.add_radiobutton(label=i,image=colors[count],compound=LEFT,command=change_theme,variable=my_value)
   count=count+1


#=================HELP MENU===============
help_menu=Menu(main_menu,tearoff=0)
main_menu.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About",
                      image=about,
                      compound=LEFT,
                      command=about_func)

#=======================FONT TOOLBARS======================

    #==============FONT FAMILIES===============
outer=ttk.Label(root)           
outer.pack(side=TOP,fill=X)

lst=list(font.families()) 

font_text=StringVar()
fonttext=ttk.Combobox(outer,
                      width=30,
                      state="readonly",
                      values=lst,
                      textvariable=font_text
                      )
fonttext.current(lst.index("Arial"))
fonttext.grid(row=0,column=0,padx=5,pady=5)

def change_fontfamily(event=None): 
  global current_font
  global current_size
  current_font=font_text.get()
  current_size=font_size.get()
  text_area.configure(font=(current_font,current_size))

fonttext.bind("<<ComboboxSelected>>", change_fontfamily)
# #==================FONT SIZE=====================
lst1=[i for i in range(8,100,2)]
font_size=IntVar()
fontsize=ttk.Combobox(outer,
                      width=20,
                      textvariable=font_size,
                      state="readonly",
                      values=lst1)
fontsize.current(2)
fontsize.grid(row=0,column=1,padx=5,pady=5)

def change_fontsize(event=None): 
  global current_font
  global current_size
  current_font=font_text.get()
  current_size=font_size.get()
  text_area.configure(font=(current_font,current_size))

fontsize.bind("<<ComboboxSelected>>",change_fontsize)

# #===============CREATING A TEXT AREA==================

text_area=Text(root,
               wrap="none",
               yscrollcommand=scroll.set,
               undo=True,
               font=(current_font,current_size)
               )
text_area.focus_set()
text_area.pack(fill=BOTH,expand=True)
scroll.config(command=text_area.yview)

# #===============FOMATTING AND ALLIGNMENT FUNCTION=================
print(font.Font(font=text_area["font"]).actual())
def bold_func(): 
  if font.Font(font=text_area["font"]).actual()["weight"]=="normal":
      text_area.config(font=(current_font,current_size,"bold"))
  else:
      text_area.config(font=(current_font,current_size,"normal"))

def italic_func():
    if font.Font(font=text_area["font"]).actual()["slant"]=="roman":
          text_area.config(font=(current_font,current_size,"italic"))
    else:
          text_area.config(font=(current_font,current_size,"roman"))


def underline_func():
   if font.Font(font=text_area["font"]).actual()["underline"]==0:
             text_area.config(font=(current_font,current_size,"underline"))
   else:
             text_area.config(font=(current_font,current_size,"normal"))

def overstrike_func():
    if font.Font(font=text_area["font"]).actual()["overstrike"]==0:
                 text_area.config(font=(current_font,current_size,"overstrike"))
    else:
                     text_area.config(font=(current_font,current_size,"normal"))
        
def color_func():
     choose=colorchooser.askcolor()
     text_area.config(fg=choose[1])

def right_func():
    get_text=text_area.get(1.0,END)
    text_area.tag_config("right",justify=RIGHT)
    text_area.delete(1.0,END)
    text_area.insert(INSERT,get_text,"right")

def left_func():
     get_text=text_area.get(1.0,END)
     text_area.tag_config("left",justify=LEFT)
     text_area.delete(1.0,END)
     text_area.insert(INSERT,get_text,"left")

def center_func():
     get_text=text_area.get(1.0,END)
     text_area.tag_config("center",justify=CENTER)
     text_area.delete(1.0,END)
     text_area.insert(INSERT,get_text,"center")

# #===================FORMATTING AND ALIGNMENT IMAGE======================
bold_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\bold-text-option.png")
bold_img=bold_img.resize((20,20),Image.LANCZOS)
bold=ImageTk.PhotoImage(bold_img)

italic_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\italic-font.png")
italic_img=italic_img.resize((20,20),Image.LANCZOS)
italic=ImageTk.PhotoImage(italic_img)

over_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\strikethrough.png")
over_img=over_img.resize((20,20),Image.LANCZOS)
over=ImageTk.PhotoImage(over_img)

color_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\color-wheel.png")
color_img=color_img.resize((20,20),Image.LANCZOS)
color=ImageTk.PhotoImage(color_img)

left_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\leftcontent.png")
left_img=left_img.resize((20,20),Image.LANCZOS)
left=ImageTk.PhotoImage(left_img)

right_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\rightcontent.png")
right_img=right_img.resize((20,20),Image.LANCZOS)
right=ImageTk.PhotoImage(right_img)

center_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\justifycontent.png")
center_img=center_img.resize((20,20),Image.LANCZOS)
center=ImageTk.PhotoImage(center_img)

under_img=Image.open(r"C:\Users\DELL\Desktop\python\Notpad Project\underline.png")
under_img=under_img.resize((20,20),Image.LANCZOS)
under=ImageTk.PhotoImage(under_img)

boldfont=Button(outer,
            image=bold,
            command=bold_func
            )
boldfont.grid(row=0,column=2,padx=15)
italicfont=Button(outer,
            image=italic,
            command=italic_func
            )
italicfont.grid(row=0,column=3,padx=15)
underfont=Button(outer,
            image=under,
            command=underline_func
            )
underfont.grid(row=0,column=4,padx=15)

overfont=Button(outer,
            image=over,
            command=overstrike_func
            )
overfont.grid(row=0,column=5,padx=15)

colorfont=Button(outer,
            image=color,
            command=color_func
            )
colorfont.grid(row=0,column=6,padx=15)

leftfont=Button(outer,
            image=left,
            command=left_func
            )
leftfont.grid(row=0,column=7,padx=15)
rightfont=Button(outer,
            image=right,
            command=right_func
            )
rightfont.grid(row=0,column=8,padx=15)
centerfont=Button(outer,
            image=center,
            command=center_func
            )
centerfont.grid(row=0,column=9,padx=8)

# #====================STATUSBAR WORD AND CHARACTER COUNT=====================
statusbar=ttk.Label(root,text="Status bar")
statusbar.pack(side=BOTTOM)

text_change = False
def change_word(event=None):
    global text_change

    if text_area.edit_modified():
        text_change = True

        word = len(text_area.get(1.0, "end-1c").split())
        character = len(text_area.get(1.0, "end-1c").replace(" ", ""))

        statusbar.config(
            text=f"character : {character} word : {word}"
        )

        text_area.edit_modified(False)


text_area.bind("<<Modified>>", change_word)

root.mainloop()