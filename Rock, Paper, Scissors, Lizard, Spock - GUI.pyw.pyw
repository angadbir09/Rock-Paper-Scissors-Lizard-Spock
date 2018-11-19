from Tkinter import *
class Application(Frame):
    def _init_(self,master):
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = Button(self, text = "Rock")
        self.button1.grid()

        self.button2 = Button(self)
        self.button2.grid()
        self.button2.configure(text="Paper")

        self.button3 = Button(self)
        self.button3.grid()
        self.button3["text"]="Scissors"

        self.button4 = Button(self)
        self.button4.grid()
        self.button4["text"]="Lizard"

        self.button3 = Button(self)
        self.button3.grid()
        self.button3["text"]="Spock"

root = Tk()
root.title("Rock, Paper, Scissors, Lizzard, Spock")
root.geometry("200x200")

app = Frame(root)
app.grid()
label = Label(app, text = "Please Select your Hand-Shape")
label.grid()

app = Application(root)
app._init_(root)

root.mainloop()









