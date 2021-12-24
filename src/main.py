from tkinter import *
from time import sleep
from PIL import Image, ImageTk
from itertools import count
from playsound import playsound
import threading

class ImageLabel(Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

print("Jurassic Park Security System v1.00")
print("Please type a command.")
i = 0
while i < 3:
    input(">>> ")
    print("PERMISSION DENIED!")
    i += 1

print("Also...")
sleep(1.5)
def spam():
    while True:
        print("YOU DIDN'T SAY THE MAGIC WORD!!!")
def app():
    sleep(2)
    root = Tk()
    root.title("HAHAHA! YOU DIDN'T SAY THE MAGIC WORD!!!")
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('image.gif')
    root.resizable(0, 0)
    root.mainloop()
t1 = threading.Thread(target=spam)
t1.start()
t2 = threading.Thread(target=app)
t2.start()
sleep(2)
while True:
    playsound("magicword.mp3")
    sleep(3)
