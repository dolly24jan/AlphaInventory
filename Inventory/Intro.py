'''
    INVENTORY MANAGEMENT SYSTEM
    Developed By : Dolly
    Developed On : 24/01/2021
'''
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

class splash:
    def __init__(self):
      self.splashminw=Tk()
      self.splashminw.title("About")
      width = 1000
      height = 700
      self.splashminw.config(bg="#75530e")
      screen_width = self.splashminw.winfo_screenwidth()
      screen_height = self.splashminw.winfo_screenheight()
      x = (screen_width / 2) - (width / 2)
      y = (screen_height / 2) - (height / 2)
      self.splashminw.geometry("%dx%d+%d+%d" % (width, height, x, y))
      self.splashminw.resizable(0,0)
      path = "images/inventorys.jpg"
      img = ImageTk.PhotoImage(Image.open(path))
      #img = imag.resize((250, 250), Image.ANTIALIAS)
      main=LabelFrame(self.splashminw, width=890, height=560,bg="#c7af7d",relief="ridge",bd=4)
      main.place(x=55,y=70)
      photoframe = LabelFrame(main, width=420, height=444, bg='#75530e', relief="raised")
      pic=Label(photoframe, image=img)
      pic.place(x=6, y=6)
      photoframe.place(x=10, y=100)
      #.resize(420,444)
      Label(main, text="Alpha Inventory System",font=('times new roman',24,'bold'),bg="snow",relief="ridge",bd=4).place(x=45, y=10,width=800, height=55)
      Label(main, text="Dolly",font=('times new roman',24,'bold'),bg="#c7af7d").place(x=450, y=260)
      Label(main, text="SheArise Training, NASSCOM",font=('times new roman',16,'bold'),bg="#c7af7d").place(x=445+5, y=300)
      Label(main, text="Batch-: Python Batch 1", font=('times new roman',16,'bold'), bg="#c7af7d").place(x=450, y=330)
      Label(main, text="Email Id-: dolly24jan@gmail.com",font=('times new roman',16,'bold'),bg="#c7af7d").place(x=445+5, y=360)
      #Label(main, text="Ph.no:- Deleted",font="roboto 16 bold",bg="snow").place(x=445+5, y=410)
      pic.bind('<Motion>', lambda event: self.splashminw.destroy())
     # self.splashminw.after(10000,lambda :self.splashminw.destroy())
      self.splashminw.mainloop()


