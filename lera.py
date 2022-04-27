class app(object) :
      def __init__(self) :
            self.app = tkinter.Tk()
            self.app.title("Lera")
            self.app.resizable(width=False, height =False)
            self.app["bg"]  = "black"
            
            self.heure = tkinter.StringVar()
            self.date = tkinter.StringVar()
            self.date.set(time.strftime("%A %d %B %Y"))
            self.daty = tkinter.Label(self.app, bg = "black",font=("Times New Roman",12), fg = "green", text = time.strftime("%A %d %B %Y"))
            self.lera = tkinter.Label(self.app,font = ("Times New Roman",15,"bold"), bg = "black", fg = "red", textvariable = self.heure.get())
            self.lucien = tkinter.Label(self.app, font =("Brush Script MT",8),bg = "black", fg = "white", text = "@Fahazavana")

            self.daty.grid(row=0)
            self.lera.grid(row= 1)
            self.lucien.grid(row=2,sticky ='w')
            self.maj()
            self.app.mainloop()
            
      def maj(self) :
            now = time.strftime("%H:%I:%S")
            self.lera.config(text=now)
            self.lera.after(10, self.maj)
      
            

if __name__ == "__main__" :
      import tkinter
      import time
      f = app()
            
