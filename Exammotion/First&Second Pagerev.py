# Multi-frame tkinter application v2.3
import tkinter as tk
from PIL import ImageTk, Image
import scriptprogres

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.title("Exammotion")
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.img = ImageTk.PhotoImage(Image.open('Background/backgroundExammotion5.jpg'))
        self.imgst= ImageTk.PhotoImage(Image.open('Background/seluruhtubuh.jpg'))
        self.imgbt= ImageTk.PhotoImage(Image.open('Background/bagiantubuh.jpg'))
        tk.Label(self,image=self.img).pack()
        st=tk.Button(self,highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(PageOne))
        st.config(image=self.imgst)
        st.place(x=430, y=530, height= 40, width= 251)
        bt=tk.Button(self, highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(PageTwo))
        bt.config(image=self.imgbt)
        bt.place(x=700, y=530,  height= 40, width= 251)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.img = ImageTk.PhotoImage(Image.open('Background/backgroundExammotion8.jpg'))
        self.img1= ImageTk.PhotoImage(Image.open('Background/1.jpg'))
        self.img4= ImageTk.PhotoImage(Image.open('Background/4.jpg'))
        self.img8= ImageTk.PhotoImage(Image.open('Background/8.jpg'))
        self.imgh= ImageTk.PhotoImage(Image.open('Background/home.png'))
        tk.Label(self,image=self.img).pack()
        satu=tk.Button(self,highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(PageA1))
        satu.config(image=self.img1)
        satu.place(x=450, y=480, height= 40, width= 100)
        empat=tk.Button(self, highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(PageA4))
        empat.config(image=self.img4)
        empat.place(x=640, y=480,  height= 40, width= 100)
        lapan=tk.Button(self, highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(PageA8))
        lapan.config(image=self.img8)
        lapan.place(x=830, y=480,  height= 40, width= 100)
        home=tk.Button(self, highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(StartPage))
        home.config(image=self.imgh)
        home.place(x=1260, y=650,  height= 70, width= 70)


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.img = ImageTk.PhotoImage(Image.open('Background/backgroundExammotion8.jpg'))
        self.img1= ImageTk.PhotoImage(Image.open('Background/1.jpg'))
        self.img4= ImageTk.PhotoImage(Image.open('Background/4.jpg'))
        self.img8= ImageTk.PhotoImage(Image.open('Background/8.jpg'))
        self.imgh= ImageTk.PhotoImage(Image.open('Background/home.png'))
        tk.Label(self,image=self.img).pack()
        satu=tk.Button(self,highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(PageB1))
        satu.config(image=self.img1)
        satu.place(x=450, y=480, height= 40, width= 100)
        empat=tk.Button(self, highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(PageB4))
        empat.config(image=self.img4)
        empat.place(x=640, y=480,  height= 40, width= 100)
        lapan=tk.Button(self, highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(PageB8))
        lapan.config(image=self.img8)
        lapan.place(x=830, y=480,  height= 40, width= 100)
        home=tk.Button(self, highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(StartPage))
        home.config(image=self.imgh)
        home.place(x=1260, y=650,  height= 70, width= 70)

class PageA1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.img = ImageTk.PhotoImage(Image.open('Background/backgroundExammotionHal2.jpg'))
        self.imgyes= ImageTk.PhotoImage(Image.open('Background/yesbut.jpg'))
        self.imgno= ImageTk.PhotoImage(Image.open('Background/nobut.jpg'))
        self.imgh= ImageTk.PhotoImage(Image.open('Background/home.png'))
        tk.Label(self,image=self.img).pack()
        yes=tk.Button(self,highlightthickness=0,relief='flat',
                  command=scriptprogres.seluruh1plot)
        yes.config(image=self.imgyes)
        yes.place(x=550, y=480, height= 40, width= 100)
        no=tk.Button(self, highlightthickness=0,relief='flat',
                  command=scriptprogres.seluruh1)
        no.config(image=self.imgno)
        no.place(x=730, y=480,  height= 40, width= 100)
        home=tk.Button(self, highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(StartPage))
        home.config(image=self.imgh)
        home.place(x=1260, y=650,  height= 70, width= 70)

class PageA4(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.img = ImageTk.PhotoImage(Image.open('Background/backgroundExammotionHal2.jpg'))
        self.imgyes= ImageTk.PhotoImage(Image.open('Background/yesbut.jpg'))
        self.imgno= ImageTk.PhotoImage(Image.open('Background/nobut.jpg'))
        self.imgh= ImageTk.PhotoImage(Image.open('Background/home.png'))
        tk.Label(self,image=self.img).pack()
        yes=tk.Button(self,highlightthickness=0,relief='flat',
                  command=scriptprogres.seluruh4plot)
        yes.config(image=self.imgyes)
        yes.place(x=550, y=480, height= 40, width= 100)
        no=tk.Button(self, highlightthickness=0,relief='flat',
                  command=scriptprogres.seluruh4)
        no.config(image=self.imgno)
        no.place(x=730, y=480,  height= 40, width= 100)
        home=tk.Button(self, highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(StartPage))
        home.config(image=self.imgh)
        home.place(x=1260, y=650,  height= 70, width= 70)

class PageA8(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.img = ImageTk.PhotoImage(Image.open('Background/backgroundExammotionHal2.jpg'))
        self.imgyes= ImageTk.PhotoImage(Image.open('Background/yesbut.jpg'))
        self.imgno= ImageTk.PhotoImage(Image.open('Background/nobut.jpg'))
        self.imgh= ImageTk.PhotoImage(Image.open('Background/home.png'))
        tk.Label(self,image=self.img).pack()
        yes=tk.Button(self,highlightthickness=0,relief='flat',
                  command=scriptprogres.seluruh8plot)
        yes.config(image=self.imgyes)
        yes.place(x=550, y=480, height= 40, width= 100)
        no=tk.Button(self, highlightthickness=0,relief='flat',
                  command=scriptprogres.seluruh8)
        no.config(image=self.imgno)
        no.place(x=730, y=480,  height= 40, width= 100)
        home=tk.Button(self, highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(StartPage))
        home.config(image=self.imgh)
        home.place(x=1260, y=650,  height= 70, width= 70)

class PageB1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.img = ImageTk.PhotoImage(Image.open('Background/backgroundExammotionHal2.jpg'))
        self.imgyes= ImageTk.PhotoImage(Image.open('Background/yesbut.jpg'))
        self.imgno= ImageTk.PhotoImage(Image.open('Background/nobut.jpg'))
        self.imgh= ImageTk.PhotoImage(Image.open('Background/home.png'))
        tk.Label(self,image=self.img).pack()
        yes=tk.Button(self,highlightthickness=0,relief='flat',
                  command=scriptprogres.bagian1plot)
        yes.config(image=self.imgyes)
        yes.place(x=550, y=480, height= 40, width= 100)
        no=tk.Button(self, highlightthickness=0,relief='flat',
                  command=scriptprogres.bagian1)
        no.config(image=self.imgno)
        no.place(x=730, y=480,  height= 40, width= 100)
        home=tk.Button(self, highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(StartPage))
        home.config(image=self.imgh)
        home.place(x=1260, y=650,  height= 70, width= 70)

class PageB4(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.img = ImageTk.PhotoImage(Image.open('Background/backgroundExammotionHal2.jpg'))
        self.imgyes= ImageTk.PhotoImage(Image.open('Background/yesbut.jpg'))
        self.imgno= ImageTk.PhotoImage(Image.open('Background/nobut.jpg'))
        self.imgh= ImageTk.PhotoImage(Image.open('Background/home.png'))
        tk.Label(self,image=self.img).pack()
        yes=tk.Button(self,highlightthickness=0,relief='flat',
                  command=scriptprogres.bagian4plot)
        yes.config(image=self.imgyes)
        yes.place(x=550, y=480, height= 40, width= 100)
        no=tk.Button(self, highlightthickness=0,relief='flat',
                  command=scriptprogres.bagian4)
        no.config(image=self.imgno)
        no.place(x=730, y=480,  height= 40, width= 100)
        home=tk.Button(self, highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(StartPage))
        home.config(image=self.imgh)
        home.place(x=1260, y=650,  height= 70, width= 70)

class PageB8(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.img = ImageTk.PhotoImage(Image.open('Background/backgroundExammotionHal2.jpg'))
        self.imgyes= ImageTk.PhotoImage(Image.open('Background/yesbut.jpg'))
        self.imgno= ImageTk.PhotoImage(Image.open('Background/nobut.jpg'))
        self.imgh= ImageTk.PhotoImage(Image.open('Background/home.png'))
        tk.Label(self,image=self.img).pack()
        yes=tk.Button(self,highlightthickness=0,relief='flat',
                  command=scriptprogres.bagian8plot)
        yes.config(image=self.imgyes)
        yes.place(x=550, y=480, height= 40, width= 100)
        no=tk.Button(self, highlightthickness=0,relief='flat',
                  command=scriptprogres.bagian8)
        no.config(image=self.imgno)
        no.place(x=730, y=480,  height= 40, width= 100)
        home=tk.Button(self, highlightthickness=0,relief='flat',
                  command=lambda: master.switch_frame(StartPage))
        home.config(image=self.imgh)
        home.place(x=1260, y=650,  height= 70, width= 70)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
