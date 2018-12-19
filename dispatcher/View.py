from tkinter import *
from time import *
from threading import *


tk=Tk()
tk.title("Title")
#tk.wm_attributes("-topmost", 1)
tk.attributes("-fullscreen", True)
canvas=Canvas(tk, width=tk.winfo_screenwidth(), height=tk.winfo_screenheight(), bd=0, highlightthickness=0)
canvas.pack()
tk.update()
sc_wd=tk.winfo_screenwidth()
sc_he=tk.winfo_screenheight()

limits=[13, 8]
side=100






#self.inputWindow.attributes("-topmost", 1)
tk.update()


class View:
    def __init__(self, side, limits):
        self.y_point=sc_he/limits[1]
        self.x_point=sc_wd/limits[0]
        self.px_x=self.x_point/side
        self.px_y=self.y_point/side
        self.screen=[]
        self.isEnd=False
        self.timeText=None
        self.sc_wd=sc_wd
        self.sc_he=sc_he
        strftime('%Y-%m-%d %H:%M:%S')
        self.inputWindow=0
        self.timeScale=None
        self.tText=None
        self.startPos=None
        self.startX=None
        self.startY=None
        self.endPos=None
        self.endX=None
        self.endY=None
        self.speedSc=None
        self.tSpeed=None


    def draw(self, obj, stable):
        for i in self.screen:
            canvas.delete(i)
        for i in obj.keys():
            for a in obj[i].keys():
                self.screen.append(canvas.create_rectangle(int(i)*self.x_point, self.y_point*(8-int(a)), int(i)*self.x_point+self.x_point, self.y_point*(8-int(a))-self.y_point, fill="blue"))   
                self.screen.append(canvas.create_text(int(i)*self.x_point+50, (8-int(a))*self.y_point-50, text=obj[i][a]))
        for i in stable:
            self.screen.append(canvas.create_rectangle(i.coords[0]*self.x_point, self.y_point*(8-i.coords[1]), i.coords[0]*self.x_point+self.x_point, self.y_point*(8-i.coords[1])-self.y_point, fill="black"))
        if self.timeText==None:
            self.timeText=canvas.create_text(50, 50, text=(''+str(localtime(time())[3])+' '+str(localtime(time())[4])+' '+str(localtime(time())[5])))
        else:
            canvas.itemconfig(self.timeText, text=(''+str(localtime(time())[3])+' '+str(localtime(time())[4])+" "+str(localtime(time())[5])))

    def update(self):
         if not self.isEnd:
            tk.update_idletasks()
            tk.update()
    
            
            
    def addAircraft(self):
        def ret():
            ret=[self.timeScale.get()]
            print(ret)
            self.inputWindow.destroy()
            return ret
        self.inputWindow=Tk()
        self.inputWindow.resizable(width=False, height=False)
        self.inputWindow.title("Input")
        self.inputWindow.geometry("120x350")
        self.timeScale=Scale(self.inputWindow, from_=0, to=10, width=8, orient='horizontal')
        self.timeScale.place(relx=.49, rely=.07, anchor='c')
        self.tText=Label(self.inputWindow, text='Time:')
        self.tText.place(relx=.27, rely=.01, anchor='c')
        self.startPos=Label(self.inputWindow, text="Start:")
        self.startPos.place(relx=.27, rely=.16, anchor='c')
        self.startX=Scale(self.inputWindow, from_=0, to=limits[0]*side,  resolution=10, width=8, orient='horizontal')
        self.startX.place(relx=.49, rely=.24, anchor='c')
        self.startY=Scale(self.inputWindow, from_=0, to=limits[1]*side,  resolution=10, width=8, orient='horizontal')
        self.startY.place(relx=.49, rely=.33, anchor='c')
        self.endPos=Label(self.inputWindow, text="Destination:")
        self.endPos.place(relx=.37, rely=.43, anchor='c')
        self.endX=Scale(self.inputWindow, from_=0, to=limits[0]*side,  resolution=10, width=8,  orient='horizontal')
        self.endX.place(relx=.49, rely=.50, anchor='c')
        self.endY=Scale(self.inputWindow, from_=0, to=limits[1]*side,  resolution=10, width=8,  orient='horizontal')
        self.endY.place(relx=.49, rely=.6, anchor='c')
        self.tSpeed=Label(self.inputWindow, text='Speed:')
        self.tSpeed.place(relx=.37, rely=.75, anchor='c')
        self.speedSc=Scale(self.inputWindow, from_=0, to=500, orient='horizontal', width=8)
        self.speedSc.place(relx=.49, rely=.83, anchor='c')
        aplly=Button(self.inputWindow, text='Start', bg='light blue', command=ret)
        aplly.place(relx=.45, rely=.975, anchor='c')


         



        
def end():
        canvas.destroy()
        tk.destroy()



    
btn=Button(text='X', command=end)
btn.place(relx=.995, rely=.01, anchor="c")