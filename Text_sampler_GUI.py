#Practice making a GUI with event-driven programming components. Lesson 12 from Introduction to Python 2.5 Programming class.
#Requirements: Python (written in 2.5); Tkinter

#GUI displays user-entered text and then modifies the display based on user button selections.


from Tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("600x350")
        self.master.title("Text Dressing Room")
        self.grid()

        #Prompts users to imput text, which they will then be able to manipulate
        self.prompt = Label(self, text = "Enter text here: ")
        self.prompt.grid(row = 0, column = 0)

        self.input = Entry(self)
        self.input.grid(row = 0, column = 1, columnspan = 2, pady = 5)

        self.button_submit = Button(self, text = "Submit", command = self.submit_click)
        self.button_submit.grid(row = 1, column = 1, columnspan = 2)

        self.user_text = StringVar()
        self.message = Label(self, textvariable = self.user_text, font = "Courier 10")
        self.message.grid(row = 2, column = 1, pady = 5)

        #Checkbuttons for adding bold, underline, italic
        self.bold_on = IntVar()
        self.check_bold = Checkbutton(self, text="Bold", variable=self.bold_on, command=self.set_font)
        self.check_bold.grid(row=3, column=0, padx = 5)

        self.underline_on = IntVar()
        self.check_underline = Checkbutton(self, text="Underline", variable=self.underline_on, command=self.set_font)
        self.check_underline.grid(row=3, column=1, padx = 5)

        self.italic_on = IntVar()
        self.check_italic = Checkbutton(self, text="Italic", variable=self.italic_on, command=self.set_font)
        self.check_italic.grid(row=3, column=2, padx=5)

        #Radiobuttons for selecting point size
        self.point_size = StringVar()
        self.point_size.set("10")
        
        self.ten_point = Radiobutton(self, text = "10 point", variable = self.point_size, value = "10", command = self.set_font)
        self.ten_point.grid(row = 4, column = 0)
        
        self.twelve_point = Radiobutton(self, text = "12 point", variable = self.point_size, value = "12", command = self.set_font)
        self.twelve_point.grid(row = 4, column = 1)

        self.twenty_point = Radiobutton(self, text = "20 point", variable = self.point_size, value = "20", command = self.set_font)
        self.twenty_point.grid(row = 4, column = 2)

        #Radiobuttons for selecting the font
        self.family = StringVar()
        self.times = Radiobutton(self, text = "Times New Roman", variable = self.family, value = "times", command = self.set_font)
        self.times.grid(row = 5, column = 0, columnspan = 2)
        
        self.courier = Radiobutton(self, text = "Courier", variable = self.family, value = "courier", command = self.set_font)
        self.courier.grid(row = 5, column = 2, columnspan = 2)

    def submit_click(self):
        sample_label = self.input.get()
        self.user_text.set(sample_label)

    def set_font(self):
        new_font = "Courier"

        if self.family.get() == "times":
            new_font = "Times"
        #NOTE key importance of the space before the append to new_font. Otherwise, will get an error.
        if self.point_size.get() == "10":
            new_font = new_font + " 10"
            
        if self.point_size.get() == "12":
            new_font = new_font + " 12"

        if self.point_size.get() == "20":
            new_font = new_font + " 20"

        if self.bold_on.get() == 1:
            new_font = new_font + " bold"

        if self.underline_on.get() == 1:
            new_font = new_font + " underline"

        if self.italic_on.get() == 1:
            new_font = new_font + " italic"


        self.message.config(font = new_font)

frame03 = MyFrame()
frame03.mainloop()




