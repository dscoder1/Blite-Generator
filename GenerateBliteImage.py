import qrcode
from tkinter import *
from tkinter.messagebox import showinfo,showerror
from PIL import Image
def savefile():
    if(pathinput.get()[-1]=='"' or pathinput.get()[0]=='"'):
        showerror(title="Blite Generator",message="Give Path Without Quotes")
    img=Image.open(pathinput.get())
    BlackAndWhite=img.convert("L")
    saved=BlackAndWhite.save(fileinput.get()+".jpg")
    showinfo(title="Blite Generator",message="File Saved With "+fileinput.get()+".jpg")
    pathinput.set("")
    fileinput.set("")
    
page=Tk()
page.title("Generate Black White Image ..")
page.iconbitmap("BliteIcon.ico")
page.geometry("1500x750+10+10")
page.resizable(False,False)
pathinput=StringVar()
fileinput=StringVar()
TitleLabel=Label(page,text="Generate Black White Image",font=("Calibri",30,"bold"),bg="black",relief=SUNKEN,fg="white")
TitleLabel.place(x=130,y=50,height=70,width=1200)
LinkLabel=Label(page,text="Image Path: ",font=("Calibri",20))
LinkLabel.place(x=280,y=200,height=60,width=150)
FileLabel=Label(page,text="File Name: ",font=("Calibri",20))
FileLabel.place(x=280,y=300,height=60,width=150)
LinkInput=Entry(page,textvariable=pathinput,font=("Calibri",20))
LinkInput.place(x=450,y=200,height=60,width=700)
FileInput=Entry(page,textvariable=fileinput,font=("Calibri",20))
FileInput.place(x=450,y=300,height=60,width=700)
SaveButton=Button(page,text="Save",bg="black",fg="white",font=("Arial Black",20,"bold"),command=savefile)
SaveButton.place(x=700,y=500,height=70,width=200)
page.mainloop()
