from tkinter import *
from time import *

tk=Tk()
tk.title("Title")
#tk.wm_attributes("-topmost", 1)
tk.attributes("-fullscreen", True)
canvas=Canvas(tk, width=tk.winfo_screenwidth(), height=tk.winfo_screenheight(), bd=0, highlightthickness=0)
canvas.pack()
tk.update()
sc_wd=tk.winfo_screenwidth()
sc_he=tk.winfo_screenheight()


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
    
            

        
def end():
        canvas.destroy()
        tk.destroy()



    
btn=Button(text='X', command=end)
btn.place(relx=.995, rely=.01, anchor="c")